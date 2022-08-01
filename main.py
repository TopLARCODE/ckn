
import logging
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardMarkup, InlineKeybordButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import Database
import random
import datetime, threading, time
from datetime import timedelta
from pyqiwip2p import QiwiP2P
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests
    
now = datetime.datetime.now()
TOKEN = "5485987229:AAGdWZsT48YrlRcbhXr1HaPd6zh8DE1Xf4Y"
ADMIN_ID = "1764135502"
savedid = 1
bb = 1
b = 1
hello = 1
a = 1
cc = 1
aa = 1   
asdas = 1
lower = 1
sdsa = 1
sfsd = 1
moneyz = 1
teas = 1
nickfury = 1
nickfury2 = 1
nickfury3 = 1

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
now = datetime.datetime.now()
p2p = QiwiP2P(auth_key="eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjJkdmVwMS0wMCIsInVzZXJfaWQiOiI3OTE5ODIwNTUzOSIsInNlY3JldCI6IjYzNTRmZDc0MDZkY2E4ZjZhYTE1YWJmYjdlNGJmYzYxODc2OWM2OTgxZDAzODYzYWJkMzM2Mzg1NmExYzI5MTIifX0=")

try:
    print("Trying run server...")
    dp = Dispatcher(bot)
    print('Running server has no errors!\n')
except Exception as e:
    print('Error run server, info ->\n' + str(e))
    exit

db = Database('database.db')


mainMenu = InlineKeyboardMarkup(row_width=1)
btnAdd = InlineKeyboardButton(text="⤵️ Добавить В Чат", url="https://t.me/CKNgame_bot?startgroup=true")
mainMenu.insert(btnAdd)
mainMenu2 = InlineKeyboardMarkup(row_width=2)
btnAdd1 = InlineKeyboardButton(text="🧆  Собрать корм", callback_data="btnRandom")
btnAdd2 = InlineKeyboardButton(text="⬆️  Купить завод", callback_data="btnRandom2")
mainMenu2.insert(btnAdd1)
mainMenu2.insert(btnAdd2)
    
def seturl(url):
    global mainMenus
    mainMenus = InlineKeyboardMarkup(row_width=1)
    btnAdda = InlineKeyboardButton(text="💸 Оплатить", url=url)
    mainMenus.insert(btnAdda)

@dp.message_handler(text=['Донат'])
async def buy(message: types.Message):
    global bill
    global nickfury
    global nickfury2
    global nickfury3
    nickfury = message.from_user.id
    price = 5
    lifetime = 5
    comment = str(message.from_user.id) + "_" + str(random.randint(1000,9999))
    bill = p2p.bill(amount=price, lifetime=lifetime, comment=comment)
    link_oplata = bill.pay_url
    seturl(link_oplata)
    nickfury2 = db.get_nickname(nickfury)
    nickfury3 = nickfury
    await message.answer("[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Привет 👋\n\n💳 Cумма: `" + str(price) + "₽`\n⌚️ Действие: `5 минут`\nДля оплаты нажмите кнопку ниже 👇", reply_markup=mainMenus, parse_mode="Markdown")
    x = threading.Thread(target=functionoplata, args=(message,))
    x.start()
def functionoplata(message):
    oplata_time = datetime.datetime.now()
    datetime_delta = oplata_time + timedelta(minutes=5)
    while True:
        time.sleep(3)
        status = p2p.check(bill_id=bill.bill_id).status 
        if status == 'PAID':
            requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + str(nickfury) + "&text=[" + str(nickfury2) + "](tg://user?id=" + str(nickfury) + "), Спасибо за покупку 🧺&parse_mode=Markdown")
            break
        elif datetime.datetime.now() > datetime_delta:
            requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + str(nickfury) + "&text=[" + str(nickfury2) + "](tg://user?id=" + str(nickfury) + "), Счёт просрочен 📒&parse_mode=Markdown")
            break
    
