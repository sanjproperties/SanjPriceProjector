import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components
import base64
import os

# --- LOGO PROCESSING ---
# We use the local file if available, otherwise fallback to GitHub raw URL
logo_path = 'image_69be75.png'
logo_base64 = ""

if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj AI Analyst | Real Estate Intel", layout="wide", initial_sidebar_state="collapsed")

# --- PREMIUM DARK THEME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    .main { background-color: #0d1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; text-align: center; }
    .est-value { color: #00ff88; font-size: 42px; font-weight: 900; line-height: 1; }
    .score-circle { width: 100px; height: 100px; border-radius: 50%; border: 4px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 28px; font-weight: 900; color: #ff4b4b; background: rgba(255, 75, 75, 0.05); }
    .news-card { background: #161b22; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; font-size: 14px; }
    .whatsapp-btn { background: #25d366; color: white !important; padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: 800; display: inline-block; margin: 10px 0; border: none; text-align: center; }
    .progress-fill { background: #00ff88; height: 8px; border-radius: 10px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 8px; margin-bottom: 15px; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; color: white; background: #161b22; border-radius: 12px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 15px; border-bottom: 1px solid #30363d; background: #0d1117; }
    td { padding: 15px; border-bottom: 1px solid #0d1117; }
    iframe { border-radius: 12px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

# --- ANALYST INTELLIGENCE ENGINE ---
def get_analyst_intel(location):
    loc = location.lower()
    if any(x in loc for x in ["corridor", "cybercity", "ujjain"]):
        return {
            "score": 94, "action": "Strong Buy", "appr": 1.27, "gain": 1.45, "yield": "3.2%",
            "infra": 96, "comm": 92, "conn": 98, "govt": 90, "demand": 97,
            "drivers": "₹300Cr AI Cybercity IT Park (Launched May 2026), Indore Metro Orange Line Ops, 2028 Simhastha Corridor development.",
            "verdict": "Highest growth potential in MP. The launch of Cybercity by Micro Mitti (May 2026) marks a structural shift for high-value office demand.",
            "news": [
                "🚀 MAY 13, 2026: Micro Mitti launches ₹300Cr 'Cybercity' IT Park on Super Corridor; 5000 jobs expected.",
                "🚇 MAY 09, 2026: MP Metro launches 'Celebration on Wheels'—Metro coaches now bookable for private events.",
                "🚧 UPDATE: IDA approves Rs 1,508.88 crore budget for 2025-26 with focus on Super Corridor infrastructure."
            ],
            "coords": "22.7554,75.8118"
        }
    elif any(x in loc for x in ["bypass", "ab road", "jhalaria"]):
        return {
            "score": 88, "action": "Buy", "appr": 1.10, "gain": 0.95, "yield": "4.1%",
            "infra": 89, "comm": 86, "conn": 92, "govt": 84, "demand": 91,
            "drivers": "TPS-4 Road completion (connecting Bypass to Jhalaria), Bypass 6-lane expansion, Rising demand for gated villas.",
            "verdict": "Best for premium residential stability. Recent IDA clearance of obstructions for TPS-4 road ensures direct connectivity to Jhalaria.",
            "news": [
                "🛣 MAY 14, 2026: IDA clears 20 structures to speed up TPS-4 road connecting Bypass to Jhalaria.",
                "🏢 APR 2026: Surge in residential demand for gated villas as bypass infrastructure nears 90% completion."
            ],
            "coords": "22.7303,75.9221"
        }
    else:
        return {
            "score": 79, "action": "Hold", "appr": 0.82, "gain": 0.65, "yield": "4.8%",
            "infra": 81, "comm": 83, "conn": 86, "govt": 72, "demand": 78,
            "drivers": "Urban Renewal Schemes, MOG Lines Redevelopment, High Rental Stability in established hubs.",
            "verdict": "Mature market performance. Solid for rental yields, but look for newer corridors for rapid capital gain.",
            "news": ["🏛 FEB 2026: MOG Lines Redevelopment Phase 1 plots auction completed; infrastructure work begins."],
            "coords": "22.7196,75.8577"
        }

# --- BRANDING & HEADER ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    if logo_base64:
        st.image(f"data:image/png;base64,{logo_base64}", width=120)
    else:
        # Fallback to your GitHub URL
        st.image("https://raw.githubusercontent.com/charchitrawal/sanj_logo/main/Sanj_Properties_Logo.png", width=120)

with col_title:
    st.markdown("<div style='color: #ff4b4b; font-weight: 800; font-size: 14px; letter-spacing: 2px; padding-top: 10px;'>SANJ PROPERTIES — WHERE VISION MEETS VELOCITY</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-bottom: 40px;'>Sanj AI Analyst</h1>", unsafe_allow_html=True)

# --- INPUT SECTION ---
with st.container():
    c1, c2, c3 = st.columns([3, 2, 1])
    with c1: loc_input = st.text_input("SEARCH AREA / PROJECT", value="Super Corridor")
    with c2: price = st.number_input("CURRENT RATE (₹/sqft)", value=5500)
    with c3:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze = st.button("RUN SANJ AI ↗")

if analyze:
    intel = get_analyst_intel(loc_input)
    est_val = int(price * (1 + intel['gain']))

    # 1. Name Display
    st.markdown(f"<h1 style='font-size: 65px; font-weight: 900; margin-bottom: 0; color: white;'>{loc_input.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8b949e; margin-top:-10px;
