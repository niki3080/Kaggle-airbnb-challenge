from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def add_watermark(
    fig=None,
    logo_path="utils/logo.png",
    title="MTS Teta 2026",
    subtitle="Airbnb Occupancy Prediction Challenge",
    zoom=0.05,
    alpha=0.4,
    accent_color="#FF6A6A",
    subtitle_color="#949494",
):
    if fig is None:
        fig = plt.gcf()

    fig_w_px = fig.get_figwidth() * fig.dpi
    fig_h_px = fig.get_figheight() * fig.dpi

    logo = mpimg.imread(logo_path)
    imagebox = OffsetImage(logo, zoom=zoom, alpha=alpha)

    ab = AnnotationBbox(
        imagebox,
        (8 / fig_w_px, 1 - 8 / fig_h_px),
        xycoords=fig.transFigure,
        frameon=False,
        box_alignment=(0, 1),
        pad=0,
    )

    fig.add_artist(ab)

    fig.text(
        50 / fig_w_px,
        1 - 10 / fig_h_px,
        title,
        ha="left",
        va="top",
        fontsize=12,
        fontweight="bold",
        color=accent_color,
        alpha=0.8,
    )

    fig.text(
        50 / fig_w_px,
        1 - 30 / fig_h_px,
        subtitle,
        ha="left",
        va="top",
        fontsize=8,
        color=subtitle_color,
        alpha=0.65,
    )