@dp.message_handler(commands=['info'])
async def start(message: types.Message):
    if str(message.from_user.id) == ADMIN_ID:
        teas = message.text
        teas = teas.replace("  ", '')
        teas = teas.replace("/info ", '')
        try:
            text = db.get_info(teas)
            await bot.send_message(message.chat.id, text, parse_mode= 'Markdown')
        except:
            await bot.send_message(message.chat.id, "Syntax error.\nCorrect: `/info {id}`", parse_mode= 'Markdown')
    else:
        await bot.send_message(message.chat.id, "Oops!\nYour account don't have administator rights.", parse_mode= 'Markdown')

             
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        db.set_real(message.from_user.id, message.from_user.first_name)
        db.set_nickname(message.from_user.id, "Игрок")
        db.set_signup(message.from_user.id, "done")
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Привет 👋\nМечтал поиграть в функционального TG бота? 🤑\n\nНажимай на кнопку ниже для добавления в группу 👇 ", parse_mode= 'Markdown', reply_markup=mainMenu)
    else:
        await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Привет 👋", parse_mode= 'Markdown')
@dp.message_handler(text=['Б', 'б'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        db.set_real(message.from_user.id, message.from_user.first_name)
        db.set_nickname(message.from_user.id, "Игрок")
        db.set_signup(message.from_user.id, "done")
    db.set_real(message.from_user.id, message.from_user.first_name)
    math = randint(0,100)
    if math <= 40:
        db.set_kurs(ADMIN_ID, int(db.get_kurs(ADMIN_ID)) - 1)
    else:
        db.set_kurs(ADMIN_ID, int(db.get_kurs(ADMIN_ID)) + 1)
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "👫 [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + ")!\n├ 💰 Монет: *" + db.get_money(message.from_user.id) + "₽*\n├ 🧆 Корм: *" + db.get_korm(message.from_user.id) + "*\n├ 🏦 Банк: *" + db.get_bank(message.from_user.id) + "₽*".format(message.from_user), parse_mode= 'Markdown')
    else:
        await bot.send_message(message.chat.id, "👫 [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + ")!\n├ 💰 Монет: *" + db.get_money(message.from_user.id) + "₽*\n├ 🧆 Корм: *" + db.get_korm(message.from_user.id) + "*\n├ 🏦 Банк: *" + db.get_bank(message.from_user.id) + "₽*".format(message.from_user), parse_mode= 'Markdown')



    @dp.message_handler()
    async def bot_message(message: types.Message):
        if(not db.user_exists(message.from_user.id)):
            db.add_user(message.from_user.id)
            db.set_real(message.from_user.id, message.from_user.first_name)
            db.set_nickname(message.from_user.id, "Игрок")
            db.set_signup(message.from_user.id, "done")
        #print(message)
        db.set_real(message.from_user.id, message.from_user.first_name)
        math = randint(0, 100)
        if math <= 40:
            db.set_kurs(ADMIN_ID, int(db.get_kurs(ADMIN_ID)) - 1)
        else:
            db.set_kurs(ADMIN_ID, int(db.get_kurs(ADMIN_ID)) + 1)
        check = message.text.lower()
        global sdsa
        global moneyz
        global teas
        if sdsa == 10:
            if str(message.from_user.id) == ADMIN_ID:
                try:
                    test = int(message.text) - 1
                    db.set_moneyz(teas, check)
                    await bot.send_message(message.chat.id, "Nice, money has been setted.\n" + str(moneyz) + " -> " + str(db.get_moneyz(teas)) + "", parse_mode= 'Markdown')
                    sdsa = 1
                except:
                    await bot.send_message(message.chat.id, "Failed set `" + message.text + "`\nDon't allowed set VARCHAR balance", parse_mode= 'Markdown')
                    sdsa = 1
            else:
                pass
        if check.find("/grant") == 0:
            if str(message.from_user.id) == ADMIN_ID:
                teas = message.text
                teas = teas.replace("  ", '')
                teas = teas.replace("/grant ", '')
                
                moneyz = db.get_moneyz(teas)
                await bot.send_message(message.chat.id, "Great, now send sum which need add.\nPlayer value: " + moneyz + ".", parse_mode= 'Markdown')
                sdsa = 10
            else:
                await bot.send_message(message.chat.id, "Oops!\nYour account don't have administator rights.", parse_mode= 'Markdown')
        if check.find("казино") == 0:
            check = check.replace("казино ","")
            if check.find("  "):
                check = check.replace("  ", " ")
            check = check.replace(".","")
            checks = check
            checks = str(check)
            if checks.find("e") != -1:
                check = "%d" % float(check)
                check = str(check)
                z = str(check)
                z = z.replace(".0", "")
                check = str(z)
            global lower
            global sfsd
            try:
                if int(check) <= 9:
                    lower = 10
                else:
                    lower = 1
            except:
                    sfsd = 10
            if lower == 10:
                await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Минимальная ставка 10₽ 😟", parse_mode= 'Markdown')
            else:
                if sfsd == 10:
                    await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Невозможно распознать число 😟", parse_mode= 'Markdown')
                else:
                        if int(db.get_money(message.from_user.id)) - int(check) <= -1:
                            if message.chat.type == 'private':
                                await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), У вас недостаточно средств 😟", parse_mode= 'Markdown')
                            else:
                                await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), У вас недостаточно средств 😟", parse_mode= 'Markdown')
                        else:
                            save = check
                            math = randint(0, 200)
                            a = int(check) / 100
                            if math <= 25 or math == 25:
                                checks = a * 75
                                money = int(db.get_money(message.from_user.id)) - int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы проиграли *0.25x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 😕"
                            elif math <= 50 or math == 50:
                                checks = a * 50
                                money = int(db.get_money(message.from_user.id)) - int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы проиграли *0.50x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 😕"
                            elif math <= 75 or math == 75:
                                checks = a * 25
                                money = int(db.get_money(message.from_user.id)) - int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы проиграли *0.75x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 😕"
                            elif math <= 100:
                                checks = a * 100
                                money = int(db.get_money(message.from_user.id))
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Деньги остаются у вас *1.0x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 🙂"
                            elif math >= 100 and math <= 125:
                                checks = a * 100
                                money = int(db.get_money(message.from_user.id))
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Деньги остаются у вас *1.0x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 🙂"
                            elif math >= 125 and math <= 150:
                                checks = a * 125
                                money = (int(db.get_money(message.from_user.id)) - int(save)) + int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы выйграли *1.25x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 🤑"
                            elif math >= 150 and math <= 175:
                                checks = a * 150
                                money = (int(db.get_money(message.from_user.id)) - int(save)) + int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы выйграли *1.50x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 🤑"
                            elif math >= 175 and math <= 185:
                                checks = a * 175
                                money = (int(db.get_money(message.from_user.id)) - int(save)) + int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы выйграли *1.75x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 🤑"
                            elif math >= 185 and math <= 201:
                                checks = a * 200
                                money = (int(db.get_money(message.from_user.id)) - int(save)) + int(checks)
                                db.set_money(message.from_user.id, money)
                                checks = int(checks)
                                checks = str(checks).replace(".0", "")
                                checks = int(checks)
                                text = "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Вы выйграли *2.0x*\n*" + str(save) + "₽* → *" + str(checks) + "₽* 🤑"
                            if message.chat.type == 'private':
                                await bot.send_message(message.from_user.id, text, parse_mode= 'Markdown')
                            else:
                                await bot.send_message(message.chat.id, text, parse_mode= 'Markdown')
        elif check.find("сменить ник") == 0:
            check = check.replace("  "," ")
            if check == "сменить ник" or check == "сменить ник ":   

                if message.chat.type == 'private':
                    await bot.send_message(message.from_user.id, "✏️ [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Для смены ника необходимо выполнить команду: `Сменить Ник {ник}`.\nТакже, в нике должно быть больше 5 символов.", parse_mode= 'Markdown')
                else:
                    await bot.send_message(message.chat.id, "✏️ [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Для смены ника необходимо выполнить команду: `Сменить Ник {ник}`.\nТакже, в нике должно быть больше 5 символов.", parse_mode= 'Markdown')
            else:
                nick = check.replace("сменить ник ", "")
                if len(nick) <= 4:
                    if message.chat.type == 'private':
                        await bot.send_message(message.from_user.id, "✏️ [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Для смены ника должно быть больше 5 символов.", parse_mode= 'Markdown')
                    else:
                        await bot.send_message(message.chat.id, "✏️ [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Для смены ника должно быть больше 5 символов.", parse_mode= 'Markdown')
                else:
                    db.set_nickname(message.from_user.id, nick)
                    if message.chat.type == 'private':
                        await bot.send_message(message.from_user.id, "✏️ [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Ваш ник успешно сменён на «`" + str(nick) + "`»", parse_mode= 'Markdown')
                    else:
                        await bot.send_message(message.chat.id, "✏️ [" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Ваш ник успешно сменён на «`" + str(nick) + "`»", parse_mode= 'Markdown')
        elif check.find("дать") == 0:
            check = check.replace("  "," ")
            to = message.reply_to_message.from_user.id
            check = check.replace("дать ", "")
            checks = check
            checks = str(check)
            if checks.find("e") != -1:
                check = "%d" % float(check)
                check = str(check)
                z = str(check)
                z = z.replace(".0", "")  
                check = str(z)
            savedz = check
            if int(check) <= 9:
                 if message.chat.type == 'private':
                    await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Минимальная перевод 10₽ 😟", parse_mode= 'Markdown')
                 else:
                    await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Минимальная перевод 10₽ 😟", parse_mode= 'Markdown')
            else:
               if int(db.get_money(message.from_user.id)) - int(check) <= -1:
                    if message.chat.type == 'private':
                        await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), У вас недостаточно средств 😟", parse_mode= 'Markdown')
                    else:
                        await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), У вас недостаточно средств 😟", parse_mode= 'Markdown')
               else:
                    money = (int(db.get_money(message.from_user.id)) - int(check))
                    moneyto = (int(db.get_money(to)) + int(check))
                    db.set_money(message.from_user.id, money)
                    db.set_money(to, moneyto)
                    if message.chat.type == 'private':
                        await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Передано *" + savedz + "₽* игроку [" + db.get_nickname(to) +"](tg://user?id=" + str(to) + ") 😃", parse_mode= 'Markdown')
                    else:
                        await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Передано *" + savedz + "₽* игроку [" + db.get_nickname(to) +"](tg://user?id=" + str(to) + ") 😃", parse_mode= 'Markdown')
        elif check.find("цкн кто") == 0:
            check = check.replace("  "," ")
            check = check.replace("цкн кто ", "")
            choice = ['🎱 Шар говорит, что ', '🔮 Шар говорит, что ', '🤔 Я думаю, что ', '🔭 Звёзды говорят, что ']
            choice = random.choice(choice)
            if message.chat.type == 'private':
                await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Я не могу это сделать в личных сообщениях 😟", parse_mode= 'Markdown')
            else:
                await bot.send_message(message.chat.id, choice + "[" + message.from_user.first_name +"](tg://user?id=" + str(message.from_user.id) + ") " + check, parse_mode= 'Markdown')
        elif check.find("помощь") == 0:
                        if message.chat.type == 'private':
                            await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Команды:\n💰 Б/Баланс\n🎰 Казино {ставка}\n🤝 Дать {сумма}\n🏭 Мой завод\n🤔 Цкн кто {вопрос}\n👨 Сменить ник {ник}\n\nПока-что это все команды, скоро будет пополнение!\nКанал: @FrostyNew 😺", parse_mode= 'Markdown')
                        else:
                            await bot.send_message(message.chat.id,  "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Команды:\n💰 Б/Баланс\n🎰 Казино {ставка}\n🤝 Дать {сумма}\n🏭 Мой завод\n🤔 Цкн кто {вопрос}\n👨 Сменить ник {ник}\n\nПока-что это все команды, скоро будет пополнение!\nКанал: @FrostyNew 😺", parse_mode= 'Markdown')




@dp.message_handler(text=['моя ферма', 'Моя Ферма', 'Моя ферма', 'моя Ферма', 'мой завод', 'Мой Завод', 'Мой завод', 'мой Завод'])
async def start(message: types.Message):
    global ofzzz
    if(not db.user_exists(message.from_user.id)):   
        db.add_user(message.from_user.id)
        db.set_real(message.from_user.id, message.from_user.first_name)
        db.set_nickname(message.from_user.id, "Игрок")
        db.set_signup(message.from_user.id, "done")
    db.set_real(message.from_user.id, message.from_user.first_name)
    math = randint(0,100)
    if math <= 40:
        db.set_kurs(ADMIN_ID, int(db.get_kurs(ADMIN_ID)) - 1)
    else:
        db.set_kurs(ADMIN_ID, int(db.get_kurs(ADMIN_ID)) + 1)
    if db.get_bbb(message.from_user.id) == "yes":
        if message.chat.type == 'private':
            if db.get_nickname(message.from_user.id) == "Игрок":
                nick = "Игрок'а"
            else:
                nick = db.get_nickname(message.from_user.id)
            global savedid
            global bb
            global a
            global cc
            global b
            global hello
            global asdas
            savedid = message.chat.id
            a = db.get_time(message.from_user.id)
            b = a[-2] + a[-1]
            hello = a[-4] + a[-3]
            aa = datetime.datetime.today().strftime("%d%H")
            bb = aa[-2] + aa[-1]
            cc = aa[-4] + aa[-3]
            if int(cc) - int(hello) != 0:
                
                asdas = 5
            else:
                if int(bb) - int(b) == 0:

                    asdas = 0
                if int(bb) - int(b) == 1:

                    asdas = 1
                elif int(bb) - int(b) == 2:
                    
                    asdas = 2
                elif int(bb) - int(b) == 3:
                    
                    asdas = 3
                elif int(bb) - int(b) == 4:
                    
                    asdas = 4
                elif int(bb) - int(b) == 5:
                    
                    asdas = 5
                elif int(bb) - int(b) >= 5:
                    
                    asdas = 5
            offz = int(db.get_kormlvl(message.from_user.id)) * 4.2321 * 2
            offic = int(offz) * int(asdas)
            ofzzz = (int(offic)) * int(db.get_kurs(ADMIN_ID))
            if int(offic) == 0:
                ofzzz = 0
            await bot.send_message(message.from_user.id, "🏭 Заводы [" + str(nick) +"](tg://user?id=" + str(message.from_user.id) + ")\n├ 💰 Прибыль: *" + str(offz) + "*฿/час\n├ 🏭 Колличество: *" + str(db.get_kormlvl(message.from_user.id)) + "* шт / *500* шт\n├ ⌚️ Заполнено: *" + str(asdas) + "* часов / *5* часов\n├ 📝 На Счету: *" + str(ofzzz) + "₽* / *" + str(offic) + "฿*".format(message.from_user), parse_mode= 'Markdown', reply_markup=mainMenu2)
        else:
            if db.get_nickname(message.from_user.id) == "Игрок":
                nick = "Игрок'а"
            else:
                nick = db.get_nickname(message.from_user.id)
            savedid = message.chat.id
            a = db.get_time(message.from_user.id)
            b = a[-2] + a[-1]
            hello = a[-4] + a[-3]
            aa = datetime.datetime.today().strftime("%d%H")
            bb = aa[-2] + aa[-1]
            cc = aa[-4] + aa[-3]
            savedid = message.chat.id
            if int(cc) - int(hello) != 0:
                
                asdas = 5
            else:
                if int(bb) - int(b) == 0:

                    asdas = 0
                if int(bb) - int(b) == 1:

                    asdas = 1
                elif int(bb) - int(b) == 2:
                    
                    asdas = 2
                elif int(bb) - int(b) == 3:
                    
                    asdas = 3
                elif int(bb) - int(b) == 4:
                    
                    asdas = 4
                elif int(bb) - int(b) == 5:
                    
                    asdas = 5
                elif int(bb) - int(b) >= 5:
                    
                    asdas = 5
            offz = int(db.get_kormlvl(message.from_user.id)) * 4.2321 * 2
            offic = int(offz) * int(asdas)
            ofzzz = (int(offic)) * int(db.get_kurs(ADMIN_ID))
            if int(offic) == 0:
                ofzzz = 0
            await bot.send_message(message.chat.id, "🏭 Заводы [" + str(nick) +"](tg://user?id=" + str(message.from_user.id) + ")\n├ 💰 Прибыль: *" + str(offz) + "*฿/час\n├ 🏭 Колличество: *" + str(db.get_kormlvl(message.from_user.id)) + "* шт / *500* шт\n├ ⌚️ Заполнено: *" + str(asdas) + "* часов / *5* часов\n├ 📝 На Счету: *" + str(ofzzz) + "₽* / *" + str(offic) + "฿*".format(message.from_user), parse_mode= 'Markdown', reply_markup=mainMenu2)
    else:
        if int(db.get_money(message.from_user.id)) - 100000 <= 0:
            if message.chat.type == 'private':
                await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Недостаточно средств для покупки 😟".format(message.from_user), parse_mode= 'Markdown')
            else:
                await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id)  +"](tg://user?id=" + str(message.from_user.id) + "), Недостаточно средств для покупки 😟".format(message.from_user), parse_mode= 'Markdown')
        else:
            intz = int(db.get_money(message.from_user.id))
            db.set_money(message.from_user.id, intz - int(100000))
            db.set_bbb(message.from_user.id, "yes")
            db.set_kormlvl(message.from_user.id, 1)
            a = datetime.datetime.today().strftime("%d%H")
            db.set_time(message.from_user.id, a)
            if message.chat.type == 'private':
                await bot.send_message(message.from_user.id, "[" + db.get_nickname(message.from_user.id) +"](tg://user?id=" + str(message.from_user.id) + "), Успешно приобретён завод за *100.000₽* 🏭".format(message.from_user), parse_mode= 'Markdown')
            else:
                await bot.send_message(message.chat.id, "[" + db.get_nickname(message.from_user.id)  +"](tg://user?id=" + str(message.from_user.id) + "), Успешно приобретён завод за *100.000₽* 🏭".format(message.from_user), parse_mode= 'Markdown')

            

