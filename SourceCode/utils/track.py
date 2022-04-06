
class Track:

    def __init__(self, name, length, tempo, volume, spectrum) -> None:
        self._name = name
        self._length = length
        self._tempo = tempo
        self._volume = volume
        self._spectrum = spectrum

    ##########GetterSetter
    ######   name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    ##### length 
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        self._length=length
    
    #### tempo
    @property
    def tempo(self):
        return self._tempo
    
    @tempo.setter
    def tempo(self, tempo):
        self._tempo=tempo

    #### volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume=volume 
    
    #### spectrum
    @property
    def spectrum(self):
        return self._spectrum
    
    @spectrum.setter
    def spectrum(self, spectrum):
       self._spectrum=spectrum
