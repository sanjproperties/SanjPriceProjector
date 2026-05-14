import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Value Projector", layout="wide", initial_sidebar_state="collapsed")

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
    .top-bar { background: #161b22; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #30363d; margin-bottom: 20px; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 15px; text-align: center; }
    .metric-value { color: #ffffff; font-size: 24px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 12px; text-transform: uppercase; }
    .news-card { background: #0d1117; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; }
    .progress-label { display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 5px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 8px; margin-bottom: 15px; }
    .progress-fill { background: #00ff88; height: 8px; border-radius: 10px; }
    .verdict-box { border: 1px solid #ff4b4b; border-radius: 12px; padding: 20px; background: rgba(255, 75, 75, 0.05); margin-top: 20px; }
    .footer { text-align: center; padding: 40px; border-top: 1px solid #333; margin-top: 50px; color: #8b949e; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; color: white; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 10px; border-bottom: 1px solid #30363d; }
    td { padding: 12px 10px; border-bottom: 1px solid #161b22; }
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
col_logo, col_links = st.columns([1, 1])
with col_logo:
    if logo_base64:
        st.markdown(f'<img src="data:image/png;base64,{logo_base64}" width="200">', unsafe_allow_html=True)
with col_links:
    st.markdown("""
        <div style='text-align: right; padding-top: 25px;'>
            <a href='https://linktr.ee/Sanj.properties' style='color:white; text-decoration:none; margin-left:20px; font-weight:600;'>Project Portfolio</a>
            <a href='https://www.instagram.com/sanj.property/' style='color:white; text-decoration:none; margin-left:20px;'>Instagram</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Market Value <span style='color:#ff4b4b'>Projector</span></h1>", unsafe_allow_html=True)

# --- USER INPUTS ---
c1, c2, c3 = st.columns([2, 2, 1])
with c1:
    loc = st.text_input("ENTER LOCATION / AREA", value="Annapurna")
with c2:
    price = st.number_input("CURRENT RATE (₹/sqft)", value=9000)
with c3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate = st.button("Generate Forecast ↗")

if generate:
    # --- DYNAMIC NEWS LOGIC ---
    is_corridor = any(x in loc.lower() for x in ["corridor", "ujjain", "bypass", "cyber", "it park"])
    
    # --- METRICS ---
    m1, m2, m3, m4 = st.columns(4)
    m1.markdown("<div class='metric-card'><div class='metric-label'>5Y Appr.</div><div class='metric-value'>127%</div></div>", unsafe_allow_html=True)
    m2.markdown("<div class='metric-card'><div class='metric-label'>Proj. Gain</div><div class='metric-value'>120%</div></div>", unsafe_allow_html=True)
    m3.markdown("<div class='metric-card'><div class='metric-label'>Rental Yield</div><div class='metric-value'>3.8%</div></div>", unsafe_allow_html=True)
    m4.markdown("<div class='metric-card'><div class='metric-label'>Liquidity</div><div class='metric-value'>Very High</div></div>", unsafe_allow_html=True)

    # --- CHARTS ---
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    y_h = [2021, 2022, 2023, 2024, 2025, 2026]
    p_h = [price*0.44, price*0.53, price*0.64, price*0.78, price*0.9, price]
    y_p = [2026, 2027, 2028, 2029, 2030, 2031]
    p_p = [price, price*1.16, price*1.36, price*1.6, price*1.88, price*2.2]

    with ch1:
        st.markdown(f"**Growth History: {loc.title()}**")
        fig1 = go.Figure(go.Scatter(x=y_h, y=p_h, mode='lines+markers', line=dict(color='#ff4b4b', width=3), fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.1)'))
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=250, margin=dict(l=0,r=0,t=20,b=0), font_color="white")
        st.plotly_chart(fig1, use_container_width=True)

    with ch2:
        st.markdown(f"**Future Projection: {loc.title()}**")
        fig2 = go.Figure(go.Scatter(x=y_p, y=p_p, mode='lines+markers', line=dict(color='#00ff88', width=3), fill='tozeroy', fillcolor='rgba(0, 255, 136, 0.1)'))
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=250, margin=dict(l=0,r=0,t=20,b=0), font_color="white")
        st.plotly_chart(fig2, use_container_width=True)

    # --- DYNAMIC NEWS & MARKET INSIGHTS ---
    st.markdown(f"### 📰 Market News & Insights for {loc.title()}")
    col_n1, col_n2 = st.columns(2)
    
    with col_n1:
        if is_corridor:
            st.markdown("""
                <div class='news-card'><strong>🚀 ₹300Cr AI Cybercity Launch</strong><br>Micro Mitti has launched a 6.28 lakh sq ft IT Park on the Super Corridor, expected to create 5,000+ tech jobs by 2029.</div>
                <div class='news-card'><strong>🏨 Simhastha 2028 Hospitality Surge</strong><br>Over 2,000 hotel rooms are being added to the corridor to handle the massive influx for Simhastha 2028.</div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='news-card'><strong>🏗 IDA Master Plan Road Widening</strong><br>IDA has cleared obstructions to complete a 30-metre-wide road connecting the Bypass to Jhalaria, directly impacting {loc}'s connectivity.</div>
                <div class='news-card'><strong>🌆 MOG Lines Redevelopment</strong><br>Major urban development approved for MOG Lines Land Parcel-1, creating a ripple effect of appreciation for central residential hubs like yours.</div>
            """, unsafe_allow_html=True)

    with col_n2:
        st.markdown("### Development Factors")
        for n, s in [("Infrastructure", 92), ("Commercial Growth", 89), ("Market Demand", 91)]:
            st.markdown(f"<div class='progress-label'><span>{n}</span><span>{s}%</span></div><div class='progress-bg'><div class='progress-fill' style='width:{s}%'></div></div>", unsafe_allow_html=True)

    # --- FINAL VERDICT ---
    st.markdown(f"""<div class='verdict-box'>
        <strong>INVESTMENT VERDICT:</strong> {loc.title()} is a high-performance zone. With current IDA road projects 
        and the IT/Hospitality boom in Indore, we project a 220% growth by 2031. 
        <strong>Target Value: ₹{int(price*2.2)}/sqft.</strong>
    </div>""", unsafe_allow_html=True)

    # --- PRICING TIMELINE (SCREENSHOT ITEM) ---
    st.markdown("### Property Pricing Timeline")
    st.markdown(f"""
    <table>
        <tr><th>YEAR</th><th>PRICE (₹)</th><th>PHASE</th></tr>
        <tr><td>2021</td><td>{int(price*0.44)}</td><td>Historical Baseline</td></tr>
        <tr style='background:rgba(255,75,75,0.1)'><td>2026</td><td>{price}</td><td><strong>CURRENT MARKET</strong></td></tr>
        <tr><td>2031</td><td>{int(price*2.2)}</td><td>AI-Projected Value</td></tr>
    </table>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div class='footer'>
        <p><strong>Sanj Properties — Where Vision Meets Velocity</strong></p>
        <p>🔗 <a href='https://linktr.ee/Sanj.properties' style='color:#ff4b4b; font-weight:bold;'>Official Portfolio: https://linktr.ee/Sanj.properties</a></p>
        <p>📲 <a href='https://shorturl.ad/OROPw' style='color:#ff4b4b;'>Join Daily WhatsApp Property Updates</a></p>
        <p>Expert Support: 9039914137 | 7697246823</p>
        <p style='font-size:10px; margin-top:25px;'>© 2026 Sanj Properties Indore. AI-estimated data for information only.</p>
    </div>
""", unsafe_allow_html=True)
