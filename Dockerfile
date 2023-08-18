# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.13-slim-buster
#LABEL maintainer="https://github.com/cohere-ai/sandbox-grounded-qa"

# Keeps Python from generating .pyc files in the container
# Turns off buffering for easier container logging
# Force UTF8 encoding for funky character handling
# Needed so imports function properly
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
ENV PYTHONIOENCODING=utf-8
ENV PYTHONPATH=/app

# Install project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Place where the app lives in the container
WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. 
CMD ["python3", "/app/discord_bot.py"]