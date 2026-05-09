import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.colors as mcolors
# THEME CHUNG
def set_theme():
    pio.templates.default = "plotly_white"
# MÀU GỐC
COLOR_FEMALE = "#FF1493"
COLOR_MALE   = "#48CAE4"
# PALETTE
FEMALE_PALETTE = ["#FFB3DA", "#FF66B2", "#FF70AD", "#FF1493"]
MALE_PALETTE   = ["#CAF0F8", "#90E0EF", "#48CAE4", "#0077B6"]
# FONT
TITLE_STYLE = dict(
    size=20,
    family="Arial",
    color="black"
)
LABEL_STYLE = dict(
    size=14,
    family="Arial",
    color="#d81b60"
)
# FIGURE SIZE
FIG_WIDTH = 700
FIG_HEIGHT = 500
# APPLY STYLE
def apply_style(fig, title, xlabel, ylabel):
    fig.update_layout(
        title=dict(
            text=title,
            font=TITLE_STYLE,
            x=0.5,
        ),
        xaxis=dict(
            title=dict(
              text=xlabel,
              font=LABEL_STYLE
            ),
            tickfont=dict(size=12),
            showgrid=False
        ),
        yaxis=dict(
            title=dict(
              text=ylabel,
              font=LABEL_STYLE,
            ),
            tickfont=dict(size=12),
            showgrid=False
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        width=FIG_WIDTH,
        height=FIG_HEIGHT,
        font=dict(
            family="Arial",
            color="black"
        ),
        margin=dict(
            l=40,
            r=40,
            t=80,
            b=60
        )
    )
    return fig
def get_text_color(hex_color):

    r, g, b = mcolors.to_rgb(hex_color)

    brightness = (
        0.299 * r +
        0.587 * g +
        0.114 * b
    )

    return (
        "#c71585"
        if brightness > 0.6
        else "#fffaf0"
    )