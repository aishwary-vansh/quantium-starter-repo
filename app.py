import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("processed_data.csv")

df["date"] = pd.to_datetime(df["date"])

df_grouped = df.groupby("date")["sales"].sum().reset_index()

fig = px.line(df_grouped, x="date", y="sales", title="Pink Morsel Sales Over Time")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Analysis Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")