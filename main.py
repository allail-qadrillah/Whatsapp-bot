import moviepy.editor as mp
from requests import api
import telebot
from telebot import types
import datetime
import time
from urllib.request import urlopen
import urllib
import json
import requests
import random
import os
from instascrape import *

bot = telebot.TeleBot("5049086779:AAGUeZhsHHBT7x250K0Wc1zGzYXjrrDbjv8")


def log(message, perintah):
    global jam, menit
    jam = time.strftime('%H')
    jam = int(jam)+7
    menit = int(time.strftime('%M'))
    detik = int(time.strftime('%S'))
    waktu = f"{jam} : {menit} : {detik}"
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    # TAMBAHKAN TEXT KE FILE .txt
    text = f"{waktu} > {nama} {nama_akhir} < {perintah} "
    print(text)
    bot.send_message(-524462976, text)


def getData(link):          # dapatkan data dari api
    url = requests.get(link)
    data = url.json()
    return data


def unduhVideo(video, namaFile):
    page = requests.get(video)
    with open(namaFile, 'wb') as file:
        file.write(page.content)


def unduhMusik(musik, namaFile):
    page = requests.get(musik)
    with open(namaFile, 'wb') as file:
        file.write(page.content)


def markupVideo(pesan, callback):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        pesan, callback_data=callback)
    markup.row(item)
    return markup


def markupVideoDuaButtton(pesan1, pesan2, callback1, callback2):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(pesan1, callback_data=callback1)
    item2 = types.InlineKeyboardButton(pesan2, callback_data=callback2)
    markup.row(item1)
    markup.row(item2)
    return markup


def updateStatus(menu, status):
    """menu paste > {hurufbesar}nama
       menu tulis > {sesuai dg namanya}"""
    file = open("status.json", "rb")  # buka file

    readJson = json.load(file)  # load data jsonnya
    readJson[menu] = status

    file = open("status.json", 'w')  # ubah isinya
    json.dump(readJson, file)
    file.close()


def panggilStatus(menu):
    file = open("status.json", "rb")  # buka file

    readJson = json.load(file)  # load data jsonnya
    status = readJson[menu]
    file.close()
    return status


# Kirim pesan keseluruh pengguna
idPengguna = ['1214473324', '1235828634', '1318920284', '1362906837', '1090735758', '1743797778', '261671993', '1965688888', '866672023', '1287257408', '1016186562', '1353477204', '1055650611', '2086602433', '1373534243', '922121235', '879463999', '1797875525', '1357555222', '1259366236', '1264335154', '1298532885', '5021016236', '1374964362', '5059892861', '1377131418', '5099128814', '5054461679', '2086547882', '852467060', '1666222581', '2052130877',
              '1298723696', '5080160424', '1158356287', '1446252254', '1373952237', '1414972369', '1158847026', '1768355373', '1105416796', '1189799968', '2128536417', '1573103212', '2138827758', '891498521', '1919922736', '5289330142', '1810014986', '1773122100', '1871920175', '5037141584', '1394568739', '905180125', '5250836836', '2096415607', '1640238613', '1929679916', '5211524564', '1060660338', '1160665729', '1359609332', '1833571121', '2088559067', 952773380]


@bot.message_handler(commands=['kirimGambar'])
def sendImage(message):
    unduhVideo(message.text[13:], 'gambar.jpg')
    for i in idPengguna:
        bot.send_photo(i, open('gambar.jpg', 'rb'))


@bot.message_handler(commands=['kirimPesan'])
def sendImage(message):
    pesan = 0
    for i in idPengguna:
        bot.send_message(i, message.text[12:])
        pesan += 1
        print(pesan)


@bot.message_handler(commands=['start'])
def downloadvidtiktok(message):
    bot.send_message(message.chat.id,
                     f'''Halo {message.from_user.first_name}
Perkenalkan saya Downloader_bot yang akan membantu anda mengunduh konten social media, berikut command yang tersedia :
1️⃣ Tiktok
1. download video tiktok nowm = paste url di chat
unduh musik click button

2️⃣ Instagram
1. download video post/reels/tv = paste url di chat
2. download insta stories = /igs_username
ex : /igs allailqadrillah_
3. stalking akun = /igstalk username
note : 'tidak perlu menggunakan @, dan username harus detail'

3️⃣ Twitter
1. download video twitter = paste url di chat

4️⃣ Facebook
1. download video Facebook = paste url di chat

5️⃣ Youtube
1. download musik youtube = paste url di chat

6️⃣ SoundCloud
1. download musik soundCloud = paste url di chat

7️⃣ Joox
1. download musik joox = /joox_judulLagu
ex : /joox Alan Walker - Different World
note : 'judul lagunya harus detail'
    ''', )

    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        'Message Developer 🧑🏻‍💻', url='https://telegram.me/Qadrillah')
    markup.row(item)
    bot.send_message(
        message.chat.id, 'jika ada fitur yang ingin ditambahkan ataupun bot terdapat masalah, bisa klik button dibawah', reply_markup=markup)
    bot.send_message(-515995341,
                     f"{message.from_user.first_name} {message.from_user.last_name} - {message.chat.id}")


