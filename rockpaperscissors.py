#ROCK PAPER SCISSORS

#This program creates a GUI environment for the user
#to play rock-paper-scissors with the computer. The
#composition is currently in the key of C. The
#result of each round decides whether the program
#appends a random choice out of the major or minor
#triad of C to the piece (or, in the case of a tie,
#the note B). The user can save a .mid file of the
#random composition.


from tkinter import *
import random
import string
from music21 import *

options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
defeats = {1: 3, 2: 1, 3: 2} # key defeats value
stream1 = stream.Stream()

window = Tk()
window.geometry('500x300')
var = IntVar()
key_var = IntVar()
cont_q = IntVar()

def matching(choice1, choice2):
    major_triad = ['C', 'E', 'G']
    minor_triad = ['C', 'Eb', 'G']
    if choice1 == choice2: # tie
        note_equal = note.Note('B', type = 'half')
        stream1.append(note_equal)
        return 'B'
    elif options.get(choice1) == choice2: # if user_choice defeats computer_choice
        sound = random.choice(major_triad)
        note_victory = note.Note(sound, type = 'whole')
        stream1.append(note_victory)
        return sound
    else:
        sound = random.choice(minor_triad) #if user is defeated
        note_defeat = note.Note(sound, type = 'whole')
        stream1.append(note_defeat)
        return sound

def game():
    user = var.get()
    user_choice = options.get(user)  # convert int input to str name of choice (eg. 1 --> 'Rock')

    items = [item[0] for item in options.items()]
    computer = random.choice(items)
    computer_choice = options.get(computer)

    next_note = matching(user_choice, computer_choice)
    text_display = 'You chose ' + user_choice + '.\n' + 'The computer chose ' + computer_choice + '.\n' + 'The new sound is ' +  next_note + '.\n' + 'Continue by clicking a new radio button or save and exit below.\n'
    label.config(text=text_display)

def save_midi():
    name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)]) #random filename
    track_name = name + '.mid'
    stream1.write("midi", track_name)

# Buttons for user choice: Rock, Paper, Scissors

rock = Radiobutton(window, text="Rock", variable=var, value=1,
                       command=game)
rock.pack(anchor=W)
paper = Radiobutton(window, text="Paper", variable=var, value=2,
                        command=game)
paper.pack(anchor=W)
scissors = Radiobutton(window, text="Scissors", variable=var, value=3,
                           command=game)
scissors.pack(anchor=W)

# Announce change to user

label = Label(window)
label.pack()

#Buttons to control

save = Button(text = "Save", command=save_midi)
save.pack(anchor = 'center')
exit = Button(text="Exit", command=window.destroy)
exit.pack(anchor = 'center')

#execute
window.mainloop()





