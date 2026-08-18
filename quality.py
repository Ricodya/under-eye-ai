
import cv2
import numpy as np


# ============================================================
# IMAGE QUALITY — BASIC METRICS
# ============================================================

def calculate_brightness_variation(
    image
):

    if image is None:
        return 0.0

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    return float(
        np.std(gray)
    )


# ============================================================
# IMAGE QUALITY SCORE
# ============================================================

def basic_quality_score(
    image
):

    if image is None:
        return 0

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    brightness = float(
        np.mean(gray)
    )

    variation = float(
        np.std(gray)
    )

    score = 100

    # Very dark / very bright images
    if brightness < 50 or brightness > 220:
        score -= 25

    # Very high variation
    if variation > 80:
        score -= 15

    # Very low variation
    if variation < 15:
        score -= 10

    return max(
        0,
        min(100, int(score))
    )
