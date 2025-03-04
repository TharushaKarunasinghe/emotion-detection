# app.py
from flask import Flask, render_template, Response
import cv2
from emotion_detector.face_detector import detect_emotion
from emotion_detector.voice_detector import recognize_audio_emotion

app = Flask(__name__)

# Capture video from webcam
def gen_frames():
    cap = cv2.VideoCapture(0)  # Start webcam capture
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotion in the current frame
        emotion = detect_emotion(frame)
        
        # Draw text on the frame
        cv2.putText(frame, f"Emotion: {emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Encode the frame to send to the frontend (Flask)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/audio')
def audio():
    emotion = recognize_audio_emotion()
    return f"Detected emotion: {emotion}"

if __name__ == '__main__':
    app.run(debug=True)
