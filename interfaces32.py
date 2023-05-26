import tkinter as tk
import tkinter_page as tkp

window = tk.Tk()

base_frame = tk.Frame(window)
# make pages like a tree and use components 
# to flip. 
#   father - 1 
#          \   
#           2 - 2.1
#             \ 2.2
# Be carefull! Tree like pages construct father first!
# make father page
father = tkp.Page(base_frame,show_child=False,flip="Tree")
label0 = tk.Label(base_frame,text="Tree Flipway Page",\
	width=40,height=2,font=('Times', '15', 'bold'))
father.add_component(label0)

# Method ONE
# make page 1 - STRONGLY NOT RECMMENDED
# Of course you can add page in this way, but this is 
# STRONGLY NOT RECMMENDED! You can use page_connect 
# function to connect father page and child page.
# step 1. Define page1 and its components
page1 = tkp.Page(base_frame,flip="Tree")
label1 = tk.Label(base_frame,text="page1",\
	width=40,height=2,font=('Times', '15', 'bold'))
page1.add_component(label1)
# step 2. Manual connect father and child
page1.set_back(father)
father.set_child_page(page1)
def to_page1_func():
	father.front = father.child_page[0]
	father.pack_forget()
	father.front.pack()
to_page1 = tk.Button(base_frame,text='Page 1',command=to_page1_func)
father.add_component(to_page1)

# Method TWO
# make page 2
# Use page_connect method - Audo generate Button
# step 1. Define page2 and its components
page2 = tkp.Page(base_frame,flip="Tree",back=father)
label2 = tk.Label(base_frame,text="page2",\
	width=40,height=2,font=('Times', '15', 'bold'))
page2.add_component(label2)
# step 2. Use connect function
# PS: You need to give "master" for generating flip component.
tkp.page_connect(father=father,child=page2,page_number=1,\
	text='Page 2',master=base_frame)
# page_number is 1 beacuse in the list - 'father.child_page[]', 
# the 'page2' array subscript is 1. ('page1' is 0.)

# Method THREE
# make page 2.1 - The custom generate Button
# step 1. Define page2_1 and its components
page2_1 = tkp.Page(base_frame,flip="Tree",back=father)
label2_1 = tk.Label(base_frame,text="page2_1",\
	width=40,height=2,font=('Times', '15', 'bold'))
page2_1.add_component(label2_1)
# step 2. use "widget" to define the flip component.
to_page2_1 = tk.Button(base_frame,text='Page 2_1',\
	height=3,width=20)
tkp.page_connect(father=page2,child=page2_1,page_number=0,\
	text='Page 2_1',widget=to_page2_1)

# Method FOUR
# make page 2.2 - The custom generate Button
# use "widget" with "flavour" and "command" to define the flip component.
# step 1. Define page2_2 and its components
page2_2 = tkp.Page(base_frame,flip="Tree",back=father)
label2_2 = tk.Label(base_frame,text="page2_2",\
	width=40,height=2,font=('Times', '15', 'bold'))
page2_2.add_component(label2_2)
# step 2. use "widget" and "flavour" to define the flip component.
to_page2_2 = tk.Button(base_frame)
flavor = {'text':'Page 2_2', 'height':3, 'width':20}
# step 3. use "command" to appand function
def hello():
	print("Hello!")
tkp.page_connect(father=page2,child=page2_2,\
	page_number=1,text='Page 2_2',widget=to_page2_2,flavor=flavor,command=hello)

base_frame.pack(fill='both',expand=1)
father.pack()

window.mainloop()