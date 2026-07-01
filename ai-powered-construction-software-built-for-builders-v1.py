import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Burst | AI-Powered Construction Software",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== DARK THEME CSS ======================
st.markdown("""
    <style>
    /* Main background - Dark */
    .stApp {
        background-color: #0F172A;
        color: #F1F5F9;
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #60A5FA;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .tagline {
        font-size: 1.5rem;
        color: #E2E8F0;
        text-align: center;
        font-style: italic;
    }

    /* Dark Cards with White Text */
    .module-card {
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        background-color: #1E2937;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s;
        color: #F1F5F9 !important;
    }
    .module-card h3 {
        color: #93C5FD !important;
    }
    .module-card p {
        color: #CBD5E1 !important;
    }

    /* Benefit Boxes */
    .benefit {
        background-color: #1E2937;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #60A5FA;
        color: #F1F5F9 !important;
    }

    /* General Text - White */
    .stMarkdown, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
    .stMarkdown h4, .stMarkdown p, .stMarkdown li, .stWrite {
        color: #F1F5F9 !important;
    }

    /* Sidebar - Dark */
    section[data-testid="stSidebar"] {
        background-color: #1E2937;
        color: #F1F5F9;
    }
    .stRadio label, .stSidebar .stMarkdown {
        color: #E2E8F0 !important;
    }

    /* Buttons & Success Messages */
    .stButton button {
        background-color: #3B82F6;
        color: white;
    }
    .stSuccess {
        background-color: #166534;
        color: #86EFAC;
    }
    .stInfo {
        background-color: #1E40AF;
        color: #BFDBFE;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://via.placeholder.com/150x50/60A5FA/0F172A?text=Burst", width=150)
st.sidebar.title("🚀 Burst")
st.sidebar.markdown("**AI-Powered Construction Software**")

page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📋 Core Modules",
    "⭐ Key Benefits",
    "🔨 Estimating",
    "💰 Financials",
    "📊 Project Management",
    "👥 Team & Subs",
    "💵 Pricing",
    "📞 Contact Us"
])

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">Burst Construction Software</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">AI-Powered Construction Software Built for Builders</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.image("https://via.placeholder.com/800x400/334155/F1F5F9?text=Burst+Dashboard+Preview", use_column_width=True)
        st.markdown("### Automate the everyday work of contractors")
        st.write("""
        From estimating to invoicing — Burst connects everything in one seamless platform. 
        Built specifically for residential contractors, remodelers, and small-to-mid-size general contractors.
        """)
    
    with col2:
        st.success("**Win more jobs • Save time • Boost profitability**")
        st.metric("Projects Managed", "1,247", "↑ 34%")
        st.metric("Average Time Saved", "18 hrs/week", "per user")
        st.metric("Profit Increase", "24%", "reported by users")
        
        if st.button("🚀 Start Free Trial", type="primary", use_container_width=True):
            st.balloons()
            st.success("Trial started! (Demo)")

    st.markdown("### Trusted by builders across the country")
    st.image("https://via.placeholder.com/800x120/475569/F1F5F9?text=Contractor+Logos+Row", use_column_width=True)

# ==================== CORE MODULES ====================
elif page == "📋 Core Modules":
    st.title("Core Solutions")
    st.write("Everything you need to run your construction business in one platform.")
    
    modules = [
        ("📋 Estimates", "Create and send professional estimates with AI"),
        ("📊 Budgets", "Effortless budgets with cashflow tracking"),
        ("📄 Invoices", "All-in-one invoicing tool"),
        ("📥 Bills", "Connect invoicing and budgeting seamlessly"),
        ("💸 Payments", "Pay and get paid with one click"),
        ("🔄 Change Orders", "Efficient management of project changes"),
        ("📸 Daily Logs", "Photo-based reporting with weather data"),
        ("⏱️ Time Tracking", "Track time per employee, job, and line item"),
        ("📈 Reporting", "Financial reporting and insights"),
        ("👷 Staff Management", "Role-based access and permissions"),
        ("🤝 Subcontractor Management", "Streamlined subcontractor workflows"),
        ("💰 Cost Tracking", "Real-time project cost monitoring")
    ]
    
    cols = st.columns(3)
    for i, (title, desc) in enumerate(modules):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="module-card">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== KEY BENEFITS ====================
elif page == "⭐ Key Benefits":
    st.title("Why Builders Love Burst")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Work Smarter")
        st.markdown('<div class="benefit">Build & share estimates easily<br>Auto-create bills from receipts<br>QuickBooks sync</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Deliver on Time & Budget")
        st.markdown('<div class="benefit">Real-time cash flow<br>Line-item change tracking<br>Profit calculation (markup/margin)</div>', unsafe_allow_html=True)
    
    with col3:
        st.subheader("Happy Customers & Partners")
        st.markdown('<div class="benefit">Client & Sub portals<br>Flexible payment options<br>Digital approvals</div>', unsafe_allow_html=True)

# ==================== OTHER PAGES ====================
elif page == "🔨 Estimating":
    st.title("AI-Powered Estimating")
    st.write("**Turn institutional knowledge into a fast, repeatable system.**")
    st.image("https://via.placeholder.com/900x500/334155/F1F5F9?text=AI+Estimating+Demo", use_column_width=True)
    
    for feature in [
        "Describe project or upload plans → AI generates complete estimate",
        "Reusable templates with industry standard codes",
        "Standardize markup, overhead, and margins",
        "Automatic conversion: Estimate → Budget",
        "Digital client approvals with branding"
    ]:
        st.success(f"✅ {feature}")

elif page == "💰 Financials":
    st.title("Financials")
    tab1, tab2, tab3 = st.tabs(["Budgets & Cash Flow", "Invoicing & Payments", "Reporting"])
    with tab1:
        st.write("Real-time budget tracking with line-item visibility")
        st.bar_chart({"Budget": [120000, 85000, 65000], "Actual": [115000, 92000, 61000]})

elif page == "📊 Project Management":
    st.title("Project Management")
    st.write("Daily Logs, Change Orders, Time Tracking, and more.")

elif page == "👥 Team & Subs":
    st.title("Team & Subcontractor Management")
    st.write("Role-based access • Subcontractor portals • Seamless payments")

elif page == "💵 Pricing":
    st.title("Simple, Transparent Pricing")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Essentials**  \n**$199/month**  \nEverything you need to run your jobs.")
        st.button("Choose Essentials", use_container_width=True)
    with col2:
        st.markdown("**PRO**  \n**$399/month**  \nFor larger jobs with crew, purchase orders, and advanced timecards.")
        st.button("Choose PRO", type="primary", use_container_width=True)
    st.info("No long-term contracts • No hidden fees • 30-day money-back guarantee")

elif page == "📞 Contact Us":
    st.title("Get in Touch")
    with st.form("contact_form"):
        st.text_input("Your Name")
        st.text_input("Company Name")
        st.text_input("Email")
        st.text_area("Message")
        if st.form_submit_button("Send Message"):
            st.success("Thank you! We'll get back to you shortly. (Demo)")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #94A3B8;'>"
    "© 2026 Burst Construction Software • constructionsoftwaretools.com"
    "</p>",
    unsafe_allow_html=True
)
