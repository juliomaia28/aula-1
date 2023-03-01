import telebot
from datetime import datetime, timedelta
Chave_API = "5810013268:AAFkA6XRkfqAnbloHndGmti0um75csXpZUM"
bot = telebot.TeleBot(Chave_API)

hoje = datetime.now()
data_aula = datetime(year=2023,month=3, day=2,hour=17,)
regressiva = data_aula-hoje
regressivas =  data_aula - hoje

option_1 = "HoraAtual"
option_2 = "DiasParaAula"
option_3 = "HorasParaAula"

@bot.message_handler(commands=[option_1])
def opcao1(mensagem):
     hora = str(hoje.hour)
     minuto = str(hoje.minute)
     bot.reply_to(mensagem, f"{hora}:{minuto} horas" )


@bot.message_handler(commands=[option_2]) 
def opcao2(mensagem):
     bot.reply_to(mensagem, regressiva.days)

@bot.message_handler(commands=[option_3]) 
def opcao3(mensagem):
    bot.reply_to(mensagem, regressivas)

def verificar(mensagem): 
     return True






@bot.message_handler(func = verificar)
def responder (mensagem): 
    texto = f"""
    Escolha uma funcao para conrinuar:
    /{option_1} que horas sao 
     /{option_2} quantos dias faltam para a aula
      /{option_3} quantas horas faltam para aula
    Responder qualquer coisa nao vai funcionar, clique em alguma opcao. """
    bot.reply_to(mensagem,texto)
 
bot.polling()