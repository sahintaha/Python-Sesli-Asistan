from gtts import gTTS
import speech_recognition as sr
import os
from os import system as komut
from pydub import AudioSegment
from youtube_search import YoutubeSearch
import webbrowser
import smtplib
import wikipedia
import sys
import cv2
import datetime
import time
import random
import psutil
import pyowm #hava
from googletrans import Translator
from pydub.playback import play
import pygame

harfBuyuk = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucuk = "abcçdefgğhıijklmnoöprsştuüvyz"


def lower(command:str):
    newText = str()
    for i in command:
        if i in command:
            if i in harfBuyuk:
                index = harfBuyuk.index(i)
                newText += kucuk[index]
            else:
                newText += i
    return newText

def konus(audio):
    print(audio)
    tts = gTTS(text=audio, lang="tr")
    tts.save("audio.mp3")
    sound = AudioSegment.from_file("audio.mp3", format="mp3")
    play(sound)

def komutlar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        komut("clear") #....linux için
        print("Dinleniyor...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print("ok")
    try:
        command = r.recognize_google(audio,language="tr")
        command = lower(command)

        print("Söylenen: " + command + "\n")

    #tekrar
    except sr.UnknownValueError:

        konus("Maalesef son dediğinizi anlayamadım.")
        command = komutlar()

    return command


hour = int(datetime.datetime.now().hour)
if hour >= 1 and hour <12:
    konus("Günaydın. Ben gözlüğünüzün asistanı İris. size nasıl yardımcı olabilirim")

elif hour >= 12 and hour < 17:
    konus("Tünaydın, Ben gözlüğünüzün asistanını İris. size nasıl yardımcı olabilirim")
else:

    konus("iyi akşamlar, Ben gözlüğünüzün asistanı İris. size nasıl yardımcı olabilirim")


def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


#-----------------------
#-----------------------

iyiyim = ["ben de iyiyim", "bende iyiyim" , "iyiyim" , "iyi"]
keyifsiz = ["neden öyle dedin", "niçin" , "neden" , "neden keyifsizsin","ama neden","peki neden","niçin"]
iltifat = ["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","teşekkür ederim","çok","iyi","çok iyi","seni seviyorum","sevdim seni"]
beceri = ["neler yapabiliyorsun","gözlük","maarifetlerin neler","yapay zeka","yeteneğin ne","ne yeteneğin var","göster maarifetlerini"]
webcm = ["kamera","kamerayı aç","kamerayı açar mısın","aç kamera","beni göster","kendimi göster","yüzümü tanı","tanı yüzümü"]
meraba = ["merhaba","selam","merhabalar","alo","selamlar","merhaba selam","selamün aleyküm","hey"]
merbdonus = ["merhaba","selam","heyy hoşgeldin","merhaba hoşgeldin"]
teknofest = ["teknofest", "teknofest nedir" , "teknofest projesi" ]
olamazsin = ["olamazsın", "yardımcı olamazsın" , "bana yardımcı olamazsın", "asla", "yürü git","olmaz","olamaz"]
sarksor = ["şarkı söyler misin", "şarkı" , "şarkı söyle" , "bana şarkı söyle", "bize şarkı söyle"]
sarksoyle = ["Ses bir iki üç. Do re mi Ankara'nın bağları da büklüm büklüm yolları."]
siir = ["şiir oku", "şiir söyle" , "şiir" , "bize şiir oku", "bir söz söyle"]
siiroku = ["İkimiz birden sevinebiliriz göğe bakalım", "seviyorum seni ekmeği tuza banıp yer gibi","Bütün kara parçalarında, Afrika hariç değil"]
e_mail = ["e-posta gönder","posta gönder","mail gönder","email gönder","e-mail gönder","gmail gönder","g-mail gönder"]
kapatma = ["sistemi kapat","uyu","kendini kapat","uyu uyu"]
kimsin = ["kimsin sen","sen kimsin","seni kim oluşturdu","kimsin","nesin","nesin sen","yaratıcın kim","kendini tanıt","tanıt","bu projenin amacı ne","amacın ne","amaç"]
saat = ["saat","kaç","saat kaç","kaç saat","zaman"]
donus = ["iyiyim sen","çok iyiyim","biraz keyifsizim"]
masalsoru = ["masal anlat", "bana masal anlat","hikaye anlat","bir şey anlat","masal oku","hikaye oku","masal",]
masaloku = ["Bir varmış bir yokmuş. Tavşan dağa küsmüş dağın haberi yokmuş. Gökten üç elma düşmüş, biri bana, biri dinleyenlere, diğeri de dünyadaki bütün iyi insanlara."]
tempature = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
nasilsincumeleleri = ["nasılsın","naber","ne haber","napıyorsun","nasıl gidiyor","naber","napıyon","nasıl","nabıyon","ne yapıyorsun", "nasılsın nasılsın"]
gun = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın","ayın kaçı"]
muzik = ["müzik","müzik oynat","müzik çal","çal müzik","müzik aç","aç müzik"]
muzik_kes = ["müzik kes","müziği kes","kes","dur","müziği durdur","kes müziği","dur dur müziği","dur dur","dur dur"]
ramm = ["ram hakkında bilgi","rem hakkında bilgi","ram","rem","bellek kullanımı","bellek","belleğin durumu","bellek hakkında bilgi"]
diskdurum = ["disk kullanımı","disk hakkında bilgi","diskim nasıl","disk durumu","disk ne kadar dolu","disk","diskim","harddisk","harddiskim","harddisk hakkında bilgi","harddisk durumu","teknik bilgi"]
blgs_kapat = ["bilgisayarımı kapat", "kapat bilgisayarı","kapat bilgisayarımı","bilgisayar kapan"]
blgs_ynden = ["bilgisayırımı yeniden başlat","yeniden başlat","başlat yeniden"]
blgs_otrm = ["oturumu kapat","oturumumu kapat","bilgisayar oturumunu kapat","uykuya al","bilgisayarı uykuya al","bilgisayar oturumumu kapat"]
yttube = ["youtube","aç youtube","youtube aç","you tube","aç you tube","you tube aç"]
srki_ytbe = ["şarkı aç","aç şarkı","youtube ile şarkı aç","you tube ile şarkı aç"]
arstr = ["araştır","google ile araştır","google araştır","wikipedia","wikipedia ile araştır","internette ara","ara"]


#-----------------------
#-----------------------


def asistan(command):

    if command in kimsin:
        a = """Ben gözlüğünüzün biricik asistanı İris. Size hizmet etmektir benim görevim"""
        konus(a)

    elif command in keyifsiz:

        konus("Şaka yaptım keyfim yerinde.")

    elif command in iyiyim:

        msg1 = ["iyi olmana sevindim","ah ne güzel","güzel","iyi olman mutluluk verici","sevindim","öyleyse çok iyi"]
        konus(random.choice(msg1))

    elif command in meraba:
        konus(random.choice(merbdonus))

    elif command in masalsoru:
        konus(random.choice(masaloku))

    elif command in sarksor:
        konus(random.choice(sarksoyle))

    elif command in beceri:
        konus("Geleceğin yegane teknolojisi olacak olan yapay zeka teknolojisini kullanarak kendi başıma görüntü işleyebiliyorum.")

    elif command in muzik:
        konus("Favori müziğinizi çalıyorum.")
        pygame.mixer.init()
        pygame.mixer.music.load("müzik.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
            
    elif command in siir:
        konus(random.choice(siiroku))

    elif command in olamazsin:
        konus("Anladım peki tamam.")

    elif command in teknofest:
        konus("TEKNOFEST Havacılık, Uzay ve Teknoloji Festivali, Türkiye'de düzenlenen havacılık, teknoloji ve uzay teknolojisi festivalidir.")


    elif command in iltifat:
        msg1 = ["Rica ederim","beni utandırıyorsun","utandım","Rica","yardımcı olabildiysem ne mutlu bana"]
        konus(random.choice(msg1))


    elif command in diskdurum:
        partition_usage = psutil.disk_usage('/')
        konus(f"  Toplam alan: {get_size(partition_usage.total)}")
        konus(f"  Kullanılan: {get_size(partition_usage.used)}")
        konus(f"  Boşta: {get_size(partition_usage.free)}")
        konus(f"  Yüzde: {partition_usage.percent}%")

        time.sleep(5)

 # -------------------------------------#


    elif command in blgs_kapat:
        konus("Tüm sistem 5 saniye içinde kapatılacak.")
        time.sleep(5)
        os.system("shutdown now -h") #raspbian için

    elif command in blgs_ynden:
        konus("Bilgisayarınız yeniden başlatılacak")
        time.sleep(3)
        os.system("shutdown -r now")#raspbian için

    elif command in blgs_otrm:
        konus("Sistem uykuya alınıyor")
        time.sleep(3)

        os.system("gnome-session-quit --no-prompt")
    elif "tarayıcımı kapat" in command:
        os.system("pkill firefox")

#-------------------kamera------------------#

    elif command in webcm:
        konus("Kameranız açılıyor")
        konus("Çıkış için ESC")
        konus("Kayıt etmek için boşluk tuşuna basınız.")
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        video_capture = cv2.VideoCapture(0) #yüzümüzü tanıtıyoruz

        img_counter = 0

        while True:

            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            k = cv2.waitKey(1)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )


            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


            cv2.imshow('FaceDetection', frame)

            if k%256 == 27: #ESC
                break

            elif k%256 == 32: #SPACE

                img_name = "facedetect_webcam_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        video_capture.release()
        cv2.destroyAllWindows()


    elif command in yttube:
        webbrowser.open("youtube.com")

    elif command in srki_ytbe:
        konus("Hangi şarkıyı açmamı istersiniz?")
        cevap1 = komutlar()
        results = YoutubeSearch(cevap1, max_results=1).to_dict()
        for v in results: #ilk sonucu açıyor
            print('https://www.youtube.com.tr' + v['link'])
            time.sleep(2)
        konus("Bu şarkıyı açmamı istermisiniz?")
        cevap2 = komutlar()
        if "aç" in cevap2 or "evet" in cevap2 or "evet aç" in cevap2:
            konus("Açılıyor")
            webbrowser.open('https://www.youtube.com.tr' + v['link'])
        if "hayır" in cevap2:
            konus("Tamam, işlemi iptal ediyorum")


    elif command in nasilsincumeleleri:
        msg = donus
        konus(random.choice(msg))

    elif command in saat:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        konus(f"Efendim, şuan saat {strTime} ")

    elif command in gun:
        strDay = datetime.datetime.now().strftime("%B %d %A")
        konus(f"Bugün günlerden {strDay} ")


    elif command in arstr:
        outputList = []
        konus("Ne araştırmalıyım?")
        cevap = komutlar()
        command = command.replace("wikipedia", "")
        wikipedia.set_lang("tr")
        results = wikipedia.summary(cevap, sentences=2)  # 2 cümleyi al
        konus(results)  # oku

    elif command in kapatma:
        konus("Tamam")
        konus("Hoşçakal, iyi günler")
        sys.exit()

    elif command in tempature: #hava durmu
        owm = pyowm.OWM("a45cb6af8b7682e70f11a79d6d993e45") #API key sanırım 60 gün geçerli
        sf = owm.weather_at_place("İstanbul, pendik")
        weather = sf.get_weather()
        w = sf.get_weather()
        a = int(weather.get_temperature("celsius")["temp"])
        wind = w.get_wind()
        h = weather.get_humidity() #-----nem
        konus("Hava sıcaklığı " + str(a) + " derece")
        konus("Rüzgar " + str(wind["speed"]) + " kilometre hızında")
        konus("Nem oranı ise %" + str(h))


##---------------------çeviri-----------##

    elif "çevir" in command or "çeviri" in command or "çevirsene" in command:
        konus("Lütfen çevireceğim kelimeyi söyleyin")
        cevi = komutlar()
        translator = Translator()
        command = cevi.replace("cevi", "")
        translated = translator.translate(command,src = "tr", dest = "en")
        konus("Söylediğiniz kelimenin ingilizcede karşığılı " + str(translated.text))

##-------------------------------##

    elif command in e_mail:
        konus("Alıcı kim?")
        alici = komutlar()

        if "taha" in alici:
            konus("Ne yazmalıyım?")
            content = komutlar()

            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("teknofest6@gmail.com", "Aa12345678a")
            mail.sendmail("Taha","0tahasahin@gmail.com",content)
            mail.close()

            konus("Posta gönderildi")

        if "ziya" in alici:

            konus("Ne yazmalıyım?")
            content = komutlar()

            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("teknofest6@gmail.com", "Aa12345678a")
            mail.sendmail("Ziya Akhan", "ziyaakhan29@gmail.com",content)
            mail.close()

            konus("Posta gönderildi")
    else:

        print("Algılanan: " + command)
        konus("Böyle bir komut yok. İnternette arayayım mı?" + command)
        cevap3 = komutlar()
        if "evet" in cevap3 or "ara" in cevap3 or "evet ara" in cevap3:
            konus("aranıyor")
            command = command.replace("wikipedia", "")
            wikipedia.set_lang("tr")
            results = wikipedia.summary(command, sentences=2)
            konus(results)  # oku

        if "hayır" in cevap3:
            konus("Tamam, işlemi iptal ediyorum.")

        time.sleep(2)

while True:
    command = komutlar()
    command = command.lower()
    asistan(command)

