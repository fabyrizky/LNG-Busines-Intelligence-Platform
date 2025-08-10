# app.py - LNG Business Intelligence Platform
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

# Page Configuration
st.set_page_config(
    page_title="LNG Business Intelligence Platform",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: white;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .stMetric {
        background: white;
        padding: 0.5rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🔥 LNG Business Intelligence Platform</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🏢 Sustraco Energy")
    st.markdown("---")
    
    menu = st.radio(
        "Navigation",
        ["🏠 Dashboard", "🤖 AI Assistant", "📚 Training", "💰 Calculator", "📊 Analysis"]
    )
    
    st.markdown("---")
    st.success("✅ System Online")

# Dashboard
if menu == "🏠 Dashboard":
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("JKM Price", "$12.85", "+0.35")
    with col2:
        st.metric("Brent Oil", "$78.45", "-1.20")
    with col3:
        st.metric("Projects", "156", "+12")
    with col4:
        st.metric("ID Demand", "8.5 MTPA", "+15%")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 LNG Price Trend")
        dates = pd.date_range(end=datetime.now(), periods=30)
        prices = [12 + i*0.1 + random.uniform(-0.5, 0.5) for i in range(30)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='JKM'))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌏 Regional Demand")
        data = pd.DataFrame({
            'Country': ['Japan', 'China', 'Korea', 'India', 'Indonesia'],
            'Demand': [70, 85, 45, 30, 8.5]
        })
        fig = px.bar(data, x='Country', y='Demand', color='Demand')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

# AI Assistant
elif menu == "🤖 AI Assistant":
    st.header("🤖 LNG AI Assistant")
    
    # Simple Q&A System
    def get_ai_response(question):
        responses = {
            "price": "Current JKM price is $12.85/MMBtu, up $0.35 from last week. Winter demand from North Asia is driving prices higher.",
            "small scale": "Small-scale LNG (0.1-1 MTPA) is ideal for Indonesia's remote areas. CAPEX: $150-300M, Payback: 5-7 years with proper PPA.",
            "regulation": "Key regulators: SKK Migas (upstream), BPH Migas (downstream), ESDM (policy). DMO requirement: 25% for domestic market.",
            "tangguh": "Tangguh Train 3 operational since 2025, adding 3.8 MTPA. Total capacity now 11.4 MTPA. Train 4 under construction.",
            "default": "I can help with LNG pricing, projects, regulations, and technical aspects. Try asking about 'price', 'small scale LNG', or 'Tangguh project'."
        }
        
        question_lower = question.lower()
        for key in responses:
            if key in question_lower:
                return responses[key]
        return responses["default"]
    
    # Chat Interface
    user_input = st.text_input("Ask me about LNG:", placeholder="e.g., What's the current JKM price?")
    
    if st.button("Send", type="primary"):
        if user_input:
            # Add to history
            st.session_state.chat_history.append({"user": user_input, "bot": get_ai_response(user_input)})
    
    # Display chat
    if st.session_state.chat_history:
        for chat in st.session_state.chat_history[-3:]:  # Show last 3
            st.info(f"👤 You: {chat['user']}")
            st.success(f"🤖 AI: {chat['bot']}")
    
    # Quick buttons
    st.markdown("### Quick Questions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Price Analysis"):
            st.info(get_ai_response("price"))
    with col2:
        if st.button("🏭 Small-Scale"):
            st.info(get_ai_response("small scale"))
    with col3:
        if st.button("📋 Regulations"):
            st.info(get_ai_response("regulation"))

# Training
elif menu == "📚 Training":
    st.header("📚 LNG Training Modules")
    
    tab1, tab2, tab3 = st.tabs(["Production", "Commercial", "Risk"])
    
    with tab1:
        st.subheader("LNG Production")
        
        with st.expander("Module 1: Liquefaction Process"):
            st.write("""
            **Process Steps:**
            1. Pre-treatment: Remove CO2, H2S, Mercury
            2. Dehydration: Remove water
            3. Liquefaction: Cool to -162°C
            4. Storage: Insulated tanks
            
            **Technologies:**
            - C3MR: Most common (65% global)
            - AP-X: Used in Qatar
            - CASCADE: For smaller plants
            """)
        
        with st.expander("Module 2: Small-Scale LNG"):
            st.write("""
            **Applications:**
            - Power generation (1-25 MW)
            - Industrial fuel
            - Marine bunkering
            
            **Economics:**
            - CAPEX: $300-400/tpa
            - OPEX: 3-4% of CAPEX
            - Payback: 5-7 years
            """)
    
    with tab2:
        st.subheader("Commercial Aspects")
        st.info("Premium content - Upgrade for full access")
    
    with tab3:
        st.subheader("Risk Management")
        st.info("Premium content - Upgrade for full access")

# Calculator
elif menu == "💰 Calculator":
    st.header("💰 Project Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Parameters")
        capacity = st.slider("Capacity (MTPA)", 0.1, 10.0, 1.0)
        capex = st.slider("CAPEX ($/ton)", 200, 1000, 600)
        opex = st.slider("OPEX (% CAPEX)", 2, 8, 3)
        lng_price = st.slider("LNG Price ($/MMBtu)", 8, 20, 12)
        gas_cost = st.slider("Gas Cost ($/MMBtu)", 2, 8, 3)
    
    with col2:
        st.subheader("Results")
        
        # Simple calculations
        total_capex = capacity * capex * 1000000
        annual_opex = total_capex * (opex/100)
        annual_revenue = capacity * 1000000 * 52 * lng_price
        annual_cost = annual_opex + (capacity * 1000000 * 52 * gas_cost)
        profit = annual_revenue - annual_cost
        payback = total_capex / profit if profit > 0 else 999
        
        st.metric("CAPEX", f"${total_capex/1000000:.0f}M")
        st.metric("Annual Profit", f"${profit/1000000:.1f}M")
        st.metric("Payback", f"{payback:.1f} years")
        
        # Simple chart
        fig = go.Figure()
        years = list(range(1, 11))
        cumulative = [profit * y - total_capex for y in years]
        fig.add_trace(go.Scatter(x=years, y=cumulative, mode='lines+markers'))
        fig.add_hline(y=0, line_dash="dash")
        fig.update_layout(title="Cumulative Cash Flow", height=300)
        st.plotly_chart(fig, use_container_width=True)

# Analysis
elif menu == "📊 Analysis":
    st.header("📊 Market Analysis")
    
    tab1, tab2 = st.tabs(["Supply/Demand", "Projects"])
    
    with tab1:
        st.subheader("Indonesia LNG Balance")
        
        years = list(range(2020, 2031))
        supply = [7.5, 7.8, 8.0, 8.2, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5]
        demand = [3.5, 4.0, 4.5, 5.2, 6.0, 7.0, 8.5, 10.0, 11.5, 13.0, 14.5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=supply, mode='lines+markers', name='Supply'))
        fig.add_trace(go.Scatter(x=years, y=demand, mode='lines+markers', name='Demand'))
        fig.update_layout(title="Supply vs Demand Projection", height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Key Insights:**
        - Demand exceeds supply by 2027
        - Opportunity for small-scale LNG
        - Focus on Eastern Indonesia
        """)
    
    with tab2:
        st.subheader("Project Pipeline")
        
        projects = pd.DataFrame({
            'Project': ['Tangguh T4', 'Abadi', 'Mini Sulawesi', 'Batam Hub'],
            'Type': ['Upstream', 'Upstream', 'Small-Scale', 'Infrastructure'],
            'Value': ['$3.5B', '$19B', '$180M', '$65M'],
            'Timeline': ['2026', '2030', '2026', '2025']
        })
        
        st.dataframe(projects, use_container_width=True)
        
        # Simple pie chart
        values = [3.5, 19, 0.18, 0.065]
        labels = projects['Project'].tolist()
        
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title="Investment Distribution", height=300)
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📧 Subscribe")
    email = st.text_input("Email", placeholder="your@email.com", label_visibility="collapsed")
    if st.button("Subscribe"):
        if email:
            st.success("Subscribed!")

with col2:
    st.markdown("### 💼 Premium")
    st.markdown("Rp 1.499.000/month")
    if st.button("Upgrade Now"):
        st.info("Contact: info@sustracoenergy.com")

with col3:
    st.markdown("### 📞 Contact")
    st.markdown("WhatsApp: +62 812-3456-7890")
    st.markdown("Email: info@sustracoenergy.com")

st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    <p>© 2025 Sustraco Energy - LNG Business Intelligence Platform</p>
    <p>Jakarta • Singapore • Houston</p>
</div>
""", unsafe_allow_html=True)
