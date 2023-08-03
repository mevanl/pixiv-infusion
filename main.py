import customtkinter as ctk
from modules.app.app import App
from modules.states.intro import Intro
from modules.app.state_changer import state_changer


if __name__ == '__main__':
    window = ctk.CTk()                              # main window (master)

    infusion = App(master=window)                   # setting up the window

    loading_screen = Intro(master=window)
    state_changer(infusion, loading_screen)
    # Activate defaults, do background task
    # call home

    window.mainloop()

