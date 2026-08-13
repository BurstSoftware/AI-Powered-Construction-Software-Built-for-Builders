import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

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

    .module-card {
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        background-color: #1E2937;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
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

    .benefit {
        background-color: #1E2937;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #60A5FA;
        color: #F1F5F9 !important;
        margin-bottom: 0.8rem;
    }

    .stMarkdown, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
    .stMarkdown h4, .stMarkdown p, .stMarkdown li, .stWrite {
        color: #F1F5F9 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #1E2937;
        color: #F1F5F9;
    }
    .stRadio label, .stSidebar .stMarkdown {
        color: #E2E8F0 !important;
    }

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
    "📋 Estimates",
    "📊 Budgets",
    "📄 Invoices",
    "📥 Bills",
    "💸 Payments",
    "🔄 Change Orders",
    "📸 Daily Logs",
    "⏱️ Time Tracking",
    "📈 Reporting",
    "💰 Cost Tracking",
    "👷 Staff Management",
    "🤝 Subcontractor Management",
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

# ==================== CORE MODULES OVERVIEW ====================
elif page == "📋 Core Modules":
    st.title("Core Solutions")
    st.write("Everything you need to run your construction business in one platform. Click any module in the sidebar to explore its full UI.")
    
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

# ==================== 📋 ESTIMATES ====================
elif page == "📋 Estimates":
    st.title("📋 AI-Powered Estimates")
    st.markdown("### Turn institutional knowledge into a fast, repeatable system")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Estimates Created", "384", "+28 this month")
    m2.metric("Win Rate", "41%", "↑ 9%")
    m3.metric("Avg. Turnaround", "18 min", "vs 3 hrs before")
    m4.metric("AI Accuracy", "94%", "vs actuals")

    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Create New Estimate", "Recent Estimates", "Templates"])
    
    with tab1:
        st.subheader("Describe the project or upload plans")
        with st.form("new_estimate"):
            colA, colB = st.columns(2)
            with colA:
                client = st.text_input("Client Name", "Johnson Residence")
                project = st.text_input("Project Title", "Kitchen Remodel")
                location = st.text_input("Location", "Austin, TX")
            with colB:
                markup = st.slider("Markup %", 10, 40, 25)
                overhead = st.slider("Overhead %", 5, 20, 12)
                contingency = st.slider("Contingency %", 0, 15, 5)
            
            description = st.text_area("Project Description / Scope", 
                "Full kitchen remodel including cabinets, countertops, flooring, electrical, and plumbing.")
            uploaded = st.file_uploader("Upload plans / photos (optional)", accept_multiple_files=True)
            
            if st.form_submit_button("✨ Generate AI Estimate", type="primary", use_container_width=True):
                st.success("AI Estimate generated successfully! (Demo)")
                st.balloons()
                
                # Sample line items
                data = {
                    "Cost Code": ["06-100", "06-200", "09-300", "15-100", "16-200", "Labor"],
                    "Description": ["Cabinets", "Countertops", "Flooring", "Plumbing", "Electrical", "Crew Labor"],
                    "Qty": [1, 45, 320, 1, 1, 120],
                    "Unit": ["LS", "SF", "SF", "LS", "LS", "HRS"],
                    "Unit Cost": [8500, 85, 12.5, 3200, 4100, 65],
                    "Total": [8500, 3825, 4000, 3200, 4100, 7800]
                }
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True)
                st.metric("Estimated Total (after markup)", f"${df['Total'].sum() * 1.25:,.0f}")

    with tab2:
        estimates = pd.DataFrame({
            "Estimate #": ["EST-1042", "EST-1041", "EST-1040", "EST-1039"],
            "Client": ["Johnson Residence", "Smith Addition", "Garcia Bath", "Lee Deck"],
            "Amount": ["$48,250", "$92,100", "$18,400", "$12,750"],
            "Status": ["Sent", "Won", "Draft", "Expired"],
            "Date": ["2026-08-10", "2026-08-05", "2026-08-01", "2026-07-20"]
        })
        st.dataframe(estimates, use_container_width=True)

    with tab3:
        st.info("Save any estimate as a reusable template with standard cost codes and markups.")

