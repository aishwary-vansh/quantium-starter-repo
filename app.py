import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_data.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Group by date (total sales per day)
df_grouped = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Sales of Pink Morsels Over Time",
    labels={"date": "Date", "sales": "Total Sales"}
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),  # ✅ Header
    dcc.Graph(figure=fig)                   # ✅ Line chart
])

# Run server
if __name__ == "__main__":
    app.run(debug=True)