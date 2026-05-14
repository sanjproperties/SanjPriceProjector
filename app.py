import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Value Projector", layout="wide", initial_sidebar_state="collapsed")

# --- LOGO PROCESSING ---
def get_base64_logo(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_url = get_base64_logo("Logo Black with Bg.png")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    .main { background-color: #0d1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .top-bar { background: #161b22; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #30363d; margin-bottom: 20px; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; text-align: center; }
    .metric-value { color: #ffffff; font-size: 26px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
    .score-circle { width: 90px; height: 90px; border-radius: 50%; border: 4px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 24px; font-weight: 800; color: #ff4b4b; background: rgba(255, 75, 75, 0.05); }
    .strategy-box { background: rgba(0, 255, 136, 0.03); border: 1px solid #00ff88; border-radius: 12px; padding: 20px; margin: 20px 0; }
    .footer { text-align: center; padding: 50px; border-top: 1px solid #30363d; margin-top: 60px; color: #8b949e; }
    table { width: 100%; border-collapse: collapse; margin-top: 25px; color: white; background: #161b22; border-radius: 12px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 18px; border-bottom: 1px solid #30363d; background: #0d1117; }
    td { padding: 18px; border-bottom: 1px solid #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("<div class='top-bar'>SANJ PROPERTIES EXPERT HOTLINE: <span style='color: #ff4b4b; font-weight: 800;'>9039914137</span> | <span style='color: #ff4b4b; font-weight: 800;'>7697246823</span></div>", unsafe_allow_html=True)

# --- BRANDED HEADER ---
c_logo, c_links = st.columns([1.5, 2])
with c_logo:
    if logo_url: st.markdown(f'<img src="{logo_url}" width="220">', unsafe_allow_html=True)
    else: st.markdown("<h2 style='color:#ff4b4b;'>Sanj Properties</h2>", unsafe_allow_html=True)
with c_links:
    st.markdown("<div style='text-align: right; padding-top: 20px;'><a href='https://linktr.ee/Sanj.properties' style='color:white; text-decoration:none; margin-left:25px; font-weight:600;'>Full Portfolio</a></div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Investment <span style='color:#ff4b4b'>Projector</span> AI</h1>", unsafe_allow_html=True)

# --- DYNAMIC ANALYST LOGIC ---
def get_analyst_data(location):
    loc = location.lower()
    if any(x in loc for x in ["corridor", "ujjain"]):
        return {"score": "9.3", "appr": 1.27, "yield": "3.1%", "h_years": [2021,2022,2023,2024,2025,2026], "h_prices": [2200,2800,3500,4200,4800,5500]}
    return {"score": "8.2", "appr": 0.85, "yield": "4.7%", "h_years": [2021,2022,2023,2024,2025,2026], "h_prices": [4500,5200,6000,7200,8100,9000]}

# --- INPUT SECTION ---
c1, c2, c3 = st.columns([2, 2, 1])
with c1: loc_input = st.text_input("PROPERTY LOCATION", value="Super Corridor")
with c2: price = st.number_input("CURRENT RATE (₹/sqft)", value=5500)
with c3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("Analyze Now ↗")

if generate:
    data = get_analyst_data(loc_input)
    
    # --- METRICS & SCORE ---
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown(f"<div class='metric-card'><div class='score-circle'>{data['score']}</div><div class='metric-label'>Analyst Score</div></div>", unsafe_allow_html=True)
    with m2: st.markdown(f"<div class='metric-card'><div class='metric-value'>{int(data['appr']*100)}%</div><div class='metric-label'>5Y Appreciation</div></div>", unsafe_allow_html=True)
    with m3: st.markdown(f"<div class='metric-card'><div class='metric-value'>{data['yield']}</div><div class='metric-label'>Rental Yield</div></div>", unsafe_allow_html=True)
    with m4: st.markdown(f"<div class='metric-card'><div class='metric-value'>₹{int(price*(1+data['appr'])):,}</div><div class='metric-label'>2031 Est. Value</div></div>", unsafe_allow_html=True)

    # --- THE MISSING CHARTS SECTION ---
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    
    # Chart 1: Price History
    with ch1:
        st.markdown("### 📊 Price History (5 Years)")
        fig_h = go.Figure(go.Scatter(x=data['h_years'], y=data['h_prices'], mode='lines+markers', line=dict(color='#ff4b4b', width=4), fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.1)'))
        fig_h.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig_h, use_container_width=True)

    # Chart 2: Future Projection
    with ch2:
        st.markdown("### 📈 Projection (Next 5 Years)")
        p_years = [2026, 2027, 2028, 2029, 2030, 2031]
        p_prices = [price, price*1.15, price*1.35, price*1.65, price*1.90, price*2.2]
        fig_p = go.Figure(go.Scatter(x=p_years, y=p_prices, mode='lines+markers', line=dict(color='#00ff88', width=4), fill='tozeroy', fillcolor='rgba(0, 255, 136, 0.1)'))
        fig_p.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig_p, use_container_width=True)

    # --- PRICING TABLE & FOOTER ---
    st.markdown("### Price Projection Timeline")
    rows = "".join([f"<tr><td>{y}</td><td>₹{int(price*(1+(data['appr']*(y-2026)/5))):,}</td><td>Projected</td></tr>" if y > 2026 else f"<tr><td>{y}</td><td>₹{int(price/(1+(data['appr']*(2026-y)/5))):,}</td><td>Historical</td></tr>" for y in range(2021, 2032)])
    st.markdown(f"<table><tr><th>YEAR</th><th>PRICE (₹)</th><th>STATUS</th></tr>{rows}</table>", unsafe_allow_html=True)

st.markdown("<div class='footer'><strong>Sanj Properties — Where Vision Meets Velocity</strong><br>📞 9039914137 | 7697246823</div>", unsafe_allow_html=True)
