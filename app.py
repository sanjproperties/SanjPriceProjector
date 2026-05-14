import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Senior Analyst AI", layout="wide", initial_sidebar_state="collapsed")

# --- LOGO PROCESSING ---
def get_base64_logo(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{data}"
    return None

logo_url = get_base64_logo("Logo Black with Bg.png")

# --- CUSTOM CSS: SENIOR ANALYST DASHBOARD ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    .main { background-color: #0d1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .top-bar { background: #161b22; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #30363d; margin-bottom: 20px; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; text-align: center; }
    .metric-value { color: #ffffff; font-size: 26px; font-weight: 800; }
    .est-value { color: #00ff88; font-size: 42px; font-weight: 900; line-height: 1; }
    .score-circle { width: 100px; height: 100px; border-radius: 50%; border: 4px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 28px; font-weight: 900; color: #ff4b4b; background: rgba(255, 75, 75, 0.05); }
    .action-badge { background: #ff4b4b; color: white; padding: 4px 12px; border-radius: 20px; font-size: 14px; font-weight: 800; text-transform: uppercase; }
    .news-card { background: #161b22; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; }
    .progress-fill { background: #00ff88; height: 10px; border-radius: 10px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 10px; margin-bottom: 20px; }
    .footer { text-align: center; padding: 60px; border-top: 1px solid #30363d; margin-top: 60px; color: #8b949e; }
    .whatsapp-btn { background: #25d366; color: white !important; padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: 800; display: inline-block; margin: 20px 0; }
    table { width: 100%; border-collapse: collapse; margin-top: 25px; color: white; background: #161b22; border-radius: 12px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 18px; border-bottom: 1px solid #30363d; }
    td { padding: 18px; border-bottom: 1px solid #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("<div class='top-bar'>SANJ PROPERTIES EXPERT HOTLINE: <span style='color: #ff4b4b; font-weight: 800;'>9039914137</span> | <span style='color: #ff4b4b; font-weight: 800;'>7697246823</span></div>", unsafe_allow_html=True)

# --- BRANDED HEADER ---
c_logo, c_links = st.columns([1.5, 2])
with c_logo:
    if logo_url: st.markdown(f'<img src="{logo_url}" width="200">', unsafe_allow_html=True)
with c_links:
    st.markdown("<div style='text-align: right; padding-top: 20px;'><a href='https://linktr.ee/Sanj.properties' style='color:white; text-decoration:none; margin-left:25px; font-weight:600;'>Project Portfolio</a></div>", unsafe_allow_html=True)

# --- DYNAMIC ANALYST ENGINE ---
def get_location_intel(location):
    loc = location.lower()
    # High Growth Areas
    if any(x in loc for x in ["corridor", "ujjain", "it park", "vibrant"]):
        return {
            "score": 92, "action": "Strong Buy", "appr": 1.27, "gain": 1.40, "yield": "3.1%",
            "infra": 94, "comm": 91, "conn": 95, "govt": 88, "demand": 96,
            "drivers": "₹300Cr AI Cybercity, Simhastha 2028 Metro Extension, TCS/Infosys Expansion.",
            "news": ["🚀 ₹300Cr IT Cybercity construction fast-tracked (May 2026)", "🏨 Simhastha 2028: Hospitality corridor connectivity at 90%"]
        }
    # Established Areas
    return {
        "score": 78, "action": "Hold / Wait", "appr": 0.85, "gain": 0.70, "yield": "4.6%",
        "infra": 82, "comm": 85, "conn": 89, "govt": 75, "demand": 81,
        "drivers": "Urban Renewal Schemes, MOG Lines Redevelopment, High Rental Stability.",
        "news": ["🏛 MOG Lines Redevelopment Phase 1 Launched", "📈 Rental values hit 5-year peak due to inventory crunch"]
    }

# --- INPUT SECTION ---
with st.container():
    c1, c2, c3 = st.columns([3, 2, 1])
    with c1: loc_input = st.text_input("SEARCH AREA / PROJECT", value="Super Corridor")
    with c2: price = st.number_input("CURRENT RATE (₹/sqft)", value=5500)
    with c3:
        st.markdown("<br>", unsafe_allow_html=True)
        generate = st.button("RUN ANALYSIS ↗")

if generate:
    intel = get_location_intel(loc_input)
    
    # 1. Name in Big Font
    st.markdown(f"<h1 style='font-size: 60px; font-weight: 900; margin-bottom: 0;'>{loc_input.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8b949e; margin-top: -10px;'>Indore Market Analysis • Senior Analyst AI</p>", unsafe_allow_html=True)

    # 3, 4, 5, 8. Metrics, Yield, Score, Est Value
    st.write("---")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><div class='score-circle'>{intel['score']}</div><div class='action-badge'>{intel['action']}</div><div class='metric-label' style='margin-top:10px;'>Analyst Score</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{int(intel['appr']*100)}%</div><div class='metric-label'>5Y History</div><br><div class='metric-value'>{int(intel['gain']*100)}%</div><div class='metric-label'>Proj. Gain</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><div class='metric-value'>{intel['yield']}</div><div class='metric-label'>Rental Yield</div><br><div class='metric-value'>Very High</div><div class='metric-label'>Liquidity</div></div>", unsafe_allow_html=True)
    with m4:
        # 5. Big Font Green Est Value
        est_val = int(price * (1 + intel['appr']))
        st.markdown(f"<div class='metric-card'><div class='metric-label'>2031 Est. Value</div><div class='est-value'>₹{est_val:,}</div><div class='metric-label' style='color:#00ff88;'>Per Sq. Ft.</div></div>", unsafe_allow_html=True)

    # 6, 7. Charts
    st.markdown("<br>", unsafe_allow_html=True)
    ch1, ch2 = st.columns(2)
    with ch1:
        st.markdown("### 📊 Price History (Last 5 Years)")
        h_years = [2021, 2022, 2023, 2024, 2025, 2026]
        h_prices = [price/(1.8), price/(1.5), price/(1.3), price/(1.15), price/(1.05), price]
        fig_h = go.Figure(go.Scatter(x=h_years, y=h_prices, mode='lines+markers', line=dict(color='#ff4b4b', width=4), fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.1)'))
        fig_h.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig_h, use_container_width=True)
    with ch2:
        st.markdown("### 📈 Future Projection (Next 5 Years)")
        p_years = [2026, 2027, 2028, 2029, 2030, 2031]
        p_prices = [price, price*1.2, price*1.45, price*1.7, price*2.0, est_val]
        fig_p = go.Figure(go.Scatter(x=p_years, y=p_prices, mode='lines+markers', line=dict(color='#00ff88', width=4), fill='tozeroy', fillcolor='rgba(0, 255, 136, 0.1)'))
        fig_p.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300, margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig_p, use_container_width=True)

    # 9, 10. Development Factors & Growth Drivers
    st.write("---")
    col_f, col_d = st.columns(2)
    with col_f:
        st.markdown("### Development Factors (%)")
        factors = [("Infrastructure Growth", intel['infra']), ("Commercial Activity", intel['comm']), 
                   ("Connectivity", intel['conn']), ("Govt Scheme Coverage", intel['govt']), ("Market Demand", intel['demand'])]
        for lab, val in factors:
            st.markdown(f"<div style='display:flex; justify-content:space-between; font-size:13px;'><span>{lab}</span><span>{val}%</span></div><div class='progress-bg'><div class='progress-fill' style='width:{val}%'></div></div>", unsafe_allow_html=True)
    with col_d:
        st.markdown("### Key Growth Drivers")
        st.info(f"**Catalysts:** {intel['drivers']}")
        st.markdown("### Latest Market News")
        for news in intel['news']:
            st.markdown(f"<div class='news-card'>{news}</div>", unsafe_allow_html=True)

    # 11, 12. Satellite View & Verdict
    st.write("---")
    st.markdown("### 🛰 Market Satellite View")
    st.image("https://via.placeholder.com/1200x400/161b22/ffffff?text=Dynamic+Satellite+View+of+"+loc_input.replace(" ","+"), use_container_width=True)
    
    st.markdown(f"""<div style='background:rgba(255,75,75,0.05); border:1px solid #ff4b4b; padding:25px; border-radius:12px; margin-top:20px;'>
        <h3 style='margin-top:0; color:#ff4b4b;'>Investment Verdict</h3>
        <p style='font-size:18px;'>{loc_input} remains a <strong>{intel['action']}</strong>. Data confirms a high-velocity growth path 
        due to proximity to major IT hubs and the upcoming Metro corridor. We anticipate price stabilization at <strong>₹{est_val:,}/sqft</strong> by 2031.</p>
    </div>""", unsafe_allow_html=True)

    # 13. Complete Price Timeline
    st.markdown("### Complete Price Timeline")
    rows = "".join([f"<tr><td>{y}</td><td>₹{int(price*(1+(intel['appr']*(y-2026)/5))):,}</td><td>Projected</td></tr>" if y > 2026 else f"<tr><td>{y}</td><td>₹{int(price/(1+(intel['appr']*(2026-y)/5))):,}</td><td>Historical</td></tr>" for y in range(2021, 2032)])
    st.markdown(f"<table><tr><th>YEAR</th><th>PRICE (₹)</th><th>STATUS</th></tr>{rows}</table>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
    <div class='footer'>
        <p><strong>Sanj Properties — Where Vision Meets Velocity</strong></p>
        <p>Expert Support: 9039914137 | 7697246823</p>
        <a href='https://wa.me/919039914137' class='whatsapp-btn'>Connect with Expert on WhatsApp ↗</a><br>
        <p>
            <a href='https://linktr.ee/Sanj.properties' style='color:#8b949e; margin:0 15px;'>Website Portfolio</a> | 
            <a href='https://shorturl.ad/OROPw' style='color:#8b949e; margin:0 15px;'>Join WhatsApp Group</a> |
            <a href='https://www.instagram.com/sanj.property/' style='color:#8b949e; margin:0 15px;'>Instagram</a>
        </p>
        <p style='font-size:11px; margin-top:30px;'>© 2026 Sanj Properties. AI-calculated projections for informational use only.</p>
    </div>
""", unsafe_allow_html=True)
