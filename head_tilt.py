import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

def detect_head_tilt():
    ret, frame = cap.read()
    if not ret:
        return "C"

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return "C"

    landmarks = results.multi_face_landmarks[0].landmark

    left_eye = landmarks[33]
    right_eye = landmarks[263]

    dx = right_eye.x - left_eye.x
    dy = right_eye.y - left_eye.y

    angle = math.degrees(math.atan2(dy, dx))

    if angle > 15:
        return "L"
    elif angle < -15:
        return "R"
    else:
        return "C"
