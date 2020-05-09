import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class TGBot:
    def __init__(self):
        self.updater = Updater(token='1226373363:AAFYKuDWmHpiuyHjTeoBReYVP1P1nwbCASM', use_context=True)

        self.updater.dispatcher.add_handler(CommandHandler('give_task', self.give_task))
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.give_task))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))

    def start(self, update, context):
        custom_keyboard = [[InlineKeyboardButton('give task', callback_data='give_task')]]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Custom Keyboard Test",
                                 reply_markup=reply_markup)

    def give_task(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="This is a task")

    def unknown(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

    def run(self):
        self.updater.start_polling()