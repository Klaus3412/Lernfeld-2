class Scooter:
    def __init__(self, id, standort):
        self.id = id
        self.standort = standort

        self.ausleihZeitpunkt = [0,0,0]
        self.rueckgabeZeitpunkt = [0,0,0]
        self.reservierungsZeitpunkt = [0,0,0]
        self.beginnZeitpunkt = [0,0,0]

        self.scooterAusgeliehen = False
        self.scooterReserviert = False
        self.wasReserviert = False

        self.aktuellerPreis = 0
        self.insgesamterPreis = 0

    def getId(self):
        return self.id
    
    def getStandort(self):
        return self.standort    

    def getScooterAusgeliehen(self):
        return self.scooterAusgeliehen
    
    def setScooterAusgeliehen(self, status):

        if isinstance(status, bool):
            self.scooterAusgeliehen = status
        else:
            raise ValueError("Status muss 'True' oder 'False' sein")

    def getScooterReserviert(self):
        return self.scooterReserviert    

    def setScooterReserviert(self, status):    
        if isinstance(status, bool):
            self.scooterReserviert = status
        else:
            raise ValueError("Status muss 'True' oder 'False' sein")

    def getScooterWasReserviert(self):
        return self.wasReserviert    

    def setScooterWasReserviert(self, status):    
        if isinstance(status, bool):
            self.wasReserviert = status
        else:
            raise ValueError("Status muss 'True' oder 'False' sein")

    def setAusleihZeitpunkt(self, ausleih_zeitpunkt):
        self.ausleihZeitpunkt = ausleih_zeitpunkt

    def getAusleihZeitpunkt(self):
        return self.ausleihZeitpunkt
    
    def getRueckgabeZeitpunkt(self):
        return self.rueckgabeZeitpunkt
    
    def setRueckgabeZeitpunkt(self, rueckgabeZeitpunkt):
        self.rueckgabeZeitpunkt = rueckgabeZeitpunkt

    def getReservierungsZeitpunkt(self):
        return self.reservierungsZeitpunkt
    
    def setReservierungsZeitpunkt(self, reservierungsZeitpunkt):
        self.reservierungsZeitpunkt = reservierungsZeitpunkt

    def getBeginnZeitpunkt(self):
        return self.beginnZeitpunkt
    
    def setBeginnZeitpunkt(self, beginnZeitpunkt):
        self.beginnZeitpunkt = beginnZeitpunkt

    def getAktuellerPreis(self):
        return self.aktuellerPreis
  
    def setAktuellerPreis(self, aktuellerPreis):
        self.aktuellerPreis = aktuellerPreis

    # TODO: Gesamt Preis fixen
    def getInsgesamterPreis(self):
        return self.insgesamterPreis
    
    def setInsgesamterPreis(self, insgesamterPreis):
        self.insgesamterPreis = insgesamterPreis
