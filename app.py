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
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .chat-message {
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 8px;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .bot-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🔥 LNG Business Intelligence Platform</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🏢 Sustraco Energy")
    st.markdown("**AI-Powered LNG Analytics**")
    st.markdown("---")
    
    menu = st.radio(
        "📋 Navigation",
        ["🏠 Dashboard", "🤖 AI Assistant", "📚 Training", "💰 Calculator"]
    )
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    st.metric("System Status", "🟢 Online", "100%")
    st.metric("Data Update", "Real-time", "✅")

# Main Content
if menu == "🏠 Dashboard":
    st.markdown("## 📊 Real-Time LNG Market Dashboard")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="JKM Price ($/MMBtu)",
            value="$12.85",
            delta="+0.35 (+2.8%)"
        )
    
    with col2:
        st.metric(
            label="Brent Oil ($/bbl)",
            value="$78.45",
            delta="-1.20 (-1.5%)"
        )
    
    with col3:
        st.metric(
            label="Active Projects",
            value="156",
            delta="+12 new"
        )
    
    with col4:
        st.metric(
            label="ID Demand (MTPA)",
            value="8.5",
            delta="+15% YoY"
        )
    
    st.markdown("---")
    
    # Charts Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 LNG Price Trend (30 Days)")
        
        # Generate sample data
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        base_price = 12.5
        prices = [base_price + i*0.02 + random.uniform(-0.3, 0.3) for i in range(30)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates, 
            y=prices, 
            mode='lines+markers',
            name='JKM Price',
            line=dict(color='#667eea', width=3),
            marker=dict(size=4)
        ))
        
        fig.update_layout(
            height=350,
            margin=dict(l=0, r=0, t=20, b=0),
            xaxis_title="Date",
            yaxis_title="Price ($/MMBtu)",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🌏 Regional LNG Demand (MTPA)")
        
        countries = ['Japan', 'China', 'South Korea', 'India', 'Indonesia', 'Thailand']
        demand = [70.5, 85.2, 45.8, 30.1, 8.5, 6.2]
        
        fig = px.bar(
            x=countries, 
            y=demand,
            color=demand,
            color_continuous_scale='viridis',
            title=""
        )
        
        fig.update_layout(
            height=350,
            margin=dict(l=0, r=0, t=20, b=0),
            xaxis_title="Country",
            yaxis_title="Demand (MTPA)",
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Market Insights
    st.markdown("### 💡 Market Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **🔥 Hot Topics**
        - Winter demand surge in North Asia
        - New Indonesia small-scale projects
        - Supply chain optimization
        """)
    
    with col2:
        st.success("""
        **📈 Opportunities**
        - Eastern Indonesia expansion
        - Small-scale LNG growth
        - Green LNG initiatives
        """)
    
    with col3:
        st.warning("""
        **⚠️ Watch Points**
        - Regulatory changes
        - Price volatility
        - Infrastructure bottlenecks
        """)

elif menu == "🤖 AI Assistant":
    st.markdown("## 🤖 LNG AI Assistant")
    st.markdown("*Ask me anything about LNG markets, projects, or technical aspects*")
    
    # AI Response Function
    def get_ai_response(question):
        responses = {
            "price": "Current JKM price is $12.85/MMBtu, up $0.35 from yesterday. Winter demand from North Asia and supply constraints are driving prices higher. Technical resistance at $13.50.",
            
            "small scale": "Small-scale LNG (0.1-1 MTPA) is perfect for Indonesia's archipelago. Typical CAPEX: $300-500M, OPEX: 3-4% annually. ROI: 12-15% with proper gas supply agreements.",
            
            "regulation": "Key Indonesian regulators: SKK Migas (upstream), BPH Migas (downstream), MEMR (policy). New regulation requires 25% DMO for domestic supply security.",
            
            "tangguh": "Tangguh Train 3 operational since Q1 2025, adding 3.8 MTPA capacity. Total Tangguh capacity now 11.4 MTPA. Train 4 construction 75% complete, targeting Q4 2026.",
            
            "demand": "Indonesia LNG demand projected to reach 14.5 MTPA by 2030, driven by power generation and industrial growth. Current gap: 6 MTPA by 2027.",
            
            "projects": "156 active LNG projects in Indonesia pipeline. Key focuses: small-scale (45%), infrastructure (30%), upstream (25%). Total investment: $28.5B.",
            
            "default": "I'm your LNG expert! Ask me about: 'price analysis', 'small scale LNG', 'Indonesian regulations', 'Tangguh project', 'demand forecast', or 'project pipeline'."
        }
        
        question_lower = question.lower()
        for key in responses:
            if key in question_lower:
                return responses[key]
        return responses["default"]
    
    # Chat Interface
    with st.container():
        user_input = st.text_input(
            "💬 Your Question:", 
            placeholder="e.g., What's driving current LNG prices?",
            key="user_input"
        )
        
        col1, col2 = st.columns([1, 5])
        with col1:
            send_button = st.button("Send 🚀", type="primary")
        
        if send_button and user_input:
            response = get_ai_response(user_input)
            st.session_state.chat_history.append({
                "user": user_input, 
                "bot": response,
                "timestamp": datetime.now()
            })
            st.rerun()
    
    # Display Recent Chats
    if st.session_state.chat_history:
        st.markdown("### 💬 Recent Conversations")
        
        # Show last 3 conversations
        for chat in reversed(st.session_state.chat_history[-3:]):
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>👤 You:</strong> {chat['user']}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 AI:</strong> {chat['bot']}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
    
    # Quick Action Buttons
    st.markdown("### ⚡ Quick Questions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Price Analysis", use_container_width=True):
            response = get_ai_response("price")
            st.success(f"🤖 **AI Response:** {response}")
    
    with col2:
        if st.button("🏭 Small-Scale LNG", use_container_width=True):
            response = get_ai_response("small scale")
            st.success(f"🤖 **AI Response:** {response}")
    
    with col3:
        if st.button("📋 Regulations", use_container_width=True):
            response = get_ai_response("regulation")
            st.success(f"🤖 **AI Response:** {response}")

elif menu == "📚 Training":
    st.markdown("## 📚 LNG Training Hub")
    
    tab1, tab2, tab3 = st.tabs(["🏭 Production", "💼 Commercial", "⚖️ Regulatory"])
    
    with tab1:
        st.markdown("### LNG Production Fundamentals")
        
        with st.expander("📖 Module 1: Liquefaction Process", expanded=True):
            st.markdown("""
            **Core Process Steps:**
            1. **Pre-treatment**: Remove CO₂, H₂S, Mercury, and heavy hydrocarbons
            2. **Dehydration**: Eliminate water content to prevent ice formation
            3. **Liquefaction**: Cool natural gas to -162°C at atmospheric pressure
            4. **Storage**: Store in cryogenic, insulated tanks
            
            **Key Technologies:**
            - **C3MR (Mixed Refrigerant)**: Most common, 65% of global capacity
            - **AP-X**: Used in mega-projects like Qatar
            - **CASCADE**: Optimal for smaller plants (<1 MTPA)
            
            **Efficiency Metrics:**
            - Energy consumption: 8-12% of production
            - Typical plant availability: 95%+
            """)
        
        with st.expander("📖 Module 2: Small-Scale LNG Economics"):
            st.markdown("""
            **Market Applications:**
            - Power generation (1-25 MW)
            - Industrial fuel switching
            - Marine bunkering
            - Peak shaving
            
            **Economic Parameters:**
            - CAPEX: $300-500/tpa
            - OPEX: 3-4% of CAPEX annually
            - Typical payback: 5-7 years
            - Break-even: $6-8/MMBtu gas cost
            """)
    
    with tab2:
        st.markdown("### Commercial Structure")
        st.info("💎 **Premium Content** - Upgrade to access advanced commercial modules including pricing strategies, contract structures, and risk management.")
        
        if st.button("🔓 Unlock Premium", type="primary"):
            st.balloons()
            st.success("Contact us at: premium@sustracoenergy.com")
    
    with tab3:
        st.markdown("### Regulatory Framework")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Key Regulators:**
            - SKK Migas: Upstream operations
            - BPH Migas: Downstream & distribution
            - MEMR: Policy & strategic planning
            """)
        
        with col2:
            st.markdown("""
            **Compliance Requirements:**
            - DMO: 25% domestic allocation
            - Environmental: AMDAL approval
            - Safety: HSE compliance
            """)

elif menu == "💰 Calculator":
    st.markdown("## 💰 LNG Project Economics Calculator")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔧 Input Parameters")
        
        capacity = st.slider("Plant Capacity (MTPA)", 0.1, 5.0, 1.0, 0.1)
        capex_per_ton = st.slider("CAPEX ($/ton annually)", 300, 800, 500, 50)
        opex_percent = st.slider("OPEX (% of CAPEX)", 2.0, 6.0, 3.5, 0.5)
        
        st.markdown("**Market Prices**")
        lng_price = st.slider("LNG Selling Price ($/MMBtu)", 8.0, 20.0, 12.0, 0.5)
        gas_cost = st.slider("Feed Gas Cost ($/MMBtu)", 2.0, 8.0, 4.0, 0.5)
        
        # Load factor
        load_factor = st.slider("Plant Load Factor (%)", 80, 98, 90, 1)
    
    with col2:
        st.markdown("### 📊 Financial Results")
        
        # Calculations
        total_capex = capacity * capex_per_ton * 1_000_000
        annual_opex = total_capex * (opex_percent / 100)
        
        # Convert MTPA to MMBtu (1 ton LNG ≈ 48 MMBtu)
        annual_production = capacity * 1_000_000 * 48 * (load_factor / 100)
        
        annual_revenue = annual_production * lng_price
        annual_gas_cost = annual_production * gas_cost
        annual_profit = annual_revenue - annual_opex - annual_gas_cost
        
        payback_years = total_capex / annual_profit if annual_profit > 0 else 999
        roi = (annual_profit / total_capex) * 100 if total_capex > 0 else 0
        
        # Display metrics
        st.metric("Total CAPEX", f"${total_capex/1_000_000:.1f}M")
        st.metric("Annual Revenue", f"${annual_revenue/1_000_000:.1f}M")
        st.metric("Annual Profit", f"${annual_profit/1_000_000:.1f}M", f"{roi:.1f}% ROI")
        st.metric("Payback Period", f"{payback_years:.1f} years")
        
        # Cash flow chart
        years = list(range(1, 11))
        cumulative_cf = []
        cumulative = -total_capex
        
        for year in years:
            cumulative += annual_profit
            cumulative_cf.append(cumulative / 1_000_000)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=years, 
            y=cumulative_cf, 
            mode='lines+markers',
            name='Cumulative Cash Flow',
            line=dict(color='#667eea', width=3)
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="red")
        fig.update_layout(
            title="10-Year Cash Flow Projection",
            xaxis_title="Year",
            yaxis_title="Cumulative Cash Flow ($M)",
            height=300,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📧 Newsletter")
    email = st.text_input("Email Address", placeholder="your@email.com", label_visibility="collapsed")
    if st.button("Subscribe", use_container_width=True):
        if email and "@" in email:
            st.success("✅ Subscribed to LNG Market Updates!")
        else:
            st.error("Please enter a valid email")

with col2:
    st.markdown("### 💎 Premium Access")
    st.markdown("**Rp 1.499.000/month**")
    st.markdown("- Advanced analytics")
    st.markdown("- Real-time alerts")
    st.markdown("- Custom reports")
    if st.button("Upgrade Now", type="primary", use_container_width=True):
        st.info("📞 Contact: premium@sustracoenergy.com")

with col3:
    st.markdown("### 📞 Support")
    st.markdown("**WhatsApp:** +62 812-3456-7890")
    st.markdown("**Email:** info@sustracoenergy.com")
    st.markdown("**Office:** Jakarta • Singapore")

st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem; padding: 1rem; background-color: #f8f9fa; border-radius: 10px;'>
    <p><strong>© 2025 Sustraco Energy - LNG Business Intelligence Platform</strong></p>
    <p>Powered by AI • Real-time Data • Professional Analytics</p>
</div>
""", unsafe_allow_html=True)