# ==================== 📊 BUDGETS ====================
elif page == "📊 Budgets":
    st.title("📊 Budgets & Cash Flow")
    st.markdown("### Effortless budgets with real-time cashflow tracking")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Active Budgets", "23")
    m2.metric("Total Budgeted", "$2.84M")
    m3.metric("Current Variance", "-3.2%", "under budget")

    st.markdown("---")
    
    st.subheader("Project Budget vs Actual")
    chart_data = pd.DataFrame({
        "Category": ["Materials", "Labor", "Subs", "Equipment", "Overhead"],
        "Budget": [120000, 85000, 95000, 22000, 18000],
        "Actual": [115000, 92000, 88000, 24500, 17200]
    }).set_index("Category")
    st.bar_chart(chart_data)

    st.subheader("Cash Flow Forecast (Next 8 Weeks)")
    weeks = [f"W{i}" for i in range(1, 9)]
    cashflow = pd.DataFrame({
        "Inflows": [45000, 32000, 78000, 21000, 55000, 40000, 67000, 29000],
        "Outflows": [38000, 41000, 52000, 35000, 48000, 39000, 51000, 33000]
    }, index=weeks)
    st.area_chart(cashflow)

    st.success("✅ Budgets auto-created from won estimates. Line-item tracking stays live as costs come in.")

# ==================== 📄 INVOICES ====================
elif page == "📄 Invoices":
    st.title("📄 Invoices")
    st.markdown("### All-in-one invoicing tool built for contractors")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Outstanding", "$187,400")
    m2.metric("Paid this month", "$94,200")
    m3.metric("Avg. Days to Pay", "11")
    m4.metric("Overdue", "$23,100")

    st.markdown("---")
    
    tab1, tab2 = st.tabs(["Create Invoice", "Invoice List"])
    
    with tab1:
        with st.form("create_invoice"):
            col1, col2 = st.columns(2)
            with col1:
                st.selectbox("Project", ["Johnson Kitchen", "Smith Addition", "Garcia Bath"])
                st.selectbox("Client", ["Johnson Residence", "Smith Family", "Garcia"])
            with col2:
                st.date_input("Invoice Date", datetime.now())
                st.date_input("Due Date", datetime.now() + timedelta(days=14))
            
            st.text_area("Line Items / Notes", "Progress billing - 40% complete\nMaterials draw\nLabor through 8/10")
            
            if st.form_submit_button("Generate & Send Invoice", type="primary", use_container_width=True):
                st.success("Invoice INV-2087 created and emailed to client. (Demo)")

    with tab2:
        inv_data = pd.DataFrame({
            "Invoice #": ["INV-2087", "INV-2086", "INV-2085", "INV-2084"],
            "Client": ["Johnson", "Smith", "Garcia", "Lee"],
            "Amount": ["$19,300", "$45,000", "$7,200", "$12,800"],
            "Status": ["Sent", "Paid", "Overdue", "Draft"],
            "Due": ["2026-08-24", "2026-08-05", "2026-08-01", "—"]
        })
        st.dataframe(inv_data, use_container_width=True)

# ==================== 📥 BILLS ====================
elif page == "📥 Bills":
    st.title("📥 Bills")
    st.markdown("### Connect invoicing and budgeting seamlessly")
    
    st.info("Upload receipts or enter bills → automatically matched to budget line items and projects.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Recent Bills")
        bills = pd.DataFrame({
            "Vendor": ["ABC Lumber", "City Plumbing", "ElectroPro", "Home Depot"],
            "Project": ["Johnson Kitchen", "Smith Addition", "Johnson Kitchen", "Garcia Bath"],
            "Amount": ["$4,280", "$1,950", "$3,100", "$687"],
            "Status": ["Matched", "Pending", "Matched", "Needs Review"],
            "Date": ["2026-08-11", "2026-08-10", "2026-08-09", "2026-08-08"]
        })
        st.dataframe(bills, use_container_width=True)
    
    with col2:
        st.subheader("Quick Add Bill")
        with st.form("add_bill"):
            st.text_input("Vendor")
            st.number_input("Amount", min_value=0.0, value=0.0)
            st.selectbox("Project", ["Johnson Kitchen", "Smith Addition", "Garcia Bath"])
            st.file_uploader("Receipt / Invoice PDF")
            if st.form_submit_button("Add & Match to Budget"):
                st.success("Bill added and matched to cost code 06-100. (Demo)")

