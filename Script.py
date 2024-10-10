import telebot

telegram_api_key='7442394616:AAEW4sZGGht01aOQua9NisRCYD6g5HXQgIo'
bot= telebot.TeleBot(telegram_api_key)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bienvenue à nouveau🤝 De nombreuses personnes connaissent notre service, nous nous sommes établis comme l'un des plus fiables à tous points de vue🛡 Nous nous sommes toujours concentrés sur vos intérêts et vos détails, c'est notre succès commun🏆")
   
bot.infinity_polling()