from threading import Thread
import customtkinter as ctk
from PIL import Image


class MenuBar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, start_x: float, end_x: float, **kwargs):
        super().__init__(master=master, **kwargs)
        self.master = master

        # Menu Attributes
        self.start_position: float = start_x
        self.end_position: float = end_x
        self.width = abs(start_x - end_x) - 0.03

        # Menu animation
        self.current_position = self.start_position
        self.on_screen = False

        self.settings_button = ctk.CTkButton(self,
                                             text='Settings',
                                             text_color='#FAFAFA',
                                             font=('Segoe UI Semibold', 35),
                                             fg_color='#0096fa',
                                             corner_radius=5)

        self.place(relx=self.start_position, rely=0.06, relwidth=self.width, relheight=0.4)
        self.settings_button.pack()

    def menu_animation(self):
        if self.on_screen:
            self.animation_backward()
        else:
            self.animation_forward()

    def animation_forward(self):
        if self.current_position < self.end_position:
            self.current_position += 0.008
            self.place(relx=self.current_position, rely=0.06, relwidth=self.width, relheight=0.4)
            self.after(1, self.animation_forward())
        else:
            self.on_screen = True

    def animation_backward(self):
        if self.current_position > self.start_position:
            self.current_position -= 0.008
            self.place(relx=self.current_position, rely=0.06, relwidth=self.width, relheight=0.4)
            self.after(1, self.animation_backward())
        else:
            self.on_screen = False

    def start_menu_animation(self):
        Thread(target=self.menu_animation(), daemon=True).start()


class SideFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, image: ctk.CTkImage, **kwargs):
        super().__init__(master=master, **kwargs)
        self.master = master
        self.side_shown: bool = False

        self.label = ctk.CTkLabel(self, text='Pixiv Infusion', text_color='#FAFAFA', font=('Segoe UI Semibold', 20))
        self.label.place(anchor='center', relx=0.5, rely=0.5)

        self.menu_bar = MenuBar(master, start_x=-0.3, end_x=0.004, fg_color='#0096fa', corner_radius=20)

        self.show_sidebar = ctk.CTkButton(self,
                                          text='',
                                          command=self.menu_bar.start_menu_animation,
                                          image=image,
                                          fg_color='#0096fa',
                                          corner_radius=5)
        self.show_sidebar.place(anchor='center', relx=0.078, rely=0.52, relwidth=0.04, relheight=0.8)


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
