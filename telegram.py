###import telebot

#Chave_API = "6264057158:AAGTNAmebiFf4Dr6AKsH631VkXXANPO8hfg"


#bot = telebot.TeleBot(Chave_API)

#@bot.message_handler(commands=["mae"])
###  bot.send_message(mensagem.chat,id, "tua mae e")
#
#@bot.message_handler(commands=["irma"])
#def irma (mensagem):
 #   bot.send_message(mensagem.chat.id,"tua irma e")

#@bot.message_handler(commands=["prima"])
#def prima (mensagem):
 #   bot.send_message(mensagem.chat.id,"tua prima e")
  #                   

   # @bot.message_handler(commands=["opcao1"])
    #def opcao1 (mensagem):
     
     #textoo = """
     #omo queres xingar o adm(clique em uma opcao)
     #/mae Mae
     #/irma Irma
     #/prima Prima """
     #bot.send_message(mensagem, textoo)


#@bot.message_handler(commands=["opcao2"])
#def opcao2 (mensagem):
 #   bot.reply_to (mensagem, "vai se lascar mogli")

#@bot.message_handler(commands=["opcao3"])
#def opcao3 (mensagem):

 #   bot.reply_to (mensagem, "vai se lascar yago")

#def verificar:
 #    return True
    








#@bot.message_handler(func=verificar)
#def responder (mensagem):
 #   texto = """
  #  Escolha uma opcao para continuar(clique no item)
   # /opcao1 xingar o adm
    #/opcao2 xingar mogli
    #opcao3 xingar yago
    #Responder qualquer coisa nao vai funcionar, clique em alguma opcao. """
    #bot.reply_to(mensagem,texto)

#bot.polling()