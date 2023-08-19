import json
import os
from types import SimpleNamespace

import aiohttp
import cohere
import discord
import yaml
from discord import app_commands


def yaml_load(path):
    with open(path, "r") as stream:
        try:
            configs = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(
                f"The config file does not exist, so we get the following error: {exc}"
            )
            return None
    return configs


CONFIGS = yaml_load(path=os.path.join(os.getcwd(), "env.yml"))

co = cohere.Client(CONFIGS["COHERE_API_KEY"])


async def async_summarize(**options):
    headers = {
        "Authorization": "BEARER " + co.api_key,
        "Content-Type": "application/json",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            co.api_url + "/summarize", headers=headers, json=options
        ) as resp:
            resp = await resp.json()
            x = json.loads(json.dumps(resp), object_hook=lambda d: SimpleNamespace(**d))
            return x


co.async_summarize = async_summarize  # add async summarize call to cohere client


MY_GUILD = discord.Object(id=int(CONFIGS["GUILD_ID"]))


class DiscordBot(discord.AutoShardedClient):
    # init discord bot properly with commands
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents, shard_count=2)
        self.tree = app_commands.CommandTree(self)

    # init discord bot properly with commands
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    async def make_history(self, message, num_historic_msgs=20):
        history = []
        messages = [
            message
            async for message in message.channel.history(
                limit=num_historic_msgs, before=message
            )
        ]
        for historic_msg in messages:
            name = historic_msg.author.name
            line = ""

            if bool(historic_msg.content):
                if (
                    historic_msg.author.name == self.user.name
                ):  # disregard previous chatbot summaries in the new summary
                    continue
                line += historic_msg.clean_content
            if line:
                history.insert(0, {name: line})
        return "\n".join(
            [
                f"{list(chat_turn.keys())[0]}: {list(chat_turn.values())[0]}"
                for chat_turn in history
            ]
        )

    def prepare_prompt(self, history, message):
        return (
            open("prompts/" + CONFIGS["PROMPT_FILE"])
            .read()
            .format(
                history=history.strip(),
                message=message,
            )
        )

    async def summarize(self, prompt):
        response = await co.async_summarize(
            text=prompt,
            model="summarize-xlarge",
            length="medium",
            extractiveness="medium",
        )
        return response.summary

    async def on_message(self, message):
        if (self.user.mentioned_in(message) and message.author != self.user):
            async with message.channel.typing():
                history = await self.make_history(message, num_historic_msgs=20)
                prompt = self.prepare_prompt(
                    history, f"{message.author.name}: {message.clean_content}"
                )
                summary = await self.summarize(prompt)
                await message.channel.send(summary)
                return


intents = discord.Intents.default()
intents.message_content = True
client = DiscordBot(intents=intents)

if __name__ == "__main__":
    client.run(CONFIGS["DISCORD_TOKEN"])
