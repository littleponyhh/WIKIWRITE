import telebot
from telebot import types
import wikipedia

#bot setup
TOKEN = '7124759861:AAESBdyNCAmVNarS8nm_bIKu5gZhvdEh9Ig'
bot= telebot.TeleBot(TOKEN)
print('bot started')
#languages 
lan = ['en', 'ar']
current_language = None
#keyboard english
keyboard = types.InlineKeyboardMarkup()
search_butt= types.InlineKeyboardButton('search', callback_data='search_en')
channel_b= types.InlineKeyboardButton('our channel', url= 'https://t.me/NS8_b')
translator_bu= types.InlineKeyboardButton('translator', callback_data='tran_en')
keyboard.add(search_butt, channel_b)
keyboard.add(translator_bu)
#keyboard arabic 
keyboard_ar = types.InlineKeyboardMarkup()
search_butt_ar= types.InlineKeyboardButton('البحث', callback_data='search_ar')
channel_b_ar= types.InlineKeyboardButton('قناتنا', url= 'https://t.me/NS8_b')
translator_bu_ar= types.InlineKeyboardButton('المترجم', callback_data='tran_en')
keyboard_ar.add(search_butt_ar, channel_b_ar)
keyboard_ar.add(translator_bu_ar)
#commands 
@bot.message_handler(commands=['en'])
def en(message):
    global current_language
    current_language = 'en'
    wikipedia.set_lang('en')
    bot.reply_to(message, 'you choose english ')
@bot.message_handler(commands=['ar'])    
def ar(message):
    global current_language
    current_language = 'ar'
    wikipedia.set_lang('ar')
    bot.reply_to(message, 'لقد اخترت العربية')
@bot.message_handler(commands=['start'])
def welcome(message):
    if current_language == 'en':
        bot.send_message(message.chat.id, 'welcome to wikiwritebot here you can search in wikipedia\n please choose an option', reply_markup=keyboard)
    elif current_language == 'ar':
        bot.send_message(message.chat.id, 'مرحبا بك في بوت ويكي رايت هنا يمكنك البحث في ويكيبيديا\nمن فضلك اختر خيارا', reply_markup=keyboard_ar)
    else:
        bot.send_message(message.chat.id, 'welcome to wikiwritebot here you can search in wikipedia\n please choose an option', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def help(message):
    if current_language == 'en':
        bot.send_message(message.chat.id, 'welcome to support:\nto set language \n/en for english \n/ar for arbic\n\n this bot devloped and published by @NS8_b ')
    if current_language == 'ar':
        bot.send_message(message.chat.id,'مرحبًا بك في الدعم:\nلتعيين الغة:\n/ar للعربية\n /en للانجليزية\n\n هذا البوت تم نشره وتطويره بواسطة @NS8_b ')
    else :
         bot.send_message(message.chat.id, 'welcome to support:\nto set language \n/en for english \n/ar for arbic\n\n this bot devloped and published by @NS8_b ')
@bot.callback_query_handler(func=lambda call : True)
def buttons(call):
    if call.data == 'search_en':
        bot.send_message(call.message.chat.id , 'please send me a word to search it for you')
    elif call.data == 'search_ar':
        bot.send_message(call.message.chat.id , 'ارسل كلمة للبحث عنها')
    else:
        bot.send_message(call.message.chat.id , 'please send me a word to search it for you')
@bot.message_handler(func= lambda message : True)
def search(message):
    if current_language == 'en':
        try:
            keyword = message.text
            summary = wikipedia.summary(keyword)
            bot.send_message(message.chat.id, summary)
            bot.send_message(message.chat.id, 'please join our channel : @NS8_b  ')
        except:
            bot.send_message(message.chat.id, 'error: please make your search more spesific')
    elif current_language == 'ar':
        try:
            keyword = message.text
            summary = wikipedia.summary(keyword)
            bot.send_message(message.chat.id, summary)
            bot.send_message(message.chat.id, 'فضلا اشترك في قناتنا : @NS8_b ')
        except:
            bot.send_message(message.chat.id, 'خطأ : هل يمكنك جعل بحثك دقيق اكثر')  
    else:
        try:
            keyword = message.text
            summary = wikipedia.summary(keyword)
            bot.send_message(message.chat.id, summary)
            bot.send_message(message.chat.id, 'please join our channel : @NS8_b  ')
        except:
            bot.send_message(message.chat.id, 'error: please make your search spesific')              
bot.polling()
