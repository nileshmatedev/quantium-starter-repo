import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Load and prepare data
DATA_PATH = os.path.join(os.path.dirname(__file__), "pink_morsels_sales.csv")
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

REGION_OPTIONS = [
    {"label": "All Regions", "value": "all"},
    {"label": "North", "value": "north"},
    {"label": "East", "value": "east"},
    {"label": "South", "value": "south"},
    {"label": "West", "value": "west"},
]

app = dash.Dash(__name__)
app.title = "Pink Morsels Sales"

# Style dictionaries to keep things tidy
PAGE_STYLE = {
    "minHeight": "100vh",
    "padding": "40px 30px 60px",
    "background": "linear-gradient(135deg, #fef3f8 0%, #ffe1f0 50%, #f7f9ff 100%)",
    "fontFamily": "'Poppins', 'Segoe UI', system-ui, sans-serif",
    "color": "#222",
}
CARD_STYLE = {
    "maxWidth": "1200px",
    "margin": "0 auto",
    "background": "#fff",
    "borderRadius": "18px",
    "boxShadow": "0 20px 45px rgba(0,0,0,0.08)",
    "padding": "26px 30px 30px",
    "border": "1px solid #f1d0e4",
}
HEADER_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "gap": "6px",
    "textAlign": "center",
    "marginBottom": "20px",
}
TITLE_STYLE = {
    "fontSize": "36px",
    "fontWeight": 700,
    "color": "#d6006a",
    "letterSpacing": "0.5px",
    "textTransform": "uppercase",
}
SUBTITLE_STYLE = {
    "fontSize": "16px",
    "color": "#4f4f4f",
}
RADIO_WRAPPER_STYLE = {
    "display": "flex",
    "justifyContent": "center",
    "gap": "14px",
    "flexWrap": "wrap",
    "margin": "24px 0 10px",
}
RADIO_STYLE = {
    "background": "#fff4fb",
    "border": "1px solid #f3b4d7",
    "borderRadius": "14px",
    "padding": "10px 14px",
    "cursor": "pointer",
    "boxShadow": "0 8px 18px rgba(214, 0, 106, 0.08)",
}
GRAPH_STYLE = {
    "padding": "8px",
    "borderRadius": "14px",
    "background": "linear-gradient(180deg, #ffffff 0%, #f9f5ff 100%)",
}

app.layout = html.Div(
    style=PAGE_STYLE,
    children=[
        html.Div(
            style=CARD_STYLE,
            children=[
                html.Div(
                    style=HEADER_STYLE,
                    children=[
                        html.Div("Pink Morsels Sales Visualizer", style=TITLE_STYLE),
                        html.Div(
                            "Explore daily sales by region and see the impact of the Jan 15, 2021 price change.",
                            style=SUBTITLE_STYLE,
                        ),
                    ],
                ),
                html.Div(
                    style=RADIO_WRAPPER_STYLE,
                    children=[
                        dcc.RadioItems(
                            id="region-filter",
                            options=REGION_OPTIONS,
                            value="all",
                            labelStyle=RADIO_STYLE,
                            inputStyle={"marginRight": "6px"},
                            style={"display": "flex", "gap": "12px", "flexWrap": "wrap"},
                        )
                    ],
                ),
                html.Div(
                    style=GRAPH_STYLE,
                    children=[
                        dcc.Graph(id="sales-chart", config={"displayModeBar": False}),
                    ],
                ),
            ],
        )
    ],
)

@app.callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_chart(region_value: str) -> go.Figure:
    # Filter data by region if needed
    filtered_df = df if region_value == "all" else df[df["Region"].str.lower() == region_value]
    grouped = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    line = go.Scatter(
        x=grouped["Date"],
        y=grouped["Sales"],
        mode="lines+markers",
        name="Sales",
        line=dict(color="#d6006a", width=3),
        marker=dict(size=6, color="#7a1ea1", line=dict(width=1, color="#f6e8ff")),
        hovertemplate="%{x|%b %d, %Y}<br>$%{y:,.0f}<extra></extra>",
    )

    price_change = dict(
        type="line",
        x0="2021-01-15",
        x1="2021-01-15",
        y0=0,
        y1=1,
        yref="paper",
        line=dict(color="#ff5c5c", width=2, dash="dash"),
    )

    annotation = dict(
        x="2021-01-15",
        y=1.02,
        xref="x",
        yref="paper",
        text="Price increase",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#ff5c5c",
        ax=0,
        ay=-28,
        font=dict(color="#ff5c5c", size=12),
    )

    layout = go.Layout(
        title=dict(text="Daily Sales Over Time", x=0.03, font=dict(size=22, color="#1f1f1f")),
        xaxis=dict(title="Date", gridcolor="rgba(0,0,0,0.08)", zeroline=False),
        yaxis=dict(title="Sales ($)", gridcolor="rgba(0,0,0,0.08)", zeroline=False),
        plot_bgcolor="#ffffff",
        paper_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        margin=dict(l=50, r=30, t=70, b=60),
        height=600,
        shapes=[price_change],
        annotations=[annotation],
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )

    fig = go.Figure(data=[line], layout=layout)
    return fig


if __name__ == "__main__":
    app.run(debug=True, port=8050)
