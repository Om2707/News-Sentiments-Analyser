from gtts import gTTS
import os

def text_to_speech(text, lang='hi', filename="output.mp3"):
    """Convert text to Hindi speech and save as an MP3 file"""
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    return filename
