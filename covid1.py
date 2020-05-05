from telebot import TeleBot, types
import requests
import bs4

res = requests.get("https://www.mohfw.gov.in/")

covid = bs4.BeautifulSoup(res.text , 'lxml')

data = covid.select("strong") 

active_cases = (data[6].getText())
cured = (data[7].getText())
deaths = (data[8].getText())
total_cases = int(active_cases) + int(cured)

TOKEN = "1195312333:AAHMH_dmWxVYb4Bu-gU75SNnNCj2KBgnlxY"

bot =TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Welcome to updatebot!\n" +
    "press /Active for Active Cases\n" +
    "press /Deaths for total deaths\n" +
    "press /Cured for Cured")

@bot.message_handler(commands=['Active'])
def active_command(message):
    bot.reply_to(message," active cases in india :" + active_cases)

@bot.message_handler(commands=['Deaths'])
def deaths_command(message):
    bot.reply_to(message," death cases in india :" + deaths)

@bot.message_handler(commands=['Cured'])
def cured_command(message):
    bot.reply_to(message," cured cases in india :" + cured)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()