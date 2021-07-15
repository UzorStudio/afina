import telebot as telebot
from telebot import types
import baseBot
import random

bot = telebot.TeleBot('1855610026:AAERud55hTLs9VK5h_q2Jizq10xYzQlNwLM')
admins = [811017432, 149750441]
#bd = baseBot.UserNOffers("localhost")

bd = baseBot.UserNOffers("mongodb+srv://admin:yapidor@cluster0.dautj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    if bd.getuser(message.chat.id) is None:
        bd.regUser(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="😂 Фемомем 😂"))
    keyboard.add(types.KeyboardButton(text="© Фемцитаты ©"))
    keyboard.add(types.KeyboardButton(text="📖 Фемофакты 📖"))
    keyboard.add(types.KeyboardButton(text="🎬 Фемтиктоки 🎬"))
    keyboard.add(types.KeyboardButton(text="🗣 Крики афины 🗣"))
    keyboard.add(types.KeyboardButton(text="Памагити :,("))
    keyboard.add(types.KeyboardButton(text="Предложить"))
    keyboard.add(types.KeyboardButton(text="bot: кто я?"))

    for i in admins:
        if message.chat.id == i:
            keyboard.add(types.KeyboardButton(text="Модерировать"))
            keyboard.add(types.KeyboardButton(text="Отправить пост"))
            keyboard.add(types.KeyboardButton(text="Добавить крик"))

    bot.send_message(message.chat.id, "Выбери действие и подпишись на канал\nhttps://t.me/feminismnaglyadno",
                     reply_markup=keyboard)