# ==================== 💸 PAYMENTS ====================
elif page == "💸 Payments":
    st.title("💸 Payments")
    st.markdown("### Pay and get paid with one click")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Received this month", "$142,800")
    m2.metric("Paid to Subs/Vendors", "$89,400")
    m3.metric("Pending Payouts", "$31,200")

    st.markdown("---")
    
    tab1, tab2 = st.tabs(["Get Paid (Client Payments)", "Pay Out (Subs & Vendors)"])
    
    with tab1:
        st.subheader("Outstanding Client Invoices")
        st.dataframe(pd.DataFrame({
            "Invoice": ["INV-2087", "INV-2083", "INV-2079"],
            "Client": ["Johnson", "Martinez", "Thompson"],
            "Amount": ["$19,300", "$28,500", "$11,200"],
            "Status": ["Awaiting Payment", "Partial", "Overdue"]
        }), use_container_width=True)
        st.button("Send Payment Reminder", use_container_width=True)
        st.button("Record Manual Payment", use_container_width=True)
    
    with tab2:
        st.subheader("Approve & Pay")
        st.dataframe(pd.DataFrame({
            "Payee": ["ABC Lumber", "Mike's Electric", "City Plumbing"],
            "Bill #": ["B-441", "B-438", "B-435"],
            "Amount": ["$4,280", "$3,100", "$1,950"],
            "Method": ["ACH", "ACH", "Check"]
        }), use_container_width=True)
        if st.button("Approve Selected & Pay", type="primary", use_container_width=True):
            st.success("Payments initiated. (Demo)")

# ==================== 🔄 CHANGE ORDERS ====================
elif page == "🔄 Change Orders":
    st.title("🔄 Change Orders")
    st.markdown("### Efficient management of project changes")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Open COs", "7")
    m2.metric("Approved Value", "$48,600")
    m3.metric("Avg. Approval Time", "1.8 days")

    st.markdown("---")
    
    with st.form("new_co"):
        st.subheader("Create Change Order")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Project", ["Johnson Kitchen", "Smith Addition"])
            st.text_input("CO Title", "Add island electrical & plumbing")
        with col2:
            st.number_input("Additional Cost", value=3200)
            st.number_input("Days Added to Schedule", value=3)
        
        st.text_area("Description & Reason")
        if st.form_submit_button("Create & Send for Approval", type="primary"):
            st.success("Change Order CO-014 created and sent to client portal. (Demo)")

    st.subheader("Active Change Orders")
    st.dataframe(pd.DataFrame({
        "CO #": ["CO-014", "CO-013", "CO-012"],
        "Project": ["Johnson Kitchen", "Smith Addition", "Garcia Bath"],
        "Amount": ["+$3,200", "+$8,450", "-$1,100"],
        "Status": ["Pending Client", "Approved", "Approved"],
        "Date": ["2026-08-12", "2026-08-08", "2026-08-03"]
    }), use_container_width=True)

# ==================== 📸 DAILY LOGS ====================
elif page == "📸 Daily Logs":
    st.title("📸 Daily Logs")
    st.markdown("### Photo-based reporting with weather data")
    
    st.info("Field crews submit logs from mobile. Weather is auto-pulled. Clients can view approved logs.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Today's Log - Johnson Kitchen")
        st.write(f"**Date:** {datetime.now().strftime('%B %d, %Y')}")
        st.write("**Weather:** 88°F • Partly Cloudy • Humidity 62%")
        st.write("**Crew:** 4 workers • 32 total hours")
        st.text_area("Work Performed", "Installed upper cabinets. Rough-in electrical for island completed. Floor prep started.")
        st.text_area("Notes / Issues", "Waiting on final countertop template.")
        st.file_uploader("Add Photos", accept_multiple_files=True)
        if st.button("Submit Daily Log", type="primary"):
            st.success("Daily log submitted and weather attached. (Demo)")
    
    with col2:
        st.subheader("Recent Logs")
        for i in range(3):
            with st.expander(f"Johnson Kitchen — {(datetime.now() - timedelta(days=i)).strftime('%b %d')}"):
                st.write("Crew: 4 • Hours: 32")
                st.write("Photos: 8 attached")
                st.write("Weather auto-logged")