@dp.callback_query_handler(text="btnRandom")
async def randomize(message: types.Message):
    try:
        if db.get_time(message.from_user.id) == datetime.datetime.today().strftime("%d%H"):
                await bot.send_message(savedid, "[" + db.get_nickname(message.from_user.id)  +"](tg://user?id=" + str(message.from_user.id) + "), У вас не заполены часы! 🏭".format(message.from_user), parse_mode= 'Markdown')
        else:
            offz = int(db.get_kormlvl(message.from_user.id)) * 4.2321 * 2
            offic = int(offz) * asdas
            ofzzzz = int(offic) * int(db.get_kurs(ADMIN_ID))
            ofzzz = int(db.get_money(message.from_user.id)) + int(ofzzzz)
            db.set_money(message.from_user.id, int(ofzzz))
            db.set_time(message.from_user.id, datetime.datetime.today().strftime("%d%H"))
            await bot.answer_callback_query(message.id, text='Успешно ✅', show_alert=False)
            await bot.send_message(savedid, "[" + db.get_nickname(message.from_user.id)  +"](tg://user?id=" + str(message.from_user.id) + "), Успешно снято *" + str(offic) + "฿* корма и переведено в *" + str(ofzzzz) + "₽* c курсом *" + str(db.get_kurs(ADMIN_ID)) + "฿* 🏭".format(message.from_user), parse_mode= 'Markdown')
    except:
            await bot.answer_callback_query(message.id, text='Это не ваш завод ❌', show_alert=False)

