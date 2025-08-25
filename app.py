import pandas as pd
import plotly.express as px
import streamlit as st

# Streamlit page config
st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/superstore_cleaned.csv")

df = load_data()

st.title("📊 Superstore Sales Dashboard")

# --- KPIs ---
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_discount = df["Discount"].mean()
avg_profit_margin = df["Profit Margin"].mean() if "Profit Margin" in df.columns else None

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("💰 Total Sales", f"${total_sales:,.0f}")
kpi2.metric("🏆 Total Profit", f"${total_profit:,.0f}")
kpi3.metric("🔖 Avg. Discount", f"{avg_discount:.2%}")
if avg_profit_margin:
    kpi4.metric("📈 Avg. Profit Margin", f"{avg_profit_margin:.2%}")

st.markdown("---")

# --- Sales over Time (Multi-Year Trend) ---
if "Year" in df.columns and "Month_Name" in df.columns:
    # Sort months properly
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    sales_trend = df.groupby(["Year", "Month_Name"])["Sales"].sum().reset_index()
    sales_trend["Month_Name"] = pd.Categorical(sales_trend["Month_Name"], categories=month_order, ordered=True)
    sales_trend = sales_trend.sort_values(["Year", "Month_Name"])

    fig_trend = px.line(
        sales_trend,
        x="Month_Name",
        y="Sales",
        color="Year",
        title="📅 Monthly Sales Trend",
        markers=True
    )
    st.plotly_chart(fig_trend, use_container_width=True)


# --- Sales & Profit Trend by Month ---
if "Month_Name" in df.columns:
    sales_trend = df.groupby("Month_Name")[["Sales", "Profit"]].sum().reindex(
        ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]
    ).reset_index()

    fig1 = px.line(sales_trend, x="Month_Name", y=["Sales","Profit"], markers=True,
                   title="📅 Monthly Sales & Profit Trend")
    st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# --- Top Products ---
col1, col2 = st.columns(2)

with col1:
    top_sales = df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
    fig2 = px.bar(top_sales, x="Sales", y="Product Name", orientation="h",
                  title="🏆 Top 10 Products by Sales", color="Sales", color_continuous_scale="Blues")
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    top_profit = df.groupby("Product Name")["Profit"].sum().nlargest(10).reset_index()
    fig3 = px.bar(top_profit, x="Profit", y="Product Name", orientation="h",
                  title="💹 Top 10 Products by Profit", color="Profit", color_continuous_scale="Greens")
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# --- Regional Analysis ---
col3, col4 = st.columns(2)

with col3:
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()
    fig4 = px.bar(region_sales, x="Region", y="Sales", color="Region",
                  title="🌍 Sales by Region")
    st.plotly_chart(fig4, use_container_width=True)

with col4:
    region_profit = df.groupby("Region")["Profit"].sum().reset_index()
    fig5 = px.bar(region_profit, x="Region", y="Profit", color="Region",
                  title="🌍 Profit by Region")
    st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# --- Profitability ---
col5, col6 = st.columns(2)

with col5:
    fig6 = px.scatter(df, x="Discount", y="Profit", size="Sales", color="Category",
                      hover_data=["Product Name"], title="📉 Profit vs Discount")
    st.plotly_chart(fig6, use_container_width=True)

with col6:
    if "Profit Margin" in df.columns:
        fig7 = px.box(df, x="Category", y="Profit Margin", color="Category",
                      title="📦 Profit Margin by Category")
        st.plotly_chart(fig7, use_container_width=True)

st.markdown("---")

# --- Sales vs Profit by Sub-Category ---
fig8 = px.bar(df.groupby("Sub-Category")[["Sales","Profit"]].sum().reset_index(),
              x="Sub-Category", y=["Sales","Profit"], barmode="group",
              title="📊 Sales vs Profit by Sub-Category")
st.plotly_chart(fig8, use_container_width=True)























# import pandas as pd
# import plotly.express as px
# import streamlit as st

# # ---------------------------
# # 1. Page Config
# # ---------------------------
# st.set_page_config(
#     page_title="Superstore Sales Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------------------
# # 2. Load Data
# # ---------------------------
# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/superstore_cleaned.csv")
#     return df

# df = load_data()

# st.title("📊 Superstore Sales Dashboard")
# st.markdown("Explore sales and profit insights interactively using filters and charts.")

# # ---------------------------
# # 3. Sidebar Filters
# # ---------------------------
# st.sidebar.header("🔎 Filter Data")

# year = st.sidebar.multiselect(
#     "Select Year:",
#     options=df["Year"].unique(),
#     default=df["Year"].unique()
# )

# region = st.sidebar.multiselect(
#     "Select Region:",
#     options=df["Region"].unique(),
#     default=df["Region"].unique()
# )

# category = st.sidebar.multiselect(
#     "Select Category:",
#     options=df["Category"].unique(),
#     default=df["Category"].unique()
# )

# df_filtered = df[
#     (df["Year"].isin(year)) &
#     (df["Region"].isin(region)) &
#     (df["Category"].isin(category))
# ]

# # ---------------------------
# # 4. KPI Metrics
# # ---------------------------
# total_sales = df_filtered["Sales"].sum()
# total_profit = df_filtered["Profit"].sum()
# avg_margin = df_filtered["Profit Margin"].mean()

# col1, col2, col3 = st.columns(3)
# col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
# col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
# col3.metric("📊 Avg Profit Margin", f"{avg_margin:.2%}")