# ==================== ⏱️ TIME TRACKING ====================
elif page == "⏱️ Time Tracking":
    st.title("⏱️ Time Tracking")
    st.markdown("### Track time per employee, job, and line item")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Hours this week", "312")
    m2.metric("Billable %", "87%")
    m3.metric("Overtime", "18 hrs")
    m4.metric("Active Clock-ins", "9")

    st.markdown("---")
    
    st.subheader("Live Time Entries")
    time_data = pd.DataFrame({
        "Employee": ["Mike R.", "Sarah T.", "Carlos M.", "James L.", "Anna K."],
        "Project": ["Johnson Kitchen", "Smith Addition", "Johnson Kitchen", "Garcia Bath", "Smith Addition"],
        "Cost Code": ["Labor - Carpentry", "Labor - Finish", "Labor - Electrical", "Labor - Plumbing", "Labor - Framing"],
        "Hours": [8.0, 7.5, 8.0, 6.0, 8.0],
        "Status": ["Clocked Out", "Clocked Out", "Active", "Clocked Out", "Active"]
    })
    st.dataframe(time_data, use_container_width=True)

    st.subheader("Quick Clock-in (Mobile View)")
    with st.form("clockin"):
        st.selectbox("Employee", ["Mike R.", "Sarah T.", "Carlos M."])
        st.selectbox("Project", ["Johnson Kitchen", "Smith Addition", "Garcia Bath"])
        st.selectbox("Cost Code / Task", ["Carpentry", "Electrical", "Plumbing", "General Labor"])
        if st.form_submit_button("Clock In", type="primary"):
            st.success("Clocked in with GPS verification. (Demo)")

# ==================== 📈 REPORTING ====================
elif page == "📈 Reporting":
    st.title("📈 Reporting & Insights")
    st.markdown("### Financial reporting and project intelligence")
    
    report_type = st.selectbox("Select Report", [
        "Job Profitability",
        "Cash Flow Summary",
        "Labor Productivity",
        "Open AR / Aging",
        "Budget Variance by Project"
    ])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Gross Profit (YTD)", "$412,000", "+18%")
        st.metric("Net Margin", "19.4%", "↑ 2.1 pts")
    with col2:
        st.metric("Revenue (YTD)", "$2.12M", "+24%")
        st.metric("Overhead Ratio", "11.8%")

    st.markdown("---")
    st.subheader("Job Profitability Overview")
    profit_df = pd.DataFrame({
        "Project": ["Johnson Kitchen", "Smith Addition", "Garcia Bath", "Lee Deck", "Thompson Patio"],
        "Revenue": [48250, 92100, 18400, 12750, 34500],
        "Cost": [36100, 71200, 14200, 9800, 28900],
        "Profit": [12150, 20900, 4200, 2950, 5600],
        "Margin %": [25.2, 22.7, 22.8, 23.1, 16.2]
    })
    st.dataframe(profit_df, use_container_width=True)
    
    st.bar_chart(profit_df.set_index("Project")[["Revenue", "Cost"]])

# ==================== 💰 COST TRACKING ====================
elif page == "💰 Cost Tracking":
    st.title("💰 Cost Tracking")
    st.markdown("### Real-time project cost monitoring")
    
    project = st.selectbox("Select Project", ["Johnson Kitchen", "Smith Addition", "Garcia Bath"])
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Original Budget", "$48,250")
    m2.metric("Revised Budget", "$51,450", "+$3,200 CO")
    m3.metric("Actual to Date", "$31,870")
    m4.metric("% Complete", "62%")

    st.markdown("---")
    
    st.subheader("Cost by Category")
    cost_df = pd.DataFrame({
        "Category": ["Materials", "Labor", "Subcontractors", "Equipment", "Other"],
        "Budget": [18500, 14200, 9800, 2200, 1750],
        "Actual": [16200, 11900, 2400, 1850, 520],
        "Remaining": [2300, 2300, 7400, 350, 1230]
    })
    st.dataframe(cost_df, use_container_width=True)
    
    st.bar_chart(cost_df.set_index("Category")[["Budget", "Actual"]])
    
    st.success("✅ Costs update automatically from bills, time entries, and change orders.")

