import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import os

FILES = {
    "Clean Girl Aesthetic": "clean_girl.csv",
    "Mob Wife Aesthetic": "mob_wife.csv",
    "Quiet Luxury": "quiet_luxury.csv",
    "Glazed Donut Nails": "glazed_donut_nails.csv",
    "Coastal Grandmother": "coastal_grandmother.csv",
    "Indie Sleaze": "indie_sleaze.csv",
    "Cottagecore": "cottagecore.csv",
    "Dark Academia": "dark_academia.csv",
    "E-Girl Aesthetic": "e_girl.csv",
    "Y2K": "y2k.csv",
    "Balletcore": "balletcore.csv",
    "VSCO Girl": "vsco_girl.csv",
    "Coquette Aesthetic": "coquette.csv",
    "Rockstar Girlfriend": "rockstar_girlfriend.csv",
    "Opium Aesthetic": "opium_aesthetic.csv",
    "Pilates Princess": "pilates_princess.csv",
    "Office Siren": "office_siren.csv",
    "Latte Makeup": "latte_makeup.csv",
    "Soap Brows": "soap_brows.csv",
}

# Eurotrash stays as fake data since it had no Google Trends data
EUROTRASH_FAKE = [0,0,0,0,0,0,0,0,0,0,2,3,5,8,12,20,35,55,75,88,95,100,100,98,95,90,85,80,75,70,65,60,55,50,45,40,35,30,25,20,18,16,14,12,10,8,6,5,4,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

def load_trend(file):
    df = pd.read_csv(file, skiprows=1, names=["date", "interest"])
    df["date"] = pd.to_datetime(df["date"])
    df["interest"] = pd.to_numeric(df["interest"], errors="coerce").fillna(0)
    return df

# Load all trends
TREND_DFS = {}
for name, file in FILES.items():
    if os.path.exists(file):
        TREND_DFS[name] = load_trend(file)

# Add eurotrash with matching date range
sample_df = list(TREND_DFS.values())[0]
dates = sample_df["date"].values
eurotrash_values = EUROTRASH_FAKE[:len(dates)]
while len(eurotrash_values) < len(dates):
    eurotrash_values.append(eurotrash_values[-1])
TREND_DFS["Eurotrash Chic"] = pd.DataFrame({"date": dates, "interest": eurotrash_values[:len(dates)]})

DESCRIPTIONS = {
    "Clean Girl Aesthetic": "Slicked buns, glazed skin, gold hoops. Born on TikTok around 2022 as a reaction to heavy glam — the fantasy of looking effortlessly put-together. Peaked hard in early 2023, now fading as audiences crave more edge and personality.",
    "Mob Wife Aesthetic": "Fur coats, bold jewelry, unapologetic maximalism. A direct counter-reaction to clean girl minimalism that exploded in late 2023. Peaked fast and burned out faster — classic viral trend lifecycle.",
    "Quiet Luxury": "No logos, no noise. Inspired by Succession and old-money dressing, this aesthetic rewarded restraint and quality over flash. Peaked mid-2023 and has been slowly settling into mainstream fashion DNA.",
    "Glazed Donut Nails": "Hailey Bieber's chrome nails broke the internet in 2022. One of the clearest single-celebrity trend launches ever recorded — peaked within months and became the nail look of that era.",
    "Coastal Grandmother": "Coined by TikToker Lex Nicoleta in 2022 — linen, Nancy Meyers films, farmers markets. A comfort aesthetic that peaked quickly but left a lasting impression on how people think about relaxed dressing.",
    "Indie Sleaze": "The 2000s party girl revival — flash photography, low-rise jeans, smudged liner. Was dormant for a decade before TikTok nostalgia brought it roaring back. Currently at peak cultural saturation in 2025-2026.",
    "Cottagecore": "The pandemic's escape fantasy — flowy dresses, bread baking, foraging. Peaked in mid-2021 as lockdowns drove people to romanticize rural simplicity. Now largely dead but left a lasting mark on sustainable fashion.",
    "Dark Academia": "Tweed, libraries, dead poets. Peaked in 2021 alongside cottagecore as the darker, more intellectual pandemic aesthetic. Both served the same need — escape into a romanticized world.",
    "E-Girl Aesthetic": "Egirl makeup, chain necklaces, alt-TikTok energy. Peaked in 2021 as the platform's counterculture identity. Faded as TikTok itself went mainstream and the aesthetic lost its edge.",
    "Y2K": "Low-rise everything, butterfly clips, Von Dutch. Has been in a slow sustained revival since 2022 driven by Gen Z nostalgia for an era they barely lived through. Still holding strong in 2026.",
    "Balletcore": "Ribbons, leotards, soft tutus worn as streetwear. Peaked in 2023 alongside the cultural ballet renaissance — driven by The Idea of You, Margot Robbie, and a broader femininity reclamation.",
    "VSCO Girl": "Hydro Flasks, scrunchies, save the turtles. Peaked explosively in 2019-2020 and collapsed just as fast. One of the clearest examples of a meme-accelerated trend lifecycle.",
    "Coquette Aesthetic": "Bows, lace, Lana Del Rey, hyper-femininity. Grew steadily from 2021 and peaked in 2023 as part of the broader feminine aesthetic wave. Now declining but left a lasting influence on pink dressing.",
    "Rockstar Girlfriend": "Band tees, leather, messy hair — the girlfriend of someone in a band. Emerged as a 2024 aesthetic and peaked quickly, filling the void left by mob wife's decline.",
    "Opium Aesthetic": "Dark, androgynous, European. Inspired by Rick Owens and Phoebe Philo's Celine. Slower burn than most trends — has been building since 2023 and currently sits at post-peak with serious staying power.",
    "Pilates Princess": "Matching sets, water bottles, reformer classes. The wellness-meets-fashion aesthetic that is still peaking in 2026. Closely tied to the broader 'that girl' lifestyle trend.",
    "Office Siren": "Power dressing reimagined — blazers, pencil skirts, quiet confidence. Peaked in 2024-2025 as remote work fatigue drove a fantasy of looking powerful in-person again.",
    "Eurotrash Chic": "Vintage luxury, slightly tacky, fully intentional. Micro-trend with a dedicated following — currently at peak. Signals a post-irony approach to dressing where bad taste becomes high taste.",
    "Latte Makeup": "Browns, bronzes, warm neutrals — makeup that matches your coffee order. Peaked in 2024 as a warmer alternative to the cool-toned clean girl look. Still relevant but beginning to plateau.",
    "Soap Brows": "Brushed-up, fluffy, architectural brows using soap. Peaked in 2022 and has been slowly declining as laminated brows and more sculpted shapes take over. A true beauty technique trend.",
}

CAUSE_OF_DEATH = {
    "Clean Girl Aesthetic": "Oversaturation killed it. Once every brand, drugstore dupe, and influencer adopted the look, the aspirational quality evaporated. The aesthetic also became coded as performative wellness rather than genuine effortlessness.",
    "Mob Wife Aesthetic": "Burned too bright, too fast. Viral trends with extreme aesthetics have short lifecycles — the internet collectively moved on within a season. The look was too costumey to survive beyond the meme cycle.",
    "Quiet Luxury": "Didn't die so much as dissolve into mainstream fashion DNA. Once fast fashion replicated the look at scale, the exclusivity that made it desirable was gone. It's now background noise rather than a statement.",
    "Glazed Donut Nails": "Single-celebrity trends are fragile. Once Hailey Bieber moved on and the look was everywhere from drugstores to nail salons, the magic was gone. Chrome nails became the new french tip — ubiquitous and invisible.",
    "Coastal Grandmother": "Too niche to sustain mass momentum. It was always more of a mood board than a wearable aesthetic for most people. Once the initial TikTok cycle ended, there was no cultural engine to keep it alive.",
    "Indie Sleaze": "Still alive — currently peaking. Watch for oversaturation as the revival becomes mainstream. The moment it hits fast fashion en masse, the cool kids will move on.",
    "Cottagecore": "The pandemic ended. Cottagecore was always tied to lockdown psychology — when people could go outside again, the fantasy of rural escape lost its urgency. Real life replaced the escapism.",
    "Dark Academia": "Same pandemic logic as cottagecore — it was a fantasy for a locked-down generation. Also became oversaturated on TikTok to the point of self-parody, which is usually a death sentence for aesthetics.",
    "E-Girl Aesthetic": "Victim of its own success. When an aesthetic goes from counterculture to mainstream, it loses the identity function that made it appealing. E-girl became a costume rather than a subculture.",
    "Y2K": "Still surviving — sustained by slow nostalgia rather than viral momentum, which makes it more durable. Will likely fade gradually rather than crash.",
    "Balletcore": "Starting to show age. The ballet cultural moment has passed, and without fresh celebrity reinforcement the aesthetic is losing oxygen. Expect a full decline by 2027.",
    "VSCO Girl": "Killed by memes. Once a trend becomes joke material faster than it spreads as genuine style inspo, it's over. VSCO girl became a Halloween costume before it even peaked.",
    "Coquette Aesthetic": "Hyper-femininity fatigue. After years of bows and lace, audiences are swinging back toward harder aesthetics. Also became associated with a very specific and limiting online persona.",
    "Rockstar Girlfriend": "Transitioning to post-peak. The aesthetic served a specific cultural moment but is now being replaced by more extreme references like indie sleaze and grunge revival.",
    "Opium Aesthetic": "Not dead yet, but the niche that sustained it is expanding, which usually signals dilution. As more mainstream brands co-opt the dark European look, its edge will soften.",
    "Pilates Princess": "Still peaking — no cause of death yet. Vulnerability: if the wellness backlash narrative gains traction, this aesthetic could become culturally coded as toxic rather than aspirational.",
    "Office Siren": "Losing steam as return-to-office anxiety normalizes. Once dressing for work becomes mundane again rather than aspirational, the fantasy dissolves.",
    "Eurotrash Chic": "Still at peak. The risk is irony fatigue — aesthetics built on intentional bad taste have a short window before the joke stops being funny.",
    "Latte Makeup": "Plateauing as cooler, more editorial color palettes take over. Warm neutrals are becoming background noise rather than a deliberate aesthetic choice.",
    "Soap Brows": "Being replaced by laminated brow techniques that offer longer-lasting results. Soap brows require daily effort for an effect that brow lamination achieves semi-permanently.",
}

DNA_TAGS = {
    "Clean Girl Aesthetic": ["TikTok-born", "minimalist", "wellness-coded", "celebrity-driven", "mainstream"],
    "Mob Wife Aesthetic":   ["maximalist", "counter-reaction", "viral-flash", "TikTok-born", "fast-cycle"],
    "Quiet Luxury":         ["TV-driven", "minimalist", "aspirational", "old-money", "slow-burn"],
    "Glazed Donut Nails":   ["celebrity-driven", "single-origin", "beauty-technique", "fast-cycle"],
    "Coastal Grandmother":  ["niche", "mood-board", "comfort-coded", "TikTok-born"],
    "Indie Sleaze":         ["nostalgia", "revival", "subculture", "slow-burn", "currently-peaking"],
    "Cottagecore":          ["pandemic-born", "escapism", "sustainable", "mood-board", "dead"],
    "Dark Academia":        ["pandemic-born", "escapism", "literary", "subculture", "dead"],
    "E-Girl Aesthetic":     ["subculture", "TikTok-born", "alt", "fast-cycle", "dead"],
    "Y2K":                  ["nostalgia", "revival", "Gen-Z", "slow-burn", "durable"],
    "Balletcore":           ["TV-driven", "femininity", "aspirational", "slow-burn"],
    "VSCO Girl":            ["meme-killed", "fast-cycle", "mainstream", "dead"],
    "Coquette Aesthetic":   ["hyper-feminine", "TikTok-born", "slow-burn", "Lana-coded"],
    "Rockstar Girlfriend":  ["post-pandemic", "edgy", "fast-cycle", "TikTok-born"],
    "Opium Aesthetic":      ["designer-driven", "niche", "androgynous", "slow-burn", "European"],
    "Pilates Princess":     ["wellness-coded", "aspirational", "currently-peaking", "lifestyle"],
    "Office Siren":         ["post-pandemic", "power-dressing", "aspirational", "slow-burn"],
    "Eurotrash Chic":       ["irony-coded", "niche", "European", "currently-peaking"],
    "Latte Makeup":         ["beauty-technique", "warm-tones", "TikTok-born", "plateauing"],
    "Soap Brows":           ["beauty-technique", "slow-burn", "declining", "replaced"],
}

ALL_TAGS = sorted(set(tag for tags in DNA_TAGS.values() for tag in tags))
COLORS = ["#d4829a", "#86c5a0", "#d4af37", "#a0a0e0", "#c4956a"]

def get_stage(df, peak_value):
    recent = df["interest"].tail(3).values
    current = recent[-1]
    if current < 15:
        return "DEAD", "#666666"
    elif recent[-1] < recent[-2] < recent[-3]:
        return "DECLINING", "#c084a0"
    elif recent[-1] > recent[-2] > recent[-3]:
        return "EMERGING", "#86c5a0"
    elif current >= peak_value * 0.85:
        return "PEAKING", "#d4af37"
    else:
        return "POST-PEAK", "#c4956a"

def predict_decline(df):
    try:
        values = df["interest"].values
        current = values[-1]
        if current < 15:
            return "Already gone"
        recent = values[-4:]
        if recent[-1] >= recent[0]:
            return "Not declining yet"
        decline_per_period = (recent[0] - recent[-1]) / 3
        if decline_per_period <= 0:
            return "Stable"
        periods_left = (current - 15) / decline_per_period
        last_date = df["date"].iloc[-1]
        months_left = periods_left * 3
        predicted = last_date + pd.DateOffset(months=int(months_left))
        return predicted.strftime("%b %Y")
    except:
        return "Unknown"

st.set_page_config(page_title="Trend Lifecycle Modeler", page_icon="✦", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #0e0a0d; color: #f0e6ea; }
.stApp { background-color: #0e0a0d; }
section[data-testid="stSidebar"] { background-color: #160f13; border-right: 1px solid #2a1a22; }
.big-title { font-family: 'Playfair Display', serif; font-size: 4rem; font-weight: 700; color: #f0e6ea; letter-spacing: -1px; line-height: 1.1; }
.big-title span { color: #d4829a; font-style: italic; }
.subtitle { font-size: 0.85rem; color: #8a7070; letter-spacing: 0.2em; text-transform: uppercase; margin-top: 8px; margin-bottom: 32px; }
.divider { border: none; border-top: 1px solid #2a1a22; margin: 24px 0; }
.metric-card { background: #160f13; border: 1px solid #2a1a22; border-radius: 4px; padding: 20px 24px; height: 100%; }
.metric-label { font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: #8a7070; margin-bottom: 6px; }
.metric-value { font-family: 'Playfair Display', serif; font-size: 1.6rem; color: #f0e6ea; }
.stage-badge { display: inline-block; padding: 4px 12px; border-radius: 2px; font-size: 0.7rem; letter-spacing: 0.15em; font-weight: 500; text-transform: uppercase; }
.description-box { background: #160f13; border: 1px solid #2a1a22; border-left: 3px solid #d4829a; border-radius: 4px; padding: 20px 24px; margin: 16px 0; }
.description-text { font-size: 0.95rem; color: #c4a8b0; line-height: 1.7; font-style: italic; }
.death-box { background: #160f13; border: 1px solid #2a1a22; border-left: 3px solid #555; border-radius: 4px; padding: 20px 24px; margin: 12px 0; }
.death-label { font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: #666; margin-bottom: 8px; }
.death-text { font-size: 0.9rem; color: #a08888; line-height: 1.7; }
.tags-row { margin: 16px 0; display: flex; flex-wrap: wrap; gap: 8px; }
.tag { display: inline-block; padding: 4px 12px; border: 1px solid #2a1a22; border-radius: 20px; font-size: 0.7rem; color: #8a7070; letter-spacing: 0.05em; background: #160f13; }
.tag-active { border-color: #d4829a; color: #d4829a; background: rgba(212,130,154,0.1); }
.rising-card { background: #160f13; border: 1px solid #2a1a22; border-left: 3px solid #86c5a0; border-radius: 4px; padding: 14px 18px; margin-bottom: 8px; }
.rising-name { font-family: 'Playfair Display', serif; font-size: 1rem; color: #f0e6ea; }
.sidebar-label { font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: #8a7070; margin-bottom: 8px; }
.methodology-box { background: #160f13; border: 1px solid #2a1a22; border-radius: 4px; padding: 28px 32px; margin-top: 8px; }
.methodology-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #f0e6ea; margin-bottom: 12px; }
.methodology-text { font-size: 0.85rem; color: #8a7070; line-height: 1.8; }
.methodology-text b { color: #c4a8b0; font-weight: 500; }
div[data-testid="stSelectbox"] label { font-size: 0.7rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; color: #8a7070 !important; }
div[data-testid="stMultiSelect"] label { font-size: 0.7rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; color: #8a7070 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='big-title'>Trend <span>Lifecycle</span><br>Modeler</div>
<div class='subtitle'>Beauty & Lifestyle Cultural Analytics — 2020 to 2026</div>
<hr class='divider'>
""", unsafe_allow_html=True)

stage_map = {}
for name, df in TREND_DFS.items():
    peak_val = df["interest"].max()
    stage, _ = get_stage(df, peak_val)
    stage_map[name] = stage

tab1, tab2, tab3 = st.tabs(["Single Trend", "Compare Trends", "Browse by Tag"])

with tab1:
    col_filter, _ = st.columns([1, 3])
    with col_filter:
        st.markdown("<div class='sidebar-label'>Filter by Stage</div>", unsafe_allow_html=True)
        selected_stage = st.selectbox("", ["All", "EMERGING", "PEAKING", "DECLINING", "POST-PEAK", "DEAD"], key="single_stage")

    filtered_trends = list(TREND_DFS.keys()) if selected_stage == "All" else [t for t, s in stage_map.items() if s == selected_stage]

    if not filtered_trends:
        st.warning("No trends in this stage.")
    else:
        st.markdown("<div class='sidebar-label'>Select a trend</div>", unsafe_allow_html=True)
        selected = st.selectbox("", filtered_trends, key="single_trend")
        df = TREND_DFS[selected]

        peak_idx = df["interest"].idxmax()
        peak_date = df.loc[peak_idx, "date"]
        peak_value = df.loc[peak_idx, "interest"]
        stage, stage_color = get_stage(df, peak_value)
        current_interest = int(df["interest"].iloc[-1])
        predicted_death = predict_decline(df)

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"<div class='metric-card'><div class='metric-label'>Current Stage</div><div class='metric-value'><span class='stage-badge' style='background:{stage_color}22; color:{stage_color}'>{stage}</span></div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-card'><div class='metric-label'>Peak Month</div><div class='metric-value'>{peak_date.strftime('%b %Y')}</div></div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div class='metric-card'><div class='metric-label'>Peak Interest</div><div class='metric-value'>{int(peak_value)}<span style='font-size:1rem; color:#8a7070'>/100</span></div></div>", unsafe_allow_html=True)
        with col4:
            st.markdown(f"<div class='metric-card'><div class='metric-label'>Current Interest</div><div class='metric-value'>{current_interest}<span style='font-size:1rem; color:#8a7070'>/100</span></div></div>", unsafe_allow_html=True)
        with col5:
            st.markdown(f"<div class='metric-card'><div class='metric-label'>Predicted Gone By</div><div class='metric-value' style='font-size:1.2rem'>{predicted_death}</div></div>", unsafe_allow_html=True)

        tags_html = "".join([f"<span class='tag'>#{tag}</span>" for tag in DNA_TAGS[selected]])
        st.markdown(f"<div class='tags-row'>{tags_html}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='description-box'><div class='description-text'>{DESCRIPTIONS[selected]}</div></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='death-box'><div class='death-label'>☠️ What killed this trend</div><div class='death-text'>{CAUSE_OF_DEATH[selected]}</div></div>", unsafe_allow_html=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["date"], y=df["interest"], mode="lines", line=dict(color="#d4829a", width=2.5), fill="tozeroy", fillcolor="rgba(212,130,154,0.08)"))
        fig.add_trace(go.Scatter(x=df["date"], y=df["interest"], mode="markers", marker=dict(color="#d4829a", size=4, line=dict(color="#0e0a0d", width=1)), showlegend=False))
        fig.add_annotation(x=peak_date, y=peak_value, text=f"↑ Peak · {peak_date.strftime('%b %Y')}", showarrow=False, yshift=18, font=dict(color="#d4af37", size=11, family="DM Sans"))
        fig.update_layout(
            paper_bgcolor="#0e0a0d", plot_bgcolor="#0e0a0d",
            font=dict(family="DM Sans", color="#8a7070"),
            title=dict(text=selected.upper(), font=dict(family="Playfair Display, serif", size=20, color="#f0e6ea"), x=0),
            xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(size=10, color="#8a7070"), tickformat="%b %Y"),
            yaxis=dict(showgrid=True, gridcolor="#1e1218", zeroline=False, tickfont=dict(size=10, color="#8a7070"), range=[0,110]),
            height=400, margin=dict(l=0, r=0, t=50, b=0), showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("<div class='sidebar-label'>Select up to 4 trends to compare</div>", unsafe_allow_html=True)
    compare_selected = st.multiselect("", list(TREND_DFS.keys()), default=["Clean Girl Aesthetic", "Quiet Luxury"], max_selections=4, key="compare_trends")

    if len(compare_selected) < 2:
        st.info("Select at least 2 trends to compare.")
    else:
        fig = go.Figure()
        for i, trend in enumerate(compare_selected):
            color = COLORS[i % len(COLORS)]
            df_c = TREND_DFS[trend]
            peak_idx = df_c["interest"].idxmax()
            peak_date = df_c.loc[peak_idx, "date"]
            peak_value = df_c.loc[peak_idx, "interest"]
            fig.add_trace(go.Scatter(x=df_c["date"], y=df_c["interest"], mode="lines+markers", name=trend, line=dict(color=color, width=2.5), marker=dict(color=color, size=3)))
            fig.add_annotation(x=peak_date, y=peak_value, text=f"↑ {peak_date.strftime('%b %Y')}", showarrow=False, yshift=14, font=dict(color=color, size=10, family="DM Sans"))

        fig.update_layout(
            paper_bgcolor="#0e0a0d", plot_bgcolor="#0e0a0d",
            font=dict(family="DM Sans", color="#8a7070"),
            title=dict(text="TREND COMPARISON", font=dict(family="Playfair Display, serif", size=20, color="#f0e6ea"), x=0),
            xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(size=10, color="#8a7070"), tickformat="%b %Y"),
            yaxis=dict(showgrid=True, gridcolor="#1e1218", zeroline=False, tickfont=dict(size=10, color="#8a7070"), range=[0,110]),
            legend=dict(bgcolor="#160f13", bordercolor="#2a1a22", borderwidth=1, font=dict(color="#f0e6ea", size=11)),
            height=450, margin=dict(l=0, r=0, t=50, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        cols = st.columns(len(compare_selected))
        for i, trend in enumerate(compare_selected):
            color = COLORS[i % len(COLORS)]
            df_c = TREND_DFS[trend]
            peak_idx = df_c["interest"].idxmax()
            peak_date = df_c.loc[peak_idx, "date"]
            stage, stage_color = get_stage(df_c, df_c["interest"].max())
            with cols[i]:
                st.markdown(f"""
                <div class='metric-card' style='border-top: 3px solid {color}'>
                    <div class='metric-label'>{trend}</div>
                    <div style='font-size:0.85rem; color:{stage_color}; letter-spacing:0.1em; margin-bottom:6px'>{stage}</div>
                    <div style='font-size:0.8rem; color:#8a7070'>Peak: {peak_date.strftime('%b %Y')}</div>
                    <div style='font-size:0.8rem; color:#8a7070'>Now: {int(df_c['interest'].iloc[-1])}/100</div>
                </div>""", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='sidebar-label'>Filter by DNA Tag</div>", unsafe_allow_html=True)
    selected_tag = st.selectbox("", ALL_TAGS, key="tag_filter")
    matching = [t for t, tags in DNA_TAGS.items() if selected_tag in tags]
    st.markdown(f"<div style='font-size:0.8rem; color:#8a7070; margin: 12px 0 20px 0'>{len(matching)} trend{'s' if len(matching) != 1 else ''} tagged <span style='color:#d4829a'>#{selected_tag}</span></div>", unsafe_allow_html=True)

    if matching:
        fig = go.Figure()
        for i, trend in enumerate(matching):
            color = COLORS[i % len(COLORS)]
            df_t = TREND_DFS[trend]
            fig.add_trace(go.Scatter(x=df_t["date"], y=df_t["interest"], mode="lines+markers", name=trend, line=dict(color=color, width=2), marker=dict(color=color, size=3)))

        fig.update_layout(
            paper_bgcolor="#0e0a0d", plot_bgcolor="#0e0a0d",
            font=dict(family="DM Sans", color="#8a7070"),
            title=dict(text=f"ALL #{selected_tag.upper()} TRENDS", font=dict(family="Playfair Display, serif", size=20, color="#f0e6ea"), x=0),
            xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(size=10, color="#8a7070"), tickformat="%b %Y"),
            yaxis=dict(showgrid=True, gridcolor="#1e1218", zeroline=False, tickfont=dict(size=10, color="#8a7070"), range=[0,110]),
            legend=dict(bgcolor="#160f13", bordercolor="#2a1a22", borderwidth=1, font=dict(color="#f0e6ea", size=11)),
            height=420, margin=dict(l=0, r=0, t=50, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i, trend in enumerate(matching):
            df_t = TREND_DFS[trend]
            stage, stage_color = get_stage(df_t, df_t["interest"].max())
            with cols[i % 3]:
                tags_html = "".join([f"<span class='tag {'tag-active' if t == selected_tag else ''}'>#{t}</span>" for t in DNA_TAGS[trend]])
                st.markdown(f"""
                <div class='metric-card' style='margin-bottom:12px'>
                    <div style='font-family: Playfair Display, serif; font-size:1rem; color:#f0e6ea; margin-bottom:6px'>{trend}</div>
                    <div style='font-size:0.75rem; color:{stage_color}; letter-spacing:0.1em; margin-bottom:10px'>{stage}</div>
                    <div class='tags-row' style='margin:0; gap:4px'>{tags_html}</div>
                </div>""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("<div class='sidebar-label' style='margin-bottom:16px'>Rising Now</div>", unsafe_allow_html=True)
rising = [t for t, s in stage_map.items() if s == "EMERGING"]
peaking = [t for t, s in stage_map.items() if s == "PEAKING"]
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='sidebar-label'>🌱 Emerging</div>", unsafe_allow_html=True)
    for t in rising:
        st.markdown(f"<div class='rising-card'><div class='rising-name'>{t}</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='sidebar-label' style='color:#d4af37'>👑 Peaking</div>", unsafe_allow_html=True)
    for t in peaking:
        st.markdown(f"<div class='rising-card' style='border-left-color:#d4af37'><div class='rising-name'>{t}</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("""
<div class='methodology-box'>
    <div class='methodology-title'>Methodology</div>
    <div class='methodology-text'>
        <b>Lifecycle Staging:</b> Each trend is classified into one of five stages — Emerging, Peaking, Post-Peak, Declining, or Dead — based on the trajectory of its last three data points relative to its all-time peak. A trend is considered Dead when its interest score falls below 15/100.<br><br>
        <b>Decline Prediction:</b> Predicted decline dates are calculated using linear extrapolation of the current rate of decline across the last four data points. The model asks: at the current rate of change, how many periods until interest falls below 15? This is an intentionally transparent model — explainable to non-technical stakeholders rather than a black-box forecast.<br><br>
        <b>Data:</b> Interest scores are sourced directly from Google Trends (trends.google.com), indexed on a 0–100 scale where 100 represents peak search interest for that term. Data spans January 2020 to March 2026 at monthly intervals. DNA tags are assigned editorially based on each trend's origin story, cultural drivers, and lifecycle pattern.<br><br>
        <b>Built with:</b> Python · Pandas · Plotly · Streamlit
    </div>
</div>
""", unsafe_allow_html=True)
