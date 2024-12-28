import random
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext


async def reply(update: Update, context: CallbackContext) -> None:
    # Log incoming message for debugging    
    cat_responses = ["meow", "meow", "meow meow", "meow meow", "brrrrrrr"]
    response = random.choice(cat_responses)
    
    # Use the async version of send_message
    await update.message.reply_text(response)

def main():
    # Initialize the bot with the correct token
    print("initializing...")
    application = Application.builder().token("7772997085:AAHdN4F2BIbAa6SUBU0w9UZrcVY3Wc2dWdY").build()
    
    # Add the message handler
    print("adding message handler...")
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    
    # Start polling
    print("start polling...")
    application.run_polling()

if __name__ == '__main__':
    main()
