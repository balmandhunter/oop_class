from View import View, ZoneView
from abc import ABC, abstractmethod
import tkinter as tk


class Controller(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #force all controllers to have a method to bind the button to an event
    @abstractmethod
    def bind(self):
        raise NotImplementedError

class ZoneController(Controller):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = tk.Tk()
        self.zoneview = ZoneView(self.root, self)
        self.zoneview.make_initial_view()

    def bind(self):
        self.zoneview.make_initial_view()
        self.zoneview.buttons['Submit'].configure(command=self.set_zone)

    def set_zone(self):
        self.zone = selected.get()
        print(zone)