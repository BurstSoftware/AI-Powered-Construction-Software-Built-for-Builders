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

    /* Feature List */
    .feature-list {
        background-color: #1E2937;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #10B981;
        margin-bottom: 1rem;
    }
    .feature-list li {
        color: #CBD5E1;
        margin-bottom: 0.6rem;
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
st.sidebar.title("🚀 Burst Construction Software")
st.sidebar.markdown("**AI-Powered Construction Software**")

page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📋 Core Modules",
    "⭐ Key Benefits",
    "📋 Estimates",
    "📊 Budgets",
    "📄 Invoices",
    "📥 Bills",
    "💸 Payments",
    "🔄 Change Orders",
    "📸 Daily Logs",
    "⏱️ Time Tracking",
    "📈 Reporting",
    "👷 Staff Management",
    "🤝 Subcontractor Management",
    "💰 Cost Tracking",
    "🔨 Estimating",
    "💰 Financials",
    "📊 Project Management",
    "👥 Team & Subs",
    "💵 Pricing",
    "📞 Contact Us"
])

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">Burst Software Development</h1>', unsafe_allow_html=True)
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

# ==================== ESTIMATES ====================
elif page == "📋 Estimates":
    st.title("📋 Professional Estimates")
    st.markdown("### Win more jobs with AI-powered, professional estimates in minutes")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Estimate+Editor", use_column_width=True)
    with col2:
        st.metric("Avg. Time to Estimate", "15 min", "vs 90 min manually")
        st.metric("Estimate Win Rate", "38%", "↑ 22% vs manual")
        st.metric("Professional Look", "100%", "Branded & polished")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>✨ AI generates estimates from descriptions or photos</li>
                <li>📐 Industry standard pricing & labor rates</li>
                <li>💾 Reusable templates for common jobs</li>
                <li>📱 Mobile-friendly estimate generation</li>
                <li>🎨 Custom branding with your logo & colors</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📧 Email directly to clients with tracking</li>
                <li>✍️ Client e-signature for digital approval</li>
                <li>🔄 Auto-convert to budget with one click</li>
                <li>📊 Track acceptance rates & revenue</li>
                <li>💼 Markup/margin customization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("How It Works")
    tab1, tab2, tab3 = st.tabs(["AI-Powered", "Templates", "Client Portal"])
    
    with tab1:
        st.write("**Describe your project or upload photos → Burst AI generates a complete estimate**")
        st.info("Our AI learns from your historical estimates to suggest the right pricing and labor costs automatically.")
    
    with tab2:
        st.write("Save time on recurring work. Build reusable templates for kitchens, bathrooms, roofing, and more.")
        st.success("Edit once, use forever. Update labor rates and materials across all templates instantly.")
    
    with tab3:
        st.write("Clients get a beautiful, branded estimate on their phone or desktop. One-click approval = signed contract.")
        st.success("Approval tracking: See exactly when they opened it and signed.")
    
    if st.button("Try Estimate Tool (Demo)", type="primary", use_container_width=True):
        st.info("Demo mode activated — upload a photo or describe a job to see AI in action!")

# ==================== BUDGETS ====================
elif page == "📊 Budgets":
    st.title("📊 Smart Budgets & Cash Flow")
    st.markdown("### See profit and loss at a glance with real-time line-item budgets")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Budget+Dashboard", use_column_width=True)
    with col2:
        st.metric("Budget Accuracy", "94%", "within ±5%")
        st.metric("Cashflow Issues Caught", "3.2x faster", "than spreadsheets")
        st.metric("Monthly Updates", "Real-time", "no delays")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>💰 Auto-create budget from estimate</li>
                <li>📊 Compare budget vs. actual at a glance</li>
                <li>⚠️ Alerts when spending exceeds budget</li>
                <li>📈 Line-item profitability tracking</li>
                <li>🔄 Update budgets without starting over</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>💵 Cashflow forecasting (30/60/90 days)</li>
                <li>🎯 Markup & margin by category</li>
                <li>📱 Mobile budget updates from the field</li>
                <li>🔗 Link invoices to budget line items</li>
                <li>📉 Historical budget performance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Budget Example")
    budget_data = {
        "Category": ["Labor", "Materials", "Subcontractors", "Equipment", "Overhead"],
        "Budget": [15000, 8000, 12000, 3000, 2000],
        "Actual": [14500, 8200, 11800, 3100, 2000],
        "Variance": [500, -200, 200, -100, 0]
    }
    st.bar_chart({"Budget": budget_data["Budget"], "Actual": budget_data["Actual"]})
    
    if st.button("View Budget Templates", type="primary", use_container_width=True):
        st.success("25+ pre-built templates available for common project types!")

