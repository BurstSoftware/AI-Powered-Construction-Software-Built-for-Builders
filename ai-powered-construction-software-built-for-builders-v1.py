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
        height: 100%;
        margin-bottom: 1rem;
    }
    .module-card h3 {
        color: #93C5FD !important;
        margin-top: 0;
    }
    .module-card p {
        color: #CBD5E1 !important;
    }

    /* Pricing Cards */
    .pricing-card {
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2rem;
        background-color: #1E2937;
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
        color: #F1F5F9 !important;
        height: 100%;
        text-align: center;
    }
    .pricing-card.popular {
        border: 2px solid #60A5FA;
        background: linear-gradient(180deg, #1E2937 0%, #1E3A5F 100%);
    }
    .pricing-card h2 {
        color: #93C5FD !important;
        margin-bottom: 0.5rem;
    }
    .pricing-card .price {
        font-size: 2.5rem;
        font-weight: bold;
        color: #F1F5F9 !important;
        margin: 1rem 0;
    }
    .pricing-card ul {
        text-align: left;
        color: #CBD5E1 !important;
        padding-left: 1.2rem;
    }
    .pricing-card li {
        margin-bottom: 0.5rem;
    }

    /* Benefit Boxes */
    .benefit {
        background-color: #1E2937;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #60A5FA;
        color: #F1F5F9 !important;
        margin-bottom: 0.8rem;
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
        st.image(
            "https://via.placeholder.com/800x400/334155/F1F5F9?text=Burst+Dashboard+Preview",
            width="stretch"
        )
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
    st.image(
        "https://via.placeholder.com/800x120/475569/F1F5F9?text=Contractor+Logos+Row",
        width="stretch"
    )

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

# ==================== ESTIMATING ====================
elif page == "🔨 Estimating":
    st.title("AI-Powered Estimating")
    st.write("**Turn institutional knowledge into a fast, repeatable system.**")
    st.image(
        "https://via.placeholder.com/900x500/334155/F1F5F9?text=AI+Estimating+Demo",
        width="stretch"
    )
    
    for feature in [
        "Describe project or upload plans → AI generates complete estimate",
        "Reusable templates with industry standard codes",
        "Standardize markup, overhead, and margins",
        "Automatic conversion: Estimate → Budget",
        "Digital client approvals with branding"
    ]:
        st.success(f"✅ {feature}")

# ==================== FINANCIALS ====================
elif page == "💰 Financials":
    st.title("Financials")
    tab1, tab2, tab3 = st.tabs(["Budgets & Cash Flow", "Invoicing & Payments", "Reporting"])
    with tab1:
        st.write("Real-time budget tracking with line-item visibility")
        st.bar_chart({"Budget": [120000, 85000, 65000], "Actual": [115000, 92000, 61000]})

# ==================== PROJECT MANAGEMENT (UPDATED) ====================
elif page == "📊 Project Management":
    st.title("Project Management")
    st.markdown("### Keep every job on track with real-time visibility and control")
    st.write("From daily logs to change orders — manage the entire job lifecycle in one place.")

    # Key metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Projects", "47", "+5")
    m2.metric("On-Time Completion", "92%", "↑ 8%")
    m3.metric("Avg. Change Orders", "3.2", "per job")
    m4.metric("Time Saved", "12 hrs/week", "on admin")

    st.markdown("---")

    # Feature cards
    st.subheader("Core Project Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>📸 Daily Logs</h3>
            <p>Photo-based daily reports with automatic weather data, crew notes, and progress tracking. Share with clients in one click.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>⏱️ Time Tracking</h3>
            <p>Clock in/out by job, employee, or cost code. GPS verification and overtime alerts included.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>🔄 Change Orders</h3>
            <p>Create, approve, and track change orders digitally. Automatic budget & schedule updates.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>📅 Scheduling</h3>
            <p>Simple Gantt-style timelines. Drag-and-drop tasks, assign crews, and set dependencies.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="module-card">
            <h3>📂 Document Hub</h3>
            <p>Plans, contracts, permits, and photos — all organized by project with version control.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>📍 Job Site Status</h3>
            <p>Live progress boards, punch lists, and inspection checklists accessible from any device.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("How it works on the job site")
    st.image(
        "https://via.placeholder.com/900x350/334155/F1F5F9?text=Project+Dashboard+%26+Mobile+App",
        width="stretch"
    )

    st.success("✅ Mobile-first design — field crews can log time, photos, and notes from any smartphone")

# ==================== TEAM & SUBS (UPDATED) ====================
elif page == "👥 Team & Subs":
    st.title("Team & Subcontractor Management")
    st.markdown("### Give the right people the right access — nothing more, nothing less")
    st.write("Role-based permissions, subcontractor portals, and seamless payments keep everyone aligned.")

    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Team Members", "28", "active")
    c2.metric("Active Subs", "64", "across projects")
    c3.metric("Avg. Payment Time", "2.1 days", "faster")

    st.markdown("---")

    st.subheader("Staff Management")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>👷 Role-Based Access</h3>
            <p>Owner • PM • Estimator • Field Supervisor • Accountant — each role sees only what they need.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>🔐 Permissions & Security</h3>
            <p>Control who can view budgets, approve change orders, or send invoices. Full audit trail included.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>📱 Easy Onboarding</h3>
            <p>Invite team members by email. They get instant access on web and mobile with no extra licenses for basic roles.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>📊 Performance Insights</h3>
            <p>Track hours, productivity, and job profitability by team member or crew.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Subcontractor Portal")

    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown("""
        <div class="module-card">
            <h3>🤝 Sub Portal Access</h3>
            <p>Subs log in to view assigned work, upload invoices, and download plans — no email chains needed.</p>
        </div>
        """, unsafe_allow_html=True)
    with colB:
        st.markdown("""
        <div class="module-card">
            <h3>💸 One-Click Payments</h3>
            <p>Approve sub invoices and pay directly from Burst. ACH, credit card, or check — your choice.</p>
        </div>
        """, unsafe_allow_html=True)
    with colC:
        st.markdown("""
        <div class="module-card">
            <h3>📋 Bid & Document Sharing</h3>
            <p>Send RFQs, collect bids, and share project documents securely with selected subcontractors.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 Pro tip: Most users report 40%+ reduction in payment delays after enabling the sub portal.")

# ==================== PRICING (UPDATED) ====================
elif page == "💵 Pricing":
    st.title("Simple, Transparent Pricing")
    st.markdown("### No long-term contracts. No hidden fees. Cancel anytime.")
    st.write("Choose the plan that fits your business size. All plans include unlimited projects and support.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="pricing-card">
            <h2>Essentials</h2>
            <p>Perfect for solo operators & small teams</p>
            <div class="price">$199<span style="font-size:1rem;">/month</span></div>
            <ul>
                <li>Unlimited projects & estimates</li>
                <li>AI-powered estimating</li>
                <li>Budgets & cash flow tracking</li>
                <li>Invoicing & payments</li>
                <li>Daily logs & time tracking</li>
                <li>Basic reporting</li>
                <li>Up to 5 team members</li>
                <li>Email support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("Choose Essentials", use_container_width=True, key="essentials")

    with col2:
        st.markdown("""
        <div class="pricing-card popular">
            <h2>PRO ⭐ Most Popular</h2>
            <p>For growing contractors with crews & subs</p>
            <div class="price">$399<span style="font-size:1rem;">/month</span></div>
            <ul>
                <li>Everything in Essentials</li>
                <li>Unlimited team members</li>
                <li>Subcontractor portals</li>
                <li>Advanced change orders</li>
                <li>Purchase orders</li>
                <li>Advanced timecards & GPS</li>
                <li>Custom roles & permissions</li>
                <li>Priority support + onboarding</li>
                <li>QuickBooks Online sync</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("Choose PRO", type="primary", use_container_width=True, key="pro")

    st.markdown("---")

    # Guarantee & extras
    g1, g2, g3 = st.columns(3)
    with g1:
        st.success("🛡️ 30-day money-back guarantee")
    with g2:
        st.info("📅 No long-term contracts")
    with g3:
        st.success("🚀 Free onboarding call included")

    st.markdown("### Frequently Asked Questions")
    with st.expander("Can I switch plans later?"):
        st.write("Yes — upgrade or downgrade anytime. Changes take effect on your next billing cycle.")
    with st.expander("Do you offer annual billing?"):
        st.write("Yes. Pay annually and get 2 months free (Essentials $1,990/yr • PRO $3,990/yr).")
    with st.expander("Is there a free trial?"):
        st.write("Absolutely. Start a 14-day free trial with full access to the PRO plan — no credit card required.")
    with st.expander("What payment methods do you accept?"):
        st.write("All major credit cards and ACH bank transfers.")

# ==================== CONTACT US ====================
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
