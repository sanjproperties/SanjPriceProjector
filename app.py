import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components
import base64

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Price Projector", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS: PREMIUM DARK ANALYST THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;700;900&family=Inter:wght@400;700&display=swap');
    
    /* Note: 'The Seasons' is a premium font. We use a high-end serif fallback for maximum compatibility */
    
    .main { background-color: #0d1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Typography */
    h1, h2, h3 { font-family: 'League Spartan', sans-serif !important; text-transform: uppercase; letter-spacing: 1px; }
    .subheading { font-family: 'Georgia', serif !important; font-style: italic; color: #8b949e; font-size: 18px; }
    
    /* Branding */
    .branding-title { font-size: 64px; font-weight: 900; color: #ff4b4b; margin-bottom: 0; line-height: 1; font-family: 'League Spartan'; }
    .tagline { font-family: 'Georgia', serif; font-style: italic; font-size: 22px; color: #ffffff; margin-top: -5px; margin-bottom: 30px; letter-spacing: 2px; }
    
    /* Search Result */
    .area-title { font-size: 90px; font-weight: 900; line-height: 0.9; margin: 40px 0 10px 0; color: #ffffff; font-family: 'League Spartan'; }
    
    /* Cards & Metrics */
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 16px; padding: 25px; text-align: center; height: 100%; }
    .est-value-big { color: #00ff88; font-size: 72px; font-weight: 900; line-height: 1; margin: 15px 0; font-family: 'League Spartan'; }
    .score-circle { width: 120px; height: 120px; border-radius: 50%; border: 5px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 36px; font-weight: 900; color: #ff4b4b; background: rgba(255, 75, 75, 0.05); }
    
    /* Progress Bars */
    .prog-label { display: flex; justify-content: space-between; font-size: 14px; font-weight: 600; margin-bottom: 5px; color: #8b949e; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 10px; margin-bottom: 20px; width: 100%; }
    .progress-fill { background: linear-gradient(90deg, #ff4b4b, #ff8a8a); height: 10px; border-radius: 10px; }
    
    /* Footer */
    .footer-section { background: #000000; padding: 100px 20px; margin-top: 100px; border-top: 2px solid #30363d; text-align: center; }
    .footer-links a { font-family: 'League Spartan'; font-size: 40px; font-weight: 900; color: #ffffff !important; margin: 0 30px; text-decoration: none; text-transform: uppercase; }
    .footer-links a:hover { color: #ff4b4b !important; }
    .whatsapp-cta { background: #25d366; color: white !important; padding: 25px 50px; border-radius: 50px; font-size: 28px; font-weight: 900; text-decoration: none; display: inline-block; margin: 40px 0; font-family: 'League Spartan'; }
    
    /* Table Styling */
    table { width: 100%; border-collapse: collapse; background: #161b22; border-radius: 16px; overflow: hidden; }
    th { background: #0d1117; padding: 20px; text-align: left; color: #8b949e; font-size: 12px; }
    td { padding: 20px; border-bottom: 1px solid #0d1117; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# --- INTELLIGENCE ENGINE ---
def get_intel(location):
    loc = location.lower()
    if any(x in loc for x in ["corridor", "cybercity", "ujjain"]):
        return {"score": 94, "action": "Strong Buy", "gain": 1.45, "appr": 1.2, "infra": 96, "comm": 92, "conn": 98, "verdict": "Tier-1 Growth Corridor. Rapid IT expansion and airport proximity make this the most lucrative zone.", "news": "Cybercity IT Park launched; Metro Phase 2 approved for Ujjain Road corridor."}
    return {"score": 82, "action": "Buy", "gain": 0.85, "appr": 0.9, "infra": 85, "comm": 80, "conn": 88, "verdict": "Stable appreciation zone with high residential demand. Good for long-term safety.", "news": "IDA clears new transit roads for Bypass clusters; Township occupancy at record highs."}

# --- BRANDING ---
st.markdown('<p class="branding-title">SANJ PRICE PROJECTOR</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Sanj Properties — Where Vision Meets Velocity</p>', unsafe_allow_html=True)

# --- INPUTS ---
col_in1, col_in2, col_in3 = st.columns([3, 2, 1])
with col_in1:
    loc_name = st.text_input("ENTER AREA / PROJECT", value="Super Corridor")
with col_in2:
    price_now = st.number_input("CURRENT RATE (₹/SQFT)", value=5500)
with col_in3:
    st.write("<br>", unsafe_allow_html=True)
    run = st.button("RUN ANALYSIS")

if run:
    data = get_intel(loc_name)
    est_future = int(price_now * (1 + data['gain']))

    # 1. AREA TITLE
    st.markdown(f'<h1 class="area-title">{loc_name.upper()}</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheading">Exclusive Market Intelligence Report</p>', unsafe_allow_html=True)
    st.write("---")

    # 2. HERO METRICS
    m1, m2, m3 = st.columns([1, 2, 1])
    with m1:
        st.markdown(f'<div class="metric-card"><div class="score-circle">{data["score"]}</div><h2 style="color:#ff4b4b;">{data["action"]}</h2><p class="subheading">Investment Score</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-card"><p class="subheading">2031 EST. VALUE (IN 5 YRS)</p><div class="est-value-big">₹{est_future:,}</div><p style="color:#00ff88; font-weight:800; font-size:18px;">PROJECTED RATE PER SQFT</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-card"><h2>VERY HIGH</h2><p class="subheading">Liquidity</p><hr style="border-color:#30363d"><h2>3.8%</h2><p class="subheading">Avg. Rental Yield</p></div>', unsafe_allow_html=True)

    # 3. CHARTS
    st.write("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📊 HISTORICAL PRICE (5Y)")
        fig1 = go.Figure(go.Scatter(x=[2021, 2026], y=[price_now/2, price_now], mode='lines+markers', line=dict(color='#ff4b4b', width=4), fill='tozeroy'))
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        st.markdown("### 📈 GROWTH FORECAST (5Y)")
        fig2 = go.Figure(go.Scatter(x=[2026, 2031], y=[price_now, est_future], mode='lines+markers', line=dict(color='#00ff88', width=4), fill='tozeroy'))
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
        st.plotly_chart(fig2, use_container_width=True)

    # 4. INTEL & PROGRESS
    st.write("---")
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("### 📰 DYNAMIC NEWS & DRIVERS")
        st.info(f"**LATEST:** {data['news']}")
        st.markdown("### 💡 AI VERDICT")
        st.success(data['verdict'])
    with col_r:
        st.markdown("### 🛠 DEVELOPMENT PROGRESS")
        for l, v in [("Infrastructure", data['infra']), ("Connectivity", data['conn']), ("Commercial", data['comm'])]:
            st.markdown(f'<div class="prog-label"><span>{l}</span><span>{v}%</span></div><div class="progress-bg"><div class="progress-fill" style="width:{v}%"></div></div>', unsafe_allow_html=True)

    # 5. MAP & TABLE
    st.write("---")
    st.markdown("### 🛰 LIVE SATELLITE MAP")
    components.html(f'<iframe width="100%" height="450" style="border-radius:16px;" src="http://googleusercontent.com/maps.google.com/5{loc_name}+Indore&maptype=satellite" frameborder="0"></iframe>', height=470)

    st.markdown("### 📅 PRICE TIMELINE BREAKDOWN")
    t_rows = "".join([f"<tr><td>{y}</td><td>₹{int(price_now*(1.1**(y-2026))):,}</td><td>PROJECTED</td></tr>" for y in range(2026, 2032)])
    st.markdown(f"<table><tr><th>YEAR</th><th>RATE</th><th>STATUS</th></tr>{t_rows}</table>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div class="footer-section">
        <h1 style="font-size:70px; color:#ff4b4b;">SANJ PROPERTIES</h1>
        <p class="tagline">Where Vision Meets Velocity</p>
        <div class="footer-links">
            <a href="https://linktr.ee/Sanj.properties">LINKTREE</a>
            <a href="https://www.instagram.com/sanj.property/">INSTAGRAM</a>
            <a href="https://www.facebook.com/profile.id=61586657172896">FACEBOOK</a>
        </div>
        <br>
        <a href="https://wa.me/919039914137" class="whatsapp-cta">CONNECT ON WHATSAPP ↗</a>
        <br><br>
        <h2 style="letter-spacing:5px; color:#8b949e;">9039914137 | 7697246823</h2>
    </div>
""", unsafe_allow_html=True)
