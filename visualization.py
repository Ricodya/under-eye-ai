
import matplotlib.pyplot as plt
import os


# ============================================================
# THEMED COMPARISON CHART
# ============================================================

def create_themed_chart(
    names,
    values,
    metric="average"
):

    if not names or not values:
        return None

    purple = "#7C3AED"

    fig = plt.figure(
        figsize=(9, 5)
    )

    bars = plt.bar(
        names,
        values,
        color=purple
    )

    if metric == "average":

        plt.title(
            "Average Under-Eye Visual Difference",
            fontsize=14,
            fontweight="bold"
        )

        plt.ylabel(
            "Relative Difference (%)"
        )

    else:

        plt.title(
            "Image Quality Comparison",
            fontsize=14,
            fontweight="bold"
        )

        plt.ylabel(
            "Quality Score / 100"
        )

        plt.ylim(
            0,
            100
        )

    plt.xlabel(
        "Image"
    )

    for bar, value in zip(
        bars,
        values
    ):

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:.1f}",
            ha="center",
            va="bottom",
            fontweight="bold"
        )

    plt.xticks(
        rotation=20,
        ha="right"
    )

    plt.grid(
        axis="y",
        alpha=0.2
    )

    plt.tight_layout()

    return fig


# ============================================================
# PREVIEW
# ============================================================

def prepare_preview_image(
    image
):

    if image is None:
        return None

    return image
