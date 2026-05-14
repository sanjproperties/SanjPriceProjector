import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Sanj Properties | Investment Projector", layout="wide", initial_sidebar_state="collapsed")

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
    .main { background-color: #0e1117; color: #ffffff; font-family: 'Inter', sans-serif; }
    .top-bar { background: #161b22; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #30363d; margin-bottom: 20px; }
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 15px; text-align: center; height: 100%; }
    .metric-value { color: #ffffff; font-size: 26px; font-weight: 800; }
    .metric-label { color: #8b949e; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
    .score-circle { width: 80px; height: 80px; border-radius: 50%; border: 4px solid #ff4b4b; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 22px; font-weight: 800; color: #ff4b4b; }
    .strategy-card { background: rgba(0, 255, 136, 0.05); border: 1px solid #00ff88; border-radius: 12px; padding: 20px; margin-top: 20px; }
    .news-card { background: #0d1117; border-left: 4px solid #ff4b4b; border-radius: 8px; padding: 15px; margin-bottom: 12px; border: 1px solid #30363d; }
    .progress-fill { background: #00ff88; height: 8px; border-radius: 10px; }
    .progress-bg { background: #30363d; border-radius: 10px; height: 8px; margin-bottom: 15px; }
    .footer { text-align: center; padding: 40px; border-top: 1px solid #333; margin-top: 50px; color: #8b949e; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; color: white; background: #161b22; border-radius: 8px; overflow: hidden; }
    th { text-align: left; color: #8b949e; font-size: 12px; padding: 15px; border-bottom: 1px solid #30363d; }
    td { padding: 15px; border-bottom: 1px solid #0d1117; }
    </style>
""", unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("""
    <div class='top-bar'>
        <span style='color: #8b949e; font-size: 12px;'>SANJ PROPERTIES EXPERT LINE:</span> 
        <span style='color: #ff4b4b; font-weight: 800; margin-left: 15px;'>9039914137</span> | 
        <span style='color: #ff4b4b; font-weight: 800; margin-left: 15px;'>7697246823</span>
    </div>
""", unsafe_allow_html=True)

# --- BRANDED HEADER ---
c_logo, c_empty, c_links = st.columns([1.5, 1, 2])
with c_logo:
    if logo_url:
        st.markdown(f'<img src="{logo_url}" width="220">', unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color:#ff4b4b; margin:0;'>Sanj Properties</h2>", unsafe_allow_html=True)
with c_links:
    st.markdown("""
        <div style='text-align: right; padding-top: 25px;'>
            <a href='https://linktr.ee/Sanj.properties' style='color:white; text-decoration:none; margin-left:20px; font-weight:600;'>Full Portfolio</a>
            <a href='https://www.instagram.com/sanj.property/' style='color:white; text-decoration:none; margin-left:20px;'>Instagram Updates</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Investment <span style='color:#ff4b4b'>Projector</span> AI</h1>", unsafe_allow_html=True)

# --- DYNAMIC DATA LOGIC ---
def get_area_data(location):
    loc = location.lower()
    if any(x in loc for x in ["corridor", "ujjain", "cyber", "vibrant"]):
        return {"score": "9.2", "appr": 1.27, "yield": "3.2%", "infra": 94, "comm": 91, "demand": 95, 
                "short": "Hold for 18-24 months to capture the IT park completion surge.",
                "long": "Excellent for commercial leasing or high-value residential plotting.",
                "news": ["🚀 ₹300Cr AI Cybercity IT Park launched on Super Corridor", "🏨 Simhastha 2028: Hospitality projects booming in the corridor"]}
    elif any(x in loc for x in ["bypass", "ab road", "jhalaria", "saakar"]):
        return {"score": "8.8", "appr": 1.10, "yield": "4.1%", "infra": 88, "comm": 82, "demand": 8