# # ---------------------------
# # 5. Visualizations
# # ---------------------------

# # Sales Trend by Month
# st.subheader("📅 Monthly Sales & Profit Trend")
# monthly_trend = df_filtered.groupby("Month_Name")[["Sales", "Profit"]].sum().reindex(
#     ["January", "February", "March", "April", "May", "June",
#      "July", "August", "September", "October", "November", "December"]
# ).reset_index()

# fig_trend = px.line(
#     monthly_trend, x="Month_Name", y=["Sales", "Profit"],
#     markers=True, title="Sales & Profit Over Months"
# )
# st.plotly_chart(fig_trend, use_container_width=True)

# # Sales by Region
# st.subheader("🌍 Sales by Region")
# fig_region = px.bar(
#     df_filtered.groupby("Region")["Sales"].sum().reset_index(),
#     x="Region", y="Sales", color="Region", title="Sales by Region"
# )
# st.plotly_chart(fig_region, use_container_width=True)

# # Sales by Category
# st.subheader("📦 Sales by Category")
# fig_category = px.pie(
#     df_filtered, names="Category", values="Sales",
#     title="Category Contribution to Sales"
# )
# st.plotly_chart(fig_category, use_container_width=True)

# # Top 10 Products
# st.subheader("🏆 Top 10 Products by Sales")
# top_products = df_filtered.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
# fig_products = px.bar(
#     top_products, x="Sales", y="Product Name",
#     orientation="h", title="Top 10 Products", color="Sales"
# )
# st.plotly_chart(fig_products, use_container_width=True)

# # Profit vs Discount
# st.subheader("💡 Profit Margin vs Discount")
# fig_scatter = px.scatter(
#     df_filtered, x="Discount", y="Profit Margin", color="Category",
#     size="Sales", hover_data=["Product Name"], title="Profit Margin vs Discount"
# )
# st.plotly_chart(fig_scatter, use_container_width=True)

# st.success("✅ Dashboard ready! Use the sidebar filters to interact with the data.")










# # # app.py - Superstore Sales Analysis Dashboard

# # import pandas as pd
# # import plotly.express as px
# # import streamlit as st

# # # =========================
# # # Page Config
# # # =========================
# # st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")

# # # =========================
# # # Load Data
# # # =========================
# # @st.cache_data
# # def load_data():
# #     df = pd.read_csv("data/superstore_cleaned.csv")
# #     return df

# # df = load_data()

# # # =========================
# # # Sidebar Filters
# # # =========================
# # st.sidebar.header("🔎 Filters")

# # year_filter = st.sidebar.multiselect(
# #     "Select Year(s):", options=df["Year"].unique(), default=df["Year"].unique()
# # )

# # region_filter = st.sidebar.multiselect(
# #     "Select Region(s):", options=df["Region"].unique(), default=df["Region"].unique()
# # )

# # category_filter = st.sidebar.multiselect(
# #     "Select Category:", options=df["Category"].unique(), default=df["Category"].unique()
# # )

# # # Apply filters
# # df_filtered = df[
# #     (df["Year"].isin(year_filter)) &
# #     (df["Region"].isin(region_filter)) &
# #     (df["Category"].isin(category_filter))
# # ]

# # # =========================
# # # Dashboard Header
# # # =========================
# # st.title("📊 Superstore Sales Analysis Dashboard")
# # st.markdown("Use the filters on the left to explore the dataset interactively.")

# # # =========================
# # # KPI Cards
# # # =========================
# # total_sales = df_filtered["Sales"].sum()
# # total_profit = df_filtered["Profit"].sum()
# # avg_discount = df_filtered["Discount"].mean()

# # col1, col2, col3 = st.columns(3)
# # col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
# # col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
# # col3.metric("🏷️ Avg. Discount", f"{avg_discount:.2%}")

# # # =========================
# # # Charts
# # # =========================

# # # Sales over Time
# # sales_trend = df_filtered.groupby(["Year", "Month_Name"])["Sales"].sum().reset_index()
# # fig_trend = px.line(
# #     sales_trend,
# #     x="Month_Name",
# #     y="Sales",
# #     color="Year",
# #     title="📅 Monthly Sales Trend",
# #     markers=True
# # )
# # st.plotly_chart(fig_trend, use_container_width=True)

# # # Sales by Category
# # fig_cat = px.bar(
# #     df_filtered.groupby("Category")["Sales"].sum().reset_index(),
# #     x="Category",
# #     y="Sales",
# #     color="Category",
# #     title="📦 Sales by Category"
# # )
# # st.plotly_chart(fig_cat, use_container_width=True)

# # # Sales by Region
# # fig_region = px.pie(
# #     df_filtered,
# #     values="Sales",
# #     names="Region",
# #     title="🌍 Sales Distribution by Region"
# # )
# # st.plotly_chart(fig_region, use_container_width=True)

# # # Profit vs Discount
# # fig_scatter = px.scatter(
# #     df_filtered,
# #     x="Discount",
# #     y="Profit",
# #     size="Sales",
# #     color="Category",
# #     hover_data=["Product Name"],
# #     title="💹 Profit vs Discount"
# # )
# # st.plotly_chart(fig_scatter, use_container_width=True)

# # # =========================
# # # Data Preview
# # # =========================
# # st.subheader("🔍 Data Preview")
# # st.dataframe(df_filtered.head(20))

