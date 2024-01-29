from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import speech_recognition as sr
from tkinter.messagebox import showinfo
from gtts import gTTS
import pyttsx3
import os

root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.config(bg = 'ghost white')

root.title("Language Translator")
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()

def speak(text: str):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    os.system("start temp.mp3")
    
def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
        except Exception as e:
            showinfo(title='Error!', message=e)
            speak("I am sorry, I did not get that, but could you please repeat that")
            return " "
        return query
   
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Input_text.place(x = 30 , y = 100)

input_btn = Button(text='Speak',font = 'arial 12 bold',pady = 5, command=lambda: Input_text.insert(END, record()), bg = 'royal blue1', activebackground = 'sky blue')
input_btn.place(x=200, y=60)
   
   
Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('Choose input language')
dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('Choose output language')


def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0,END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
    speak(translated.text)


trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y= 180 )
root.mainloop()

