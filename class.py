class Radio:
    def __init__(self):
        self.turn_on = False
        self.station = 'Di FM'

    def Turn_on(self):
        self.turn_on = True

    def change_the_wave(self):
        self.station = 'Di FM2'