@bot.message_handler(commands=['menu'])
def downloadvidtiktok(message):
    dataStatus = [panggilStatus('Tiktok'),  # 0
                  panggilStatus('Instagram'),  # 1
                  panggilStatus('igs'),  # 2
                  panggilStatus('igStalk'),  # 3
                  panggilStatus('Twitter'),
                  panggilStatus('Youtube'),
                  panggilStatus('SoundCloud'),
                  panggilStatus('Joox'),  # 7
                  panggilStatus('Facebook')]
    bot.send_message(message.chat.id,
                     f'''Halo {message.from_user.first_name}👋
berikut command yang tersedia :
1️⃣ Tiktok
1. video Tiktok nowm{dataStatus[0]} = paste url di chat
unduh musik click button

2️⃣ Instagram
1. video post/reels/tv{dataStatus[1]} = paste url di chat
2. stories{dataStatus[2]} = /igs username
ex : /igs allailqadrillah_
3. stalking akun{dataStatus[3]} = /igstalk username
note : 'tidak perlu menggunakan @, dan username harus detail'

3️⃣ Twitter
1. video Twitter{dataStatus[4]} = paste url di chat

4️⃣ Facebook
1. download video Facebook{dataStatus[8]} = paste url di chat

5️⃣ Youtube
1. audio Youtube{dataStatus[5]} = paste url di chat

6️⃣ SoundCloud
1. musik SoundCloud{dataStatus[6]} = paste url di chat

7️⃣ Joox
1. musik Joox{dataStatus[7]} = /joox judulLagu
ex : /joox Alan Walker - Different World
note : 'judul lagunya harus detail'

    ''')


@bot.message_handler(commands=['tentang'])
def downloadvidtiktok(message):
    bot.send_message(message.chat.id,
                     f'''Halo {message.from_user.first_name}👋 berikut info tentang saya :
- Dibuat menggunakan Python
- Tubuh saya ada di heroku
- Otak saya ada di github''')
    bot.send_message(message.chat.id,
                     f'''
Credits API
- zenzapi.xyz
- hadi-api.herokuapp.com
- instagram47.p.rapidapi.com''')


"""                                      CALLLBACKKK KETIKA BUTTON DI CLICK                                                         """


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    # TIKTOK BUTTON ACTION
    if call.data in callbackOriTiktok:
        bot.send_chat_action(call.from_user.id, "upload_audio")
        bot.send_audio(call.from_user.id, open(f"{call.data}.mp3", 'rb'))
        log(call.message, f"TIKTOK AUDIO")

    if call.data in callbackVidTiktok:
        bot.send_chat_action(call.from_user.id, "upload_audio")
        # convert video menjadi audio
        clip = mp.VideoFileClip(f"{call.data.split('-')[0]}.mp4")
        clip.audio.write_audiofile(f"{call.data}VID.mp3")
        bot.send_audio(call.from_user.id, open(
            f"{call.data}VID.mp3", 'rb'))
        log(call.message, f"TIKTOK AUDIO CONVERT")


# key ZENZAPI
api_key = ["b9b38e428d49"]
"""                                          TIKTOK DOWNLOADER                                                                  """
callbackOriTiktok = []
callbackVidTiktok = []


