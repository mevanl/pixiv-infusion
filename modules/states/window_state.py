from abc import ABC, abstractmethod


class WindowState(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_widgets(self):
        ...

    @abstractmethod
    def unload_widgets(self):
        ...
