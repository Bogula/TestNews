import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder(pause_threshold=1.0)
if audio_bytes:
    wav= st.audio(audio_bytes, format="audio/wav")
    st.write(type(audio_bytes))
   
