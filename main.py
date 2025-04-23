import json
from re import search
from string import whitespace
from tkinter import *
from PIL import Image, ImageTk  # Make sure Pillow is installed
from difflib import get_close_matches
from tkinter import messagebox
# get_close_matches(word,possibilities, n ,cutoff)
import json
import pyttsx3 # will help to convert text to audio

engine = pyttsx3.init()  # creating instance of engine class

voice = engine.getProperty('voices') # To get the voice
engine.setProperty('voice',voice[1].id)

# function part

def search():
    data = json.load(open('data.json'))
    word = entryword.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        # print(meaning)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n')
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        print((close_match))
        res = messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')

        if res == True:
            entryword.delete(0,END) # jab meaning galat ho to sahi meaning entry field me insert ho  jaye
            entryword.insert(END,close_match)
            meaning = data[close_match]

            textarea.delete(1.0,END)
            for value in meaning:
                textarea.insert(END, u'\u2022' + value + '\n')
        else:
            messagebox.showerror('Error',"The word doesn't exist, plese double check it")
            entryword.delete(0,END)
            textarea.delete(1.0,END)
    else:
        messagebox.showinfo('Information',"The word doesn't exist")
        entryword.delete(0,END) # deleted from word entry field
        textarea.delete(1.0,END)  # deleted from meaning text area

def clear():
    entryword.delete(0,END)
    textarea.delete(1.0,END)

def exit():
    res = messagebox.askyesno('Confirm',"Do you want to exit ?")
    if res == True:
        root.destroy()
    else:
        pass

def word_to_audio():
    engine.say(entryword.get())
    engine.runAndWait()

def meaning_to_audio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()


# GUI part


root = Tk()

root.geometry('1000x600+100+30')
root.title("Talking Disctionary")
root.resizable(0,0)

bgimg = PhotoImage(file='design-311260_1280.png')
bgLabel = Label(root,image=bgimg)
bgLabel.place(x=0, y=0)

enterwordLabel = Label(root, text='Enter Word', font=('castellar','25','bold'),background='orange', foreground='black')
enterwordLabel.place(x = 50, y= 50)

entryword = Entry(root, font=('arial',18,'bold'),justify="center",border=5, relief=RIDGE)
entryword.place(x=100, y= 160)

imgr = Image.open("basic-ui.png")  # Make sure this file exists

#  Resize it
imgr = imgr.resize((60, 60))

# Convert it to a Tkinter-compatible image
imgr = ImageTk.PhotoImage(imgr)

# Now use it in a button
btnSearch = Button(
    root,
    image=imgr,
    border=0,
    bg='skyblue',
    activebackground='skyblue',
    cursor='hand2',
    command=search
)
btnSearch.place(x=120, y=220)

# Prevent garbage collection
btnSearch.image = imgr

# ========================================================================

# micButton ******************************

imgMic = Image.open("microphone.png")  # Make sure this file exists

# Resize it
imgMic = imgMic.resize((60, 60))

# Convert it to a Tkinter-compatible image
imgMic = ImageTk.PhotoImage(imgMic)

# Step 4: Now use it in a button
btnSearch = Button(
    root,
    image=imgMic,
    borderwidth=0,
    highlightthickness=0,
    bg='skyblue',
    activebackground='skyblue',
    cursor='hand2',
    command=word_to_audio
)
btnSearch.place(x=270, y=220)

# Prevent garbage collection
btnSearch.image = imgMic

#============================================================================

# Meaning Label ******************
textLabel = Label(root, text='MEANING', font=('castellar','25','bold'),background='skyblue', foreground='black')
textLabel.place(x = 150, y= 330)


# Meaning Text Area ***************************************************************

textarea  = Text(root,  width=50, height=10, font=('arial',10,'bold'),border=5, relief=GROOVE)
textarea.place(x=80, y= 400)

# ===============================================================================

# audioButton
audioImg = Image.open("microphone.png")  # Make sure this file exists

# Resize it
audioImg = audioImg.resize((60, 60))

# Convert it to a Tkinter-compatible image
audioImg = ImageTk.PhotoImage(audioImg)

# Now use it in a button
audioButton = Button(
    root,
    image=audioImg,
    borderwidth=0,
    highlightthickness=0,
    bg='skyblue',
    activebackground='skyblue',
    cursor='hand2',
    command=meaning_to_audio
)
audioButton.place(x=450, y=450)

# Prevent garbage collection
audioButton.image = audioImg

# ===============================================================


# clear button
clearImg = Image.open("closed.png")  # Make sure this file exists

# Resize it
clearImg = clearImg.resize((60, 60))

# Convert it to a Tkinter-compatible image
clearImg = ImageTk.PhotoImage(clearImg)

# Now use it in a button
clearButton = Button(
    root,
    image=clearImg,
    borderwidth=0,
    highlightthickness=0,
    bg='skyblue',
    activebackground='skyblue',
    cursor='hand2',
    command= clear
)
clearButton.place(x=530, y=450)

# Prevent garbage collection
clearButton.image = clearImg

# ====================================================================================

# exiButton
exitImg = Image.open("emergency-exit.png")  # Make sure this file exists

# Step 2: Resize it
exitImg = exitImg.resize((60, 60))

# Convert it to a Tkinter-compatible image
exitImg = ImageTk.PhotoImage(exitImg)

# Step 4: Now use it in a button
exitButton = Button(
    root,
    image=exitImg,
    borderwidth=0,
    highlightthickness=0,
    bg='skyblue',
    activebackground='skyblue',
    cursor='hand2',
    command=exit
)
exitButton.place(x=600, y=450)

# Prevent garbage collection
exitButton.image = exitImg
# ======================================================================================

def enter_function(event):
    search()

root.bind('<Return>',enter_function)

root.mainloop()
