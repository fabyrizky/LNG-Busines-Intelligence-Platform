# app.py - Main Application
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json

# Page Configuration
st.set_page_config(
    page_title="LNG Business Intelligence Platform",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #E0F2FE 0%, #DBEAFE 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🔥 LNG Business Intelligence Platform</h1>', unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/1E3A8A/FFFFFF?text=Sustraco+Energy", width=300)
    st.markdown("---")
    
    menu = st.radio(
        "Navigation Menu",
        ["🏠 Dashboard", "📚 LNG Training", "💰 Project Calculator", 
         "📊 Market Analysis", "🎯 Opportunity Tracker"]
    )
    
    st.markdown("---")
    st.info("💡 **Pro Tip**: Upgrade to Premium untuk akses penuh semua fitur!")

# Dashboard Page
if menu == "🏠 Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("JKM Price ($/MMBtu)", "12.85", "+0.35")
    with col2:
        st.metric("Brent Oil ($/bbl)", "78.45", "-1.20")
    with col3:
        st.metric("Active Projects", "156", "+12")
    with col4:
        st.metric("Indonesia Demand (MTPA)", "8.5", "+15%")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 LNG Price Trend (Last 30 Days)")
        dates = pd.date_range(end=datetime.now(), periods=30)
        prices = [12 + i*0.1 + (-1)**i * 0.5 for i in range(30)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines+markers', name='JKM Price'))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌏 Regional LNG Demand")
        demand_data = pd.DataFrame({
            'Region': ['Japan', 'China', 'Korea', 'India', 'Indonesia'],
            'Demand': [70, 85, 45, 30, 8.5]
        })
        fig = px.bar(demand_data, x='Region', y='Demand', color='Demand')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

# LNG Training Module
elif menu == "📚 LNG Training":
    st.header("📚 Interactive LNG Training Modules")
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["🏭 Production", "🚢 Transportation", "📋 Commercial", "⚠️ Risk Management"]
    )
    
    with tab1:
        st.subheader("LNG Production & Value Chain")
        
        with st.expander("Module 1: Gas Treatment & Liquefaction"):
            st.write("""
            **Proses Liquefaction:**
            1. **Pre-treatment**: Removal of CO2, H2S, Mercury
            2. **Dehydration**: Water removal to prevent ice formation
            3. **Liquefaction**: Cooling to -162°C
            4. **Storage**: Insulated tanks at atmospheric pressure
            
            **Key Technologies:**
            - C3MR (Propane Pre-cooled Mixed Refrigerant)
            - AP-X (Air Products Process)
            - CASCADE Process
            - DMR (Dual Mixed Refrigerant)
            """)
            
            if st.button("📝 Take Quiz - Module 1"):
                st.info("Premium feature - Upgrade untuk akses quiz interaktif!")
        
        with st.expander("Module 2: Small-Scale LNG Technologies"):
            st.write("""
            **Aplikasi Small-Scale LNG di Indonesia:**
            - Power generation untuk daerah terpencil
            - Bunkering untuk kapal
            - Trucking LNG untuk industri
            - Peak shaving untuk utilitas gas
            
            **Keuntungan Ekonomis:**
            - CAPEX lebih rendah (30-50% dari large-scale)
            - Faster time to market (2-3 tahun)
            - Modular expansion capability
            """)
    
    with tab2:
        st.subheader("LNG Transportation & Logistics")
        st.info("🔒 Premium Content - Upgrade untuk akses penuh!")
        
    with tab3:
        st.subheader("Commercial & Legal Aspects")
        st.info("🔒 Premium Content - Upgrade untuk akses penuh!")
        
    with tab4:
        st.subheader("Risk Management")
        st.info("🔒 Premium Content - Upgrade untuk akses penuh!")

# Project Calculator
elif menu == "💰 Project Calculator":
    st.header("💰 LNG Project Feasibility Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Project Parameters")
        capacity = st.number_input("Plant Capacity (MTPA)", 0.1, 10.0, 1.0, 0.1)
        capex_per_ton = st.number_input("CAPEX ($/ton)", 100, 1000, 600, 50)
        opex_percent = st.slider("OPEX (% of CAPEX)", 1, 10, 3)
        lng_price = st.number_input("LNG Selling Price ($/MMBtu)", 5.0, 20.0, 12.0, 0.5)
        gas_cost = st.number_input("Feed Gas Cost ($/MMBtu)", 1.0, 10.0, 3.0, 0.5)
        
    with col2:
        st.subheader("Financial Metrics")
        
        # Simple calculations
        total_capex = capacity * capex_per_ton * 1_000_000
        annual_opex = total_capex * (opex_percent / 100)
        annual_revenue = capacity * 1_000_000 * 52 * lng_price  # Simplified
        annual_feedgas = capacity * 1_000_000 * 52 * gas_cost
        annual_profit = annual_revenue - annual_opex - annual_feedgas
        payback = total_capex / annual_profit if annual_profit > 0 else 999
        
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            st.metric("Total CAPEX", f"${total_capex/1_000_000:.1f}M")
            st.metric("Annual Revenue", f"${annual_revenue/1_000_000:.1f}M")
        with col2_2:
            st.metric("Annual Profit", f"${annual_profit/1_000_000:.1f}M")
            st.metric("Payback Period", f"{payback:.1f} years")
        
        if st.button("📊 Generate Detailed Report"):
            st.success("Report generated! Download link akan dikirim ke email.")
            st.info("💡 Upgrade ke Premium untuk instant download!")

# Market Analysis
elif menu == "📊 Market Analysis":
    st.header("📊 LNG Market Analysis Indonesia")
    
    tab1, tab2, tab3 = st.tabs(["Supply & Demand", "Price Forecast", "Competitor Analysis"])
    
    with tab1:
        st.subheader("Indonesia LNG Supply-Demand Balance")
        
        years = list(range(2020, 2031))
        supply = [7.5, 7.8, 8.0, 8.2, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5]
        demand = [3.5, 4.0, 4.5, 5.2, 6.0, 7.0, 8.5, 10.0, 11.5, 13.0, 14.5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=supply, mode='lines+markers', name='Supply', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=years, y=demand, mode='lines+markers', name='Demand', line=dict(color='red')))
        fig.update_layout(
            title="Indonesia LNG Supply vs Demand Projection",
            xaxis_title="Year",
            yaxis_title="Volume (MTPA)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Key Insights:**
        - Demand akan melebihi supply mulai 2027
        - Peluang untuk small-scale LNG & import terminal
        - Focus pada Eastern Indonesia development
        """)

# Opportunity Tracker
elif menu == "🎯 Opportunity Tracker":
    st.header("🎯 LNG Project Opportunities")
    
    opportunities = pd.DataFrame({
        'Project': ['Tangguh Train 4', 'Abadi LNG', 'Masela FLNG', 'Mini LNG Sulawesi', 'LNG Bunkering Batam'],
        'Type': ['Upstream', 'Upstream', 'FLNG', 'Small-Scale', 'Infrastructure'],
        'Value': ['$8B', '$20B', '$15B', '$200M', '$50M'],
        'Stage': ['FEED', 'Pre-FEED', 'Planning', 'Tender', 'Construction'],
        'Timeline': ['2027', '2029', '2028', '2026', '2025']
    })
    
    st.dataframe(opportunities, use_container_width=True)
    
    st.subheader("🔔 Tender Alerts")
    st.info("Subscribe to Premium untuk real-time tender notifications!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>© 2025 Sustraco Energy - LNG Business Intelligence Platform</p>
    <p>Powered by AI | Contact: info@sustracoenergy.com</p>
</div>
""", unsafe_allow_html=True)
