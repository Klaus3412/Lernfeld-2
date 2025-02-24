import random
import datetime
from datetime import *

import ScooterClassUi

class ScooterRentalApp:
    GEBUEHR = 1
    PRICE_PER_MINUTE_RESERVE = 0.05
    PRICE_PER_MINUTE_DRIVE = 0.10

    MINDEST_ENTFERNUNG = 10
    MAXIMALE_ENTFERNUNG = 2500

    def __init__(self):
        self.scooter = ScooterClassUi.Scooter
        self.scooter_list = []
        self.ausgeliehene_scooter = []

        for i in range(10):
            scooter_for_list = self.scooter(i + 1, self.getRandomStandort())
            self.scooter_list.append(scooter_for_list)

        self.bearbeiteterScooterId = 1

    def getRandomStandort(self):
        return random.randint(self.MINDEST_ENTFERNUNG, self.MAXIMALE_ENTFERNUNG)
    
    def getScooterById(self, id):
        for scooter in self.scooter_list:
            if scooter.getId() == id:
                return scooter
        #print("Keinen Scooter mit dieser Id gefunden.")

    @staticmethod
    def getCurrentTimeStamp():
        now = datetime.now()
        hours = int(now.strftime("%H"))
        minutes = int(now.strftime("%M"))
        seconds = int(now.strftime("%S"))

        return [hours, minutes, seconds]

    @staticmethod
    def getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt):
        frueher = datetime(2020, 1, 1, fruehererZeitpunkt[0], fruehererZeitpunkt[1], fruehererZeitpunkt[2])
        spaeter = datetime(2020, 1, 1, spaetererZeitpunkt[0], spaetererZeitpunkt[1], spaetererZeitpunkt[2])
        
        differenz = spaeter - frueher
        differenz_in_secs = differenz.total_seconds()
        hours = int(differenz_in_secs // 3600)
        minutes = int((differenz_in_secs % 3600) // 60)
        seconds = int(differenz_in_secs % 60)
        
        return [hours, minutes, seconds]

    @staticmethod
    def getDrivePrice(timeInMinutes):
        price = timeInMinutes * ScooterRentalApp.PRICE_PER_MINUTE_DRIVE + ScooterRentalApp.GEBUEHR
        formattedPrice = "{:.2f}".format(price)
        return formattedPrice
    
    @staticmethod
    def getReservePrice(timeInMinutes):
        price = timeInMinutes * ScooterRentalApp.PRICE_PER_MINUTE_RESERVE + ScooterRentalApp.GEBUEHR

        formattedPrice = "{:.2f}".format(price)
        return formattedPrice
    
    def getGesamterPreisDesAusleihens(self, id):
        scooter = self.getScooterById(id)
    
        ausleihZeitpunkt = scooter.getAusleihZeitpunkt()
        rueckgabeZeitpunkt = scooter.getRueckgabeZeitpunkt()

        timeDifferance = self.getTimeDifferance(ausleihZeitpunkt, rueckgabeZeitpunkt)#

        hours = timeDifferance[0]
        minutes = timeDifferance[1]
        seconds = self.getCurrentTimeStamp()[2]

        timeInMinutes = int(hours) * 60 + int(minutes)
        if seconds != 0:
            timeInMinutes += 1

        return timeInMinutes * ScooterRentalApp.PRICE_PER_MINUTE_DRIVE + ScooterRentalApp.GEBUEHR

    def getGesamterPreisDerReservierung(self, id):
        scooter = self.getScooterById(id)
    
        beginnZeitpunkt = scooter.getBeginnZeitpunkt()
        rueckgabeZeitpunkt = scooter.getRueckgabeZeitpunkt()

        if not scooter.getScooterWasReserviert():
            return 0

        timeDifferance = self.getTimeDifferance(beginnZeitpunkt, rueckgabeZeitpunkt)#

        hours = timeDifferance[0]
        minutes = timeDifferance[1]
        seconds = self.getCurrentTimeStamp()[2]

        timeInMinutes = int(hours) * 60 + int(minutes)
        if seconds != 0:
            timeInMinutes += 1

        return timeInMinutes * ScooterRentalApp.PRICE_PER_MINUTE_RESERVE + ScooterRentalApp.GEBUEHR


    def scooterAusleihen(self, id):

        selected_scooter = self.getScooterById(id)
        
        if selected_scooter:
            #print("\n\n- Scooter Ausleihen -\n")
            aktuelleZeit = self.getCurrentTimeStamp()
            ausleihZeitpunkt = [aktuelleZeit[0], aktuelleZeit[1], aktuelleZeit[2]]
            selected_scooter.setAusleihZeitpunkt(ausleihZeitpunkt)
            #formattedPricePerMinute = "{:.2f}".format(self.PRICE_PER_MINUTE_DRIVE)
            ausleihZeitpunkt = selected_scooter.getAusleihZeitpunkt()
            
            #print(f"Du hast den Scooter {selected_scooter.getId()} ausgeliehen.")
            #print(f"Scooter ausgeliehen um: {ausleihZeitpunkt[0]}:{ausleihZeitpunkt[1]} Uhr")
            #print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {self.PRICE_PER_MINUTE_DRIVE}€")
            #print(f"Der Preis pro angefangene Minute beträgt {formattedPricePerMinute}€")

            if selected_scooter.getBeginnZeitpunkt() == [0,0,0]:
                selected_scooter.setBeginnZeitpunkt(self.getCurrentTimeStamp())

            selected_scooter.setScooterAusgeliehen(True)
            self.bearbeiteterScooterId = selected_scooter.getId()
            self.ausgeliehene_scooter.append(selected_scooter)

    def scooterZurueckgeben(self, id):
        selected_scooter = self.getScooterById(id)
        
        if selected_scooter:
            selected_scooter.setRueckgabeZeitpunkt(self.getCurrentTimeStamp())
            selected_scooter.setScooterAusgeliehen(False)
            selected_scooter.setScooterReserviert(False)
            self.ausgeliehene_scooter.remove(selected_scooter)
            
            #print("\n\n- Scooter Zurueckgeben -\n")
           
            ausleihZeitpunkt = selected_scooter.getAusleihZeitpunkt()
            rueckgabeZeitpunkt = selected_scooter.getRueckgabeZeitpunkt()

            #print(f"Scooter zurueckgeben am: {rueckgabeZeitpunkt[0]}:{rueckgabeZeitpunkt[1]} Uhr")
            
            timeDifference = self.getTimeDifferance(ausleihZeitpunkt, rueckgabeZeitpunkt)
            hours = timeDifference[0]
            minutes = timeDifference[1]
            seconds = self.getCurrentTimeStamp()[2]

            #print(f"Insgesamt ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")
            
            timeInMinutes = int(hours) * 60 + int(minutes)
            if seconds != 0:
                timeInMinutes += 1

            preisA = self.getGesamterPreisDesAusleihens(id)
            preisB = self.getGesamterPreisDerReservierung(id)

            preisGesamt = preisA + preisB

            if selected_scooter.getScooterWasReserviert():
                preisGesamt -= 1

            formattedPrice = "{:.2f}".format(preisGesamt)
            selected_scooter.setInsgesamterPreis(formattedPrice)

            selected_scooter.setScooterWasReserviert(False)

    def scooterReservieren(self, id):

        selected_scooter = self.getScooterById(id)

        current_time = datetime.now()
        hours, minutes, seconds = [0,20,0] 
        reservierungsZeitpunkt = current_time + timedelta(hours=hours, minutes=minutes, seconds=seconds)

        hours = int(reservierungsZeitpunkt.hour)
        minutes = int(reservierungsZeitpunkt.minute)
        seconds = int(reservierungsZeitpunkt.second)

        if selected_scooter:
            selected_scooter.setReservierungsZeitpunkt([hours, minutes, seconds])
            selected_scooter.setScooterReserviert(True)
            selected_scooter.setScooterWasReserviert(True)
            
            if selected_scooter.getBeginnZeitpunkt() == [0,0,0]:
                selected_scooter.setBeginnZeitpunkt(self.getCurrentTimeStamp())

            if selected_scooter.getScooterReserviert():
                self.ausgeliehene_scooter.append(selected_scooter)

        self.bearbeiteterScooterId = id

    def scooterReservierenBeenden(self, id):
        selected_scooter = self.getScooterById(id)
        selected_scooter.setScooterReserviert(False)

        
    #def uebersichtScooter(self):
        #if self.ausgeliehene_scooter:
            #selected_scooter = None
           # for scooter in self.ausgeliehene_scooter:
               # if scooter.getScooterReserviert():
                   # selected_scooter = scooter
            
            #if selected_scooter and selected_scooter.getScooterReserviert():
                #reservierungsZeitpunkt = selected_scooter.getReservierungsZeitpunkt()
                #print("Es ist eine Reservierung vorhanden")
                #print(f"Der Scooter {selected_scooter.getId()} ist für dich reserviert")
                #if reservierungsZeitpunkt[1] <= 9:
                #    print(f"Deine Reservierung beginnt um: {reservierungsZeitpunkt[0]}:0{reservierungsZeitpunkt[1]}")
                #else:
                #    print(f"Deine Reservierung beginnt um: {reservierungsZeitpunkt[0]}:{reservierungsZeitpunkt[1]}")
            #else:
                #print("Du hast keinen Scooter reserviert")

    def hasReservierung(self):
        for scooter in self.ausgeliehene_scooter:
            if scooter.getScooterReserviert():
                return True
        return False
