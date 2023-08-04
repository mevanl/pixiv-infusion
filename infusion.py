import customtkinter as ctk


class TopFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, **kwargs):
        super().__init__(master=master, **kwargs)
        self.master = master

        self.label = ctk.CTkLabel(self, text='Pixiv Infusion', text_color='#FAFAFA', font=('Segoe UI Semibold', 20))
        self.label.place(anchor='center', relx=0.5, rely=0.5)


class Infusion:
    def __init__(self, master: ctk.CTk):
        self.master = master

        #  Window Geometry
        self.master.geometry('1280x720')
        self.master.minsize(1280, 720)
        self.master.maxsize(3840, 2160)
        self.master.resizable(True, True)

        # Window Appearance
        self.master.wm_title('Pixiv Infusion')
        self.master.iconbitmap()  # TODO: add logo in future
        self.master.configure(fg_color='#FAFAFA')

        # Top Frame
        self.top_frame = TopFrame(self.master, fg_color='#0096fa')
        self.top_frame.place(relx=0.5, rely=0.026, relwidth=1.1, relheight=0.06, anchor='center')


if __name__ == '__main__':
    window = ctk.CTk()  # The master window

    infusion = Infusion(master=window)  # Main Window created

    window.mainloop()
