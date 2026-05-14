import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components

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

    # 1. Name Display
    st.markdown(f"<h1 style='font-size: 65px; font-weight: 900; margin-bottom: 0; color: white;'>{loc_input.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8b949e; margin-top:-10px; font-weight: 600;'>INDORE REAL ESTATE • AI-POWERED INVESTMENT INSIGHTS</p>", unsafe_allow_html=True)

    # 2. Latest News & Key Drivers
    st.write("---")
    col_news, col_factors = st.columns(2)
    with col_news:
        st.markdown("### 📰 Latest Market News")
        for n in intel['news']:
            st.markdown(f"<div class='news-card'>{n}</div>", unsafe_allow_html=True)
    with col_factors:
        st.markdown("### 🚀 Key Growth Drivers")
        st.info(intel['drivers'])

    # 3-5. Metrics Display
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><div class='score-circle'>{intel['score']}</div><div style='background:#ff4b4b; border-radius:20px; font-size:12px; font-weight:800; padding:4px 12px;'>{intel['action']}</div><div class='metric-label' style='margin-top:10px;'>Investment Score</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{int(intel['appr']*100)}%</div><div class='metric-label'>Past 5Y Appr.</div><br><div class='metric-value'>{int(intel['gain']*100)}%</div><div class='metric-label'>Next 5Y Proj.</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{intel['yield']}</div><div class='metric-label'>Rental Yield</div><br><div class='metric-value'>Very High</div><div class='metric-label'>Market Liquidity</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='metric-card'><div class='metric-label'>2031 Est. Value</div><div class='est-value'>₹{est_val:,}</div><div class='metric-label' style='color:#00ff88; font-weight:700;'>Target Price / Sqft</div></div>", unsafe_allow_html=True)

    # 6-7. Interactive Charts
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    with ch1:
        st.markdown("### 📊 Price History")
        fig_h = go.Figure(go.Scatter(x=list(range(2021, 2027)), y=[price/2, price/1.7, price/1.4, price/1.2, price/1.1, price], mode='lines+markers', line=dict(color='#ff4b4b', width=4), fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.1)'))
        fig_h.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
        st.plotly_chart(fig_h, use_container_width=True)
    with ch2:
        st.markdown("### 📈 Projection")
        fig_p = go.Figure(go.Scatter(x=list(range(2026, 2032)), y=[price, price*1.2, price*1.5, price*1.8, price*2.1, est_val], mode='lines+markers', line=dict(color='#00ff88', width=4), fill='tozeroy', fillcolor='rgba(0, 255, 136, 0.1)'))
        fig_p.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
        st.plotly_chart(fig_p, use_container_width=True)

    # 8-10. Development Progress & Detailed Verdict
    st.write("---")
    v_left, v_right = st.columns([2, 1])
    with v_left:
        st.markdown("### 🛠 Development Factors (%)")
        factors = [("Infrastructure", intel['infra']), ("Commercial", intel['comm']), ("Connectivity", intel['conn']), ("Government", intel['govt'])]
        for lab, val in factors:
            st.markdown(f"<div style='display:flex; justify-content:space-between; font-size:13px;'><span>{lab}</span><span>{val}%</span></div><div class='progress-bg'><div class='progress-fill' style='width:{val}%'></div></div>", unsafe_allow_html=True)
    with v_right:
        st.markdown(f"<div style='background:rgba(0,255,136,0.05); border:1px solid #00ff88; padding:20px; border-radius:12px;'><h3>AI Verdict</h3><p>{intel['verdict']}</p></div>", unsafe_allow_html=True)

    # 12. PRICE TIMELINE TABLE
    st.markdown("### 📅 Detailed Price Timeline")
    rows = ""
    for y in range(2021, 2032):
        p_val = price / (1 + (intel['appr'] * (2026 - y) / 5)) if y < 2026 else price * (1 + (intel['gain'] * (y - 2026) / 5))
        status = "Historical" if y < 2026 else "CURRENT" if y == 2026 else "Projected"
        rows += f"<tr><td>{y}</td><td>₹{int(p_val):,}</td><td style='color:{'#00ff88' if 'Projected' in status else '#ff4b4b'};'>{status}</td></tr>"
    st.markdown(f"<table><tr><th>YEAR</th><th>PRICE / SQFT</th><th>STATUS</th></tr>{rows}</table>", unsafe_allow_html=True)

# --- FOOTER & WHATSAPP ---
st.markdown(f"""
    <div style='text-align:center; padding:60px; border-top:1px solid #30363d; margin-top:80px; background:#161b22; border-radius:12px;'>
        <h3 style='color:#ff4b4b;'>Sanj Properties — Where Vision Meets Velocity</h3>
        <p>Expert Advice: 9039914137 | 7697246823</p>
        <a href='https://wa.me/919039914137' class='whatsapp-btn'>CHAT ON WHATSAPP ↗</a>
        <p style='font-size:12px; margin-top:30px; color:#8b949e;'>
            <a href='https://linktr.ee/Sanj.properties' style='color:#8b949e;'>Our Curated Portfolio</a> | 
            <a href='https://www.instagram.com/sanj.property/' style='color:#8b949e;'>Instagram</a> | 
            <a href='https://www.facebook.com/profile.id=61586657172896' style='color:#8b949e;'>Facebook</a>
        </p>
    </div>
""", unsafe_allow_html=True)
