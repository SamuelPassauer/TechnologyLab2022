import tensorflow 

class Sample:

    def __init__(self, name, disassembling_strategy, disassembling_number, order_number, track) -> None:
        self._name = name
        self._tensor = None
        self._disassembling_strategy = disassembling_strategy
        self._disassembling_number = disassembling_number
        self._order_number = order_number
        self._track = track
    ##########GetterSetter
    ######   name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    ######   disassembling_strategy
    @property
    def disassembling_strategy(self):
       return self._disassembling_strategy

    @disassembling_strategy.setter
    def disassembling_strategy(self, disassembling_strategy):
        self._disassembling_strategy=disassembling_strategy
    
    ########  disassembling_number
    @property 
    def disassembling_number(self):
        return self._disassembling_number
    
    @disassembling_number.setter
    def disassembling_number(self,disassembling_number):
        self.disassembling_number=disassembling_number
    
   ##########  order number 
    @property 
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        self._order_number=order_number
    
    ########  track
    @property
    def track(self):
        return self._track
    
    @track.setter
    def track(self, track):
        self._track=track


    


    