# ==================== INVOICES ====================
elif page == "📄 Invoices":
    st.title("📄 Professional Invoicing")
    st.markdown("### Get paid faster with branded invoices and automated reminders")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Invoice+Generator", use_column_width=True)
    with col2:
        st.metric("Invoice Turnaround", "2 days faster", "vs manual")
        st.metric("Payment Collection", "36% faster", "with reminders")
        st.metric("Error Rate", "99% reduction", "automated checks")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📋 Auto-generate from budget line items</li>
                <li>🎨 Custom branding & logo placement</li>
                <li>📄 Progress billing (% complete)</li>
                <li>💳 Accept payments directly in invoice</li>
                <li>📧 Send & track opening automatically</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>⏰ Automatic payment reminders (overdue)</li>
                <li>📊 Invoice history & templates</li>
                <li>🔗 Link to project for context</li>
                <li>📱 Mobile invoice creation</li>
                <li>🔐 Secure client portal access</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 Tip: Most users get paid 36% faster by enabling online payment options directly on invoices.")
    
    if st.button("Create Invoice Template", type="primary", use_container_width=True):
        st.success("Template saved! Use it for all future invoices.")

# ==================== BILLS ====================
elif page == "📥 Bills":
    st.title("📥 Bill Management & Expenses")
    st.markdown("### Track every expense and connect it to your project budget")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Bill+Tracking", use_column_width=True)
    with col2:
        st.metric("Expense Processing", "10x faster", "with OCR")
        st.metric("Budget Accuracy", "Improved 31%", "when tracking bills")
        st.metric("Lost Expenses", "Down 87%", "documented automatically")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📸 Snap receipt photos from phone</li>
                <li>🔍 OCR reads vendor, date & amount</li>
                <li>📊 Auto-match to budget categories</li>
                <li>🔗 Attach to specific job or line item</li>
                <li>💾 Digital receipt storage</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📋 Organize by vendor or category</li>
                <li>⚠️ Alert when spending exceeds budget</li>
                <li>📈 Expense reports & tax summaries</li>
                <li>🏦 Sync with accounting software</li>
                <li>📱 Mobile receipt capture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.success("✅ Keep receipts organized digitally — never lose a deduction again.")
    
    if st.button("Upload Receipt (Demo)", type="primary", use_container_width=True):
        st.info("Click to capture a receipt photo and see instant expense categorization!")

# ==================== PAYMENTS ====================
elif page == "💸 Payments":
    st.title("💸 Pay & Get Paid")
    st.markdown("### One-click payments to subs, vendors, and employees — with full visibility")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Payment+Processing", use_column_width=True)
    with col2:
        st.metric("Payment Speed", "Same day ACH", "or instant card")
        st.metric("Payment Methods", "6 options", "ACH, card, check, etc.")
        st.metric("Processing Fees", "Highly competitive", "transparent pricing")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>💰 One-click pay from invoice or bill</li>
                <li>🏦 ACH, credit card, or check</li>
                <li>📱 Mobile payment approval</li>
                <li>📋 Batch payments to multiple vendors</li>
                <li>🔐 Role-based approval workflows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>🎯 Auto-categorize for accounting</li>
                <li>📊 Payment history & reconciliation</li>
                <li>📧 Automatic payment notifications</li>
                <li>💵 Accept payments from clients online</li>
                <li>🔄 Recurring payment scheduling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 Save time: Set up recurring payments for regular vendors and never think about it again.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("✅ ACH Transfers")
        st.caption("1-2 business days")
    with col2:
        st.success("✅ Instant Pay")
        st.caption("Same day (fee applies)")
    with col3:
        st.success("✅ Check by Mail")
        st.caption("3-5 business days")
    
    if st.button("Send Payment (Demo)", type="primary", use_container_width=True):
        st.success("Payment scheduled! Vendor will receive notification.")

# ==================== CHANGE ORDERS ====================
elif page == "🔄 Change Orders":
    st.title("🔄 Change Order Management")
    st.markdown("### Streamline change requests without losing track of scope or margin")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Change+Orders", use_column_width=True)
    with col2:
        st.metric("Time to Process", "4x faster", "vs manual forms")
        st.metric("Margin Protection", "98%", "capture all changes")
        st.metric("Scope Disputes", "Down 92%", "documented approval")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📝 Create change orders in seconds</li>
                <li>🔄 Auto-update budget and schedule</li>
                <li>💵 Automatic cost impact calculation</li>
                <li>🏷️ Track scope changes by category</li>
                <li>📧 Send to client for approval</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>✍️ E-signature for approval</li>
                <li>📋 Version control & audit trail</li>
                <li>🔗 Link change orders to invoice line items</li>
                <li>📊 Change order trend reports</li>
                <li>⏱️ Track time from request to approval</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.success("✅ Never lose money to scope creep. Every change is captured and approved.")
    
    if st.button("Create Change Order (Demo)", type="primary", use_container_width=True):
        st.info("Demo: Fill out the change order form and see it update your budget automatically!")