@dp.callback_query_handler(text="btnRandom2")
async def randomize(message: types.Message):
        try:
            if int(db.get_money(message.from_user.id)) - int(db.get_sum(message.from_user.id)) <= -1:
                await bot.send_message(savedid, "[" + db.get_nickname(message.from_user.id)  +"](tg://user?id=" + str(message.from_user.id) + "), Невозможно купить завод - недостаточно средств 🏭\nЦена завода: *" + str(db.get_sum(message.from_user.id)) + "₽*".format(message.from_user), parse_mode= 'Markdown')
            else:
                    money = int(db.get_money(message.from_user.id)) - int(db.get_sum(message.from_user.id))
                    db.set_money(message.from_user.id, money)
                    saved = db.get_sum(message.from_user.id)
                    bank = int(db.get_sum(message.from_user.id)) * 1.4
                    db.set_sum(message.from_user.id, int(bank))
                    sumzas = int(db.get_kormlvl(message.from_user.id)) + 1
                    db.set_kormlvl(message.from_user.id, int(sumzas))
                    bank = int(bank)
                    bank = str(bank).replace(".0", "")
                    bank = int(bank)
                    await bot.answer_callback_query(message.id, text='Успешно ✅', show_alert=False)
                    await bot.send_message(savedid, "[" + db.get_nickname(message.from_user.id)  +"](tg://user?id=" + str(message.from_user.id) + "), Успешно куплен завод за *" + str(saved) + "₽* 🏭\nЦена След.Завода: *" + str(bank) + "₽*".format(message.from_user), parse_mode= 'Markdown')
        except:
            await bot.answer_callback_query(message.id, text='Это не ваш завод ❌', show_alert=False)


if __name__ == "__main__":
    try:
        print("Trying polling server...")
        executor.start_polling(dp, skip_updates = True)
    except Exception as e:
        print('Error run polling, info ->\n' + str(e))
        exit
