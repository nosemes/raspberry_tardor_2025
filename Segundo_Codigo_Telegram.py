import telebot
from telebot import custom_filters
import time
import random



bot = telebot.TeleBot('8398261892:AAEf-fgq_UVzA25Uxs8ZXJx-LVwrlBpjZoM') 


@bot.message_handler(commands=['start'])

def moviment(message):
    
    while True:
        
        numero = random.randrange(10,1000)
        
        if 0 < numero < 300:
            
             bot.send_message(message.chat.id, f"{numero} que pertenece a primer tercio!!!!")
             
        elif 300 <= numero < 666:
            
              bot.send_message(message.chat.id, f"{numero} que pertenece a segundo tercio!!!!")
              
        else:
            
              bot.send_message(message.chat.id, f"{numero} que pertenece a último tercio!!!!")
              
        time.sleep(10)


bot.add_custom_filter(custom_filters.ChatFilter())

bot.polling(none_stop=True)








