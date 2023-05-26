import telebot
import dotenv

Chave_API= "6099222039:AAHOO0KbGaOMj2mEPrJYKaInxfzUsCAUn6Q"
bot =telebot.TeleBot(Chave_API)

def enviar_mensagem(mensagem):
    bot.send_message(chat_id= "text=mensagem")

    while True:
        novas_mensagens = bot.get_updates()
    if novas_mensagens:
        mensagem = novas_mensagens[-1].message.text
        if mensagem == 'notificacao':
            enviar_mensagem('Recebi sua notificacao!')
        else:
            enviar_mensagem('Nao entendi o que voce quis dizer...')