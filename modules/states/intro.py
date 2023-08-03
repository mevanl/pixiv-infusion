from modules.states.window_state import WindowState
import customtkinter as ctk


class Intro(WindowState):
    """
    Intro is the starting loading screen.
    """
    def __init__(self, master: ctk.CTk) -> None:
        super().__init__()

        self.program_name = ctk.CTkLabel(master, text='Pixiv Infusion')

    def unload_widgets(self):
        pass

    def load_widgets(self):
        self.program_name.place(relx=0.5, rely=0.5)
        # place all widgets in here
