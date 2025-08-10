# app.py - LNG Business Intelligence Platform with AI Assistant
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import random
import time

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
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    .stMetric {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        animation: fadeIn 0.5s ease;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .user-message {
        background: #E3F2FD;
        margin-left: 20%;
    }
    .bot-message {
        background: #F3E5F5;
        margin-right: 20%;
    }
</style>
""", unsafe_allow_html=True)

# AI Assistant Module (Simulated - No API Key Required)
class LNGAssistant:
    def __init__(self):
        self.knowledge_base = {
            "lng basics": {
                "temperature": "-162°C",
                "volume_reduction": "600:1",
                "composition": "85-95% methane, ethane, propane, butane",
                "energy_content": "~50 MJ/kg"
            },
            "indonesia_projects": {
                "tangguh": {"capacity": "11.4 MTPA", "location": "Papua Barat", "operator": "BP"},
                "bontang": {"capacity": "22.6 MTPA", "location": "Kalimantan Timur", "operator": "Pertamina"},
                "donggi_senoro": {"capacity": "2.0 MTPA", "location": "Sulawesi Tengah", "operator": "Sulawesi LNG"}
            },
            "technologies": {
                "C3MR": "Most common for large-scale, 65% of global capacity",
                "AP-X": "Air Products technology, used in Qatar",
                "DMR": "Shell technology, efficient for offshore",
                "PRICO": "Good for small-scale, <1 MTPA"
            }
        }
    
    def generate_response(self, query):
        query_lower = query.lower()
        
        # Context-based responses
        if "price" in query_lower or "jkm" in query_lower:
            current_price = 12.85 + random.uniform(-0.5, 0.5)
            return f"""📊 **LNG Market Price Analysis**
            
Current JKM (Japan Korea Marker) Price: ${current_price:.2f}/MMBtu
- Weekly change: {random.uniform(-5, 5):.1f}%
- Monthly trend: {'Bullish' if random.random() > 0.5 else 'Bearish'}

**Key Factors:**
- Winter demand from North Asia
- European gas storage levels at {random.randint(75, 95)}%
- New supply from US Gulf Coast projects

**Recommendation:** {'Consider locking in contracts' if current_price < 13 else 'Wait for better pricing'}"""

        elif "small scale" in query_lower or "mini lng" in query_lower:
            return """🏭 **Small-Scale LNG Solutions for Indonesia**

**Optimal Applications:**
- **Power Generation**: 1-25 MW untuk pulau terpencil
- **Industrial**: Textile, food processing, ceramics
- **Marine Bunkering**: Growing market in Batam/Surabaya

**Economics (untuk 0.5 MTPA plant):**
- CAPEX: $150-200 million
- OPEX: 3-4% of CAPEX annually
- Payback: 5-7 years dengan PLN PPA

**Teknologi Recommended:**
- PRICO process untuk <1 MTPA
- ISO containers untuk distribusi
- Virtual pipeline untuk last-mile

**Success Case:** Mini LNG Pesanggaran di Bali - supplying 6 hotels & 2 hospitals"""

        elif "tangguh" in query_lower or "abadi" in query_lower:
            return """🚀 **Indonesia Major LNG Projects Update**

**Tangguh Train 3:**
- Status: Operational since 2025
- Added capacity: 3.8 MTPA
- Total Tangguh: 11.4 MTPA
- Investment: $8 billion

**Abadi LNG (Masela):**
- Status: FEED completion 2025
- Planned capacity: 9.5 MTPA
- FID target: 2026
- First gas: 2030
- Investment: ~$20 billion

**Market Impact:**
- Strengthens Indonesia's LNG position
- Supports domestic gas needs
- Enhances energy security untuk Eastern Indonesia"""

        elif "regulation" in query_lower or "skk" in query_lower:
            return """⚖️ **Indonesian LNG Regulatory Framework**

**Key Regulators:**
- **SKK Migas**: Upstream regulation & PSC management
- **BPH Migas**: Downstream & distribution
- **ESDM**: Policy & licensing

**Important Regulations:**
- PP 35/2004: Natural gas business activities
- Permen ESDM 3/2010: Domestic market obligation (DMO)
- New Presidential Reg 2025: LNG allocation priorities

**DMO Requirements:**
- 25% minimum untuk domestic market
- Price formula: Linked to ICP
- Priority sectors: Fertilizer, Power, Petrochemical"""

        else:
            return f"""🤖 **LNG Intelligence Assistant Response**

Saya memahami Anda bertanya tentang: *{query}*

**Quick Insights:**
- Indonesia LNG capacity: ~30 MTPA (existing)
- Domestic demand growth: 8-10% annually
- Key opportunity: Small-scale LNG untuk 3T regions

**Recommended Actions:**
1. Analyze specific project economics
2. Review regulatory compliance
3. Assess market demand in target area

💡 **Tips:** Coba tanyakan tentang:
- "JKM price forecast"
- "Small scale LNG economics"
- "Tangguh expansion update"
- "Indonesian LNG regulations"

Butuh analisis lebih detail? Upgrade ke Premium untuk akses penuh!"""

# Header
st.markdown('<h1 class="main-header">🔥 LNG Business Intelligence Platform</h1>', unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/1E3A8A/FFFFFF?text=Sustraco+Energy", width=300)
    st.markdown("---")
    
    menu = st.radio(
        "🧭 Navigation",
        ["🏠 Dashboard", "🤖 AI Assistant", "📚 LNG Training", 
         "💰 Project Calculator", "📊 Market Analysis", "🎯 Opportunity Tracker"]
    )
    
    st.markdown("---")
    st.success("✅ System Online")
    st.info("💡 **Pro Tip**: Chat dengan AI Assistant untuk insights real-time!")

# Dashboard Page
if menu == "🏠 Dashboard":
    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("JKM Price ($/MMBtu)", "12.85", "+0.35", delta_color="normal")
    with col2:
        st.metric("Brent Oil ($/bbl)", "78.45", "-1.20", delta_color="inverse")
    with col3:
        st.metric("Active Projects", "156", "+12")
    with col4:
        st.metric("Indonesia Demand (MTPA)", "8.5", "+15%")
    
    st.markdown("---")
    
    # Charts with tabs
    tab1, tab2, tab3 = st.tabs(["📈 Price Trends", "🌏 Regional Analysis", "📊 Market Forecast"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("LNG vs Oil Price Correlation")
            dates = pd.date_range(end=datetime.now(), periods=60)
            lng_prices = [12 + i*0.05 + random.uniform(-0.5, 0.5) for i in range(60)]
            oil_prices = [75 + i*0.03 + random.uniform(-2, 2) for i in range(60)]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=lng_prices, mode='lines', name='LNG ($/MMBtu)', 
                                    line=dict(color='#667eea', width=2)))
            fig.add_trace(go.Scatter(x=dates, y=[p/6 for p in oil_prices], mode='lines', 
                                    name='Oil/6 ($/MMBtu eq)', line=dict(color='#764ba2', width=2)))
            fig.update_layout(height=350, hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Price Volatility Index")
            categories = ['Daily', 'Weekly', 'Monthly', 'Quarterly']
            volatility = [8.5, 15.2, 22.1, 18.5]
            
            fig = go.Figure(go.Bar(x=categories, y=volatility, 
                                  marker_color=['#667eea', '#764ba2', '#f093fb', '#f5576c']))
            fig.update_layout(height=350)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Asia-Pacific LNG Demand Forecast")
        
        countries = ['China', 'Japan', 'Korea', 'India', 'Taiwan', 'Indonesia']
        current = [85, 70, 45, 30, 18, 8.5]
        forecast_2030 = [130, 65, 42, 55, 20, 14.5]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name='2025', x=countries, y=current, marker_color='#667eea'))
        fig.add_trace(go.Bar(name='2030F', x=countries, y=forecast_2030, marker_color='#764ba2'))
        fig.update_layout(barmode='group', height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Supply & Demand Balance Projection")
        
        years = list(range(2020, 2031))
        supply = [7.5, 7.8, 8.0, 8.2, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5]
        demand = [3.5, 4.0, 4.5, 5.2, 6.0, 7.0, 8.5, 10.0, 11.5, 13.0, 14.5]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=supply, mode='lines+markers', name='Supply',
                                line=dict(color='green', width=3), marker=dict(size=8)))
        fig.add_trace(go.Scatter(x=years, y=demand, mode='lines+markers', name='Demand',
                                line=dict(color='red', width=3), marker=dict(size=8)))
        fig.add_trace(go.Scatter(x=years, y=[s-d for s,d in zip(supply, demand)],
                                mode='lines', name='Balance', line=dict(color='blue', dash='dash')))
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)

# AI Assistant Page
elif menu == "🤖 AI Assistant":
    st.header("🤖 LNG Intelligence AI Assistant")
    st.markdown("Tanyakan apapun tentang LNG business, market analysis, atau technical aspects!")
    
    # Initialize AI Assistant
    assistant = LNGAssistant()
    
    # Chat Interface
    col1, col2 = st.columns([3, 1])
    with col1:
        user_input = st.text_input("💬 Your Question:", placeholder="e.g., What's the current JKM price trend?")
    with col2:
        send_button = st.button("Send 📤", type="primary", use_container_width=True)
    
    if send_button and user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Generate AI response
        with st.spinner("🤔 Analyzing..."):
            time.sleep(1)  # Simulate processing
            response = assistant.generate_response(user_input)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("### 💬 Conversation History")
        for message in st.session_state.chat_history[-5:]:  # Show last 5 messages
            if message["role"] == "user":
                st.markdown(f'<div class="chat-message user-message">👤 {message["content"]}</div>', 
                          unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message bot-message">🤖 {message["content"]}</div>', 
                          unsafe_allow_html=True)
    
    # Quick Questions
    st.markdown("### 🚀 Quick Questions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 JKM Price Analysis"):
            response = assistant.generate_response("What is the current JKM price?")
            st.info(response)
    
    with col2:
        if st.button("🏭 Small-Scale LNG"):
            response = assistant.generate_response("Tell me about small scale LNG")
            st.info(response)
    
    with col3:
        if st.button("📋 Regulations"):
            response = assistant.generate_response("Indonesian LNG regulations")
            st.info(response)

# LNG Training Module  
elif menu == "📚 LNG Training":
    st.header("📚 Interactive LNG Training Modules")
    
    # Progress Tracker
    progress = st.container()
    with progress:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Modules Completed", "2/10", "20%")
        with col2:
            st.metric("Quiz Score", "85%", "+5%")
        with col3:
            st.metric("Certificate Progress", "40%", "+10%")
    
    st.markdown("---")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🏭 Production", "🚢 Transportation", "📋 Commercial", "⚠️ Risk", "🎓 Quiz"]
    )
    
    with tab1:
        st.subheader("Module 1: LNG Production & Value Chain")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.expander("📖 1.1 Gas Treatment & Pre-Processing", expanded=True):
                st.markdown("""
                **Learning Objectives:**
                - Understand feed gas requirements
                - Master contamination removal processes
                - Calculate treatment efficiency
                
                **Content:**
                
                🔬 **Feed Gas Specification Requirements:**
                - CO₂: < 50 ppmv (prevents dry ice formation)
                - H₂S: < 4 ppmv (prevents corrosion)
                - Mercury: < 0.01 μg/Nm³ (prevents aluminum heat exchanger damage)
                - Water: < 1 ppmv (prevents hydrate formation)
                
                ⚙️ **Treatment Technologies:**
                1. **Acid Gas Removal (AGR)**
                   - Amine absorption (MEA, DEA, MDEA)
                   - Physical solvents (Selexol, Rectisol)
                   - Membrane separation
                
                2. **Dehydration**
                   - Molecular sieves (most common)
                   - Glycol absorption (TEG)
                   
                3. **Mercury Removal**
                   - Activated carbon beds
                   - Metal sulfide adsorbents
                """)
                
                if st.button("▶️ Watch Video Tutorial", key="video1"):
                    st.info("🎥 Video tutorial akan tersedia di Premium version")
        
        with col2:
            st.info("📊 **Module Stats**")
            st.progress(0.3, text="30% Complete")
            st.metric("Time Spent", "45 min")
            st.metric("Last Access", "Today")
            
            st.success("🏆 **Achievements**")
            st.write("✅ Basics Completed")
            st.write("⏳ Advanced In Progress")

    with tab5:
        st.subheader("🎓 Knowledge Assessment Quiz")
        
        score = 0
        
        q1 = st.radio(
            "1. What is the liquefaction temperature of LNG?",
            ["−142°C", "−152°C", "−162°C", "−172°C"]
        )
        if q1 == "−162°C":
            score += 1
        
        q2 = st.multiselect(
            "2. Which are common liquefaction technologies? (Select all)",
            ["C3MR", "AP-X", "CASCADE", "OSMOSIS"]
        )
        if set(q2) == {"C3MR", "AP-X", "CASCADE"}:
            score += 1
        
        q3 = st.select_slider(
            "3. Typical CO₂ limit in feed gas (ppmv):",
            options=[10, 50, 100, 500, 1000]
        )
        if q3 == 50:
            score += 1
        
        if st.button("📝 Submit Quiz", type="primary"):
            st.balloons()
            percentage = (score/3)*100
            if percentage >= 70:
                st.success(f"🎉 Excellent! Score: {percentage:.0f}%")
            else:
                st.warning(f"📚 Keep studying! Score: {percentage:.0f}%")

# Project Calculator
elif menu == "💰 Project Calculator":
    st.header("💰 Advanced LNG Project Feasibility Calculator")
    
    # Input tabs
    tab1, tab2, tab3 = st.tabs(["📊 Basic Parameters", "⚙️ Technical Specs", "💵 Financial Model"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Plant Configuration")
            plant_type = st.selectbox("Plant Type", ["Onshore", "FLNG", "Small-Scale"])
            capacity = st.number_input("Capacity (MTPA)", 0.1, 20.0, 2.0, 0.1)
            location = st.selectbox("Location", ["Western Indonesia", "Eastern Indonesia", "Offshore"])
        
        with col2:
            st.subheader("Cost Parameters")
            if plant_type == "Small-Scale":
                capex_default = 300
            elif plant_type == "FLNG":
                capex_default = 800
            else:
                capex_default = 600
            
            capex_per_ton = st.number_input("CAPEX ($/tpa)", 100, 1500, capex_default, 50)
            opex_percent = st.slider("OPEX (% of CAPEX)", 1.0, 10.0, 3.5, 0.5)
            
        with col3:
            st.subheader("Market Prices")
            lng_price = st.number_input("LNG Price ($/MMBtu)", 5.0, 25.0, 12.85, 0.5)
            gas_cost = st.number_input("Feed Gas ($/MMBtu)", 1.0, 10.0, 3.5, 0.5)
            carbon_price = st.number_input("Carbon Credit ($/ton CO2)", 0.0, 50.0, 10.0, 1.0)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Technical Specifications")
            efficiency = st.slider("Plant Efficiency (%)", 80, 95, 90)
            availability = st.slider("Availability Factor (%)", 85, 98, 95)
            rampup_years = st.number_input("Ramp-up Period (years)", 1, 3, 2)
        
        with col2:
            st.subheader("Environmental")
            co2_intensity = st.number_input("CO2 Intensity (ton/ton LNG)", 0.1, 0.5, 0.25, 0.05)
            renewable_percent = st.slider("Renewable Power (%)", 0, 100, 20)
    
    with tab3:
        st.subheader("📈 Financial Analysis Results")
        
        # Calculations
        total_capex = capacity * capex_per_ton * 1_000_000
        annual_opex = total_capex * (opex_percent / 100)
        
        # Adjusted for efficiency and availability
        effective_capacity = capacity * (efficiency/100) * (availability/100)
        annual_production = effective_capacity * 1_000_000
        
        # Revenue calculations
        lng_revenue = annual_production * 52 * lng_price
        carbon_revenue = co2_intensity * annual_production * carbon_price * (renewable_percent/100)
        total_revenue = lng_revenue + carbon_revenue
        
        # Cost calculations  
        feedgas_cost = annual_production * 52 * gas_cost * 1.05  # 5% shrinkage
        total_cost = annual_opex + feedgas_cost
        
        # Profitability
        ebitda = total_revenue - total_cost
        ebitda_margin = (ebitda / total_revenue * 100) if total_revenue > 0 else 0
        payback = total_capex / ebitda if ebitda > 0 else 999
        
        # IRR approximation
        irr_estimate = (ebitda / total_capex) * 100 if total_capex > 0 else 0
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total CAPEX", f"${total_capex/1_000_000:.0f}M")
            st.metric("Annual OPEX", f"${annual_opex/1_000_000:.1f}M")
        
        with col2:
            st.metric("Annual Revenue", f"${total_revenue/1_000_000:.0f}M")
            st.metric("EBITDA", f"${ebitda/1_000_000:.0f}M")
        
        with col3:
            st.metric("EBITDA Margin", f"{ebitda_margin:.1f}%")
            st.metric("Payback Period", f"{payback:.1f} years")
        
        with col4:
            st.metric("IRR Estimate", f"{irr_estimate:.1f}%")
            feasible = "✅ Feasible" if irr_estimate > 12 else "⚠️ Review Required"
            st.metric("Project Status", feasible)
        
        # Sensitivity Analysis
        st.markdown("---")
        st.subheader("📊 Sensitivity Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # LNG Price Sensitivity
            price_range = [p for p in range(8, 18)]
            irr_by_price = [(((annual_production * 52 * p + carbon_revenue) - total_cost) / total_capex * 100) 
                           for p in price_range]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=price_range, y=irr_by_price, mode='lines+markers',
                                    line=dict(color='#667eea', width=3)))
            fig.add_hline(y=12, line_dash="dash", line_color="red", 
                         annotation_text="Min IRR Threshold")
            fig.update_layout(title="IRR vs LNG Price", 
                            xaxis_title="LNG Price ($/MMBtu)",
                            yaxis_title="IRR (%)", height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # CAPEX Sensitivity
            capex_range = [c for c in range(300, 900, 50)]
            payback_by_capex = [(capacity * c * 1_000_000) / ebitda if ebitda > 0 else 999 
                               for c in capex_range]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=capex_range, y=payback_by_capex,
                               marker_color='#764ba2'))
            fig.add_hline(y=7, line_dash="dash", line_color="red",
                         annotation_text="Max Payback Target")
            fig.update_layout(title="Payback vs CAPEX",
                            xaxis_title="CAPEX ($/tpa)",
                            yaxis_title="Payback (years)", height=350)
            st.plotly_chart(fig, use_container_width=True)
        
        # Export Report
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Generate PDF Report", type="primary", use_container_width=True):
                st.success("✅ Report generated! Check your email.")
        
        with col2:
            if st.button("📊 Export to Excel", type="secondary", use_container_width=True):
                st.info("📥 Excel file will be downloaded...")
        
        with col3:
            if st.button("📧 Share Analysis", use_container_width=True):
                st.info("🔗 Shareable link copied!")

# Market Analysis
elif menu == "📊 Market Analysis":
    st.header("📊 Comprehensive LNG Market Analysis")
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["🌏 Regional Markets", "📈 Price Analytics", "🏭 Supply Chain", "🔮 Forecasting"]
    )
    
    with tab1:
        st.subheader("Asia-Pacific LNG Market Overview")
        
        # Interactive Map Placeholder
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Market share pie chart
            labels = ['Japan', 'China', 'South Korea', 'India', 'Taiwan', 'Others']
            values = [27, 32, 17, 11, 7, 6]
            
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
            fig.update_traces(hoverinfo='label+percent', textinfo='value+percent',
                            marker=dict(colors=px.colors.sequential.Plasma))
            fig.update_layout(title="2025 Asia-Pacific LNG Import Market Share", height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.info("🌏 **Market Highlights**")
            st.metric("Total Imports", "380 MTPA", "+5.2%")
            st.metric("Average Price", "$12.85/MMBtu", "+$0.35")
            st.metric("Spot vs Term", "35% / 65%")
            
            st.success("**Growth Drivers:**")
            st.write("• Coal-to-gas switching")
            st.write("• Industrial demand recovery")
            st.write("• New power plants")

# Opportunity Tracker
elif menu == "🎯 Opportunity Tracker":
    st.header("🎯 LNG Project Opportunity Tracker")
    
    # Filters
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        project_type = st.multiselect("Project Type", 
                                     ["Upstream", "Midstream", "Downstream", "FLNG", "Small-Scale"],
                                     default=["Upstream", "Small-Scale"])
    with col2:
        investment_range = st.select_slider("Investment Size",
                                           options=["<$100M", "$100M-500M", "$500M-1B", ">$1B"],
                                           value="$100M-500M")
    with col3:
        stage = st.multiselect("Project Stage",
                              ["Pre-FEED", "FEED", "FID", "Construction", "Commissioning"],
                              default=["FEED", "FID"])
    with col4:
        region = st.selectbox("Region", ["All Indonesia", "Western", "Central", "Eastern"])
    
    st.markdown("---")
    
    # Opportunities Table
    opportunities_data = {
        'Project': ['Tangguh Train 4', 'Abadi LNG', 'Mini LNG Lombok', 'Bali LNG Terminal', 
                   'Sulawesi Gas Pipeline', 'Java FSRU-3', 'Batam Bunkering Hub'],
        'Type': ['Upstream', 'Upstream', 'Small-Scale', 'Terminal', 'Midstream', 'FSRU', 'Infrastructure'],
        'Investment': ['$3.5B', '$19B', '$180M', '$450M', '$1.2B', '$200M', '$65M'],
        'Stage': ['Construction', 'FEED', 'FID', 'Pre-FEED', 'FEED', 'Commissioning', 'Construction'],
        'Completion': ['2026', '2030', '2026', '2028', '2027', '2025', '2025'],
        'IRR Est.': ['15%', '14%', '18%', '16%', '12%', '20%', '22%'],
        'Risk Level': ['Low', 'Medium', 'Low', 'Medium', 'High', 'Low', 'Low']
    }
    
    df = pd.DataFrame(opportunities_data)
    
    # Styled dataframe
    def color_risk(val):
        if val == 'Low':
            color = 'background-color: #90EE90'
        elif val == 'Medium':
            color = 'background-color: #FFD700'
        else:
            color = 'background-color: #FFB6C1'
        return color
    
    styled_df = df.style.applymap(color_risk, subset=['Risk Level'])
    st.dataframe(styled_df, use_container_width=True, height=300)
    
    # Opportunity Details
    st.markdown("---")
    selected_project = st.selectbox("Select Project for Details", df['Project'].tolist())
    
    if selected_project:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(f"📋 {selected_project} - Detailed Analysis")
            
            # Project details (simulated)
            st.markdown(f"""
            **Executive Summary:**
            {selected_project} represents a strategic opportunity in Indonesia's LNG sector with 
            strong fundamentals and attractive returns.
            
            **Key Highlights:**
            • Strategic location with access to gas reserves
            • Strong offtake agreements in negotiation
            • Government support through fiscal incentives
            • Environmental compliance with latest standards
            
            **Commercial Structure:**
            • Contract type: Tolling / Merchant hybrid
            • Offtake: 70% contracted, 30% spot
            • Payment terms: LC-backed with credit enhancement
            
            **Next Steps:**
            1. Complete technical due diligence
            2. Finalize financing structure
            3. Secure remaining permits
            4. Target FID by Q3 2025
            """)
        
        with col2:
            st.info("📊 **Quick Metrics**")
            
            project_idx = df[df['Project'] == selected_project].index[0]
            st.metric("Investment Required", df.loc[project_idx, 'Investment'])
            st.metric("Expected IRR", df.loc[project_idx, 'IRR Est.'])
            st.metric("Risk Assessment", df.loc[project_idx, 'Risk Level'])
            st.metric("Target Completion", df.loc[project_idx, 'Completion'])
            
            st.success("**Your Match Score: 85%**")
            st.progress(0.85, text="Based on your profile")
            
            if st.button("📞 Connect with Project Team", type="primary", use_container_width=True):
                st.success("✅ Connection request sent!")
                st.info("Team akan menghubungi Anda dalam 24 jam")

# Footer
st.markdown("---")

# Newsletter Subscription
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    email = st.text_input("", placeholder="Enter email for weekly insights", label_visibility="collapsed")

with col2:
    if st.button("Subscribe to LNG Intelligence", type="primary", use_container_width=True):
        if email:
            st.success("✅ Subscribed successfully!")
        else:
            st.error("Please enter your email")

with col3:
    st.markdown("📧 **5,000+ subscribers**")

st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; border-radius: 15px; margin-top: 2rem;'>
    <h3>🚀 Upgrade to Premium</h3>
    <p>Unlock full access to all features, real-time data, and expert consultations</p>
    <p style='font-size: 1.5rem; font-weight: bold;'>Special Offer: Rp 1.499.000/month</p>
    <p style='text-decoration: line-through;'>Normal Price: Rp 2.000.000/month</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; color: #666; margin-top: 3rem;'>
    <p>© 2025 Sustraco Energy - LNG Business Intelligence Platform</p>
    <p>Powered by Advanced AI | Contact: info@sustracoenergy.com | WhatsApp: +62 812-3456-7890</p>
    <p>Jakarta • Singapore • Houston</p>
</div>
""", unsafe_allow_html=True)
