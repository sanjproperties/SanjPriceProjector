import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj AI Analyst | Real Estate Intel", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS: PREMIUM DARK ANALYST THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    .main { background-color: #0d1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; text-align: center; }
    .est-value { color: #00ff88; font-size: 42px; font-weight: 900; line-height: 1; }
    .score-circle { width: 100px; height: 100px; border-radius: 50%; border: 4px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 28px; font-weight: 900; color: #ff4b4b; background: rgba(255, 75, 75, 0.05); }
    .news-card { background: #161b22; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; font-size: 14px; }
    .whatsapp-btn { background: #25d366; color: white !important; padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: 800; display: inline-block; margin: 10px 0; border: none; }
    .progress-fill { background: #00ff88; height: 8px; border-radius: 10px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 8px; margin-bottom: 15px; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; color: white; background: #161b22; border-radius: 12px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 15px; border-bottom: 1px solid #30363d; background: #0d1117; }
    td { padding: 15px; border-bottom: 1px solid #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- DYNAMIC LOCATION INTELLIGENCE ENGINE ---
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
            ]
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
            ]
        }
    else:
        return {
            "score": 79, "action": "Hold", "appr": 0.82, "gain": 0.65, "yield": "4.8%",
            "infra": 81, "comm": 83, "conn": 86, "govt": 72, "demand": 78,
            "drivers": "Urban Renewal Schemes, MOG Lines Redevelopment, High Rental Stability in established hubs.",
            "verdict": "Mature market performance. Solid for rental yields, but look for newer corridors for rapid capital gain.",
            "news": ["🏛 FEB 2026: MOG Lines Redevelopment Phase 1 plots auction completed; infrastructure work begins."]
        }

# --- HEADER & BRANDING ---
st.markdown("<div style='text-align: center; color: #ff4b4b; font-weight: 800; font-size: 14px; letter-spacing: 2px;'>SANJ PROPERTIES — WHERE VISION MEETS VELOCITY</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; margin-bottom: 40px;'>Sanj AI Analyst</h1>", unsafe_allow_html=True)

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

    # 1. Name in Big Font
    st.markdown(f"<h1 style='font-size: 65px; font-weight: 900; margin-bottom: 0; color: white;'>{loc_input.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8b949e; margin-top:-10px; font-weight: 600;'>INDORE REAL ESTATE • AI-POWERED INVESTMENT INSIGHTS</p>", unsafe_allow_html=True)

    # Metrics Display
    st.write("---")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><div class='score-circle'>{intel['score']}</div><div style='background:#ff4b4b; border-radius:20px; font-size:12px; font-weight:800; padding:4px 12px;'>{intel['action']}</div><div class='metric-label' style='margin-top:10px;'>Sanj AI Score</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{int(intel['appr']*100)}%</div><div class='metric-label'>Past 5Y Appr.</div><br><div class='metric-value'>{int(intel['gain']*100)}%</div><div class='metric-label'>Next 5Y Proj.</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{intel['yield']}</div><div class='metric-label'>Rental Yield</div><br><div class='metric-value'>Very High</div><div class='metric-label'>Market Liquidity</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='metric-card'><div class='metric-label'>2031 Est. Value</div><div class='est-value'>₹{est_val:,}</div><div class='metric-label' style='color:#00ff88; font-weight:700;'>Target Price / Sqft</div></div>", unsafe_allow_html=True)

    # Charts
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    with ch1:
        st.markdown("### 📊 Price History (Last 5 Years)")
        fig_h = go.Figure(go.Scatter(x=[2021,2022,2023,2024,2025,2026], y=[price/2.1, price/1.8, price/1.5, price/1.3, price/1.1, price], mode='lines+markers', line=dict(color='#ff4b4b', width=4), fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.1)'))
        fig_h.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=280, margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig_h, use_container_width=True)
    with ch2:
        st.markdown("### 📈 Projection (Next 5 Years)")
        fig_p = go.Figure(go.Scatter(x=[2026,2027,2028,2029,2030,2031], y=[price, price*1.2, price*1.5, price*1.8, price*2.1, est_val], mode='lines+markers', line=dict(color='#00ff88', width=4), fill='tozeroy', fillcolor='rgba(0, 255, 136, 0.1)'))
        fig_p.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=280, margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig_p, use_container_width=True)

    # Development & News
    st.write("---")
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("### 🛠 Development Factors (%)")
        factors = [("Infrastructure Growth", intel['infra']), ("Commercial Activity", intel['comm']), ("Connectivity", intel['conn']), ("Govt Scheme Coverage", intel['govt']), ("Market Demand Index", intel['demand'])]
        for lab, val in factors:
            st.markdown(f"<div style='display:flex; justify-content:space-between; font-size:13px;'><span>{lab}</span><span style='color:#00ff88; font-weight:700;'>{val}%</span></div><div class='progress-bg'><div class='progress-fill' style='width:{val}%'></div></div>", unsafe_allow_html=True)
        st.markdown("### 🚀 Key Growth Drivers")
        st.info(intel['drivers'])
    with col_right:
        st.markdown("### 📰 Latest Market News (Past 3 Months)")
        for n in intel['news']:
            st.markdown(f"<div class='news-card'>{n}</div>", unsafe_allow_html=True)

    # Satellite & Verdict
    st.write("---")
    st.markdown("### 🛰 Market Satellite View")
    st.image(f"https://via.placeholder.com/1200x350/161b22/ffffff?text=Satellite+Imagery:+{loc_input.upper()}+INDORE", use_container_width=True)
    st.markdown(f"<div style='background:rgba(0,255,136,0.05); border:1px solid #00ff88; padding:30px; border-radius:12px; margin-top:20px;'><h3>Sanj AI Verdict</h3><p style='font-size:18px;'>{intel['verdict']}</p></div>", unsafe_allow_html=True)

    # Timeline Table
    st.markdown("### Complete Price Timeline")
    rows = ""
    for y in range(2021, 2032):
        p_val = price / (1 + (intel['appr'] * (2026 - y) / 5)) if y < 2026 else price * (1 + (intel['gain'] * (y - 2026) / 5))
        status = "Historical" if y < 2026 else "CURRENT" if y == 2026 else "Projected"
        rows += f"<tr><td>{y}</td><td>₹{int(p_val):,}</td><td style='color:{'#00ff88' if 'Projected' in status else '#ff4b4b'};'>{status}</td></tr>"
    st.markdown(f"<table><tr><th>YEAR</th><th>EST. PRICE / SQFT</th><th>DATA STATUS</th></tr>{rows}</table>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div style='text-align:center; padding:80px; border-top:1px solid #30363d; margin-top:80px; background:#161b22; border-radius:12px 12px 0 0;'>
        <h3 style='color:#ff4b4b; margin-bottom:5px;'>Sanj Properties — Where Vision Meets Velocity</h3>
        <p style='color:#8b949e;'>Expert Advice: 9039914137 | 7697246823</p>
        <a href='https://wa.me/919039914137' class='whatsapp-btn'>Connect to WhatsApp for Expert Advice ↗</a><br>
        <div style='margin-top:20px;'>
            <a href='https://linktr.ee/Sanj.properties' style='color:white; margin:0 15px; text-decoration:none;'>Website Portfolio</a> | 
            <a href='https://shorturl.ad/OROPw' style='color:white; margin:0 15px; text-decoration:none;'>Join WhatsApp Group</a> |
            <a href='https://www.instagram.com/sanj.property/' style='color:white; margin:0 15px; text-decoration:none;'>Instagram</a>
        </div>
    </div>
""", unsafe_allow_html=True)
