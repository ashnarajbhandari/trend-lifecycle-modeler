# Trend Lifecycle Modeler

> A data dashboard that tracks how beauty and lifestyle aesthetics are born, peak, and die — using real Google Trends data from 2020 to 2026.

**[View Live Dashboard →](https://trend-lifecycle-modeler.streamlit.app/)**

---

## What It Does

The Trend Lifecycle Modeler analyzes 20 beauty and lifestyle trends and maps their full cultural arc — from emergence to peak to decline. Each trend is classified into a lifecycle stage, paired with a predicted decline date, cultural context, and DNA tags that reveal the patterns behind why trends rise and fall.

**Features:**
- Lifecycle curve visualization for 20 trends using real Google Trends data
- Automatic stage classification: Emerging, Peaking, Post-Peak, Declining, or Dead
- Predicted decline dates based on current rate of change
- Cultural descriptions and "what killed this trend" analysis for each aesthetic
- DNA tagging system — filter trends by origin type (TikTok-born, celebrity-driven, nostalgia, etc.)
- Side-by-side trend comparison (up to 4 trends)
- Rising Now and Peaking Now sections updated from live data

---

## Methodology

**Lifecycle Staging** — Each trend is classified based on the trajectory of its last three data points relative to its all-time peak. A trend is considered Dead when its interest score falls below 15/100.

**Decline Prediction** — Predicted decline dates use linear extrapolation of the current rate of decline. The model calculates how many periods remain until interest falls below 15, then converts that to a calendar date. Intentionally transparent rather than a black-box forecast.

**Data** — Interest scores are sourced from Google Trends (trends.google.com), indexed 0–100 where 100 = peak search interest. Data spans January 2020 to March 2026 at monthly intervals. DNA tags are assigned editorially based on each trend's origin story, cultural drivers, and lifecycle pattern.

---

## Built With

- Python
- Pandas
- Plotly
- Streamlit

---

*Built by [Ashna Rajbhandari](https://github.com/ashnarajbhandari)*
