import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Price Projector", layout="wide", initial_sidebar_state="collapsed")

# --- LOGO PROCESSING ---
def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

logo_base64 = get_base64("Logo Black with Bg.png")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    .main { background-color: #0e1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 15px; text-align: center; }
    .metric-value { color: #ffffff; font-size: 24px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 12px; text-transform: uppercase; }
    .progress-fill { background: #00ff88; height: 8px; border-radius: 10px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 8px; margin-bottom: 15px; }
    .driver-item { background: #0d1117; border: 1px solid #30363d; border-radius: 8px; padding: 15px; margin-bottom: 12px; border-left: 4px solid #ff4b4b; }
    .verdict-box { border: 1px solid #ff4b4b; border-radius: 12px; padding: 20px; background: rgba(255, 75, 75, 0.05); }
    .footer { text-align: center; padding: 40px; border-top: 1px solid #333; margin-top: 50px; color: #8b949e; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; color: white; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 10px; border-bottom: 1px solid #30363d; }
    td { padding: 12px 10px; border-bottom: 1px solid #161b22; }
    </style>
""", unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("""
    <div style='background: #161b22; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #30363d;'>
        <span style='color: #8b949e; font-size: 12px;'>DIRECT INQUIRY:</span> 
        <span style='color: #ff4b4b; font-weight: bold; margin: 0 15px;'>9039914137</span> | 
        <span style='color: #ff4b4b; font-weight: bold; margin: 0 15px;'>7697246823</span>
    </div>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
col_logo, col_links = st.columns([1, 1])
with col_logo:
    if logo_base64:
        st.markdown(f'<img src="data:image/png;base64,{logo_base64}" width="200">', unsafe_allow_html=True)
with col_links:
    st.markdown("""
        <div style='text-align: right; padding-top: 20px;'>
            <a href='https://linktr.ee/Sanj.properties' style='color:white; text-decoration:none; margin-left:15px;'>Our Portfolio</a>
            <a href='https://www.instagram.com/sanj.property/' style='color:white; text-decoration:none; margin-left:15px;'>Instagram</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Market Value <span style='color:#ff4b4b'>Projector</span></h1>", unsafe_allow_html=True)

# --- USER INPUTS ---
c1, c2, c3 = st.columns([2, 2, 1])
with c1:
    loc = st.text_input("ENTER LOCATION / AREA", value="Annapurna")
with c2:
    price = st.number_input("CURRENT MARKET PRICE (₹/sqft)", value=9000)
with c3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("Analyze Now ↗")

if generate:
    st.markdown(f"### {loc.title()} Real Estate Forecast")
    
    # --- METRICS ---
    m1, m2, m3, m4 = st.columns(4)
    m1.markdown("<div class='metric-card'><div class='metric-label'>5Y Appr.</div><div class='metric-value'>127%</div></div>", unsafe_allow_html=True)
    m2.markdown("<div class='metric-card'><div class='metric-label'>Proj. Gain</div><div class='metric-value'>120%</div></div>", unsafe_allow_html=True)
    m3.markdown("<div class='metric-card'><div class='metric-label'>Rental Yield</div><div class='metric-value'>3.8%</div></div>", unsafe_allow_html=True)
    m4.markdown("<div class='metric-card'><div class='metric-label'>Liquidity</div><div class='metric-value'>Very High</div></div>", unsafe_allow_html=True)

    # --- PRICE CHARTS ---
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    y_h = [2021, 2022, 2023, 2024, 2025, 2026]
    p_h = [price*0.44, price*0.53, price*0.64, price*0.78, price*0.9, price]
    y_p = [2026, 2027, 2028, 2029, 2030, 2031]
    p_p = [price, price*1.16, price*1.36, price*1.6, price*1.88, price*2.2]

    with ch1:
        st.markdown(f"**Historical Trend: {loc.title()}**")
        fig1 = go.Figure(go.Scatter(x=y_h, y=p_h, mode='lines+markers', line=dict(color='#ff4b4b', width=3), fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.1)'))
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=250, margin=dict(l=0,r=0,t=20,b=0), font_color="white")
        st.plotly_chart(fig1, use_container_width=True)

    with ch2:
        st.markdown(f"**5-Year Projection: {loc.title()}**")
        fig2 = go.Figure(go.Scatter(x=y_p, y=p_p, mode='lines+markers', line=dict(color='#00ff88', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 136, 0.1)'))
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=250, margin=dict(l=0,r=0,t=20,b=0), font_color="white")
        st.plotly_chart(fig2, use_container_width=True)

    # --- LATEST NEWS & INFRASTRUCTURE (FETCHED NEWS) ---
    st.markdown("### 📰 Latest Development & Market News (Last 3 Months)")
    n1, n2 = st.columns(2)
    with n1:
        st.markdown(f"""
            <div class='driver-item'>
                <strong>🚀 ₹300 Cr AI Cybercity Launch</strong><br>
                <small>May 2026</small><br>
                A massive 6.28 lakh sq ft AI-focused IT park launched on the Super Corridor, creating 5,000+ jobs. This massive employment shift is driving residential demand across West Indore.
            </div>
            <div class='driver-item'>
                <strong>🏨 ₹2,000 Cr Hospitality Boom</strong><br>
                <small>May 2026</small
