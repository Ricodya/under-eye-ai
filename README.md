# Under-Eye AI

## Computer Vision Based Under-Eye Visual Analysis Prototype

Under-Eye AI is an experimental computer-vision project designed to analyze
under-eye regions from facial images using facial landmarks, brightness
measurements, image-quality assessment, and multi-image comparison.

## Project Overview

The system processes facial images through the following pipeline:

Input Face Image
→ Face Detection
→ Facial Landmark Detection
→ Under-Eye Region Identification
→ Brightness Analysis
→ Nearby Skin Comparison
→ Relative Darkness
→ Brightness Variation
→ Image Quality Assessment
→ Multi-Image Comparison
→ Interactive Dashboard

## Features

- Facial landmark detection
- Under-eye region identification
- Under-eye brightness measurement
- Nearby-skin brightness comparison
- Relative darkness calculation
- Brightness variation analysis
- Image-quality assessment
- Multi-image comparison
- Visual comparison charts
- Highlighted AI analysis preview
- Interactive Gradio dashboard
- Technical analysis report

## Analysis Metrics

### Under-Eye Brightness

Average brightness measured within the selected under-eye region.

### Nearby Skin Brightness

Brightness measured from a nearby facial-skin reference region.

### Relative Darkness

Relative Darkness (%) =
((Nearby Skin Brightness - Under-Eye Brightness)
 / Nearby Skin Brightness) × 100

### Normalized Brightness Ratio

Normalized Ratio =
Under-Eye Brightness / Nearby Skin Brightness

### Brightness Variation

Standard deviation is used as an experimental measure of local brightness
variation.

## Image Quality

The prototype evaluates factors such as:

- Facial detection
- Lighting balance
- Brightness variation
- Under-eye texture variation
- Left/right measurement consistency

Example prototype quality categories:

90–100  → Good
70–89   → Moderate
Below 70 → Lower quality

These are prototype-level rules and are not clinical standards.

## Technology Stack

Python
OpenCV
MediaPipe
NumPy
Pandas
Matplotlib
Gradio

## Project Structure

under-eye-ai/
├── app.py
├── analysis.py
├── visualization.py
├── quality.py
├── requirements.txt
├── README.md
├── assets/
├── outputs/
└── backup/

## Installation

Clone the repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>

cd under-eye-ai

Install dependencies:

pip install -r requirements.txt

## Running the Application

python app.py

The Gradio interface will start locally.

## Dashboard

The dashboard provides:

1. Face-image upload
2. AI analysis preview
3. Left-eye measurement
4. Right-eye measurement
5. Overall comparison
6. Image-quality score
7. Visual comparison charts
8. Detailed technical report

## Example Experimental Results

Example measurements from the prototype include:

8500 (1).jpg

Left Eye:
Relative Darkness: 34.11%

Right Eye:
Relative Darkness: 16.38%

Example image-quality results:

8500 (1).jpg → 70/100
8498 (1).jpg → 95/100
8499 (2).jpg → 90/100

These are experimental computer-vision measurements.

## Limitations

Results can be affected by:

- Lighting conditions
- Camera exposure
- Shadows
- Camera angle
- Facial expression
- Image resolution
- Skin illumination
- Landmark detection accuracy

The prototype is therefore a computer-vision demonstration and is not a
clinically validated system.

## Future Improvements

Possible future development includes:

- Larger and more diverse datasets
- Better illumination normalization
- Improved face alignment
- Robust under-eye segmentation
- Deep-learning based feature extraction
- More rigorous validation
- Explainable AI visualizations
- Cross-device robustness testing

## Privacy

Facial images are sensitive visual data.

A production implementation should include appropriate consent, secure
storage, data deletion controls, access controls, and privacy documentation.

## Disclaimer

Under-Eye AI is an experimental computer-vision prototype and is not a
medical diagnostic tool.

The measurements should not be interpreted as medical severity scores,
diagnoses, or treatment recommendations.