# ==================== DAILY LOGS ====================
elif page == "📸 Daily Logs":
    st.title("📸 Photo-Based Daily Reports")
    st.markdown("### Capture job progress with photos, weather, and crew notes in one tap")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Daily+Log+Mobile", use_column_width=True)
    with col2:
        st.metric("Report Time", "2 min per day", "vs 20 min manual")
        st.metric("Photo Storage", "Unlimited", "cloud-backed")
        st.metric("Client Updates", "Instant", "auto-share portal")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📸 Upload photos from job site</li>
                <li>🏷️ Auto-tag photos with date/location</li>
                <li>🌤️ Automatic weather data included</li>
                <li>👷 Crew member & task notes</li>
                <li>📋 Attendance tracking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📱 Mobile-first design for field use</li>
                <li>🔗 Link to project for context</li>
                <li>🤝 Share with clients instantly</li>
                <li>📊 Progress reports automated</li>
                <li>🔐 Secure photo archival</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 Field crews love it: No paperwork, just photos. Everything else is automatic.")
    
    if st.button("Take Daily Log Photo (Demo)", type="primary", use_container_width=True):
        st.info("Demo mode: Pretend to upload a job site photo and see it become a full daily report!")

# ==================== TIME TRACKING ====================
elif page == "⏱️ Time Tracking":
    st.title("⏱️ Job Costing Time Tracking")
    st.markdown("### See where every hour goes — by employee, job, and task")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Time+Tracking", use_column_width=True)
    with col2:
        st.metric("Timesheet Errors", "Down 94%", "automated verification")
        st.metric("Payroll Processing", "2x faster", "instant sync")
        st.metric("Job Costing Accuracy", "±3%", "real-time visibility")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>⏰ Clock in/out by job & cost code</li>
                <li>📱 Mobile app with one-tap clocking</li>
                <li>📍 GPS verification of location</li>
                <li>⚠️ Overtime alerts (automatic)</li>
                <li>👷 Track labor costs by employee</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>🔄 Automatic timesheet routing for approval</li>
                <li>💰 Compare actual labor vs. budget</li>
                <li>📊 Productivity reports by crew</li>
                <li>🎯 Capture billable hours separately</li>
                <li>📈 Historical labor cost analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.success("✅ Reduce time theft and streamline payroll. Everyone clocks in once, data flows everywhere.")
    
    if st.button("Clock In (Demo)", type="primary", use_container_width=True):
        st.info("Demo: You clocked in at 8:00 AM on Renovation Project - Kitchen.")

# ==================== REPORTING ====================
elif page == "📈 Reporting":
    st.title("📈 Financial Reporting & Insights")
    st.markdown("### Dashboard view of profit, cash flow, and project performance")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Reports+Dashboard", use_column_width=True)
    with col2:
        st.metric("Report Generation", "5 min", "vs 4 hours manual")
        st.metric("Insights Discovered", "3.2x more", "with automated reports")
        st.metric("Decision Speed", "Faster", "real-time data")
    
    st.markdown("---")
    st.subheader("Key Reports")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>💼 Profit & Loss</h3>
            <p>By project, month, or year. See exactly what's profitable.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>💰 Cash Flow</h3>
            <p>30/60/90-day forecasts. Never run out of working capital.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="module-card">
            <h3>📊 Project Health</h3>
            <p>Budget vs. actual, timeline status, and profitability per job.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Additional Reports")
        st.markdown("""
        - Aging receivables (who owes you?)
        - Aging payables (what do you owe?)
        - Labor cost analysis
        - Material cost variance
        - Employee productivity
        - Subcontractor performance
        """)
    
    with col2:
        st.subheader("Data Export & Integration")
        st.markdown("""
        - Export to Excel or PDF
        - Email scheduled reports
        - QuickBooks Online sync
        - Tax-ready summaries
        - API access for custom tools
        - Historical data (7+ years)
        """)
    
    if st.button("View Sample Report", type="primary", use_container_width=True):
        st.success("Opening sample P&L report showing year-over-year comparison...")