@bot.message_handler(content_types="text")
def Menu(message):
    if message.text == "bot: кто я?":
        bot.send_message(message.chat.id, """Да защитит тебя патриархат от феминизма, мой дорогой друг!
 
⚠️ Я ПРОТИВ НАСИЛИЯ И БУЛЛИНГА
Я НЕ НЕСУ ОТВЕТСТВЕННОСТИ ЗА ВЫСКАЗЫВАНИЯ УЧАСТНИКОВ, НО СТАРАЮСЬ ПРЕСЕКАТЬ ИХ НА КОРНЮ.
ВСЕ, ЧТО ТУТ РАЗМЕЩЕНО, НЕСЕТ СУГУБО РАЗВЛЕКАТЕЛЬНО-ПОУЧИТЕЛЬНЫЙ ХАРАКТЕР И НЕ ПРИЗЫВАЕТ К НЕНАВИСТИ К ОПРЕДЕЛЕННЫМ КЛАССАМ, ДВИЖЕНИЯМ И ВЫБОРУ ЛЮДЕЙ. ЛЮБОЙ КОНТЕНТ НЕ ИМЕЕТ ЦЕЛИ ОСКОРБИТЬ ИЛИ УНИЗИТЬ КОГО-ЛИБО. ⚠️

Ты находишься в безопасном пространстве, где можешь ссаться кипятком от смеха и эдьюкейтить себя, чтобы быть выше и сильнее феминисток!

Каждый участник бота может являться неотъемлемой частью
сотворения адекватности и просвещения! Для вас я сделала предложку и верю, что вы будете правильно ей пользоваться.
(А не как фем-ки своей вагиной)(шутка) 

Фемомемы - мемы про феминисток (туда же будут попадаться мемы про ЛГБТ, БЛМ и остальная толерастия).

Фемцитаты - собираем цитаты феминисток, а потом выдается цитата со словами в рандомном порядке. 

Фемтиктоки - мемные и интересные видосы про феминизм и кто его населяет. 

Фемофакты - кнопочка для тех, кто пришел подтянуть предметы, которые вы так любили пропускать в школе: историю, обществознание психологию, политологию, чутка русского языка; и немного посамообразовываться.

🤝 Обратная связь:

💖 Мой папочка, здравый смысл: 

@hetkelt

(Сделает тебе такого-же прекрасного бота, как я) 
__________________________

💖 Моя мамочка, искоренение невежества:

@Forever_Sleep

tiktok.com/@xenasleepforever

Inst

 (http://instagram.com/_x_x.death.x_x_)Вк (https://vk.com/all_we_need_are_peace_love_music)""")
    try:
        if message.text == "😂 Фемомем 😂":
            print(len(bd.getMemOffer()))
            mm = bd.getMemOffer()[random.randint(0, len(bd.getMemOffer()) - 1)]["offerData"]
            print(mm + "femmem")
            bot.send_photo(message.chat.id, mm)
        if message.text == "© Фемцитаты ©":
            txt = bd.getCitOffer()[random.randint(0, len(bd.getCitOffer()) - 1)]["offerData"].split(" ")
            txt2 = bd.getCitOffer()[random.randint(0, len(bd.getCitOffer()) - 1)]["offerData"].split(" ")
            txt3 = txt + txt2
            txt4 = []
            i = 0
            j = random.randint(2, 5)
            while i != j:
                if len(txt3) > 0:
                    a = txt3[random.randint(0, len(txt3) - 1)]
                    del txt3[txt3.index(a)]
                    txt4.append(a)
                i += 1

            txt4 = " ".join(txt4) + "\n© Одна фемка"

            bot.send_message(message.chat.id, txt4)
        if message.text == "📖 Фемофакты 📖":
            bot.send_message(message.chat.id, "Фемки сосут хуй (Просто хорошо это скрывают) 😉")
        if message.text == "🎬 Фемтиктоки 🎬":
            tk = bd.getTikOffer()[random.randint(0, len(bd.getTikOffer()) - 1)]["offerData"]
            bot.send_video(message.chat.id, tk)
        if message.text == "Предложить":
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="😂 Фемомем 😂", callback_data="mem"))
            keyboard.add(types.InlineKeyboardButton(text="© Фемцитаты ©", callback_data="cit"))
            keyboard.add(types.InlineKeyboardButton(text="🎬 Фемтиктоки 🎬", callback_data="tik"))
            bot.send_message(chat_id=message.chat.id, text="Что предложим?", reply_markup=keyboard)
        if message.text == "🗣 Крики афины 🗣":
            voc = bd.getVocOffer()[random.randint(0, len(bd.getVocOffer()) - 1)]
            print(voc)
            bot.send_voice(message.chat.id, voc["offerData"], voc["caption"])
        if message.text == "Памагити :,(":
            bot.send_message(message.chat.id,"""СБЕРБАНК: 4276 5500 5659 2077

DonationAlerts: https://www.donationalerts.com/r/forever_sleep

Обязательно подпиши "Афина, живи!"
Спасибо, сладенький! :*
Каждое воскресенье будет список топ донатеров! 💖""")
    except ValueError:
        bot.send_message(message.chat.id,"Ничего нет в этой рубрике")

    for i in admins:
        if message.chat.id == i:
            if message.text == "Модерировать":
                try:
                    off = bd.getAllOffer()[random.randint(0, len(bd.getAllOffer()) - 1)]
                    bd.setModer(message.chat.id, off["_id"])
                    stri = "Всего предложек: " + str(len(bd.getAllOffer()))
                    bot.send_message(message.chat.id, stri)
                    print(off)
                    if off["type"] == "tik":
                        keyboard = types.InlineKeyboardMarkup()
                        keyboard.add(types.InlineKeyboardButton(text="❤", callback_data="likeadm"))
                        keyboard.add(types.InlineKeyboardButton(text="💔", callback_data="dislikeadm"))
                        bot.send_video(message.chat.id, off["offerData"], reply_markup=keyboard)
                    if off["type"] == "mem":
                        keyboard = types.InlineKeyboardMarkup()
                        keyboard.add(types.InlineKeyboardButton(text="❤", callback_data="likeadm"))
                        keyboard.add(types.InlineKeyboardButton(text="💔", callback_data="dislikeadm"))
                        bot.send_photo(message.chat.id, off["offerData"], reply_markup=keyboard)
                    if off["type"] == "cit":
                        keyboard = types.InlineKeyboardMarkup()
                        keyboard.add(types.InlineKeyboardButton(text="❤", callback_data="likeadm"))
                        keyboard.add(types.InlineKeyboardButton(text="💔", callback_data="dislikeadm"))
                        bot.send_message(message.chat.id, off["offerData"], reply_markup=keyboard)
                    if off["type"] == "voc":
                        print(off)
                        keyboard = types.InlineKeyboardMarkup()
                        keyboard.add(types.InlineKeyboardButton(text="❤", callback_data="likeadm"))
                        keyboard.add(types.InlineKeyboardButton(text="💔", callback_data="dislikeadm"))
                        bot.send_voice(message.chat.id, off["offerData"], caption=off["caption"])
                        bot.send_message(message.chat.id, "Оцени", reply_markup=keyboard)
                except ValueError:
                    bot.send_message(message.chat.id, "Все кончилось!")

            if message.text == "Отправить пост":
                bot.send_message(message.chat.id, "пришлите картинку на пост")
                bot.register_next_step_handler(message, postImg)
            if message.text == "Добавить крик":
                bot.send_message(message.chat.id, "Запиши голосовое, радость чудесная)")
                bot.register_next_step_handler(message, voice_processing)



