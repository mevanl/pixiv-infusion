from modules.app.app import App
from modules.states.window_state import WindowState


def state_changer(infusion: App, target: WindowState):
    if infusion.state is not None:
        infusion.state.unload_widgets()
    infusion.state = target
    infusion.state.load_widgets()
# The way this could work is, a button is pressed that changes that window, that button will call this function