@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):
    # dapatkan data dari api hingga berhasil
    try:
        bot.send_chat_action(message.chat.id, "upload_video")
        link = f"https://hadi-api.herokuapp.com/api/tiktok?url={message.text}"
        dataTiktok = getData(link)
        # dapatankan link yang diperlukan
        urlNOWM = dataTiktok['result']['video']['nowm']
        urlAudio = dataTiktok['result']['audio_only']['audio1']

        file = f"{message.from_user.first_name}_{message.text.split('/')[3]}"
        file2 = f"{message.from_user.first_name}_{message.text.split('/')[3]}-video"
        # unduh file
        bot.send_chat_action(message.chat.id, "upload_video")
        unduhVideo(urlNOWM, f"{file}.mp4")
        markup = markupVideoDuaButtton(
            'Download Musik Original 🎶', 'Download Musik Video 🎶', file, file2)
        # kirim video dan button untuk mendownload musik
        bot.send_video(message.chat.id, open(
            f"{file}.mp4", 'rb'), reply_markup=markup)
        callbackOriTiktok.append(file)
        callbackVidTiktok.append(file2)

        log(message, f"TIKTOK VID HADI ")
        unduhMusik(urlAudio, f"{file}.mp3")

    except:                                 # API CADANGAN
        i = len(api_key) - 1
        while True:
            bot.send_chat_action(message.chat.id, "upload_video")
            link = f"https://zenzapi.xyz/downloader/musically?url={message.text}&apikey={api_key[i]}"
            dataTiktok = getData(link)
            if dataTiktok['status'] == False:
                i -= 1
            elif dataTiktok['status'] == "OK":
                break
        # ambil url yang diperlukan
        urlNOWM = dataTiktok['result']['nowm']
        urlAudio = dataTiktok['result']['audio']

        file = f"{message.from_user.first_name}_{message.text.split('/')[3]}"
        file2 = f"{message.from_user.first_name}_{message.text.split('/')[3]}-video"
        # unduh file
        bot.send_chat_action(message.chat.id, "upload_video")
        unduhVideo(urlNOWM, f"{file}.mp4")
        markup = markupVideoDuaButtton(
            'Download Musik Original 🎶', 'Download Musik Video 🎶', file, file2)
        # kirim video dan button untuk mendownload musik
        bot.send_video(message.chat.id, open(
            f"{file}.mp4", 'rb'), reply_markup=markup)
        callbackOriTiktok.append(file)
        callbackVidTiktok.append(file2)

        log(message, f"TIKTOK VID ZENZ- {message.text}")
        unduhMusik(urlAudio, f"{file}.mp3")


