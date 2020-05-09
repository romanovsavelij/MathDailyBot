import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CallbackQueryHandler
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from task.task_manager import TaskManager

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class TGBot:
    def __init__(self):
        REQUEST_KWARGS = {
            'proxy_url': 'socks5://proxy.kuldoshin.site:2453',
        }

        self.task_manager = TaskManager()
        self.updater = Updater(token='1226373363:AAFYKuDWmHpiuyHjTeoBReYVP1P1nwbCASM', use_context=True, request_kwargs=REQUEST_KWARGS)
        self.add_handlers()

    def add_handlers(self):
        self.updater.dispatcher.add_handler(CommandHandler('give_task', self.give_task))
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.all, self.button_messages_handler))

    def start(self, update: telegram.update, context):
        self.task_manager.register_new_user(update.effective_chat.id)

        custom_keyboard = [[KeyboardButton('Give task')]]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Hey, take a task to solve!",
                                 reply_markup=reply_markup)

    def give_task(self, update, context):
        task_statement = self.task_manager.get_task(update.effective_chat.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=task_statement)

    def button_messages_handler(self, update, context):
        message_text = update.message.text
        print(f'message_text: {message_text}')
        if message_text == 'Give task':
            self.give_task(update, context)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, I don\'t understand you.')

    def run(self):
        self.updater.start_polling()