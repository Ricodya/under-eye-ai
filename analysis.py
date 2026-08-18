
import cv2
import numpy as np
import mediapipe as mp


# ============================================================
# MEDIAPIPE FACE LANDMARKS
# ============================================================

mp_face_mesh = mp.solutions.face_mesh


# ============================================================
# FACE LANDMARK DETECTION
# ============================================================

def detect_face_landmarks(image):

    rgb_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5
    ) as face_mesh:

        result = face_mesh.process(
            rgb_image
        )

    if not result.multi_face_landmarks:
        return None

    return result.multi_face_landmarks[0]


# ============================================================
# IMAGE LOADER
# ============================================================

def load_image(image_path):

    image = cv2.imread(
        image_path
    )

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    return image


# ============================================================
# NOTE
# ============================================================

# The complete experimental analysis logic remains in the
# validated Colab notebook backup.
#
# This file is the initial GitHub-ready analysis module.
#
# We will migrate the remaining validated functions here
# incrementally instead of guessing or rewriting them.
