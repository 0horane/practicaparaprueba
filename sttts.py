import tkinter as tk
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

r.energy_threshold  = 1000
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def hi():
    print("hello")

def sttts():             # Reading Microphone as source # listening the speech and store in audio_text variable
#    global listening
#    if listening==True:
#        return
#    listening=True
    with sr.Microphone() as source:
        print("Talk")
        lbl_output["text"] = "Listening..."
        audio_text = r.listen(source)
        print("Time over, thanks")
        lbl_output["text"] = "Time over, thanks"
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            retext=r.recognize_google(audio_text, language=ent_lang.get())
            print(retext)
            lbl_output["text"] = retext
            engine.say(retext)
            engine.runAndWait()
        except:
             print("Sorry, I did not get that") 
             
#    listening=False
    
def tts():
    engine.say(txt_tts.get("1.0", tk.END))
    engine.runAndWait()
    
def updateEngine():
    rate = engine.getProperty('rate')  
    engine.setProperty('rate', int(ent_rate.get()))     

    volume = engine.getProperty('volume')   
    engine.setProperty('volume',float(ent_volume.get()))    
    
    voices = engine.getProperty('voices')    
    engine.setProperty('voice', voices[voicedict.index(voicevar.get())].id)
    
    

    
window = tk.Tk()
window.geometry("900x300")

voicevar = tk.StringVar(window)
voicedict= []
for item in engine.getProperty('voices'):
    voicedict.append(item.name)

lbl_title = tk.Label(text="Speech To Text To Speech Control panel thing")
lbl_title.pack()

frm_speech = tk.Frame(master=window, width=400, height=100)
frm_sttts = tk.Frame(master=frm_speech, width=200, height=100, padx=5, pady=20)
frm_tts = tk.Frame(master=frm_speech, width=200, height=100, padx=5, pady=20)
frm_config = tk.Frame(master=window, width=400, height=100)

frm_speech.pack()
frm_sttts.grid(row=0, column=0)
frm_tts.grid(row=0, column=1)
frm_config.pack()

btn_StartSttts = tk.Button(master=frm_sttts,text="Listen from Microphone", command=sttts)
btn_StartSttts.pack()

lbl_output = tk.Label(master=frm_sttts,text="", width=50, height=5, wraplength=200)
lbl_output.pack()

txt_tts = tk.Text(master=frm_tts,height=5,width=30)
txt_tts.pack()

btn_StartTts = tk.Button(master=frm_tts,text="Read from Text", command=tts)
btn_StartTts.pack()



lbl_voice = tk.Label(master=frm_config,text="     Voice (0-3)     ")
lbl_voice.grid(row=0, column=0)

lbl_volume = tk.Label(master=frm_config,text="     Volume (0.0-1.0)     ")
lbl_volume.grid(row=0, column=1)

lbl_rate = tk.Label(master=frm_config,text="     Rate (???)     ")
lbl_rate.grid(row=0, column=2)

#ent_voice=tk.Entry(master=frm_config,width=15) 
ent_volume=tk.Entry(master=frm_config,width=5)
ent_rate=tk.Entry(master=frm_config, width=5)

#ent_voice.grid(row=1, column=0)
ent_volume.grid(row=1, column=1)
ent_rate.grid(row=1, column=2)

ent_lang=tk.Entry(master=frm_config,width=5)
ent_lang.grid(row=2, column=0)

#ent_voice.insert(0, "1")
ent_volume.insert(0, engine.getProperty('volume'))
ent_rate.insert(0, engine.getProperty('rate'))
ent_lang.insert(0, 'en_US')

opm_voice = tk.OptionMenu(frm_config, voicevar, *voicedict)
opm_voice.grid(row=1, column=0)

btn_StartTts = tk.Button(master=frm_config ,text="Update", command=updateEngine)
btn_StartTts.grid(row=2, column=1)



window.mainloop()



