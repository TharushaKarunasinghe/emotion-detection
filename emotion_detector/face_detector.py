# emotion_detector/face_detector.py
from deepface import DeepFace

def detect_emotion(image_path):
    try:
        # Analyze the image for facial emotion
        analysis = DeepFace.analyze(image_path, actions=['emotion'])
        dominant_emotion = analysis[0]['dominant_emotion']
        return dominant_emotion
    except Exception as e:
        return str(e)
