import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# --- LOGO PROCESSING ---
# This converts your uploaded PNG to a format Streamlit can render directly
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Using the filename of the uploaded PNG logo
logo_path = 'image_69ae98.png' 
logo_html = ""
if os.path.exists(logo_path):
    bin_str = get_base64_of_bin_file(logo_path)
    logo_html = f"data:image/png;base64,{bin_str}"

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | AI Analyst", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for the "Senior Analyst" Premium Dark Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .main { background-color: #0e1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    .stTextInput>div>div>input { background-color: #161b22 !important; color: white !important; border: 1px solid #30363d !important; border-radius: 8px; }
    .stButton>button {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff7575 100%);
        color: white; font-weight: 800; width: 100%; border: none; border-radius: 12px; height: 50px;
    }
    
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 15px; text-align: center; }
    .metric-value { color: #ff4b4b; font-size: 24px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 12px; text-transform: uppercase; }
    
    .verdict-box { background: rgba(255, 75, 75, 0.1); border: 1px solid #ff4b4b; border-radius: 12px; padding: 20px; }
    
    .footer { text-align: center; color: #8b949e; font-size: 14px; margin-top: 50px; padding: 20px; border-top: 1px solid #30363d; }
    a { color: #ff4b4b !important; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

# --- LOGO & HEADER ---
col_logo, col_links = st.columns([1, 1])
with col_logo:
    if logo_html:
        st.image(logo_html, width=180)
with col_links:
    st.markdown("<p style='text-align: right;'><a href='https://linktr.ee/Sanj.properties'>Official Website</a> | <a href='https://www.instagram.com/sanj.property/'>Instagram</a></p>", unsafe_allow_html=True)

# --- INPUTS ---
st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>Property Price Projector</h1>", unsafe_allow_html=True)

with st.container():
    c1, c2 = st.columns(2)
    with c1:
        loc = st.text_input("LOCATION / AREA", placeholder="e.g. Super Corridor")
    with c2:
        price = st.number_input("CURRENT PRICE (₹/sqft)", min_value=500, value=5000)

if st.button("RUN AI ANALYSIS ↗"):
    if loc:
        # Simulated Data for V4 UI Demonstration
        data = {
            "locationFull": f"{loc}, Indore, MP",
            "investmentScore": 88,
            "metrics": {"appreciation5yr": "127%", "projectedGain": "120%", "rentalYield": "3.8%", "liquidity": "Very High"},
            "historical": [2200, 2650, 3200, 3900, 4500, 5000],
            "projected": [5800, 6800, 8000, 9400, 11000],
            "years_h": [2020, 2021, 2022, 2023, 2024, 2025],
            "years_p": [2026, 2027, 2028, 2029, 2030]
        }

        # --- SCORE & METRICS ---
        st.markdown(f"<h2 style='color: #ff4b4b;'>{data['locationFull']}</h2>", unsafe_allow_html=True)
        
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.markdown(f"<div class='metric-card'><div class='metric-label'>Score</div><div class='metric-value'>{data['investmentScore']}</div></div>", unsafe_allow_html=True)
        m2.markdown(f"<div class='metric-card'><div class='metric-label'>5Y Appr.</div><div class='metric-value'>{data['metrics']['appreciation5yr']}</div></div>", unsafe_allow_html=True)
        m3.markdown(f"<div class='metric-card'><div class='metric-label'>Proj. Gain</div><div class='metric-value'>{data['metrics']['projectedGain']}</div></div>", unsafe_allow_html=True)
        m4.markdown(f"<div class='metric-card'><div class='metric-label'>Rental</div><div class='metric-value'>{data['metrics']['rentalYield']}</div></div>", unsafe_allow_html=True)
        m5.markdown(f"<div class='metric-card'><div class='metric-label'>Liquidity</div><div class='metric-value' style='font-size: 16px; padding-top:8px;'>{data['metrics']['liquidity']}</div></div>", unsafe_allow_html=True)

        # --- CHARTS ---
        st.write("---")
        ch1, ch2 = st.columns(2)
        
        with ch1:
            st.markdown("### 📊 Price History (5 Years)")
            fig_h = go.Figure(go.Scatter(x=data['years_h'], y=data['historical'], mode='lines+markers', line=dict(color='#ff4b4b', width=4), fill='tozeroy'))
            fig_h.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig_h, use_container_width=True)

        with ch2:
            st.markdown("### 📈 Projection (Next 5 Years)")
            fig_p = go.Figure(go.Scatter(x=data['years_p'], y=data['projected'], mode='lines+markers', line=dict(color='#00ff88', width=4), fill='tozeroy'))
            fig_p.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig_p, use_container_width=True)

        # --- VERDICT ---
        st.markdown("### 📝 Investment Verdict")
        st.markdown(f"<div class='verdict-box'>Super Corridor is Indore's single most promising corridor. With Infosys, TCS, and IIM nearby, and the Metro Phase 2 confirmed, prices are projected to reach ₹11,000/sqft by 2030. <strong>Strong BUY recommendation.</strong></div>", unsafe_allow_html=True)

        # --- FOOTER ---
        st.markdown(f"""
            <div class="footer">
                <p><strong>Sanj Properties — Where Vision Meets Velocity</strong></p>
                <p>9039914137 | 7697246823</p>
                <a href="https://wa.me/919039914137">Chat on WhatsApp</a> | <a href="https://linktr.ee/Sanj.properties">Our Portfolio</a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter a location.")
