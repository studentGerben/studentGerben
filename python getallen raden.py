from tkinter import *
from tkinter import messagebox
from random import randint


# Hoe groot je de interface wilt en de title van het spel
root = Tk()
root.geometry("400x400")
root.title("Getallen raden spel")

# Hier geneer je het nummer
def GenerateNumberFunc():
    global Number
    Number = randint(1, 25)
    messagebox.showinfo("Er is een nummer gegenereerd!", "Raad het nummer")

# Wanneer je gegokt hebt geeft het programma aan of het "Juist, Lager/Hoger gegokt moet worden"
def GuessNumberFunc():
    global Number
    UserResponse = AnswerEntry.get()

    UserResponse = int(UserResponse)
    if UserResponse > Number:
        ResultLabel.config(text="Niet correct! Raad eens lager", fg="Red")
    elif UserResponse < Number:
        ResultLabel.config(text="Niet correct! Raad hoger", fg="Red")
    else:
        ResultLabel.config(text="Je hebt het goed geraden! Het nummer was {}".format(Number), fg="Green")
        # hier sluit het spel af wanneer je goed hebt gegokt
        AnswerEntry.delete(0, "end")
# Title met font en font size
Title = Label(root, text="Nummer raadspel", font=("Verdana", 25))
Title.pack()

# Dit stukje code houd de opmaak netjes, title & font, size etc.
MainFrame = Frame(root)
MainFrame.pack(pady=10)

GuessNumLabel = Label(MainFrame, text="Raad een getal van 1 tot 25", font=("Verdana", 16))
GuessNumLabel.pack()
GuessNumLabel = Label(MainFrame, text="Druk eerst op de genereer knop om te beginnen", fg="Red", font=("Verdana", 8))
GuessNumLabel.pack()

AnswerEntry = Entry(MainFrame, font=("Gill Sans", 16))
AnswerEntry.pack(pady=10)

GenerateNumberBtn = Button(MainFrame, text="Genereer nummer", width=15, font=("Verdana", 16), background="#30BAEC", command=GenerateNumberFunc)
GenerateNumberBtn.pack()


GuessBtn = Button(MainFrame, text="Gokken", width=14, font=("Verdana", 16), background="#1FF137", command=GuessNumberFunc)
GuessBtn.pack(pady=5)


ResultLabel = Label(MainFrame, text="", font=("Verdana", 16))
ResultLabel.pack()

# uitvoert wat we willen uitvoeren in een applicatie (laat Tkinter de applicatie starten)
root.mainloop()