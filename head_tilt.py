import cv2
import mediapipe as mp

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

def get_head_tilt():
    ret, frame = cap.read()
    if not ret:
        return None

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        lm = result.multi_face_landmarks[0].landmark

        left_eye = lm[33].x
        right_eye = lm[263].x

        diff = left_eye - right_eye

        if diff > 0.015:
            return "LEFT"
        elif diff < -0.015:
            return "RIGHT"

    return None