# ==================== STAFF MANAGEMENT ====================
elif page == "👷 Staff Management":
    st.title("👷 Staff Management & Permissions")
    st.markdown("### Control who sees what — by role and access level")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Team+Management", use_column_width=True)
    with col2:
        st.metric("Onboarding Time", "5 min", "per team member")
        st.metric("Security Breaches", "Down 99%", "role-based controls")
        st.metric("Audit Trail", "Complete", "every action logged")
    
    st.markdown("---")
    st.subheader("User Roles")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>👔 Owner</h3>
            <p>Full access to all data, billing, and team management.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>📋 Project Manager</h3>
            <p>View/edit projects, budgets, schedules, and team hours.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="module-card">
            <h3>🔨 Field Supervisor</h3>
            <p>Log time, capture photos, update status (no financials).</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>💼 Estimator</h3>
            <p>Create/edit estimates, view project data, no billing access.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>💰 Accountant</h3>
            <p>Full financial visibility, no project editing capability.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Permission Controls")
    st.markdown("""
    - View/edit budgets
    - Approve invoices & payments
    - Send estimates to clients
    - View financial reports
    - Export data
    - Delete/archive projects
    - Invite new team members
    - Custom role creation
    """)
    
    st.success("✅ Full audit trail: See who did what, when, and from where.")
    
    if st.button("Invite Team Member (Demo)", type="primary", use_container_width=True):
        st.info("Demo: Enter an email address to invite a new team member!")

# ==================== SUBCONTRACTOR MANAGEMENT ====================
elif page == "🤝 Subcontractor Management":
    st.title("🤝 Subcontractor Management")
    st.markdown("### Streamlined workflows for RFQs, bidding, and payment")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Sub+Portal", use_column_width=True)
    with col2:
        st.metric("Payment Processing", "40% faster", "with portal")
        st.metric("RFQ Response Time", "Avg 2.1 days", "automated tracking")
        st.metric("Sub Satisfaction", "94%", "self-service portal")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📋 Create and send RFQs in seconds</li>
                <li>📊 Compare bids side-by-side</li>
                <li>📱 Subs respond on mobile (easy UX)</li>
                <li>🔗 Link to project & documents</li>
                <li>📁 Organize by trade & location</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>🤝 Sub portal with job access</li>
                <li>💵 One-click invoice upload</li>
                <li>💸 One-click payment approval</li>
                <li>📋 Download plans & specs</li>
                <li>📞 Built-in messaging (no email chains)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 Pro tip: Subs report spending 40% less time on admin with the self-service portal.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("📊 Performance Tracking")
        st.caption("Track on-time completion, quality ratings, and profitability by subcontractor")
    
    with col2:
        st.success("💰 Manage Relationships")
        st.caption("Store contact info, rates, insurance docs, and certifications in one place")
    
    if st.button("Invite Subcontractor (Demo)", type="primary", use_container_width=True):
        st.info("Demo: Send a portal invite to a subcontractor email!")

# ==================== COST TRACKING ====================
elif page == "💰 Cost Tracking":
    st.title("💰 Real-Time Cost Tracking")
    st.markdown("### See project costs as they happen — not after the fact")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://via.placeholder.com/600x350/334155/F1F5F9?text=Cost+Tracking", use_column_width=True)
    with col2:
        st.metric("Cost Overruns Caught", "3.5x faster", "vs manual tracking")
        st.metric("Project Margin Protected", "±2%", "accurate forecasting")
        st.metric("Budget Variance", "Real-time visibility", "no surprises")
    
    st.markdown("---")
    st.subheader("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>📊 Dashboard showing all costs</li>
                <li>🔍 Line-item cost breakdown</li>
                <li>💸 Labor, materials, subs all integrated</li>
                <li>⚠️ Real-time overage alerts</li>
                <li>📈 Trending & forecasting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-list">
            <ul>
                <li>🔗 All costs tied to budget line items</li>
                <li>📱 Mobile cost entry from field</li>
                <li>🏷️ Automatic categorization</li>
                <li>📊 Cost reports & variance analysis</li>
                <li>📉 Historical cost benchmarks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Cost Categories Tracked")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Direct Costs**\n- Labor\n- Materials\n- Equipment")
    with col2:
        st.markdown("**Subcontractor Costs**\n- Sub labor\n- Sub materials\n- Change orders")
    with col3:
        st.markdown("**Overhead**\n- Permits\n- Insurance\n- Site management")
    
    st.markdown("---")
    st.success("✅ Every bill, expense, and timesheet automatically flows into your cost tracking.")
    
    if st.button("View Cost Breakdown (Demo)", type="primary", use_container_width=True):
        st.info("Opening cost dashboard for Sample Renovation Project...")

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

# ==================== PROJECT MANAGEMENT ====================
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

# ==================== TEAM & SUBS ====================
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

# ==================== PRICING ====================
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
