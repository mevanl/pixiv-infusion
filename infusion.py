import customtkinter as ctk
from PIL import Image


class MenuBar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, **kwargs):
        super().__init__(master=master, **kwargs)
        self.master = master

        self.settings_button = ctk.CTkButton(self,
                                             text='Settings',
                                             text_color='#FAFAFA',
                                             font=('Segoe UI Semibold', 35),
                                             fg_color='#0096fa',
                                             corner_radius=5)


class SideFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, image: ctk.CTkImage, **kwargs):
        super().__init__(master=master, **kwargs)
        self.master = master
        self.side_shown: bool = False

        self.label = ctk.CTkLabel(self, text='Pixiv Infusion', text_color='#FAFAFA', font=('Segoe UI Semibold', 20))
        self.label.place(anchor='center', relx=0.5, rely=0.5)

        self.menu_bar = MenuBar(master, fg_color='#0096fa', corner_radius=0)

        self.show_sidebar = ctk.CTkButton(self,
                                          text='',
                                          command=self.toggle_sidebar,
                                          image=image,
                                          fg_color='#0096fa',
                                          corner_radius=5)
        self.show_sidebar.place(anchor='center', relx=0.078, rely=0.52, relwidth=0.04, relheight=0.8)

    def toggle_sidebar(self):
        if self.side_shown:
            self.menu_bar.settings_button.place_forget()
            self.menu_bar.place_forget()
            self.side_shown = False
        else:
            self.menu_bar.place(anchor='center', relx=0.0, rely=0.6, relwidth=0.4, relheight=1.1)
            self.menu_bar.settings_button.place(anchor='center', relx=0.74, rely=0.23)
            self.side_shown = True
        return

class Infusion:
    def __init__(self, master: ctk.CTk, image_list: list):
        self.master = master

        #  Window Geometry
        self.master.geometry('800x800')
        self.master.minsize(800, 800)
        self.master.maxsize(800, 800)
        self.master.resizable(False, False)

        # Window Appearance
        self.master.wm_title('Pixiv Infusion')
        self.master.iconbitmap()  # TODO: add logo in future
        self.master.configure(fg_color='#FAFAFA')
        self.image_list: list = image_list
        self.sidebar_shown = False

        # Side Frame
        self.side_frame = SideFrame(self.master, self.image_list[0], fg_color='#0096fa')
        self.side_frame.place(relx=0.5, rely=0.026, relwidth=1.1, relheight=0.06, anchor='center')


def get_images() -> list:
    image_list = []

    # Sidebar Image
    sidebar_image: ctk.CTkImage = ctk.CTkImage(dark_image=Image.open('style/menu.png'))
    image_list.append(sidebar_image)

    return image_list


if __name__ == '__main__':

    images = get_images()

    ctk.set_appearance_mode('dark')
    window = ctk.CTk()  # The master window
    infusion = Infusion(master=window, image_list=images)  # Main Window created
    window.mainloop()
