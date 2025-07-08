import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the WAV file


audio_file = "your file path" 


# Opening the audio file and recognize speech
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Recognize speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data)
    print("Text from audio: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

    


'''import speech_recognition as sr
z
# Initialize recognizer
recognizer = sr.Recognizer()

# Load the WAV file
audio_file = "your file path "

# Open the audio file and recognize speech using PocketSphinx
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Recognize speech using PocketSphinx
try:
    text = recognizer.recognize_sphinx(audio_data)
    print("Text from audio: ", text)
except sr.UnknownValueError:
    print("PocketSphinx could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from PocketSphinx service; {e}")'''




#language convertion like tamil
'''import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Path to your Tamil audio file
audio_file = "your file path with \\"

# Recognize Tamil speech
with sr.AudioFile(audio_file) as source:
    print("Processing the audio...")
    audio_data = recognizer.record(source)  # Load the audio into memory

try:
    # Recognize speech with Tamil language code
    text = recognizer.recognize_google(audio_data, language="hi-IN")
    print("Recognized Text in Tamil:", text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")'''



#instead we can use google api which is cost users for their work and it can be more accurate


