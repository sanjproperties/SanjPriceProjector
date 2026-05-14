import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Value Projector", layout="wide", initial_sidebar_state="collapsed")

# --- LOGO PROCESSING (Robust Version) ---
def get_base64_logo(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_url = get_base64_logo("Logo Black with Bg.png")

# --- CUSTOM CSS: PREMIUM DARK ANALYST THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    .main { background-color: #0d1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .top-bar { background: #161b22; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #30363d; margin-bottom: 20px; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; text-align: center; }
    .metric-value { color: #ffffff; font-size: 28px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
    .score-circle { width: 90px; height: 90px; border-radius: 50%; border: 4px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 26px; font-weight: 800; color: #ff4b4b; background: rgba(255, 75, 75, 0.05); }
    .news-card { background: #161b22; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; }
    .progress-fill { background: #00ff88; height: 10px; border-radius: 10px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 10px; margin-bottom: 20px; }
    .strategy-box { background: rgba(0, 255, 136, 0.03); border: 1px solid #00ff88; border-radius: 12px; padding: 20px; margin: 20px 0; }
    .footer { text-align: center; padding: 50px; border-top: 1px solid #30363d; margin-top: 60px; color: #8b949e; }
    table { width: 100%; border-collapse: collapse; margin-top: 25px; color: white; background: #161b22; border-radius: 12px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 18px; border-bottom: 1px solid #30363d; background: #0d1117; }
    td { padding: 18px; border-bottom: 1px solid #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("""
    <div class='top-bar'>
        <span style='color: #8b949e; font-size: 13px;'>SANJ PROPERTIES EXPERT HOTLINE:</span> 
        <span style='color: #ff4b4b; font-weight: 800; margin-left: 15px;'>9039914137</span> | 
        <span style='color: #ff4b4b; font-weight: 800; margin-left: 15px;'>7697246823</span>
    </div>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
c_logo, c_empty, c_links = st.columns([1.5, 1, 2])
with c_logo:
    if logo_url:
        st.markdown(f'<img src="{logo_url}" width="220">', unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color:#ff4b4b; margin:0;'>Sanj Properties</h2>", unsafe_allow_html=True)
with c_links:
    st.markdown("""
        <div style='text-align: right; padding-top: 25px;'>
            <a href='https://linktr.ee/Sanj.properties' style='color:white; text-decoration:none; margin-left:25px; font-weight:600;'>Project Portfolio</a>
            <a href='https://www.instagram.com/sanj.property/' style='color:white; text-decoration:none; margin-left:25px;'>Instagram Updates</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-top: 10px;'>Investment <span style='color:#ff4b4b'>Projector</span> AI</h1>", unsafe_allow_html=True)

# --- DYNAMIC ANALYST LOGIC ---
def get_analyst_data(location):
    loc = location.lower()
    if any(x in loc for x in ["corridor", "ujjain", "it park"]):
        return {"score": "9.3", "appr": 1.27, "yield": "3.1%", "infra": 96, "comm": 92, "demand": 94,
                "strategy": "Super Corridor is in a 'Hyper-Growth' phase. The ₹300Cr IT Cybercity launch is a primary catalyst.",
                "news": ["🚀 ₹300Cr AI Cybercity IT Park construction fast-tracked [May 2026]", "🏨 Simhastha 2028: Corridor connectivity infrastructure hits 85% completion"]}
    elif any(x in loc for x in ["bypass", "ab road", "jhalaria"]):
        return {"score": "8.9", "appr": 1.10, "yield": "4.2%", "infra": 90, "comm": 84, "demand": 88,
                "strategy": "Stable growth with high rental demand. Focus on residential luxury segments.",
                "news": ["🏗 IDA completes 30m Jhalaria-Bypass connecting road", "🛣 AB Road 6-lane expansion approved for North-South connectivity"]}
    else:
        return {"score": "8.2", "appr": 0.85, "yield": "4.7%", "infra": 84, "comm": 86, "demand": 82,
                "strategy": "Established market. Wealth preservation play with steady rental yields.",
                "news": ["🏛 MOG Lines Land Parcel-1 redevelopment officially launched", "📈 Central Indore rental market surges 15% due to limited new inventory"]}

# --- INPUT SECTION ---
with st.container():
    c1, c2, c3 = st.columns([2, 2, 1])
    with c1:
        loc_input = st.text_input("PROPERTY LOCATION", value="Super Corridor")
    with c2:
        price = st.number_input("CURRENT RATE (₹/sqft)", value=5500)
    with c3:
        st.markdown("<br>", unsafe_allow_html=True)
        generate = st.button("Analyze Now ↗")

if generate:
    data = get_analyst_data(loc_input)
    
    # --- METRICS & SCORE ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><div class='score-circle'>{data['score']}</div><div class='metric-label'>Investment Score</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{int(data['appr']*100)}%</div><div class='metric-label'>5Y Appreciation</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{data['yield']}</div><div class='metric-label'>Rental Yield</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>₹{int(price*(1+data['appr'])):,}</div><div class='metric-label'>2031 Est. Value</div></div>", unsafe_allow_html=True)

    # --- STRATEGY BOX ---
    st.markdown(f"""<div class='strategy-box'>
        <h3 style='color:#00ff88; margin-top:0;'>AI Strategy & Suggestion</h3>
        <p><strong>Short Term (1-3Y):</strong> Capture appreciation from the current infrastructure spike.</p>
        <p><strong>Long Term (5-10Y):</strong> {data['strategy']}</p>
    </div>""", unsafe_allow_html=True)

    # --- GROWTH DRIVERS & NEWS ---
    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("### Growth Potential")
        for label, score in [("Infrastructure", data['infra']), ("Commercial Potential", data['comm']), ("Demand Index", data['demand'])]:
            st.markdown(f"<div style='display:flex; justify-content:space-between; font-size:14px; margin-bottom:5px;'><span>{label}</span><span>{score}%</span></div><div class='progress-bg'><div class='progress-fill' style='width:{score}%'></div></div>", unsafe_allow_html=True)
    with col_r:
        st.markdown("### Latest Market Insights")
        for n in data['news']:
            st.markdown(f"<div class='news-card'>{n}</div>", unsafe_allow_html=True)

    # --- PRICING TIMELINE TABLE ---
    st.markdown("### Price Projection Timeline")
    rows = ""
    for yr in range(2021, 2032):
        if yr < 2026:
            p = int(price / (1 + (data['appr'] * (2026-yr)/5)))
            rows += f"<tr><td>{yr}</td><td>₹{p:,}</td><td>Historical</td></tr>"
        elif yr == 2026:
            rows += f"<tr style='background:rgba(255,75,75,0.15)'><td>2026</td><td>₹{price:,}</td><td><strong>CURRENT MARKET</strong></td></tr>"
        else:
            p = int(price * (1 + (data['appr'] * (yr-2026)/5)))
            rows += f"<tr><td>{yr}</td><td>₹{p:,}</td><td>Projected</td></tr>"
    st.markdown(f"<table><tr><th>YEAR</th><th>PRICE (₹)</th><th>STATUS</th></tr>{rows}</table>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div class='footer'>
        <p><strong>Sanj Properties — Where Vision Meets Velocity</strong></p>
        <p>🔗 <a href='https://linktr.ee/Sanj.properties' style='color:#ff4b4b; font-weight:bold;'>Portfolio: https://linktr.ee/Sanj.properties</a></p>
        <p>📲 <a href='https://shorturl.ad/OROPw' style='color:#ff4b4b;'>Daily WhatsApp Group</a></p>
        <p>9039914137 | 7697246823</p>
    </div>
""", unsafe_allow_html=True)
