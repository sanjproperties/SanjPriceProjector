import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Value Projector", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    .main { background-color: #0e1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .top-bar { background: #161b22; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #30363d; margin-bottom: 20px; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 15px; text-align: center; }
    .metric-value { color: #ffffff; font-size: 24px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 12px; text-transform: uppercase; }
    .news-card { background: #0d1117; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; }
    .progress-label { display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 5px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 8px; margin-bottom: 15px; }
    .progress-fill { background: #00ff88; height: 8px; border-radius: 10px; }
    .footer { text-align: center; padding: 40px; border-top: 1px solid #333; margin-top: 50px; color: #8b949e; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; color: white; background: #161b22; border-radius: 8px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 15px; border-bottom: 1px solid #30363d; }
    td { padding: 15px; border-bottom: 1px solid #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("""
    <div class='top-bar'>
        <span style='color: #8b949e; font-size: 12px; letter-spacing: 1px;'>EXPERT ADVISORY:</span> 
        <span style='color: #ff4b4b; font-weight: 800; margin-left: 15px;'>9039914137</span> | 
        <span style='color: #ff4b4b; font-weight: 800; margin-left: 15px;'>7697246823</span>
    </div>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
st.markdown("<h1 style='text-align: center;'>Market Value <span style='color:#ff4b4b'>Projector</span></h1>", unsafe_allow_html=True)

# --- DYNAMIC DATA MAPPING ---
# Logic to differentiate area performance
def get_area_data(location):
    loc = location.lower()
    if any(x in loc for x in ["corridor", "ujjain", "cyber"]):
        return {
            "appr": "127%", "gain": "140%", "yield": "3.2%", 
            "infra": 94, "comm": 91, "demand": 95,
            "news": [
                "🚀 ₹300Cr AI Cybercity Launch on Super Corridor",
                "🏨 Simhastha 2028 Hospitality wave driving North-West land prices"
            ]
        }
    elif any(x in loc for x in ["bypass", "ab road", "jhalaria"]):
        return {
            "appr": "110%", "gain": "115%", "yield": "4.1%", 
            "infra": 88, "comm": 82, "demand": 89,
            "news": [
                "🏗 IDA opens 30-metre road connecting Bypass to major residential hubs",
                "🌆 Bypass infrastructure upgrade: New flyovers clearing traffic bottlenecks"
            ]
        }
    else: # Central/Established areas like Annapurna
        return {
            "appr": "85%", "gain": "70%", "yield": "4.5%", 
            "infra": 82, "comm": 85, "demand": 80,
            "news": [
                "🏛 MOG Lines Land Parcel-1 redevelopment approved",
                "📈 Central Indore Rental Yields hit 5-year high due to lack of new supply"
            ]
        }

# --- INPUT SECTION ---
c1, c2, c3 = st.columns([2, 2, 1])
with c1:
    loc_input = st.text_input("ENTER LOCATION / AREA", value="Super Corridor")
with c2:
    price = st.number_input("CURRENT RATE (₹/sqft)", value=5000)
with c3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("Analyze ↗")

if generate:
    data = get_area_data(loc_input)
    
    # --- METRICS ---
    m1, m2, m3, m4 = st.columns(4)
    m1.markdown(f"<div class='metric-card'><div class='metric-label'>5Y Appr.</div><div class='metric-value'>{data['appr']}</div></div>", unsafe_allow_html=True)
    m2.markdown(f"<div class='metric-card'><div class='metric-label'>Proj. Gain</div><div class='metric-value'>{data['gain']}</div></div>", unsafe_allow_html=True)
    m3.markdown(f"<div class='metric-card'><div class='metric-label'>Rental Yield</div><div class='metric-value'>{data['yield']}</div></div>", unsafe_allow_html=True)
    m4.markdown("<div class='metric-card'><div class='metric-label'>Liquidity</div><div class='metric-value'>High</div></div>", unsafe_allow_html=True)

    # --- GROWTH DRIVERS & PROGRESS BARS ---
    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown(f"### Growth Factors for {loc_input.title()}")
        for label, score in [("Infrastructure", data['infra']), ("Commercial Activity", data['comm']), ("Market Demand", data['demand'])]:
            st.markdown(f"<div class='progress-label'><span>{label}</span><span>{score}%</span></div><div class='progress-bg'><div class='progress-fill' style='width:{score}%'></div></div>", unsafe_allow_html=True)
    
    with col_r:
        st.markdown("### Latest Market Insights")
        for news_item in data['news']:
            st.markdown(f"<div class='news-card'>{news_item}</div>", unsafe_allow_html=True)

    # --- COMPLETE PRICING TIMELINE ---
    st.markdown("### Complete Price Timeline")
    timeline_years = [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    # Dynamic calculation based on area appreciation rate
    appr_factor = float(data['appr'].replace('%',''))/100
    
    rows = ""
    for yr in timeline_years:
        if yr < 2026:
            p = int(price / (1 + (appr_factor * (2026-yr)/5)))
            rows += f"<tr><td>{yr}</td><td>₹{p:,}</td><td>Historical</td></tr>"
        elif yr == 2026:
            rows += f"<tr style='background:rgba(255,75,75,0.1)'><td>2026</td><td>₹{price:,}</td><td><strong>CURRENT</strong></td></tr>"
        else:
            p = int(price * (1 + (appr_factor * (yr-2026)/5)))
            rows += f"<tr><td>{yr}</td><td>₹{p:,}</td><td>Projected</td></tr>"

    st.markdown(f"""
    <table>
        <tr><th>YEAR</th><th>PRICE (₹)</th><th>PHASE</th></tr>
        {rows}
    </table>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div class='footer'>
        <p><strong>Sanj Properties — Where Vision Meets Velocity</strong></p>
        <p>🔗 <a href='https://linktr.ee/Sanj.properties' style='color:#ff4b4b;'>Full Project Portfolio: https://linktr.ee/Sanj.properties</a></p>
        <p>📲 <a href='https://shorturl.ad/OROPw' style='color:#ff4b4b;'>Join Daily WhatsApp Update Group</a></p>
        <p>Contact: 9039914137 | 7697246823</p>
    </div>
""", unsafe_allow_html=True)
