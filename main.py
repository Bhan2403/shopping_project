from style import (
    set_theme,
    apply_style,
    FEMALE_PALETTE,
    MALE_PALETTE,
    COLOR_MALE,
    COLOR_FEMALE,
    get_text_color 
)
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.colors as mcolors
import pandas as pd
import numpy as np
# LOAD DATA
df = pd.read_csv("shopping_behavior_updated.csv")
set_theme()
# =========================
# ==========PLOT 1=========
def plot_review_by_gender(df):
    fig = px.violin(
        df,
        x="Gender",
        y="Review Rating",
        color="Gender",
        box=True,
        color_discrete_map={
            "Male": COLOR_MALE,
            "Female": "#FF66B2"
        }
    )
    fig.update_yaxes(range=[2, 5])
    fig = apply_style(
        fig,
        "",
        "GENDER",
        "RATING"
    )
    fig.update_layout(
    showlegend=False
    )
    return fig
# =========PLOT 2==========
def plot_size_by_gender(df):
    size_gender = (
        df.groupby(["Size", "Gender"])
        .size()
        .reset_index(name="n")
    )
    pivot_table = size_gender.pivot(
        index="Gender",
        columns="Size",
        values="n"
    ).fillna(0)
    fig = px.imshow(
        pivot_table,
        text_auto=False,
        color_continuous_scale=FEMALE_PALETTE,
        aspect="auto"
    )
    custom_text_colors = []
    for row in pivot_table.values:
        color_row = []
        row_min = np.min(row)
        row_max = np.max(row)
        for value in row:
            normalized = (
                (value - row_min) /
                (row_max - row_min + 1e-9)
            )
            fake_color = (
                "#c71585"
                if normalized > 0.4
                else "#ffc0cb"
            )
            color_row.append(
                get_text_color(fake_color)
            )
        custom_text_colors.append(color_row)

    for i, gender in enumerate(pivot_table.index):
        for j, size in enumerate(pivot_table.columns):
            fig.add_annotation(
                x=size,
                y=gender,
                text=f"<b>{int(pivot_table.iloc[i, j])}</b>",
                showarrow=False,
                font=dict(
                    color=custom_text_colors[i][j],
                    size=14,
                    family="Arial Black"
                )
            )
    fig.update_layout(
        coloraxis_colorbar=dict(
            title=""
        )
    )
    fig = apply_style(
        fig,
        "",
        "CLOTHING SIZE",
        "GENDER"
    )
    return fig
# =========PLOT 3=========
def plot_payment_methods(df):
    payment_data = (
        df['Payment Method']
        .value_counts()
        .sort_values()
        .reset_index()
    )
    payment_data.columns = [
        'Method',
        'Count'
    ]
    n_methods = len(payment_data)
    colors = [
        f"rgb({r},{g},{b})"
        for r, g, b in zip(
            np.linspace(72, 255, n_methods),
            np.linspace(202, 20, n_methods),
            np.linspace(228, 147, n_methods)
        )
    ]
    fig = go.Figure()
    for i, row in payment_data.iterrows():
        # line
        fig.add_trace(go.Scatter(
            x=[0, row["Count"]],
            y=[row["Method"], row["Method"]],
            mode="lines",
            line=dict(
                color=colors[i],
                width=3
            ),
            hoverinfo='skip',
            showlegend=False
        ))
        # dot
        fig.add_trace(go.Scatter(
            x=[row["Count"]],
            y=[row["Method"]],
            mode="markers",
            marker=dict(
                size=12,
                color=colors[i]
            ),
            hovertemplate=
            "<b>%{y}</b><br>" +
            "Transactions: %{x}<extra></extra>",
            showlegend=False
        ))
        # number label
        fig.add_annotation(
            x=row["Count"],
            y=row["Method"],
            text=f"<b>{row['Count']}</b>",
            showarrow=False,
            xshift=22,
            font=dict(
                size=12,
                color="#c71585",
                family="Arial Black"
            )
        )
    fig.update_xaxes(
        range=[
            0,
            payment_data['Count'].max() * 1.08
        ],
        showgrid=False
    )
    # STYLE
    fig = apply_style(
        fig,
        "",
        "NUMBER OF TRANSACTIONS",
        "PAYMENT METHOD"
    )
    return fig
# =========PLOT 4==========
def get_category_text_color(hex_color):
    r, g, b = mcolors.to_rgb(hex_color)
    brightness = (
        0.299 * r +
        0.587 * g +
        0.114 * b
    )
    is_pink = r > b
    if is_pink:
        return (
            "#c71585"
        )
    else:
        return (
            "#1e90ff"
            if brightness > 0.7
            else "#e0ffff"
        )
