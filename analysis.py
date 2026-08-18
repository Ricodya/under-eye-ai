from pathlib import Path
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# ============================================================
# MEDIAPIPE FACE LANDMARKER
# ============================================================

MODEL_PATH = str(Path(__file__).parent / "assets" / "face_landmarker.task")

_base_options = python.BaseOptions(
    model_asset_path=MODEL_PATH
)

_options = vision.FaceLandmarkerOptions(
    base_options=_base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_faces=1,
    min_face_detection_confidence=0.5,
    min_face_presence_confidence=0.5,
    min_tracking_confidence=0.5,
)

_face_landmarker = vision.FaceLandmarker.create_from_options(
    _options
)


# ============================================================
# FACE LANDMARK DETECTION
# ============================================================

def detect_face_landmarks(image):

    if image is None:
        return None

    rgb_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_image
    )

    result = _face_landmarker.detect(mp_image)

    if not result.face_landmarks:
        return None

    return result.face_landmarks[0]


# ============================================================
# IMAGE LOADER
# ============================================================

def load_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    return image
