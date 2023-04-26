import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import ttk
import textblob
import googletrans
import pyttsx3
from tkinter import messagebox

app = tk.Tk(__name__)
app.title('Just Translate It!')
app.iconbitmap(r"C:\Users\hp\OneDrive\Desktop\PROJECT\project\l.ico")
app.geometry('700x700')

img=Image.open(r"C:\Users\hp\OneDrive\Desktop\PROJECT\project\jod2.jpg")
img_resized=img.resize((700,700))
img2=ImageTk.PhotoImage(img)
img2=ImageTk.PhotoImage(img_resized)
Image_label=tk.Label(app,image=img2)
Image_label.grid()

def translator():
    opt2.delete(1.0,END)
    try:
        for key,Value in languages.items():
            if(Value==fv.get()):
                from_language_key=key
        for key,Value in languages.items():
            if(Value==sv.get()):
                to_language_key=key
        words=textblob.TextBlob(opt.get(1.0,END))
        words=words.translate(from_lang=from_language_key,to=to_language_key)
        opt2.insert(1.0,words)
        engine=pyttsx3.init()
        engine.say(words)
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("Translator",e)


def clears():
    opt.delete(1.0,END)
    opt2.delete(1.0,END)

languages=googletrans.LANGUAGES
lang_list=list(languages.values())

opt=Text(app,height=5,width=30)
opt.place(x='60',y='300')

opt2=Text(app,height=5,width=30)
opt2.place(x='400',y='300')

tk.Label(app,text='Choose a Language',font=('Comic Sans MS',13)).place(x='80',y='220')
tk.Label(app,text='Translated Language',font=('Comic Sans MS',13)).place(x='400',y='220')

fv=ttk.Combobox(app,width=30)
fv.set('english')
fv.place(x='70',y='260')

sv=ttk.Combobox(app,width=30,value=lang_list) 
sv.current(26)
sv.place(x='400',y='260')

clear=Button(app,text='Translate it!' ,font=('Comic Sans MS',12),width=30,bg='blue',fg='white',command=translator)
clear.place(x='220',y='400')

clear=Button(app,text='clear',width=20,bg='red',fg='white',command=clears)
clear.place(x='300',y='450')

app.mainloop()