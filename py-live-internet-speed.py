import plotly.graph_objects as go
import speedtest

s = speedtest.Speedtest()
speed = round(s.download() / 1e6, 2)

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=speed,
        title={"text": "Download Speed (Mbps)"},
        gauge={"axis": {"range": [0, 300]}},
    )
)
fig.show()