@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    for i in admins:
        if message.chat.id == i:
            print(message)
            bot.send_voice(message.chat.id, message.voice.file_id)
            bd.OfferCreate(message.chat.id, message.voice.file_id, "voc")
            bot.send_message(message.chat.id, "Напиши теперь текст для описания")
            bot.register_next_step_handler(message, voice_caption)


def voice_caption(message):
    bd.AddOfferCaption(message.chat.id, message.text)


@bot.message_handler(content_types="video")
def video(message):
    try:
        if bd.getuser(message.chat.id)["change"] == "tik":
            bd.OfferCreate(message.chat.id, message.video.file_id, "tik")
        print(message.video.file_id)
    except (AttributeError, TypeError):
        bot.send_message(message.chat.id, "Сюда можно присылать только Видео!")


@bot.message_handler(content_types=['photo'])
def photo(message):
    try:
        if bd.getuser(message.chat.id)["change"] == "mem":
            bd.OfferCreate(message.chat.id, message.photo[0].file_id, "mem")
        print(message.photo[0].file_id)
    except (AttributeError, TypeError):
        bot.send_message(message.chat.id, "Сюда можно присылать только Фото!")


@bot.message_handler(content_types=['text'])
def text(message):
    try:
        if bd.getuser(message.chat.id)["change"] == "cit":
            bd.OfferCreate(message.chat.id, message.text.lower(), "cit")
        print(message.text)
    except (AttributeError, TypeError):
        bot.send_message(message.chat.id, "Сюда можно присылать только текст!")


def postImg(message):
    bd.NewPostImage(message.chat.id, message.photo[0].file_id)
    bot.send_message(message.chat.id, "теперь напиши текст!")
    bot.register_next_step_handler(message, postText)


def postText(message):
    bd.NewPostText(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Пост готов!")
    post = bd.NewPostGet(message.chat.id)
    usr = bd.getalluser()
    i = 0
    try:
        for u in usr:
            bot.send_photo(u["usrId"], post["img"], caption=post["text"])
            i += 1
    except:
        pass

    txt = "пост был отправлен людям в количестве: " + str(i)
    bot.send_message(message.chat.id, txt)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.message)
    if call.message:
        bd.setChange(call.message.chat.id, call.data)
        if call.data == "tik":
            bot.send_message(call.message.chat.id, "Отправьте видео боту")
            bot.register_next_step_handler(call.message, video)
        elif call.data == "mem":
            bot.send_message(call.message.chat.id, "Отправьте фото")
            bot.register_next_step_handler(call.message, photo)
        elif call.data == "cit":
            bot.send_message(call.message.chat.id, "Отправьте цитату в текстовом формате")
            bot.register_next_step_handler(call.message, text)

        elif call.data == "likeadm":
            bd.setOfferApp(bd.getuser(call.message.chat.id)["moder"], True)
            bot.delete_message(call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, "Одобрено!")
        elif call.data == "dislikeadm":
            bd.DellOffer(bd.getuser(call.message.chat.id)["moder"])
            bot.delete_message(call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, "Наухй!!")


bot.polling(none_stop=True)