# ==================== 👷 STAFF MANAGEMENT ====================
elif page == "👷 Staff Management":
    st.title("👷 Staff Management")
    st.markdown("### Role-based access and permissions")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Team Members", "28")
    m2.metric("Active Today", "19")
    m3.metric("Roles Defined", "6")

    st.markdown("---")
    
    st.subheader("Team Directory")
    staff = pd.DataFrame({
        "Name": ["Alex Rivera", "Jordan Lee", "Sam Patel", "Taylor Brooks", "Casey Nguyen"],
        "Role": ["Owner", "Project Manager", "Estimator", "Field Supervisor", "Accountant"],
        "Projects": [12, 8, 15, 6, 0],
        "Status": ["Active", "Active", "Active", "Active", "Active"],
        "Last Login": ["Today", "Today", "Yesterday", "Today", "2 days ago"]
    })
    st.dataframe(staff, use_container_width=True)

    st.subheader("Roles & Permissions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>Owner / Admin</h3>
            <p>Full access to everything including billing, user management, and financials.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>Project Manager</h3>
            <p>Projects, change orders, daily logs, time approval, limited financial view.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="module-card">
            <h3>Field / Estimator</h3>
            <p>Assigned jobs only. Can submit logs, time, and create draft estimates.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.form("invite_user"):
        st.subheader("Invite New Team Member")
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Email")
            st.selectbox("Role", ["Project Manager", "Estimator", "Field Supervisor", "Accountant", "Viewer"])
        with c2:
            st.multiselect("Assign Projects", ["Johnson Kitchen", "Smith Addition", "Garcia Bath"])
        if st.form_submit_button("Send Invite"):
            st.success("Invitation sent. (Demo)")

# ==================== 🤝 SUBCONTRACTOR MANAGEMENT ====================
elif page == "🤝 Subcontractor Management":
    st.title("🤝 Subcontractor Management")
    st.markdown("### Streamlined subcontractor workflows")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Active Subs", "64")
    m2.metric("Open Work Orders", "18")
    m3.metric("Pending Invoices", "$41,200")

    st.markdown("---")
    
    st.subheader("Subcontractor Directory")
    subs = pd.DataFrame({
        "Company": ["Elite Electric", "Pro Plumb Co", "Summit Framing", "Apex Drywall", "GreenScape"],
        "Trade": ["Electrical", "Plumbing", "Framing", "Drywall", "Landscaping"],
        "Active Jobs": [3, 2, 1, 4, 1],
        "Rating": ["4.9", "4.7", "4.8", "4.6", "5.0"],
        "Portal Access": ["Yes", "Yes", "Yes", "No", "Yes"]
    })
    st.dataframe(subs, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>Sub Portal</h3>
            <p>Subs log in to view assigned scopes, download plans, submit invoices, and track payment status.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>Work Orders & RFQs</h3>
            <p>Send digital work orders and collect bids. All communication and documents stay in one place.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.form("invite_sub"):
        st.subheader("Invite Subcontractor to Portal")
        st.text_input("Company Name")
        st.text_input("Contact Email")
        st.selectbox("Primary Trade", ["Electrical", "Plumbing", "Framing", "Drywall", "Other"])
        if st.form_submit_button("Send Portal Invite"):
            st.success("Portal invitation sent. (Demo)")

# ==================== PROJECT MANAGEMENT (HIGH-LEVEL) ====================
elif page == "📊 Project Management":
    st.title("Project Management")
    st.markdown("### Keep every job on track with real-time visibility and control")
    st.write("From daily logs to change orders — manage the entire job lifecycle in one place. Use the sidebar to dive into specific tools.")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Projects", "47", "+5")
    m2.metric("On-Time Completion", "92%", "↑ 8%")
    m3.metric("Avg. Change Orders", "3.2", "per job")
    m4.metric("Time Saved", "12 hrs/week", "on admin")

    st.markdown("---")

    st.subheader("Core Project Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>📸 Daily Logs</h3>
            <p>Photo-based daily reports with automatic weather data, crew notes, and progress tracking.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>⏱️ Time Tracking</h3>
            <p>Clock in/out by job, employee, or cost code. GPS verification and overtime alerts.</p>
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
            <p>Plans, contracts, permits, and photos — organized by project with version control.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="module-card">
            <h3>📍 Job Site Status</h3>
            <p>Live progress boards, punch lists, and inspection checklists from any device.</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== TEAM & SUBS (HIGH-LEVEL) ====================
elif page == "👥 Team & Subs":
    st.title("Team & Subcontractor Management")
    st.markdown("### Give the right people the right access — nothing more, nothing less")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Team Members", "28", "active")
    c2.metric("Active Subs", "64", "across projects")
    c3.metric("Avg. Payment Time", "2.1 days", "faster")

    st.markdown("---")
    st.write("Use the sidebar to open **Staff Management** or **Subcontractor Management** for full functionality.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>👷 Staff Management</h3>
            <p>Role-based access, permissions, onboarding, and performance insights.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>🤝 Subcontractor Portal</h3>
            <p>Work orders, document sharing, invoice submission, and one-click payments.</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== PRICING ====================
elif page == "💵 Pricing":
    st.title("Simple, Transparent Pricing")
    st.markdown("### No long-term contracts. No hidden fees. Cancel anytime.")
    
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
