import customtkinter as ctk
from tkinter import font

master = ctk.CTk()
master.geometry('800x800')
master.title('Test')
master.resizable(True, True)
master.configure(fg_color='#FAFAFA')

top_frame = ctk.CTkFrame(master, fg_color='#0096fa')

top_frame_label = ctk.CTkLabel(top_frame, text='Label')
top_frame_label.place(anchor='center', relx=0.5, rely=0.5)


top_frame.place(anchor='center', relx=0.5, rely=0.03, relwidth=1.1, relheigh=0.07)

print(font.names())

master.mainloop()
