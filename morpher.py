from morphing_functions import functions

class Morpher:
    
    def __init__(self, seed = None):
        self.state = seed
        
    def morph(self, morpher = None, function = None):
        self.state = functions[function](self.state, morpher)