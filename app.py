
import gradio as gr
import cv2
from pathlib import Path


from analysis import detect_face_landmarks
from visualization import create_themed_chart, prepare_preview_image
from quality import basic_quality_score, calculate_brightness_variation


# ============================================================
# THEME
# ============================================================

final_theme = gr.themes.Soft(
    primary_hue="purple",
    secondary_hue="purple",
    neutral_hue="slate"
)


# ============================================================
# CSS
# ============================================================

final_css = """

.gradio-container {
    max-width: 1200px !important;
}

h1, h2, h3 {
    font-weight: 700 !important;
}

button.primary {
    font-weight: 600 !important;
}

"""


# ============================================================
# ANALYSIS CALLBACK
# ============================================================

def analyze_images(files):

    if not files:
        return (
            None,
            "—",
            "—",
            "—",
            "—",
            "Upload images and click **Analyze Images**.",
            None,
            None,
            "No images supplied."
        )

    results = []
    quality_values = []
    brightness_values = []
    names = []

    for file in files:

        image = load_uploaded_image(file)

        landmarks = detect_face_landmarks(image)

        quality = basic_quality_score(image)
        brightness = calculate_brightness_variation(image)

        results.append(
            (file, landmarks, quality, brightness)
        )

        quality_values.append(quality)
        brightness_values.append(brightness)
        names.append(Path(file).stem)

    first_image, landmarks, quality, brightness = results[0]

    face_status = (
        "Face detected"
        if landmarks is not None
        else "No face detected"
    )

    summary = (
        f"### Analysis Complete\n\n"
        f"**Images analyzed:** {len(results)}  \n"
        f"**Face status:** {face_status}  \n"
        f"**Brightness variation:** {brightness:.1f}  \n"
        f"**Image quality:** {quality}/100"
    )

    quality_chart = create_themed_chart(
        names,
        quality_values,
        metric="quality"
    )

    average_chart = create_themed_chart(
        names,
        brightness_values,
        metric="average"
    )

    report = "\n".join(
        [
            f"{name}: quality={q}/100, brightness variation={b:.1f}"
            for name, q, b in zip(
                names,
                quality_values,
                brightness_values
            )
        ]
    )

    return (
        prepare_preview_image(first_image),
        f"Quality: {quality}/100",
        f"Brightness: {brightness:.1f}",
        f"Faces: {'Detected' if landmarks is not None else 'Not detected'}",
        f"{len(results)} image(s)",
        summary,
        average_chart,
        quality_chart,
        report
    )


def load_uploaded_image(file):

    image = cv2.imread(file)

    if image is None:
        raise ValueError(
            f"Could not read image: {file}"
        )

    return image


# ============================================================
# APP
# ============================================================

with gr.Blocks(
    title="Under-Eye AI",
    theme=final_theme,
    css=final_css
) as app:

    gr.Markdown(
        """
        # 👁️ Under-Eye AI

        ### Intelligent Under-Eye Visual Analysis

        **Computer Vision · Facial Landmarks · Image Quality**
        """
    )

    gr.Markdown(
        """
        Upload face images to explore experimental
        under-eye visual patterns.
        """
    )

    image_files = gr.File(
        label="📷 Upload Face Images",
        file_count="multiple",
        file_types=["image"]
    )

    analyze_button = gr.Button(
        "✨ Analyze Images",
        variant="primary"
    )

    gr.Markdown(
        "## 👁️ AI Analysis Preview"
    )

    preview_image = gr.Image(
        label="Detected Analysis Region",
        type="numpy"
    )

    gr.Markdown(
        "## 📊 Key Results"
    )

    with gr.Row():

        left_card = gr.Textbox(
            label="LEFT EYE",
            value="—",
            interactive=False
        )

        right_card = gr.Textbox(
            label="RIGHT EYE",
            value="—",
            interactive=False
        )

        overall_card = gr.Textbox(
            label="OVERALL",
            value="—",
            interactive=False
        )

        quality_card = gr.Textbox(
            label="IMAGE QUALITY",
            value="—",
            interactive=False
        )

    gr.Markdown(
        "## 🏆 Analysis Overview"
    )

    overall_summary = gr.Markdown(
        "Upload images and click **Analyze Images**."
    )

    gr.Markdown(
        "## 📈 Visual Comparison"
    )

    with gr.Row():

        average_chart = gr.Plot(
            label="Under-Eye Visual Difference"
        )

        quality_chart = gr.Plot(
            label="Image Quality"
        )

    with gr.Accordion(
        "🔎 Detailed Technical Analysis",
        open=False
    ):

        detailed_report = gr.Textbox(
            label="Technical Report",
            lines=30,
            interactive=False
        )
    
    analyze_button.click(
        fn=analyze_images,
        inputs=image_files,
        outputs=[
            preview_image,
            left_card,
            right_card,
            overall_card,
            quality_card,
            overall_summary,
            average_chart,
            quality_chart,
            detailed_report
        ]
    )

    gr.Markdown(
        """
        ---

        ## ⚙️ Analysis Pipeline

        **Face Detection**
        → **Facial Landmarks**
        → **Under-Eye ROI**
        → **Skin Comparison**
        → **Brightness Analysis**
        → **Image Quality**
        → **Multi-Image Comparison**

        ---

        ⚠️ **Experimental Computer-Vision Prototype**

        Results may be influenced by lighting, shadows,
        camera angle, facial expression and image quality.

        **This tool is not a medical diagnosis.**
        """
    )


if __name__ == "__main__":
    app.launch()
