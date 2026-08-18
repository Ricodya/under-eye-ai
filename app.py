
import gradio as gr

from analysis import detect_face_landmarks
from visualization import create_themed_chart
from quality import basic_quality_score


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
