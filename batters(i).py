import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
file_path = "Batting_ODI.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Convert columns to numeric
cols_to_numeric = ['Runs', 'Ave', 'SR', '100', '50']
for col in cols_to_numeric:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values
df = df.dropna(subset=cols_to_numeric)

# Select top 15 players
top_batsmen = df.sort_values(by=['Runs', 'Ave', 'SR', '100'], ascending=False).head(15).copy()
top_batsmen = top_batsmen.reset_index(drop=True)
players = top_batsmen['Player']

# Plot 1: Bar chart for Runs
fig1 = px.bar(top_batsmen, x='Player', y='Runs', title='Total Runs by Top 15 Batsmen',
              color_discrete_sequence=['skyblue'])
fig1.update_layout(xaxis_tickangle=-45)

# Plot 2: Line chart for Strike Rate and Average
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=players, y=top_batsmen['SR'], mode='lines+markers',
                          name='Strike Rate', marker=dict(symbol='circle', color='orange')))
fig2.add_trace(go.Scatter(x=players, y=top_batsmen['Ave'], mode='lines+markers',
                          name='Batting Average', marker=dict(symbol='square', color='green')))
fig2.update_layout(title='Strike Rate and Batting Average',
                   xaxis_title='Player', yaxis_title='Value',
                   xaxis_tickangle=-45)

# Plot 3: Line chart for 50s and 100s
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=players, y=top_batsmen['50'], mode='lines+markers',
                          name='50s', marker=dict(symbol='circle', color='teal')))
fig3.add_trace(go.Scatter(x=players, y=top_batsmen['100'], mode='lines+markers',
                          name='100s', marker=dict(symbol='square', color='purple')))
fig3.update_layout(title='Number of 50s and 100s',
                   xaxis_title='Player', yaxis_title='Count',
                   xaxis_tickangle=-45)

# Show the plots
fig3.show()
fig2.show()
fig1.show()

