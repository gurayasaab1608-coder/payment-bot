import telebot
from telebot import types

# Initialize bot with your token
bot = telebot.TeleBot("8477512161:AAGNaSytbH6GJEB1lJSXFw91rlncddumgT8")

# Placeholder UPI ID and admin username
UPI_ID = "your_upi_id@example.com"
ADMIN_USERNAME = "gurayasaab1608-coder"

# Welcome message
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_message = (
        "Welcome to the VIP Payment Bot!\n"
        "Features:\n"
        "- Membership Plans\n"
        "- Contact Admin\n"
        "- Payment Flow\n"
        "- Score Checking\n"
    )
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Membership Plans")
    item2 = types.KeyboardButton("Contact Admin")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

# Handle membership plans button
@bot.message_handler(func=lambda message: message.text == "Membership Plans")
def membership_plans(message):
    bot.send_message(message.chat.id, "Here are the membership plans...")

# Handle contact admin button
@bot.message_handler(func=lambda message: message.text == "Contact Admin")
def contact_admin(message):
    bot.send_message(message.chat.id, f"Contact the admin: @{ADMIN_USERNAME}")

# Payment flow
@bot.message_handler(commands=['paid'])
def payment_status(message):
    txn_id = message.text.split()[1]
    bot.send_message(message.chat.id, f"Payment status for transaction ID {txn_id}...")

# Score checking
@bot.message_handler(commands=['score'])
def check_score(message):
    bot.send_message(message.chat.id, "Your current score is...")

# Start the bot
bot.polling()