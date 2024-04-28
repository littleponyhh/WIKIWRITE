#imports
import telebot
from telebot import types
import wikipedia

#bot setup
Token = '7124759861:AAESBdyNCAmVNarS8nm_bIKu5gZhvdEh9Ig'
bot = telebot.TeleBot(Token)
print('bot started')

# start command
@bot.message_handler(commands=['start'])
def welcome(message):
    # keybors setup
    keyboard = types.InlineKeyboardMarkup()
    # add keyboard buttons
    butt1 = types.InlineKeyboardButton(text="english 🇺🇸", callback_data='en')
    butt2 = types.InlineKeyboardButton(text="arabic (العربية) 🇸🇦", callback_data='ar')
    keyboard.add(butt1)
    keyboard.add(butt2)
    # send start message
    bot.reply_to(message, f'Welcome to WikiWrite Bot 📝!nPlease choose your language:', reply_markup=keyboard,)

@bot.callback_query_handler(func= lambda message : True)
def buttons(call):
    if call.data == 'en':
       
        wikipedia.set_lang('en')
        keyboard_en = types.InlineKeyboardMarkup()
        button_search = types.InlineKeyboardButton(text='search', callback_data='search')
        button_channel = types.InlineKeyboardButton(text='our channel', url='https://t.me/NS8_b')
        keyboard_en.add(button_search, button_channel)
        bot.send_message(call.message.chat.id, 'Welcome to the WikiWrite bot. You selected English. Please make a choice.', reply_markup=keyboard_en)

    if call.data == 'ar':
        # تعيين ويكيبيديا للغة العربية وإعداد الرد الخاص بالعربية
        wikipedia.set_lang('ar')
        keyboard_ar = types.InlineKeyboardMarkup()
        button_search = types.InlineKeyboardButton(text='البحث', callback_data='search_ar')
        button_channel = types.InlineKeyboardButton(text='قناتنا', url='https://t.me/NS8_b')
        keyboard_ar.add(button_search, button_channel)
        bot.send_message(call.message.chat.id, 'مرحبا بك في بوت ويكي رايت. لقد اخترت العربية. يرجى إجراء اختيار.', reply_markup=keyboard_ar)
    if call.data == 'search':
        bot.send_message(call.message.chat.id,'please enter a keyword for search for it: ')
    if call.data == 'search_ar':
        wikipedia.set_lang('ar')
        bot.send_message(call.message.chat.id, 'ادخل كلمة للبحث عنها')     
      
        
@bot.message_handler(func=lambda message : True)

def search_eng(message):
    
    keyword = message.text
    summary = wikipedia.summary(keyword)
   try:
        bot.reply_to(message, summary)
        bot.send_message(message.chat.id, 'please join our channel : @NS8_b \n فضلا اشترك في قناتنا : @NS8_b ')
    except:
        serch = 'i could not acces to your search can you make it more specific'
        search_r = 'لم استطع الحصول على بحثك هل يمكنك جعله دقيق اكثر'
        bot.reply_to(message,f'ERROR: \n {serch}\n {search_r} ')
