# Diva: Discord Ozet Botu 
## Cohere API'i kullanarak Discord konusmalari ozetleyen bir bot yazmak
### Yazilim Ortami Kurulumu:

1. Python ile kod yazacagiz, Python3'un kurulu olduguna emin olun. 
2. Anaconda veya Miniconda kullanarak gelistirme ortamimizi duzenleyecegiz. Buradan Anaconda indirebilirsiniz: https://docs.anaconda.com/free/anaconda/install/index.html
3. Bu klasoru kopyaladiktan sonra klasore cd'leyip bu komutu calistirin: `conda env create -f conda_env.yml; conda activate workshop_env`.
4. Istege bagli olarak Docker da indirip calistirabilirsiniz. Linki burada: https://www.docker.com/products/docker-desktop/ Zamanimiz kalirsa Docker ile ufak bir iki sey yapabiliriz. 

### Discord Ile Ilgili Kurulum:
Bu adimlarin sonunda kendimize bir Discord sunucusu acip botumuzu oraya eklemis olacagiz. 
1. Linkteki adimlari takip ederek bir Discord sunucusu ve Discord botu olusturun. https://appmaster.io/tr/blog/discord-botu-nasil-olusturulur-ve-sunucuya-eklenir
!HENUZ SUNUCUYA EKLEMEYIN! Once botumuzun ayarlarini yapacagiz :)) Bu siteden “Bir bot oluşturun ve onu sunucuya ekleyin, bot jetonunu kopyalayın” basligi altindaki 4. maddeye kadar tamamlayin. 
2. Botu olusturduktan sonra https://discord.com/developers/applications/ sitesine gidin ve botunuzun ait oldugu uygulamaya tiklayin. 
3. Sol sagdaki menuden “Bot”a tiklayin ve Message Content Intent’i aktive edip kaydedin.
4. Ayni menuden “OAuth2”ye tiklayin ve sonra da hemen altindaki “URL Generator”a tiklayin.
5. Bu sayfada “bot” ve “applications.commands” seceneklerini secin. Bu yeni bir menu acilmasina sebep olacaktir. O menudeki “Text Permissions” sutunu altindaki butun secenekleri isaretleyip secin. 
6. Bu degisiklikleri yaptiktan sonra bu sayfanin altindaki “Generated URL” kismindaki linki kopyalayip tarayiciniza yapistirin. 1. Asamada yarattiginiz sunucuyu secip “Authorize”a tiklayin. Ve bu hareketle botunuz o sunucuya eklenmis oldu! 

### Cohere API Key
1. https://cohere.com 'a gidin. Hesap olusturup giris yapin. 
2. https://dashboard.cohere.ai/api-keys linkine gidip API key'inize ulasabilirsiniz.

### env.yml dosyasi olusturma (Dersin basinda bu kismin uzerinden bir kere daha gececegiz)

1. `env.yml` diye bir dosya olusturup `env_example.yml`in icerigini ona kopyalayin. 
2. `DISCORD_TOKEN` satirina yukarida olusturdugunuz botun tokenini yapistirin. Bu linkte yarattiginiz uygulamaya tiklayarak tokeni bulabilirsiniz: https://discord.com/developers/applications/
3. `COHERE_API_KEY` satirina Cohere API key'inizi yapistirin.
4. `GUILD_ID` kismina yukarida yarattiginiz sunucunun ID'sini yapistirin. ID'yi bulmak icin buradaki asamalari takip edebilirsiniz: https://support.discord.com/hc/tr/articles/206346498-Kullan%C4%B1c%C4%B1-Sunucu-Mesaj-ID-sini-Nerden-Bulurum-