# IG image/REELS/TV s
@bot.message_handler(regexp='https://www.instagram.com/')
def downloadvidinstagram(message):

 # scrape konten

    url = f"https://www.instagram.com/p/{message.text.split('/')[-2]}/?__a=1"
    SESSIONID = '2135077396%3ApJrfONzhO4FjRO%3A13'  # ganti session id
    headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
               "cookie": f"sessionid={SESSIONID};"}
    r = requests.get(url, headers=headers)
    data = r.json()["items"]

    # jika konten berslide
    if 'carousel_media' in data[0]:
        for i in range(len(data[0]['carousel_media'])):
            if data[0]['carousel_media'][i]['media_type'] == 2:  # jika video
                url = data[0]['carousel_media'][i]['video_versions'][0]['url']
                bot.send_chat_action(message.chat.id, "upload_video")
                unduhVideo(
                    url, f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.mp4")
                bot.send_video(message.chat.id, open(
                    f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.mp4", "rb"))

            else:  # jika gambar
                url = data[0]['carousel_media'][i]['image_versions2']['candidates'][i]['url']
                bot.send_chat_action(message.chat.id, "upload_photo")
                unduhVideo(
                    url, f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.jpg")
                bot.send_photo(message.chat.id, open(
                    f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.jpg", "rb"))
        log(message,
            f"IG POST SLIDE {data[0]['user']['username']}_{message.text.split('/')[-2]}_{len(data[0]['carousel_media'])}")
    # jika hanya konten biasa
    else:
        if data[0]['media_type'] == 2:  # jika video
            url = data[0]['video_versions'][0]['url']
            bot.send_chat_action(message.chat.id, "upload_video")
            unduhVideo(
                url, f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.mp4")
            bot.send_video(message.chat.id, open(
                f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.mp4", "rb"))
            log(message,
                f"IG VIDEO {data[0]['user']['username']}_{message.text.split('/')[-2]}")

        else:  # jika gambar
            url = data[0]['image_versions2']['candidates'][0]['url']
            bot.send_chat_action(message.chat.id, "upload_photo")
            unduhVideo(
                url, f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.jpg")
            bot.send_photo(message.chat.id, open(
                f"{data[0]['user']['username']}_{message.text.split('/')[-2]}.jpg", "rb"))
            log(message,
                f"IG Photo {data[0]['user']['username']}_{message.text.split('/')[-2]}")


# key rapid api https://rapidapi.com/Prasadbro/api/instagram47/                                                             """
api2 = ["c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c",
        "f355e8c71bmsh2f12c8e8772a755p1aba64jsn14d36932fc37"]


# FULL STORY downloader
@bot.message_handler(commands=['igs'])
def downloadStoriesIG(message):
    # cari id dari username
    try:   # eror username
        key = 0
        while True:  # ambil api key yang masih berlaku
            try:
                url = "https://instagram47.p.rapidapi.com/get_user_id"
                querystring = {"username": message.text.split(' ')[1]}
                headers = {
                    'x-rapidapi-host': "instagram47.p.rapidapi.com",
                    'x-rapidapi-key': api2[key]}
                response = requests.request(
                    "GET", url, headers=headers, params=querystring)
                dataID = json.loads(response.text)

                if dataID['status'] == "Success":
                    ID = dataID["user_id"]
                    break
            except:
                key += 1
                continue

        try:  # dapatkan stories
            url = "https://instagram-stories1.p.rapidapi.com/v1/get_stories"
            querystring = {"userid": ID}
            headers = {
                'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
                'x-rapidapi-key': api2[key]}
            response = requests.request(
                "GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)

            if data['status'] == 'Fail':  # kirim pesan untuk setiap warning
                bot.send_message(message.chat.id, data['Warning'])
            elif data['totalStories'] == 0:  # kirim pesan jika storiesnya nol
                bot.send_message(
                    message.chat.id, "user tidak memiliki stories!")

            else:
                # unduh story
                data = data['downloadLinks']
                for i in range(0, int(len(data))):  # unduh setiap stories
                    if data[i]["media_type"] == 2:  # stories video
                        bot.send_chat_action(
                            message.chat.id, "upload_video")
                        namaFile = f"{message.text[5:]}_{i}.mp4"
                        snap = data[i]["url"]
                        unduhVideo(snap, namaFile)
                        bot.send_video(message.chat.id,
                                       open(namaFile, 'rb'))

                    elif data[i]["media_type"] == 1:  # stories image
                        bot.send_chat_action(
                            message.chat.id, "upload_photo")
                        namaFile = f"{message.text[5:]}_{i}.jpg"
                        snap = data[i]["url"]
                        unduhVideo(snap, namaFile)
                        bot.send_photo(message.chat.id,
                                       open(namaFile, 'rb'))

                bot.send_message(
                    message.chat.id, f"total {len(data)} stories")
                log(message, f"IG STORY {key} {message.text[5:]}")
                updateStatus('igs', '✅')
        except:  # kirim pesan jika terdapat error
            bot.send_message(
                message.chat.id, "tidak dapat mengunduh story :(")
            bot.send_message(
                message.chat.id, "jika masalah masih berlanjut, hubungi developer yaa")

    except:  # eror username
        bot.send_message(message.chat.id, dataID['Warning'])
        updateStatus('igs', '❎')


# stalk akun instagram
@bot.message_handler(commands=['igstalk'])
def downloadStoriesIG(message):
    try:
        bot.send_chat_action(message.chat.id, "upload_photo")
        url = f"https://www.instagram.com/{message.text.split(' ')[1]}/?__a=1"
        SESSIONID = '51038695795%3AreeyFZX3qR6BBo%3A6'  # ganti session id
        headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
                   "cookie": f"sessionid={SESSIONID};"}
        r = requests.get(url, headers=headers)
        data = r.json()['graphql']

        user = data['user']
        unduhVideo(user['profile_pic_url_hd'],
                   f"{message.text.split(' ')[1]}.jpg")
        bot.send_photo(message.chat.id, open(
            f"{message.text.split(' ')[1]}.jpg", 'rb'))
        bot.send_chat_action(message.chat.id, "typing")
        output = f"""
Nama : {user['full_name']}
Username : {message.text.split(' ')[1]}
Category : { user['category_name']}
Private? : {user['is_private']}
Followers : {user['edge_followed_by']['count']}
Following : {user['edge_follow']['count']}
Postingan : {user['edge_owner_to_timeline_media']['count']}
bio : 
{user['biography']}
"""

        bot.send_message(message.chat.id, output)
        log(message, f"igStalk {message.text.split(' ')[1]}")
        updateStatus('igStalk', '✅')
    except:
        bot.send_message(message.chat.id, "username tidak ditemukan")
        updateStatus('igStalk', '❎')


"""                                             JOOX                                                            """
callbackJoox = []


@bot.message_handler(commands=['joox'])
def downloadjoox(message):
    # ambil api key yang tidak kadaluarsa

    try:
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(
                f"https://zenzapi.xyz/downloader/joox?query={message.text[6:]}&apikey={api_key[i]}")
            dataJoox = url.json()

            if dataJoox['status'] == False:
                i += 1
            elif dataJoox['status'] == "OK":
                break

        page = dataJoox['result']['mp3Link']
        laguJoox = dataJoox['result']['lagu']

        unduhMusik(page, f"{laguJoox}.mp3")
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, open(f"{laguJoox}.mp3", 'rb'))
        log(message, f"JOOX {i} {laguJoox}")
        updateStatus('Joox', '✅')
        # buat tombol untuk mendapatkan lirik lagunya
    except:
        bot.send_message(
            message.chat.id, f"tidak dapat mengunduh musik {message.text[6:]} :(")
        updateStatus('Joox', '❎')


"""
                                   YOUTUBE MUSIK DOWNLOADER                         
"""


@bot.message_handler(regexp='youtu')
def downloadMusikYoutube(message):
    try:
        i = 0
        while True:

            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(
                f"https://zenzapi.xyz/downloader/ytmp3?url={message.text}&index=2&apikey={api_key[i]}")
            data = url.json()

            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break

        page = data['result']['url']
        title = data['result']['title']

        unduhMusik(page, f"{title}.mp3")
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, open(f"{title}.mp3", 'rb'))
        log(message, f"YOUTUBE {i} {title}")
        updateStatus('Youtube', '✅')
    except:
        bot.send_message(message.chat.id, f"tidak dapat mengunduh musik :(")
        updateStatus('Youtube', '❎')


"""                                 SOUND CLOUND DOWNLOADER                                                                             """


@bot.message_handler(regexp='https://soundcloud.com/')
def downloadjoox(message):
    try:
        # ambil api key yang tidak kadaluarsa
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(
                f"https://zenzapi.xyz/downloader/soundcloud?url={message.text.split('?')[0]}&apikey={api_key[i]}")
            data = url.json()

            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break

            # doenload musik
        page = data['result']['url']
        title = data['result']['title']

        unduhMusik(page, f"{title}.mp3")
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, open(f"{title}.mp3", 'rb'))
        log(message, f"SOUNDCLOUD {i} {title}")
        updateStatus('SoundCloud', '✅')
    except:
        bot.send_message(message.chat.id, f"tidak dapat mengunduh musik :(")
        updateStatus('SoundCloud', '❎')


"""                                TWITTER DOWNLOADER                                    """
# VIDEO POST, REELS and TV downloader


@bot.message_handler(regexp='https://twitter.com')
def downloadvidtiktok(message):
    try:
        bot.send_chat_action(message.chat.id, "upload_video")
    # ambil apikey satu persatu
        i = 0
        while True:
            url = requests.get(
                f"https://zenzapi.xyz/downloader/twitter?url={message.text.split('?')[0]}&apikey={api_key[i]}")
            data = url.json()
            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break

        video = data['result']['HD']

        unduhVideo(video, f"{message.from_user.first_name}_twitter.mp4")
        bot.send_video(message.chat.id, open(
            f"{message.from_user.first_name}_twitter.mp4", 'rb'))
        log(message, f"TWITTER {i} ")
        updateStatus('Twitter', '✅')
    except:
        bot.send_message(message.chat.id, f"tidak dapat mengunduh video :(")
        updateStatus('Twitter', '❎')


"""                                 FACEBOOK DONWLOADER             """


@bot.message_handler(regexp='https://fb.')
def downloadvidfacebook(message):
    try:
        bot.send_chat_action(message.chat.id, "upload_video")
        url = requests.get(
            f"https://zenzapi.xyz/downloader/facebook?url={message.text}&apikey=b9b38e428d49")
        data = url.json()

        video = data['result']['medias'][0]['url']

        unduhVideo(video, f"{message.from_user.first_name}_facebook.mp4")

        bot.send_video(message.chat.id, open(
            f"{message.from_user.first_name}_facebook.mp4", 'rb'))
        log(message, f"Facebook  ")
        updateStatus('Facebook', '✅')
    except:
        bot.send_message(message.chat.id, f"tidak dapat mengunduh video :(")
        updateStatus('Facebook', '❎')


bot.send_message(1214473324, "bot starting!!")
print("bot  running...!! ")
bot.polling()
