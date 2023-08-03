from modules.states.window_state import WindowState
import customtkinter as ctk


class App:
    def __init__(self, master: ctk.CTk, state: WindowState = None) -> None:

        # Main Window Settings
        self.master = master                   # master is the main window for ctk
        self.master.geometry('1280x720')       # Default resolution
        self.master.minsize(1280, 720)         # Smallest resolution possible
        self.master.resizable(True, True)
        self.master.wm_title('Pixiv Infusion')

        self.__state = state

    @property
    def state(self) -> WindowState:
        return self.__state

    @state.setter
    def state(self, new_state: WindowState):
        self.__state = new_state
