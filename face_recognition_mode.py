import face_recognition
import cv2
import numpy as np

class FaceRecognitionMode:
    def __init__(self):
        self.known_faces = {}
        self.known_encodings = []
        self.known_names = []

    def add_face(self, name, image):
        encoding = face_recognition.face_encodings(image)[0]
        self.known_encodings.append(encoding)
        self.known_names.append(name)

    def identify_face(self, image):
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_names[first_match_index]

            face_names.append(name)

        return face_locations, face_names