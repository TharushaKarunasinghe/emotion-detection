# emotion_detector/voice_detector.py
import speech_recognition as sr

def recognize_audio_emotion():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone to record audio
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        
        # For now, just check for common words (like 'happy', 'angry', etc.)
        if 'happy' in text:
            return "Happy"
        elif 'sad' in text:
            return "Sad"
        elif 'angry' in text:
            return "Angry"
        else:
            return "Neutral"
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error with speech recognition: {e}"
