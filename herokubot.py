import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re
import os,sys
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from telegram import MessageEntity 
from functools import wraps
updater = Updater(token='428239435:AAGA-VxXxxZj5sVGfevk44SqrZzt6x7L7ac')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
from functools import wraps
from telegram.ext.dispatcher import run_async
# Create a function to tell what the bot to do for specific update
#def start(bot, update):
  # bot.send_message(chat_id=update.message.chat_id, text="https://docs.python.org/3/tutorial/controlflow.html")

 #Assign handler "start" to the dispatcher to send to telegram, startpolling start the process ONLY for /start
#start_handler = CommandHandler('start', start)
#dispatcher.add_handler(start_handler)

# Answer to all messages
#def echo(bot, update):
  #bot.send_message(chat_id=update.message.chat_id, text='0x52908400098527886E0F7030069857D2E4169EE7')  # bot reply with whatever user send

#echo_handler = MessageHandler(Filters.text, echo) # Filter is use to handle diff incoming messages, video.. 
#dispatcher.add_handler(echo_handler)

#def deletemsg(bot, update):
  #  bot.delete_message(chat_id=update.effective_chat.id,message_id=update.effective_message.message_id)

#delete_handler = MessageHandler(Filters.entity('www.google.com')| #Filters.sticker|Filters.document,callback=deletemsg)
#dispatcher.add_handler(delete_handler)

#def error(bot, update, error):
    #if not (error.message == "Message is not modified"):
        #error.warning('Update "%s" caused error "%s"' % (update, error))

#dispatcher.add_error_handler(error)

#LIST_OF_ADMINS = [439735363,521527129]

#def restricted(func):
    #@wraps(func)
    #def wrapped(bot, update, *args, **kwargs):
        #user_id = update.effective_user.id
        #if user_id not in LIST_OF_ADMINS:
           # print("Unauthorized access denied for {}.".format(user_id))
           # return
        #return func(bot, update, *args, **kwargs)
    #return wrapped

@run_async
def delete_gifs(bot,update):
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

@run_async
def delete_link(bot,update):
     admins = []
     admins = bot.getChatAdministrators(chat_id=update.message.chat_id)
     user = bot.getChatMember(chat_id=update.message.chat_id,user_id=update.message.from_user.id)
     if user not in admins:
         bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

@run_async
def delete_method(bot, update):
     admins = []
     admins = bot.getChatAdministrators(chat_id=update.message.chat_id)
     user = bot.getChatMember(chat_id=update.message.chat_id,user_id=update.message.from_user.id)
     mlist=['0x[a-fA-F0-9]{40}','etherscan.io','pornhub']
     if user not in admins:
       for i in mlist: 
          if re.search(i, update.message.text):
                 bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
                 bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user.id)
                 bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user.id)      

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "428239435:AAGA-VxXxxZj5sVGfevk44SqrZzt6x7L7ac"
    NAME = "topico88"


    # Port is given by Heroku
    PORT = int(os.environ.get('PORT', '8443'))    

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    updater = Updater(token='428239435:AAGA-VxXxxZj5sVGfevk44SqrZzt6x7L7ac')
    dispatcher = updater.dispatcher

    gif_handler = MessageHandler(Filters.sticker|Filters.document|Filters.video|Filters.photo, delete_gifs)

    link_handler = MessageHandler(Filters.entity(MessageEntity.URL),delete_link)

    text_handler = MessageHandler(Filters.text & Filters.user,delete_method)
    
    #dispatcher.add_handler(start_handler)
    dispatcher.add_handler(gif_handler)
    dispatcher.add_handler(link_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()






