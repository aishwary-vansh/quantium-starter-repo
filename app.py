import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_data.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1(
        "Pink Morsel Sales Dashboard",
        style={"textAlign": "center", "color": "#2c3e50"}
    ),

    # Radio buttons
    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    # Graph
    dcc.Graph(id="sales-chart")

],
style={
    "backgroundColor": "#f4f6f7",
    "padding": "20px"
})

# Callback (dynamic filtering)
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    # Group data
    grouped = filtered_df.groupby("date")["sales"].sum().reset_index()

    # Create chart
    fig = px.line(
        grouped,
        x="date",
        y="sales",
        title=f"Sales Trend ({selected_region.upper()})",
        labels={"date": "Date", "sales": "Total Sales"}
    )

    # Optional: price change marker
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)