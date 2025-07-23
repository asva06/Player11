import pandas as pd
import plotly.express as px

# Load and clean data
df = pd.read_csv("Bowling_ODI.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
numeric_cols = ['Mat', 'Inns', 'Balls', 'Runs', 'Wkts', 'Ave', 'Econ', 'SR', '4', '5']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna(subset=['Wkts', 'Ave', 'Econ', 'SR'])

# Compute Bowling Score
df['BowlingScore'] = df['Wkts'] * 1.5 - df['Ave'] * 0.5 - df['Econ'] * 1.0 - df['SR'] * 0.3

# Get Top 15 Bowlers
top_15 = df.sort_values(by='BowlingScore', ascending=False).head(15)

# -------- PLOT 1: Bowling Score --------
fig1 = px.bar(
    top_15,
    x='Player',
    y='BowlingScore',
    title='Overall Performance: Bowling Score of Top 15 ODI Bowlers',
    color='BowlingScore',
    color_continuous_scale='Viridis',
    hover_data=['Wkts', 'Ave', 'Econ', 'SR']
)
fig1.update_layout(xaxis_tickangle=-45)


# -------- PLOT 2: Bowling Average & Strike Rate (Line Graph) --------
fig2 = px.line(
    top_15,
    x='Player',
    y=['Ave', 'SR'],
    title='Efficiency Detail: Bowling Average vs Strike Rate',
    markers=True
)
fig2.update_layout(xaxis_tickangle=-45, yaxis_title="Metric Value")


# -------- PLOT 3: Economy Rate --------
fig3 = px.bar(
    top_15,
    x='Player',
    y='Econ',
    title='Control: Economy Rate of Top 15 ODI Bowlers',
    color='Econ',
    color_continuous_scale='Cividis',
    hover_data=['Wkts', 'Ave', 'SR']
)
fig3.update_layout(xaxis_tickangle=-45)

fig3.show()
fig2.show()
fig1.show()
