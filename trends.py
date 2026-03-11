import pandas as pd
import plotly.graph_objects as go
import numpy as np

data = {
    "date": [
        "2020-01-01","2020-04-01","2020-07-01","2020-10-01",
        "2021-01-01","2021-04-01","2021-07-01","2021-10-01",
        "2022-01-01","2022-04-01","2022-07-01","2022-10-01",
        "2023-01-01","2023-04-01","2023-07-01","2023-10-01",
        "2024-01-01","2024-04-01","2024-07-01","2024-10-01",
    ],
    "interest": [
        5, 5, 6, 7,
        8, 10, 15, 20,
        30, 55, 85, 95,
        100, 90, 75, 60,
        45, 35, 25, 20,
    ]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

# Find peak
peak_idx = df["interest"].idxmax()
peak_date = df.loc[peak_idx, "date"]
peak_value = df.loc[peak_idx, "interest"]

# Get last 3 data points to determine current trajectory
recent = df["interest"].tail(3).values
current_value = recent[-1]

# Classify lifecycle stage
if current_value < 20:
    stage = "💀 Dead"
    color = "#999999"
elif recent[-1] < recent[-2] and recent[-2] < recent[-3]:
    stage = "📉 Declining"
    color = "#E8A0B4"
elif recent[-1] > recent[-2] and recent[-2] > recent[-3]:
    stage = "🚀 Emerging"
    color = "#A8D8A8"
elif current_value >= peak_value * 0.85:
    stage = "👑 Peaking"
    color = "#FFD700"
else:
    stage = "📉 Post-Peak"
    color = "#FFB347"

print(f"\n--- Trend Analysis: Clean Girl Aesthetic ---")
print(f"Peak date:      {peak_date.strftime('%B %Y')}")
print(f"Peak interest:  {peak_value}/100")
print(f"Current stage:  {stage}")
print(f"--------------------------------------------\n")

# Plot
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["date"],
    y=df["interest"],
    mode="lines+markers",
    name="clean girl aesthetic",
    line=dict(color="#E8A0B4", width=3)
))

# Mark the peak
fig.add_annotation(
    x=peak_date,
    y=peak_value,
    text=f"Peak: {peak_date.strftime('%b %Y')}",
    showarrow=True,
    arrowhead=2,
    arrowcolor="#A0506A",
    font=dict(color="#A0506A", size=12)
)

fig.update_layout(
    title=f'Trend Lifecycle: "Clean Girl Aesthetic" — Current Stage: {stage}',
    xaxis_title="Date",
    yaxis_title="Search Interest (0-100)",
    template="plotly_white"
)
fig.show()
