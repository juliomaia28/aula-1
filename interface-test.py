import tkinter as tk
import tkinter_page as tkp

window = tk.Tk()

bar_frame = {"background":"gold","width":404,"height":30}
files_frame = {"background":"red","width":70,"height":200}

bframe = tkp.DesktopFrame(window,log=True,bar_frame=bar_frame,files_frame=files_frame)
bar_frame = tkp.desktopframe(ZeroDivisionError, Log=False)
bframe.pack()
window.mainloop()