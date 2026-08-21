import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

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

    /* UI Card */
    .ui-card {
        background-color: #1E2937;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 1rem;
    }

    .ui-card h4 {
        color: #93C5FD;
        margin-top: 0;
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

    .stWarning {
        background-color: #92400E;
        color: #FCD34D;
    }

    /* Status Badges */
    .status-badge {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }
    .status-active {
        background-color: #166534;
        color: #86EFAC;
    }
    .status-pending {
        background-color: #92400E;
        color: #FCD34D;
    }
    .status-paid {
        background-color: #1E40AF;
        color: #BFDBFE;
    }

    .table-header {
        background-color: #1E2937;
        padding: 1rem;
        border-radius: 8px;
        border-bottom: 2px solid #334155;
        margin-bottom: 0.5rem;
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
            use_column_width=True
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
        use_column_width=True
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

# ==================== ESTIMATES UI ====================
elif page == "📋 Estimates":
    st.title("📋 Professional Estimates")
    st.markdown("### Win more jobs with AI-powered, professional estimates in minutes")
    
    tab1, tab2, tab3 = st.tabs(["Create Estimate", "Templates", "Sent Estimates"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### Quick Estimate Builder")
            with st.form("estimate_form"):
                project_name = st.text_input("Project Name", value="Kitchen Remodel - Main St")
                customer_name = st.text_input("Customer Name", value="John Smith")
                
                st.markdown("**Project Details**")
                col_a, col_b = st.columns(2)
                with col_a:
                    project_type = st.selectbox("Project Type", ["Kitchen Remodel", "Bathroom Remodel", "Roofing", "Siding", "Deck", "Addition", "Custom"])
                with col_b:
                    square_footage = st.number_input("Square Footage", value=500, min_value=100)
                
                st.markdown("**Line Items**")
                
                line_items_data = {
                    "Description": ["Labor", "Materials", "Permits & Fees", "Contingency (10%)"],
                    "Quantity": [40, 1, 1, 1],
                    "Unit": ["hrs", "job", "job", "job"],
                    "Rate": [65, 4200, 500, 470],
                    "Total": [2600, 4200, 500, 470]
                }
                
                line_items_df = pd.DataFrame(line_items_data)
                
                edited_df = st.data_editor(
                    line_items_df,
                    key="estimate_items",
                    hide_index=True,
                    use_container_width=True
                )
                
                st.markdown("**Pricing**")
                col_x, col_y, col_z = st.columns(3)
                with col_x:
                    markup_percent = st.slider("Markup %", 0, 50, 20)
                with col_y:
                    margin_percent = st.slider("Margin %", 0, 50, 25)
                with col_z:
                    discount_percent = st.slider("Discount %", 0, 20, 0)
                
                col_p1, col_p2 = st.columns(2)
                with col_p1:
                    st.text_input("Estimate Valid Until", value=(datetime.now() + timedelta(days=30)).strftime("%m/%d/%Y"))
                with col_p2:
                    st.selectbox("Currency", ["USD", "CAD", "EUR"])
                
                if st.form_submit_button("Generate Estimate", type="primary", use_container_width=True):
                    st.success("✅ Estimate created successfully!")
                    st.balloons()
        
        with col2:
            st.markdown("### Estimate Preview")
            st.markdown("""
            <div class="ui-card">
                <h4>📄 Estimate #EST-2024-001</h4>
                <p style="color: #CBD5E1; font-size: 0.9rem;">
                    <strong>Customer:</strong> John Smith<br>
                    <strong>Project:</strong> Kitchen Remodel - Main St<br>
                    <strong>Date:</strong> Dec 15, 2024<br>
                    <strong>Valid Until:</strong> Jan 14, 2025
                </p>
                <hr style="border-color: #334155;">
                <p style="color: #93C5FD; font-weight: bold;">Subtotal: $7,770</p>
                <p style="color: #93C5FD; font-weight: bold;">Tax (8%): $622</p>
                <p style="color: #10B981; font-weight: bold; font-size: 1.2rem;">Total: $8,392</p>
                <hr style="border-color: #334155;">
                <div style="margin-top: 1rem;">
                    <button style="width: 100%; padding: 0.5rem; background-color: #3B82F6; color: white; border: none; border-radius: 6px; cursor: pointer;">📧 Email to Client</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Recent Estimates**")
            recent = pd.DataFrame({
                "Status": ["✅ Accepted", "⏳ Pending", "❌ Declined"],
                "Customer": ["Smith", "Johnson", "Davis"],
                "Amount": ["$8,392", "$12,500", "$5,200"],
                "Date": ["Dec 15", "Dec 10", "Dec 5"]
            })
            st.dataframe(recent, use_container_width=True, hide_index=True)
    
    with tab2:
        st.markdown("### Reusable Templates")
        template_cols = st.columns(3)
        templates = [
            ("🏠 Kitchen Remodel", "Average: $8,500", "12 components"),
            ("🚿 Bathroom Remodel", "Average: $5,200", "8 components"),
            ("🛖 Deck Build", "Average: $6,800", "6 components"),
        ]
        
        for col, (name, price, items) in zip(template_cols, templates):
            with col:
                st.markdown(f"""
                <div class="ui-card">
                    <h4>{name}</h4>
                    <p>{price}<br><small>{items}</small></p>
                    <button style="width: 100%; padding: 0.5rem; background-color: #3B82F6; color: white; border: none; border-radius: 6px; cursor: pointer;">Use Template</button>
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Estimate Status Tracker")
        
        estimates_data = pd.DataFrame({
            "Estimate #": ["EST-001", "EST-002", "EST-003", "EST-004", "EST-005"],
            "Customer": ["John Smith", "Sarah Johnson", "Mike Davis", "Lisa Brown", "Tom Wilson"],
            "Amount": ["$8,392", "$12,500", "$5,200", "$15,800", "$3,900"],
            "Sent": ["Dec 15", "Dec 10", "Dec 5", "Nov 28", "Nov 15"],
            "Status": ["✅ Accepted", "⏳ Viewed", "⏳ Pending", "❌ Declined", "✅ Accepted"],
            "Win %": ["100%", "67%", "45%", "0%", "100%"]
        })
        
        st.dataframe(estimates_data, use_container_width=True, hide_index=True)
        
        # Stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Sent", "127", "this month")
        with col2:
            st.metric("Accepted", "52", "41% win rate")
        with col3:
            st.metric("Total Value", "$487,500", "pending")
        with col4:
            st.metric("Avg. Time to Sign", "3.2 days")

# ==================== BUDGETS UI ====================
elif page == "📊 Budgets":
    st.title("📊 Smart Budgets & Cash Flow")
    st.markdown("### Real-time budget tracking with instant alerts")
    
    tab1, tab2, tab3 = st.tabs(["Budget Dashboard", "Create Budget", "Cash Flow Forecast"])
    
    with tab1:
        # KPIs
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Active Projects", "12", "within budget")
        with col2:
            st.metric("At Risk", "2", "over 10%")
        with col3:
            st.metric("Total Budget", "$487,500", "↑ $12,000 this week")
        with col4:
            st.metric("Avg. Variance", "±3.2%", "excellent accuracy")
        
        st.markdown("---")
        
        # Project Budget List
        st.markdown("### Project Budgets")
        
        budget_data = pd.DataFrame({
            "Project": ["Kitchen Remodel", "Bathroom Remodel", "Deck Addition", "Siding Project", "Roof Repair"],
            "Budget": [15000, 8500, 12000, 9500, 6200],
            "Actual": [14500, 8900, 11800, 9800, 6100],
            "Remaining": [500, -400, 200, -300, 100],
            "% Complete": [97, 105, 98, 103, 98]
        })
        
        for idx, row in budget_data.iterrows():
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
            
            with col1:
                st.write(f"**{row['Project']}**")
            with col2:
                st.write(f"${row['Budget']:,}")
            with col3:
                st.write(f"${row['Actual']:,}")
            with col4:
                status = "🔴" if row['Remaining'] < 0 else "🟢"
                st.write(f"{status} ${row['Remaining']:,}")
            with col5:
                st.progress(min(row['% Complete'] / 100, 1.0))
        
        st.markdown("---")
        
        # Chart
        st.markdown("### Budget vs. Actual (All Projects)")
        
        fig = go.Figure(data=[
            go.Bar(name='Budget', x=budget_data['Project'], y=budget_data['Budget'], marker_color='#3B82F6'),
            go.Bar(name='Actual', x=budget_data['Project'], y=budget_data['Actual'], marker_color='#10B981')
        ])
        fig.update_layout(
            barmode='group',
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            hovermode='x unified',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### Create New Budget")
        
        with st.form("budget_form"):
            col1, col2 = st.columns(2)
            with col1:
                project_name = st.text_input("Project Name", value="New Renovation")
                project_type = st.selectbox("Project Type", ["Kitchen", "Bathroom", "Deck", "Roof", "Siding", "Custom"])
            with col2:
                start_date = st.date_input("Start Date")
                end_date = st.date_input("End Date")
            
            st.markdown("**Budget Categories**")
            
            categories = {
                "Labor": 5000,
                "Materials": 8000,
                "Subcontractors": 4000,
                "Equipment": 1500,
                "Permits & Fees": 500,
                "Contingency (10%)": 1900
            }
            
            budget_items = {}
            for category, default_val in categories.items():
                budget_items[category] = st.number_input(f"{category}", value=default_val, min_value=0, step=100)
            
            total_budget = sum(budget_items.values())
            
            st.markdown(f"### Total Budget: ${total_budget:,}")
            
            if st.form_submit_button("Create Budget", type="primary", use_container_width=True):
                st.success("✅ Budget created successfully!")
    
    with tab3:
        st.markdown("### Cash Flow Forecast (90 Days)")
        
        dates = pd.date_range(start=datetime.now(), periods=12, freq='W')
        cash_in = np.cumsum(np.random.randint(5000, 15000, 12))
        cash_out = np.cumsum(np.random.randint(4000, 12000, 12))
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=cash_in, name='Cash In', mode='lines+markers', 
                                 line=dict(color='#10B981', width=3)))
        fig.add_trace(go.Scatter(x=dates, y=cash_out, name='Cash Out', mode='lines+markers',
                                 line=dict(color='#EF4444', width=3)))
        
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            hovermode='x unified',
            height=400,
            yaxis_title="Amount ($)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Projected Cash In", "$187,500", "next 90 days")
        with col2:
            st.metric("Projected Cash Out", "$156,200", "next 90 days")
        with col3:
            st.metric("Forecasted Balance", "$31,300", "positive trend")

# ==================== INVOICES UI ====================
elif page == "📄 Invoices":
    st.title("📄 Professional Invoicing")
    st.markdown("### Get paid faster with branded invoices and automated reminders")
    
    tab1, tab2, tab3 = st.tabs(["Send Invoice", "Invoice Templates", "Payment Status"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### Create Invoice")
            
            with st.form("invoice_form"):
                col_a, col_b = st.columns(2)
                with col_a:
                    project = st.selectbox("Project", ["Kitchen Remodel", "Bathroom Remodel", "Deck Build"])
                    customer = st.text_input("Customer Email", value="john@email.com")
                with col_b:
                    invoice_type = st.selectbox("Invoice Type", ["Final", "Progress (50%)", "Progress (75%)"])
                    amount = st.number_input("Invoice Amount", value=8392, step=100)
                
                description = st.text_area("Description", value="Kitchen Remodel - Project Completion")
                
                due_date = st.date_input("Due Date", value=datetime.now() + timedelta(days=30))
                
                col_x, col_y = st.columns(2)
                with col_x:
                    accept_payments = st.checkbox("Accept online payments", value=True)
                with col_y:
                    send_reminders = st.checkbox("Auto-send payment reminders", value=True)
                
                if st.form_submit_button("Send Invoice", type="primary", use_container_width=True):
                    st.success("✅ Invoice sent to customer!")
        
        with col2:
            st.markdown("### Invoice Preview")
            st.markdown(f"""
            <div class="ui-card">
                <h4>INVOICE #INV-2024-001</h4>
                <p style="color: #CBD5E1; font-size: 0.9rem;">
                    <strong>Bill To:</strong> John Smith<br>
                    <strong>Project:</strong> Kitchen Remodel<br>
                    <strong>Date:</strong> Today<br>
                    <strong>Due:</strong> {due_date.strftime("%m/%d/%Y")}
                </p>
                <hr style="border-color: #334155;">
                <p style="color: #F1F5F9;"><strong>Description</strong></p>
                <p style="color: #CBD5E1;">Kitchen Remodel - Project Completion</p>
                <hr style="border-color: #334155;">
                <p style="color: #93C5FD; font-weight: bold; font-size: 1.2rem;">Amount Due: ${amount:,}</p>
                <hr style="border-color: #334155;">
                <div style="margin-top: 1rem;">
                    <button style="width: 100%; padding: 0.5rem; background-color: #10B981; color: white; border: none; border-radius: 6px; cursor: pointer; margin-bottom: 0.5rem;">💳 Pay Now</button>
                    <button style="width: 100%; padding: 0.5rem; background-color: #3B82F6; color: white; border: none; border-radius: 6px; cursor: pointer;">📧 Share Invoice</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Invoice Template Gallery")
        
        template_cols = st.columns(3)
        templates = [
            "Standard Invoice",
            "Progress Billing",
            "Retainer Invoice"
        ]
        
        for col, template in zip(template_cols, templates):
            with col:
                st.markdown(f"""
                <div class="ui-card">
                    <h4>📄 {template}</h4>
                    <p style="color: #CBD5E1;">Professionally designed template</p>
                    <button style="width: 100%; padding: 0.5rem; background-color: #3B82F6; color: white; border: none; border-radius: 6px; cursor: pointer;">Use Template</button>
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Invoice Payment Status")
        
        invoices = pd.DataFrame({
            "Invoice": ["INV-001", "INV-002", "INV-003", "INV-004", "INV-005"],
            "Customer": ["Smith", "Johnson", "Davis", "Brown", "Wilson"],
            "Amount": ["$8,392", "$12,500", "$5,200", "$15,800", "$3,900"],
            "Sent": ["Dec 15", "Dec 10", "Dec 5", "Nov 28", "Nov 15"],
            "Due": ["Jan 14", "Jan 9", "Jan 4", "Dec 28", "Dec 15"],
            "Status": ["✅ Paid", "⏳ Pending", "⏳ Pending", "🔴 Overdue", "✅ Paid"],
            "Days": ["0", "5", "10", "18", "27"]
        })
        
        st.dataframe(invoices, use_container_width=True, hide_index=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Invoiced", "$46,192")
        with col2:
            st.metric("Paid", "$12,292", "27%")
        with col3:
            st.metric("Pending", "$30,000", "65%")
        with col4:
            st.metric("Overdue", "$3,900", "8%")

# ==================== BILLS UI ====================
elif page == "📥 Bills":
    st.title("📥 Bill Management & Expenses")
    st.markdown("### Track every expense and connect it to your budget")
    
    tab1, tab2, tab3 = st.tabs(["Upload Receipt", "Expense List", "Budget Matching"])
    
    with tab1:
        st.markdown("### Capture Receipt")
        
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            uploaded_file = st.file_uploader("Upload Receipt Photo or PDF", type=['jpg', 'png', 'pdf'])
            
            if uploaded_file is not None:
                st.image(uploaded_file, width=300)
            
            with st.form("receipt_form"):
                st.markdown("**OCR Extracted Data** (Edit as needed)")
                
                vendor = st.text_input("Vendor", value="Home Depot")
                amount = st.number_input("Amount", value=1200.50, step=0.01)
                category = st.selectbox("Category", ["Materials", "Tools", "Equipment", "Labor", "Permits", "Other"])
                project = st.selectbox("Project", ["Kitchen Remodel", "Bathroom Remodel", "Deck Build"])
                
                date = st.date_input("Date")
                
                if st.form_submit_button("Save Expense", type="primary", use_container_width=True):
                    st.success("✅ Receipt saved and categorized!")
        
        with col2:
            st.markdown("**Quick Stats**")
            st.metric("Receipts This Month", "47")
            st.metric("Total Captured", "$23,450")
            st.metric("Processing Time", "Avg 2 sec")
    
    with tab2:
        st.markdown("### Recent Expenses")
        
        expenses = pd.DataFrame({
            "Date": ["Dec 15", "Dec 14", "Dec 12", "Dec 10", "Dec 8"],
            "Vendor": ["Home Depot", "Lowes", "Ace Hardware", "Local Supplier", "Tool Rental"],
            "Amount": ["$1,200", "$650", "$320", "$2,100", "$450"],
            "Category": ["Materials", "Materials", "Tools", "Materials", "Equipment"],
            "Project": ["Kitchen", "Bathroom", "Deck", "Kitchen", "All"],
            "Receipt": ["✅", "✅", "✅", "❌", "✅"]
        })
        
        st.dataframe(expenses, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("### Budget vs Actual Expenses")
        
        budget_comparison = pd.DataFrame({
            "Category": ["Labor", "Materials", "Equipment", "Subs", "Permits"],
            "Budget": [5000, 8000, 1500, 4000, 500],
            "Actual": [4800, 8200, 1400, 3900, 450],
            "Variance": [200, -200, 100, 100, 50]
        })
        
        fig = go.Figure(data=[
            go.Bar(name='Budget', x=budget_comparison['Category'], y=budget_comparison['Budget'], marker_color='#3B82F6'),
            go.Bar(name='Actual', x=budget_comparison['Category'], y=budget_comparison['Actual'], marker_color='#EF4444')
        ])
        fig.update_layout(
            barmode='group',
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================== PAYMENTS UI ====================
elif page == "💸 Payments":
    st.title("💸 Pay & Get Paid")
    st.markdown("### One-click payments with full visibility")
    
    tab1, tab2, tab3 = st.tabs(["Make Payment", "Payment History", "Set Up Recurring"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### Process Payment")
            
            with st.form("payment_form"):
                payee_type = st.radio("Pay to", ["Vendor/Sub", "Employee", "Payroll"])
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if payee_type == "Vendor/Sub":
                        payee = st.selectbox("Select Vendor", ["Home Depot", "Plumber - John's Plumbing", "Electrical - ABC Electric"])
                    else:
                        payee = st.selectbox("Select Employee", ["Mike Johnson", "Sarah Davis", "Tom Wilson"])
                
                with col_b:
                    amount = st.number_input("Amount", value=1200.00, step=0.01)
                
                invoice_ref = st.text_input("Invoice/Reference #", value="INV-001")
                
                payment_method = st.selectbox("Payment Method", ["ACH Transfer (1-2 days)", "Instant Pay (+$5 fee)", "Check by Mail (3-5 days)"])
                
                project = st.selectbox("Link to Project", ["Kitchen Remodel", "Bathroom Remodel", "All Projects"])
                
                notes = st.text_area("Notes", value="Payment for materials delivery")
                
                if st.form_submit_button("Confirm Payment", type="primary", use_container_width=True):
                    st.success("✅ Payment approved and scheduled!")
                    st.info(f"Payment of ${amount} will be processed via {payment_method.split('(')[0].strip()}")
        
        with col2:
            st.markdown("### Payment Methods")
            
            st.markdown("""
            <div class="ui-card">
                <h4>💳 Linked Cards</h4>
                <p style="color: #CBD5E1;">Chase Business (****1234)</p>
                <p style="color: #CBD5E1;">Amex (****5678)</p>
            </div>
            
            <div class="ui-card">
                <h4>🏦 Bank Accounts</h4>
                <p style="color: #CBD5E1;">Business Checking - Chase</p>
                <p style="color: #CBD5E1;">Operations - Wells Fargo</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Payment History (Last 30 Days)")
        
        payments = pd.DataFrame({
            "Date": ["Dec 15", "Dec 12", "Dec 10", "Dec 8", "Dec 5"],
            "Payee": ["Home Depot", "John's Plumbing", "ABC Electric", "Lowes", "Equipment Rental"],
            "Amount": ["$1,200", "$2,100", "$1,500", "$650", "$450"],
            "Method": ["ACH", "Check", "Card", "ACH", "Card"],
            "Status": ["✅ Complete", "✅ Complete", "✅ Complete", "⏳ Processing", "✅ Complete"],
            "Reference": ["PO-001", "INV-045", "INV-046", "PO-002", "RENT-234"]
        })
        
        st.dataframe(payments, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Paid (30d)", "$5,900")
        with col2:
            st.metric("Processing", "$450", "in progress")
        with col3:
            st.metric("Avg. Payment Time", "2.1 days")
    
    with tab3:
        st.markdown("### Recurring Payments")
        
        st.info("Set up automatic recurring payments for regular expenses")
        
        recurring = pd.DataFrame({
            "Vendor": ["Insurance Co", "Software License", "Equipment Lease"],
            "Amount": ["$500", "$150", "$800"],
            "Frequency": ["Monthly", "Monthly", "Weekly"],
            "Next Payment": ["Dec 20", "Jan 1", "Dec 18"],
            "Status": ["✅ Active", "✅ Active", "✅ Active"]
        })
        
        st.dataframe(recurring, use_container_width=True, hide_index=True)
        
        if st.button("+ Add Recurring Payment", use_container_width=True):
            st.success("New recurring payment form opened")

# ==================== CHANGE ORDERS UI ====================
elif page == "🔄 Change Orders":
    st.title("🔄 Change Order Management")
    st.markdown("### Streamline changes without losing track of margin")
    
    tab1, tab2, tab3 = st.tabs(["Create Change Order", "Pending Approvals", "Change Order History"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### New Change Order")
            
            with st.form("change_order_form"):
                project = st.selectbox("Project", ["Kitchen Remodel", "Bathroom Remodel", "Deck Build"])
                reason = st.text_area("Reason for Change", value="Client requested upgraded countertops")
                
                st.markdown("**Scope Changes**")
                
                change_items = pd.DataFrame({
                    "Item": ["Original Scope", "Additional Countertops", "Upgraded Hardware"],
                    "Description": ["As per estimate", "Granite instead of laminate", "Premium fixtures"],
                    "Amount": [8392, 1500, 300]
                })
                
                st.data_editor(change_items, key="change_items", hide_index=True, use_container_width=True)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    timeline_impact = st.selectbox("Timeline Impact", ["No change", "+3 days", "+1 week", "+2 weeks"])
                with col_b:
                    status = st.selectbox("Status", ["Draft", "Pending Client Approval", "Approved"])
                
                if st.form_submit_button("Create Change Order", type="primary", use_container_width=True):
                    st.success("✅ Change order created and saved!")
        
        with col2:
            st.markdown("### Impact Summary")
            st.markdown("""
            <div class="ui-card">
                <h4>📊 Financial Impact</h4>
                <p style="color: #CBD5E1;">
                    <strong>Original:</strong> $8,392<br>
                    <strong>Changes:</strong> +$1,800<br>
                    <strong>New Total:</strong> $10,192
                </p>
            </div>
            
            <div class="ui-card">
                <h4>⏱️ Schedule Impact</h4>
                <p style="color: #CBD5E1;">
                    <strong>Original:</strong> Dec 30<br>
                    <strong>New:</strong> Jan 3 (+3 days)
                </p>
            </div>
            
            <div class="ui-card">
                <h4>💰 Margin Impact</h4>
                <p style="color: #10B981; font-weight: bold;">Margin maintained at 25%</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Pending Client Approvals")
        
        pending = pd.DataFrame({
            "CO #": ["CO-001", "CO-002"],
            "Project": ["Kitchen", "Bathroom"],
            "Description": ["Upgraded countertops", "Extra bathroom tile"],
            "Amount": ["$1,800", "$450"],
            "Sent": ["Dec 15", "Dec 10"],
            "Status": ["⏳ Awaiting", "⏳ Viewed (3 days ago)"]
        })
        
        st.dataframe(pending, use_container_width=True, hide_index=True)
        
        if st.button("📧 Send Reminder", use_container_width=True):
            st.info("Reminder email sent to customer")
    
    with tab3:
        st.markdown("### Approved Change Orders (This Month)")
        
        history = pd.DataFrame({
            "CO #": ["CO-2024-01", "CO-2024-02", "CO-2024-03", "CO-2024-04"],
            "Project": ["Kitchen", "Bathroom", "Deck", "Kitchen"],
            "Reason": ["Upgrades", "Bathroom tile", "Extra railings", "Additional outlets"],
            "Amount": ["$1,800", "$450", "$600", "$200"],
            "Approved": ["Dec 12", "Dec 5", "Nov 28", "Nov 15"],
            "Completed": ["✅", "✅", "✅", "✅"]
        })
        
        st.dataframe(history, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Approved", "$3,050")
        with col2:
            st.metric("Avg. Amount", "$762.50")
        with col3:
            st.metric("Approval Time", "3.2 days avg")

# ==================== DAILY LOGS UI ====================
elif page == "📸 Daily Logs":
    st.title("📸 Photo-Based Daily Reports")
    st.markdown("### Capture progress, not paperwork")
    
    tab1, tab2, tab3 = st.tabs(["Create Report", "Photo Gallery", "Daily Reports"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### Today's Report")
            
            with st.form("daily_log_form"):
                project = st.selectbox("Project", ["Kitchen Remodel", "Bathroom Remodel"])
                date = st.date_input("Date", value=datetime.now())
                
                st.markdown("**Upload Photos**")
                uploaded_photos = st.file_uploader("Choose photos from today", type=['jpg', 'png'], accept_multiple_files=True)
                
                if uploaded_photos:
                    st.success(f"✅ {len(uploaded_photos)} photos ready to upload")
                
                st.markdown("**Crew & Tasks**")
                col_a, col_b = st.columns(2)
                with col_a:
                    crew_count = st.number_input("Crew Members Present", value=3, min_value=1)
                with col_b:
                    trades = st.multiselect("Trades", ["Framing", "Plumbing", "Electrical", "Drywall", "Finishing"])
                
                st.markdown("**Notes**")
                notes = st.text_area("Work Completed & Notes", value="Framing walls completed. Ready for inspection tomorrow.")
                
                st.markdown("**Auto-Detected**")
                col_x, col_y = st.columns(2)
                with col_x:
                    st.info(f"📍 Location: Main St (GPS verified)")
                with col_y:
                    st.info(f"🌤️ Weather: 65°F, Partly Cloudy")
                
                if st.form_submit_button("Save Daily Report", type="primary", use_container_width=True):
                    st.success("✅ Daily report saved!")
        
        with col2:
            st.markdown("**Stats**")
            st.metric("Reports This Month", "28")
            st.metric("Photos Captured", "287")
            st.metric("Avg Report Time", "3 min")
    
    with tab2:
        st.markdown("### Photo Gallery - Kitchen Remodel")
        
        # Create a simple photo gallery
        photos = [
            ("Framing Stage", "Dec 15"),
            ("Electrical Rough-In", "Dec 12"),
            ("Plumbing Installation", "Dec 10"),
            ("Foundation", "Dec 8"),
        ]
        
        photo_cols = st.columns(3)
        for idx, (photo_name, date_taken) in enumerate(photos):
            with photo_cols[idx % 3]:
                st.image(f"https://via.placeholder.com/200x150/334155/F1F5F9?text={photo_name}", use_column_width=True)
                st.caption(f"{photo_name} - {date_taken}")
    
    with tab3:
        st.markdown("### Recent Daily Reports")
        
        logs = pd.DataFrame({
            "Date": ["Dec 15", "Dec 14", "Dec 12", "Dec 10", "Dec 8"],
            "Project": ["Kitchen", "Kitchen", "Bathroom", "Kitchen", "Deck"],
            "Crew": ["3", "4", "2", "3", "5"],
            "Photos": ["8", "12", "6", "10", "15"],
            "Status": ["✅", "✅", "✅", "✅", "✅"]
        })
        
        st.dataframe(logs, use_container_width=True, hide_index=True)

# ==================== TIME TRACKING UI ====================
elif page == "⏱️ Time Tracking":
    st.title("⏱️ Job Costing Time Tracking")
    st.markdown("### Every hour tracked. Every project costs visible.")
    
    tab1, tab2, tab3 = st.tabs(["Clock In/Out", "Timesheets", "Labor Analysis"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### Clock In/Out")
            
            employee = st.selectbox("Select Employee", ["Mike Johnson", "Sarah Davis", "Tom Wilson", "Lisa Brown"])
            project = st.selectbox("Project", ["Kitchen Remodel", "Bathroom Remodel", "Deck Build"])
            cost_code = st.selectbox("Cost Code", ["Framing", "Electrical", "Plumbing", "Finishing", "General Labor"])
            
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🟢 Clock In", use_container_width=True, type="primary"):
                    st.success(f"✅ {employee} clocked in at 8:00 AM on {project}")
            with col_b:
                if st.button("🔴 Clock Out", use_container_width=True):
                    st.info(f"⏱️ {employee} clocked out at 4:30 PM (8.5 hours)")
            
            st.markdown("**Today's Hours**")
            col_x, col_y, col_z = st.columns(3)
            with col_x:
                st.metric("Hours Today", "8.5")
            with col_y:
                st.metric("This Week", "42.0")
            with col_z:
                st.metric("This Month", "168.5")
        
        with col2:
            st.markdown("**Team Status**")
            
            team_status = pd.DataFrame({
                "Employee": ["Mike Johnson", "Sarah Davis", "Tom Wilson", "Lisa Brown"],
                "Status": ["🟢 On Clock", "🟢 On Clock", "⚫ Clocked Out", "🟢 On Clock"],
                "Project": ["Kitchen", "Bathroom", "Off", "Deck"],
                "Hours Today": ["5.5", "6.0", "8.0", "4.5"]
            })
            
            st.dataframe(team_status, use_container_width=True, hide_index=True)
    
    with tab2:
        st.markdown("### Weekly Timesheets (Dec 9-15)")
        
        timesheet_data = pd.DataFrame({
            "Employee": ["Mike Johnson", "Sarah Davis", "Tom Wilson"],
            "Mon": ["8.0", "8.0", "8.0"],
            "Tue": ["9.0", "8.5", "8.0"],
            "Wed": ["8.5", "8.0", "0.0"],
            "Thu": ["8.0", "8.0", "8.5"],
            "Fri": ["8.5", "8.0", "8.0"],
            "Sat": ["4.0", "0.0", "0.0"],
            "Total": ["46.0", "40.5", "32.5"],
            "Status": ["⏳ Pending", "✅ Approved", "✅ Approved"]
        })
        
        st.dataframe(timesheet_data, use_container_width=True, hide_index=True)
        
        if st.button("✅ Approve All Timesheets", type="primary", use_container_width=True):
            st.success("✅ All timesheets approved!")
    
    with tab3:
        st.markdown("### Labor Cost Analysis")
        
        labor_data = pd.DataFrame({
            "Project": ["Kitchen", "Bathroom", "Deck", "Roof Repair"],
            "Budgeted": [5000, 3000, 4000, 2500],
            "Actual": [4800, 3200, 3900, 2400],
            "Hours": ["75", "50", "65", "40"],
            "Avg Rate": ["64", "64", "60", "60"],
            "Variance": ["$200", "-$200", "$100", "$100"]
        })
        
        fig = go.Figure(data=[
            go.Bar(name='Budgeted', x=labor_data['Project'], y=labor_data['Budgeted'], marker_color='#3B82F6'),
            go.Bar(name='Actual', x=labor_data['Project'], y=labor_data['Actual'], marker_color='#10B981')
        ])
        fig.update_layout(
            barmode='group',
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(labor_data, use_container_width=True, hide_index=True)

# ==================== REPORTING UI ====================
elif page == "📈 Reporting":
    st.title("📈 Financial Reporting & Insights")
    st.markdown("### Real-time dashboards of your entire business")
    
    tab1, tab2, tab3 = st.tabs(["Dashboard", "P&L Report", "Cash Flow"])
    
    with tab1:
        st.markdown("### Business Dashboard")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Revenue (YTD)", "$487,500", "↑ 24%")
        with col2:
            st.metric("Gross Profit", "$146,250", "30% margin")
        with col3:
            st.metric("Cash Balance", "$78,450", "↑ $12,000")
        with col4:
            st.metric("Active Projects", "12", "4 on budget")
        
        st.markdown("---")
        
        # Revenue trend
        st.markdown("### Revenue Trend (Last 12 Months)")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        revenue = [25000, 28000, 32000, 30000, 38000, 42000, 45000, 41000, 39000, 42000, 48000, 52000]
        
        fig = go.Figure(data=[
            go.Scatter(x=months, y=revenue, mode='lines+markers', name='Revenue', 
                      line=dict(color='#10B981', width=3), marker=dict(size=8))
        ])
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Profit by project
        st.markdown("### Profitability by Project (YTD)")
        
        profit_data = pd.DataFrame({
            "Project": ["Kitchen #1", "Bathroom #2", "Deck Addition", "Roof Repair", "Siding Job"],
            "Revenue": [15000, 8500, 12000, 6200, 9800],
            "Cost": [11250, 7225, 10200, 5270, 7840],
            "Profit": [3750, 1275, 1800, 930, 1960],
            "Margin %": ["25%", "15%", "15%", "15%", "20%"]
        })
        
        fig = px.bar(profit_data, x='Project', y=['Revenue', 'Cost'], barmode='stack',
                    color_discrete_map={'Revenue': '#10B981', 'Cost': '#EF4444'})
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### Profit & Loss Statement (YTD)")
        
        pl_data = pd.DataFrame({
            "Line Item": [
                "Total Revenue",
                "Cost of Labor",
                "Cost of Materials",
                "Subcontractor Costs",
                "Gross Profit",
                "Overhead Expenses",
                "Administrative",
                "Operating Profit",
                "Interest/Other",
                "Net Profit"
            ],
            "Amount": [487500, 146250, 146250, 97500, 97500, 24375, 14625, 58500, -2000, 56500],
            "% of Revenue": ["100%", "30%", "30%", "20%", "20%", "5%", "3%", "12%", "0.4%", "11.6%"]
        })
        
        st.dataframe(pl_data, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("### Cash Flow Statement")
        
        dates = pd.date_range(start='2024-11-01', periods=12, freq='M')
        opening = [50000, 55000, 63000, 72000, 68000, 78000, 85000, 92000, 88000, 95000, 105000, 113000]
        
        fig = go.Figure(data=[
            go.Scatter(x=dates, y=opening, mode='lines+markers', name='Cash Balance',
                      line=dict(color='#3B82F6', width=3), marker=dict(size=10),
                      fill='tozeroy', fillcolor='rgba(59, 130, 246, 0.2)')
        ])
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            height=400,
            yaxis_title="Cash Balance ($)"
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================== STAFF MANAGEMENT UI ====================
elif page == "👷 Staff Management":
    st.title("👷 Staff Management & Permissions")
    st.markdown("### Control who sees what")
    
    tab1, tab2, tab3 = st.tabs(["Team Members", "Invite User", "Audit Log"])
    
    with tab1:
        st.markdown("### Active Team Members")
        
        team_data = pd.DataFrame({
            "Name": ["Mike Johnson", "Sarah Davis", "Tom Wilson", "Lisa Brown", "John Martinez"],
            "Role": ["Project Manager", "Estimator", "Field Supervisor", "Accountant", "Owner"],
            "Status": ["✅ Active", "✅ Active", "✅ Active", "✅ Active", "✅ Active"],
            "Last Login": ["Today", "Yesterday", "2 days ago", "Today", "Today"],
            "Actions": ["Edit", "Edit", "Edit", "Edit", "Edit"]
        })
        
        st.dataframe(team_data, use_container_width=True, hide_index=True)
    
    with tab2:
        st.markdown("### Invite Team Member")
        
        with st.form("invite_form"):
            col1, col2 = st.columns(2)
            with col1:
                email = st.text_input("Email Address", placeholder="teammate@company.com")
                first_name = st.text_input("First Name")
            with col2:
                last_name = st.text_input("Last Name")
                role = st.selectbox("Role", ["Owner", "Project Manager", "Estimator", "Field Supervisor", "Accountant", "Custom"])
            
            st.markdown("**Permissions**")
            
            perms = st.columns(4)
            perms_list = ["View Budgets", "Edit Budgets", "Approve Invoices", "View Reports"]
            for col, perm in zip(perms, perms_list):
                with col:
                    st.checkbox(perm)
            
            if st.form_submit_button("Send Invite", type="primary", use_container_width=True):
                st.success(f"✅ Invite sent to {email}!")
    
    with tab3:
        st.markdown("### Audit Trail (Last 50 Actions)")
        
        audit_data = pd.DataFrame({
            "Date": ["Dec 15, 1:23 PM", "Dec 15, 11:45 AM", "Dec 14, 3:30 PM", "Dec 14, 2:15 PM"],
            "User": ["Mike Johnson", "Sarah Davis", "Tom Wilson", "Mike Johnson"],
            "Action": ["Approved Invoice INV-001", "Created Estimate EST-005", "Clocked out - Kitchen", "Viewed Budget Report"],
            "Details": ["$8,392", "Kitchen Remodel", "8.5 hours", "Q4 Summary"]
        })
        
        st.dataframe(audit_data, use_container_width=True, hide_index=True)

# ==================== SUBCONTRACTOR MANAGEMENT UI ====================
elif page == "🤝 Subcontractor Management":
    st.title("🤝 Subcontractor Management")
    st.markdown("### RFQs, bidding, and payments - all streamlined")
    
    tab1, tab2, tab3 = st.tabs(["Send RFQ", "Active Subs", "Bid Comparison"])
    
    with tab1:
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("### Create RFQ")
            
            with st.form("rfq_form"):
                project = st.selectbox("Project", ["Kitchen Remodel", "Bathroom Remodel", "Deck Build"])
                trade = st.selectbox("Trade", ["Plumbing", "Electrical", "HVAC", "Framing", "Drywall", "Painting"])
                
                scope = st.text_area("Scope of Work", value="Supply and install new plumbing for kitchen and bathroom remodel including water lines, drain lines, fixtures installation.")
                
                due_date = st.date_input("Bid Due Date", value=datetime.now() + timedelta(days=5))
                
                subs = st.multiselect("Select Subcontractors", ["John's Plumbing", "ABC Electric", "Premier HVAC", "Quality Framing", "Smooth Drywall"])
                
                if st.form_submit_button("Send RFQ", type="primary", use_container_width=True):
                    st.success(f"✅ RFQ sent to {len(subs)} subcontractors!")
        
        with col2:
            st.markdown("**RFQ Status**")
            st.metric("RFQs Sent This Month", "12")
            st.metric("Avg Response Time", "2.1 days")
            st.metric("Completion Rate", "94%")
    
    with tab2:
        st.markdown("### Active Subcontractors")
        
        subs_data = pd.DataFrame({
            "Sub Name": ["John's Plumbing", "ABC Electric", "Premier HVAC", "Quality Framing"],
            "Trade": ["Plumbing", "Electrical", "HVAC", "Framing"],
            "Status": ["✅ Active", "✅ Active", "✅ Active", "⚠️ No Recent Work"],
            "Projects": ["2", "3", "1", "0"],
            "Avg Rating": ["5.0", "4.8", "4.9", "4.5"]
        })
        
        st.dataframe(subs_data, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("### Recent Bid Comparison")
        
        bids = pd.DataFrame({
            "Subcontractor": ["John's Plumbing", "Premium Plumbing", "City Plumbing"],
            "Bid Amount": ["$4,200", "$4,500", "$3,950"],
            "Timeline": ["5 days", "7 days", "3 days"],
            "Insurance": ["✅", "✅", "❌"],
            "Rating": ["5.0", "4.2", "3.8"],
            "Selected": ["✅", "", ""]
        })
        
        st.dataframe(bids, use_container_width=True, hide_index=True)

# ==================== COST TRACKING UI ====================
elif page == "💰 Cost Tracking":
    st.title("💰 Real-Time Cost Tracking")
    st.markdown("### See project costs as they happen")
    
    tab1, tab2, tab3 = st.tabs(["Cost Dashboard", "Cost Breakdown", "Variance Analysis"])
    
    with tab1:
        st.markdown("### Project Cost Summary")
        
        cost_summary = pd.DataFrame({
            "Project": ["Kitchen", "Bathroom", "Deck", "Roof", "Siding"],
            "Budget": [15000, 8500, 12000, 6200, 9800],
            "Spent": [14500, 8200, 11800, 5500, 9600],
            "Remaining": [500, 300, 200, 700, 200],
            "% Spent": ["96.7%", "96.5%", "98.3%", "88.7%", "98.0%"]
        })
        
        fig = go.Figure(data=[
            go.Bar(name='Spent', x=cost_summary['Project'], y=cost_summary['Spent'], marker_color='#EF4444'),
            go.Bar(name='Remaining', x=cost_summary['Project'], y=cost_summary['Remaining'], marker_color='#10B981')
        ])
        fig.update_layout(
            barmode='stack',
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            plot_bgcolor='rgba(30, 41, 55, 1)',
            font=dict(color='#F1F5F9'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### Cost Breakdown - Kitchen Remodel")
        
        breakdown = pd.DataFrame({
            "Category": ["Labor", "Materials", "Equipment", "Subcontractors", "Permits"],
            "Budget": [5000, 6000, 1500, 2000, 500],
            "Actual": [4800, 6200, 1400, 1900, 200],
            "Variance": [200, -200, 100, 100, 300]
        })
        
        fig = px.pie(breakdown, values='Actual', names='Category',
                    color_discrete_sequence=['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'])
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(15, 23, 42, 1)',
            font=dict(color='#F1F5F9'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(breakdown, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("### Variance Analysis")
        
        variance = pd.DataFrame({
            "Category": ["Labor", "Materials", "Equipment", "Subs", "Permits"],
            "Budget": [5000, 6000, 1500, 2000, 500],
            "Actual": [4800, 6200, 1400, 1900, 200],
            "Variance": [200, -200, 100, 100, 300],
            "Variance %": ["4.0%", "-3.3%", "6.7%", "5.0%", "60.0%"],
            "Status": ["✅", "⚠️", "✅", "✅", "✅"]
        })
        
        st.dataframe(variance, use_container_width=True, hide_index=True)

# ==================== PRICING ====================
elif page == "💵 Pricing":
    st.title("Simple, Transparent Pricing")
    st.markdown("### No long-term contracts. No hidden fees. Cancel anytime.")

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
