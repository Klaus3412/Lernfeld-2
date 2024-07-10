import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import *

import ScooterRentalAppUi

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ScooterRentalAppUi

root = ctk.CTk()
root.title("ScooTeq App")
root.iconbitmap("UiVersion/scooTecIcon.ico")
root.geometry("500x350")

# Windows
frontPage = None
scooterUebersicht = None

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def update_time(updatingLabel):
    updatingLabel.configure(text=app.getCurrentTimeStamp())
    updatingLabel.after(1000, update_time, updatingLabel)


#fruehererZeitpunkt = selected_scooter.getAusleihZeitpunkt()
fruehererZeitpunkt = [8,30,0]
spaetererZeitpunkt = app.getCurrentTimeStamp()

def update_field(updatingLabel):
    global fruehererZeitpunkt
    spaetererZeitpunkt = app.getCurrentTimeStamp()
    time_difference = app.getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt)
    updatingLabel.configure(text=time_difference)
    updatingLabel.after(1000, update_field, updatingLabel)

def create_frontPage():
    global frontPage
    frontPage = ctk.CTkFrame(master=root)
    frontPage.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)

    label = ctk.CTkLabel(frontPage, text="Was möchtest du machen?", font=("Helvetica", 15, "bold"))
    label.pack(pady=12, padx=10)

    ausleihen_button = ctk.CTkButton(frontPage, text="ausleihen", command=app.scooterAusleihen)
    ausleihen_button.pack(pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(frontPage, text="reservieren", command=app.scooterReservieren)
    reservieren_button.pack(pady=12, padx=18)
    
    reservieren_button = ctk.CTkButton(frontPage, text="Beenden", command=root.destroy)
    reservieren_button.pack(pady=12, padx=18)

    switch_button1 = ctk.CTkButton(frontPage, text="Go to Frame 2", command=lambda: show_frame(scooterUebersicht))
    switch_button1.pack(pady=20)

def create_scooterUebersicht():
    global scooterUebersicht
    scooterUebersicht = ctk.CTkFrame(root)
    scooterUebersicht.grid(row=0, column=0, sticky='nsew', pady=20, padx=60)
    
    dauerAusleihenField = ctk.CTkLabel(scooterUebersicht, text="", font=("Calibri", 23))
    dauerAusleihenField.pack(pady=20)

    update_field(dauerAusleihenField)

    exampleTimeField = ctk.CTkLabel(scooterUebersicht, text="", font=("Calibri", 23))
    exampleTimeField.pack(pady=20)

    update_time(exampleTimeField)

    switch_button2 = ctk.CTkButton(scooterUebersicht, text="Go to Frame 1", command=lambda: show_frame(frontPage))
    switch_button2.pack(pady=20)

def show_frame(frame):
    frame.tkraise()

def runApp():
    create_frontPage()
    create_scooterUebersicht()
    show_frame(frontPage)
    root.mainloop()

while True:
    runApp()