def plot_categories_by_gender(df):
    df_counts = (
        df.groupby(['Gender', 'Category'])
        .size()
        .reset_index(name='Count')
    )
    fig = go.Figure()
    # FEMALE COLUMN
    female_data = df_counts[
        df_counts["Gender"] == "Female"
    ]
    for i, row in female_data.iterrows():
        color = FEMALE_PALETTE[
            i % len(FEMALE_PALETTE)
        ]
        fig.add_trace(go.Bar(
            x=["Female"],
            y=[row["Count"]],
            name=row["Category"],
            marker=dict(
                color=color
            ),
            text=[row["Count"]],
            textposition=(
                "outside"
                if row["Count"] < 120
                else "inside"
            ),
            insidetextanchor="middle",
            textfont=dict(
                color=get_category_text_color(color),
                size=12.5,
                family="Arial Black"
            ),
            cliponaxis=False
        ))
    # MALE COLUMN
    male_data = df_counts[
        df_counts["Gender"] == "Male"
    ]
    for i, row in male_data.iterrows():
        color = MALE_PALETTE[
            i % len(MALE_PALETTE)
        ]
        fig.add_trace(go.Bar(
            x=["Male"],
            y=[row["Count"]],
            name=row["Category"],
            marker=dict(
                color=color
            ),
            text=[row["Count"]],
            textposition="inside",
            insidetextanchor="middle",
            textfont=dict(
                color=get_category_text_color(color),
                size=12.5,
                family="Arial Black"
            ),
            showlegend=True
        ))
    # LAYOUT
    fig.update_layout(
        barmode='stack',
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )
    fig = apply_style(
        fig,
        "",
        "GENDER",
        "NUMBER OF CUSTOMERS"
    )
    return fig
# =========PLOT 5==========
def plot_stacked_area(df):
    data = df.copy()
    bins = [0, 25, 50, 75, 100]
    labels = [
        "Low",
        "Lower-mid",
        "Mid",
        "High"
    ]
    data["amount_group"] = pd.cut(
        data["Purchase Amount (USD)"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )
    # GROUP DATA
    df_group = (
        data.groupby(
            ["amount_group", "Frequency of Purchases"]
        )
        .size()
        .reset_index(name="n")
    )
    # PIVOT TABLE
    pivot_df = df_group.pivot(
        index="amount_group",
        columns="Frequency of Purchases",
        values="n"
    ).fillna(0)

    frequency_colors = {
    "Annually":"#FFE5F1",
    "Bi-Weekly":"#FFD6E8",
    "Every 3 Months":"#FFBFD9",
    "Fortnightly":"#FF99C8",
    "Monthly":"#FF73B7",
    "Quarterly":"#FF4DA6",
    "Weekly":"#FF1493"
    }
    # FIGURE
    fig = go.Figure()
    for i, col in enumerate(pivot_df.columns):
        fig.add_trace(go.Scatter(
            x=pivot_df.index,
            y=pivot_df[col],
            mode='lines',
            stackgroup='one',
            name=col,
            line=dict(
                width=1,
                color=frequency_colors[str(col).strip()]
            ),
            fillcolor=frequency_colors[str(col).strip()],
            hovertemplate=
            "<b>%{fullData.name}</b><br>" +
            "Purchase Range: %{x}<br>" +
            "Customers: %{y}<extra></extra>"
        ))
    # LAYOUT
    fig.update_layout(
        hovermode="x unified",
        legend=dict(
            title="Frequency",
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.02
        ),
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )
    # STYLE
    fig = apply_style(
        fig,
        "",
        "PURCHASE AMOUNT RANGE",
        "NUMBER OF CUSTOMERS"
    )
    return fig
# =========PLOT 6==========
def plot_shipping_pie(df, selected_shipping=None):
    summary_data = (
        df['Shipping Type']
        .value_counts()
        .reset_index()
    )
    summary_data.columns = [
        'Shipping Type',
        'n'
    ]
    base_colors = {
        "Express": "#FF1493",
        "Free Shipping": "#FF73B7",
        "Standard": "#FF99C8",
        "Store Pickup": "#FFBFD9",
        "Next Day Air": "#FFD6E8",
        "2-Day Shipping": "#FFE5F1"
    }
    colors = []
    for label in summary_data["Shipping Type"]:
        colors.append(
            base_colors[label]
        )
    colors = []
    for label in summary_data["Shipping Type"]:
      if (
        selected_shipping is None
        or selected_shipping == "Select All"
      ):
        colors.append(
            base_colors[label]
        )
      elif label == selected_shipping:
        colors.append(
            base_colors[label]
        )
      else:
        colors.append(
            "#f0ffff"
        )
    # PIE CHART
    fig = go.Figure(
        data=[
            go.Pie(
                labels=summary_data['Shipping Type'],
                values=summary_data['n'],
                marker=dict(
                    colors=colors
                ),
                textinfo='percent',
                textposition='inside',
                insidetextfont=dict(
                    size=13,
                    color="black",
                    family="Arial Black"
                ),
                hovertemplate=
                "<b>%{label}</b><br>" +
                "Customers: %{value}<br>" +
                "Percentage: %{percent}<extra></extra>"
            )
        ]
    )
    # LAYOUT
    fig.update_layout(
        showlegend=True,
        legend=dict(
            title="Shipping Type",
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.02
        ),
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )
    # STYLE
    fig = apply_style(
        fig,
        "",
        "",
        ""
    )
    return fig
#==========PLOT 7==========
def plot_purchase_boxplot(df):
    df['Purchase Amount (USD)'] = pd.to_numeric(
        df['Purchase Amount (USD)'],
        errors='coerce'
    )
    fig = px.box(
        df,
        x="Season",
        y="Purchase Amount (USD)",
        color="Season",
        color_discrete_sequence=[
            '#FFB3DA',
            '#FF66B2',
            '#FF70AD',
            '#FF1493'
        ]
    )
    fig = apply_style(
        fig,
        "",
        "SEASON",
        "PURCHASE AMOUNT (USD)"
    )
    fig.update_layout(
        showlegend=False
    )
    return fig
