import random
import tkinter as tkp

from telnetlib import NAOCRD

root= tkp.Tk()
root.geometry("200x200")

# def hover(event):
#     x = random.randint(0,200)
#     y = random.randint(0,200)
#     NAOCRD.place(x=x, y=y)

#     def mensage():
#         message = tkp.Label(root, text="vc e gay")
#         message.place(x=70, y=120, relx=0, rely=0)

#         pergunta = tkp.Label(root, text="voce e um membro do nome da lista?")
#         pergunta.pack(anchor='n', pady=20)

#         nao = tkp.Button(root, text='nao')
#         nao.place(x=140, y=80)
#         nao.bind('<enter>', hover)

#         sim = tkp.Button(root, text='sim',command = message)
#         sim.place(x=25, y=80, relx=0, rely=0)

#         root.mainloop()

# hover(root)