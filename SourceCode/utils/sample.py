import tensorflow 

class Sample:

    def __init__(self, name, disassembling_strategy, disassembling_number, order_number, track) -> None:
        self._name = name
        self._tensor = None
        self._disassembling_strategy = disassembling_strategy
        self._disassembling_number = disassembling_number
        self._order_number = order_number
        self._track = track
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    #ToDo Getter setter

