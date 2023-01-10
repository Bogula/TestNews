import streamlit as st
import whisper
from audio_recorder_streamlit import audio_recorder


# Whisper

Model ="base"
English = True

model = whisper.load_model(f'{Model}{".en" if English else ""}')
#system("say --rate=190 --voice=Anna Willkommen beim Mobility Genius.")
system("say --rate=190 --voice=Anna Willkommen beim Mobility Genius. Drück auf die Mikrofonbutton um was zu fragen") 
    

audio_bytes = audio_recorder(pause_threshold=1.0)
if audio_bytes:
    wav= st.audio(audio_bytes, format="audio/wav")
    st.write(type(audio_bytes))
    wav_file = open("audio.wav", "wb")
    wav_file.write(audio_bytes)
   

