import streamlit as st
import pandas as pd
from main import plot_review_by_gender, plot_size_by_gender, plot_payment_methods, plot_categories_by_gender, plot_stacked_area, plot_shipping_pie, plot_purchase_boxplot
import style
st.set_page_config(
    page_title="Shoplytics",
    page_icon="🛒",
    layout="wide"
)
st.markdown(
    """
    <style>
    iframe {
        pointer-events: auto !important;
    }
    .stPlotlyChart {
        z-index: 1;
    }
    div[data-baseweb="select"] {
        z-index: 999 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<style>
/* nền toàn app */
.stApp {
    background: linear-gradient(135deg, #FFF0F6 0%, #F0F9FF 100%);
}
/* xóa nền trắng vùng header + top container */
header[data-testid="stHeader"] {
    background: transparent !important;
}
/* xóa nền chính container */
.block-container {
    background: transparent !important;
    padding-top: 2rem;
}
/* xóa background của main wrapper */
main {
    background: transparent !important;
}            
div[data-baseweb="select"] > div {
    background-color: #fff5fa !important;
    border: 2px solid #f8bbd0 !important;
    border-radius: 12px !important;
}
div[data-baseweb="select"] > div:hover {
    border-color: #ff66b2 !important;
}
/* selected text */
div[data-baseweb="select"] span {
    color: #1f2a44 !important;
    font-weight: 500;
}
/* focus */
div[data-baseweb="select"] > div:focus-within {
    box-shadow: 0 0 0 3px rgba(255, 20, 147, 0.15) !important;
    border-color: #ff1493 !important;
}
/* selected text */
div[data-baseweb="select"] span {
    color: #1f2a44 !important;
    font-weight: 500;
}
/* MULTISELECT TAG */
span[data-baseweb="tag"] {
    background-color: #FFD6E8 !important;
    color: #c71585 !important;
    border-radius: 8px !important;
    border: 1px solid #FFB3DA !important;
}
/* dấu x */
span[data-baseweb="tag"] svg {

    color: #c71585 !important;
}
/* disable legend cursor */

.legendtoggle {

    cursor: default !important;
}
</style>
""", unsafe_allow_html=True)
# ===== PAGE STATE =====
if "page" not in st.session_state:
    st.session_state.page = "home"
# ===== LANDING =====
if st.session_state.page == "home":
    st.markdown("""
    <style>
    /* BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #ffe0f0 0%, #fff0f6 50%, #fce4ec 100%);
    }
    /* ẨN HEADER STREAMLIT */
    header {
        visibility: hidden;
    }
    /* LEFT CONTENT */
    .hero-left {
        width: 100%;
        text-align: center;
        padding-top: 6vh;   
        padding-left: 8%;
        padding-right: 8%;
    }
    /* TITLE */
    .big-title {
        font-size: 55px;
        font-weight: 800;
        color: #d81b60;
        margin-bottom: 15px;
    }
    /* INTRODCTION */
    .welcome-text {
        font-size: 36px;
        font-weight: 700;
        color: #6d214f;
        margin-bottom: 15px;
    }
    /* PARAGRAPH */
    .intro-text {
        font-size: 18px;
        color: #6d214f;
        line-height: 1.7;
        margin-bottom: 30px;
    }
    /* BUTTON */
    div.stButton > button {
        background-color: #FF1493;
        color: white;
        padding: 12px 28px;
        border-radius: 12px;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)
    # layout 2 cột
    col1, col2 = st.columns([1, 1])
    # LEFT
    with col1:
        st.markdown('<div class="hero-left">', unsafe_allow_html=True)
        st.markdown('<div class="big-title">SHOPPING ANALYSIS 🛒</div>', unsafe_allow_html=True)
        st.markdown('<div class="welcome-text">INTRODUCTION</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="intro-text">
        Hello there! Welcome to Our Shopping Insights Journey!<br>
        We are so excited to have you here! This project is our first deep dive into the world of shopping behavior, where we’ve turned thousands of data points into a colorful story about how people shop. Whether you’re curious about which products are trending or how different age groups prefer to pay, our interactive charts are here to show you the way. Take a look around, play with the data, and we hope you find these insights as fascinating as we did while building this for you!
        </div>
        """, unsafe_allow_html=True)
        if st.button("Let's Get Started!"):
            st.session_state.page = "dashboard"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    # RIGHT
    with col2:
     st.markdown("""
     <div style="display:flex; justify-content:center;">
        <img src="https://images.unsplash.com/photo-1607082349566-187342175e2f?w=1200&q=80&auto=format"
             style="width:100%; transform: translateY(50px);">
     </div>
    """, unsafe_allow_html=True)
#====== BACK BUTTON=======
elif st.session_state.page == "gift":
    st.markdown(
        """
        <div style="text-align:center; padding-top:100px;">
            <h1 style="color:#d81b60;">💖 Thank You 💖</h1>
        <p style="font-size:20px;">
            Our gift to you is… <br>
            The appreciation from all five members of our team!!! <br>
            Thank you for visiting our website!<br>
            We truly appreciate your time exploring our Shoplytics.<br>
            Hope you enjoyed it as much as we enjoyed building it! <br><br>
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("⬅ Back to Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
# ===== DASHBOARD =====
elif st.session_state.page == "dashboard":
    st.markdown("""
    <style>
    /* SIDEBAR nền */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff0f5 0%, #ffe4ec 100%);
        padding: 25px 20px;
    }
    /*  CATEGORY */
    .category-title {
        text-align: center;
        font-size: 30px;
        font-weight: 900;
        color: #ff4da6;
        margin-bottom: 10px;
    }
    /*  ICON */
    .sparkle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 10px;
    }
    /*  AGE LABEL */
    .age-label {
        font-size: 20px;
        font-weight: 800;
        color: #444;
        margin-top: 10px;
        margin-bottom: 10px;
        text-align: center;
    }
    /*  LINE */
    .divider {
        height: 1px;
        background: #f8a5c2;
        margin: 20px 0;
        border-radius: 10px;
    }
    /*  SLIDER  */
    section[data-testid="stSidebar"] .stSlider {
        transform: none !important;
    }
    /*  BUTTON */
    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        border-radius: 18px;
        background: linear-gradient(45deg, #ff4da6, #ff85c1);
        color: white;
        font-weight: 700;
        font-size: 16px;
        padding: 12px;
        border: none;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        box-shadow: 0 5px 15px rgba(255, 77, 166, 0.4);
    }
    /*  BACKGROUND MAIN */
    .stApp {
        background: linear-gradient(135deg, #FFF0F6 0%, #F0F9FF 100%);
    }
    section[data-testid="stSidebar"] > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    df = pd.read_csv("shopping_behavior_updated.csv")
    st.title("")
    # ===== CSS (PHẢI ĐẶT TRONG DASHBOARD) =====
    st.markdown("""
    <style>
    button[data-baseweb="tab"] {
        font-weight: 700;
        font-size: 16px;
        margin-right: 20px;
    }
    button[aria-selected="true"] {
        color: #FF1493;
    }
    </style>
    """, unsafe_allow_html=True)
    # ===== SIDEBAR =====
    with st.sidebar:
     st.markdown("""
<div style="
    text-align:center;
    font-size:30px;
    font-weight:900;
    color:#ff4da6;
">
<span style="font-size:18px;">✨</span>
 CATEGORY 
<span style="font-size:18px;">✨</span>
</div>
""", unsafe_allow_html=True)
     st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
     st.markdown('<div class="age-label">AGE RANGE</div>', unsafe_allow_html=True)
     age_range = st.slider(
        "",
        int(df["Age"].min()),
        int(df["Age"].max()),
        (18, 30),
        step = 1
    )
     st.markdown( '<div class="divider"></div>', unsafe_allow_html=True)
     st.markdown('<div class="age-label">GENDER</div>', unsafe_allow_html=True)
     gender_filter = st.multiselect(
        "",
        options=["Male", "Female"],
        default=["Male", "Female"]
    )
     filtered_df = df[
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1]) &
    (df["Gender"].isin(gender_filter))
    ]
     st.markdown( "<div style='height:25px'></div>", unsafe_allow_html=True )
     st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
     col1, col2, col3 = st.columns([1, 2, 1])
     with col2:
        if st.button("Click here for gift!"):
            st.session_state.page = "gift"
            st.rerun()
    # ===== TABS =====
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "**PURCHASE TREND**",
        "**PRODUCT**",
        "**PAYMENT & SHIPPING**",
        "**REVIEW RATING**",
        "**DATA FRAME**"
    ])
    # ===== TAB 1 =====
    with tab1:
        st.markdown(
            """
         <h2 style="
           color:#d81b60;
           font-weight:700;
           font-family:Arial;
           margin-bottom:10px;
         ">
           PURCHASE TREND 📊
         </h2>
         """,
         unsafe_allow_html=True
        )
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
         st.subheader("**Purchase Frequency**")
         selected_frequency = st.multiselect(
                label="Frequency of Purchases",
                options=["Weekly","Quarterly","Monthly","Fortnightly","Every 3 Months","Bi-Weekly","Annually","Select All"],
                default=[], 

                placeholder="Select option"
            )
         if (
                len(selected_frequency) == 0
                or "Select All" in selected_frequency
            ):
               filtered_frequency_df = filtered_df
         else:
               filtered_frequency_df = filtered_df[
                    filtered_df["Frequency of Purchases"].isin(selected_frequency)
                ]      
         fig = plot_stacked_area( filtered_frequency_df )
         st.plotly_chart( fig, use_container_width=True )
         st.markdown(
            "<p style='font-size:16px; color:black;'>This chart visualizes the relationship between shopping frequency and the amount spent by customers. It helps in understanding how different purchasing habits, ranging from weekly to annually, contribute to various purchase amount tiers.</p>",
            unsafe_allow_html=True
         )
        with col2:
         st.subheader("**Purchase Amount by Season**")
         st.markdown("<br>", unsafe_allow_html=True)
         fig = plot_purchase_boxplot(filtered_df)
         st.plotly_chart(fig, use_container_width=True)
         st.markdown(
            "<p style='font-size:16px; color:black;'>The plot displays the spread and central tendency of customer spending across the four seasons. It provides a visual summary of purchase amounts, helping to identify seasonal trends and variations in overall customer expenditure.</p>",
            unsafe_allow_html=True
         )
    # ===== TAB 2 =====
    with tab2:
        st.markdown(
            """
         <h2 style="
           color:#d81b60;
           font-weight:700;
           font-family:Arial;
           margin-bottom:10px;
         ">
           PRODUCT ANALYSIS 🛍️
         </h2>
         """,
         unsafe_allow_html=True
        )
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
            st.subheader("**Product Categories**")
            selected_category = st.multiselect(
                label="Category",
                options=["Clothing","Accessories","Footwear","Outwear"],
                default=[],
                placeholder="Select option"
            )
            if len(
                selected_category) == 0:
                filtered_category_df = filtered_df
            else:
                filtered_category_df = filtered_df[
                    filtered_df["Category"].isin(selected_category)
                ]      
            fig = plot_categories_by_gender(filtered_category_df)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(
               "<p style='font-size:16px; color:black;'>This chart illustrates the shopping preferences of male and female customers across four main product categories.</p>",
               unsafe_allow_html=True
            )
        with col2:
            st.subheader("**Size Distribution**")
            st.markdown("<br><br>", unsafe_allow_html=True)
            fig = plot_size_by_gender(filtered_df)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(
               "<p style='font-size:16px; color:black;text-align:justify'>The plot displays the distribution of clothing sizes purchased by customers. It helps in understanding the demand for various sizes across different groups.</p>",
               unsafe_allow_html=True
            )
    # ===== TAB 3 =====
    with tab3:
        st.markdown(
            """
         <h2 style="
           color:#d81b60;
           font-weight:700;
           font-family:Arial;
           margin-bottom:10px;
         ">
          💳 PAYMENT & SHIPPING TYPE 🚚
         </h2>
         """,
         unsafe_allow_html=True
        )
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
            st.subheader("**Payment Method**")
            fig = plot_payment_methods(filtered_df)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(
               "<p style='font-size:16px; color:black;text-align:justify'>This plot compares the total number of transactions completed using various payment methods. It provides a clear ranking of preferred payment options, helping to identify how customers most commonly choose to pay for their purchases.</p>",
               unsafe_allow_html=True
            )
        with col2:
            st.subheader("**Shipping Type**")
            st.markdown(
               """
              """,
             unsafe_allow_html=True
            )     
            fig = plot_shipping_pie(filtered_df)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown(
               "<p style='font-size:16px; color:black;text-align:justify'>This chart illustrates the proportion of various delivery methods selected by customers. It helps in understanding customer preferences for shipping speed and convenience by showing the relative popularity of each available option.</p>",
               unsafe_allow_html=True
            )
    # ===== TAB 4 =====
    with tab4:
     st.markdown(
            """
         <h2 style="
           color:#d81b60;
           font-weight:700;
           font-family:Arial;
           margin-bottom:10px;
         ">
           REVIEW RATING ⭐
         </h2>
         """,
         unsafe_allow_html=True
        )
     col1, col2 = st.columns([1, 1], gap="large")
     with col1:
        fig = plot_review_by_gender(filtered_df)
        st.plotly_chart(fig, use_container_width=True)
     with col2:
        st.markdown("""
        <div style='display:flex; align-items:center; height:400px;'>
           <div style='font-size:16px; color:black; text-align:justify;line-height:1.6;'>
             The plot displays the distribution of clothing sizes purchased by customers. It helps in understanding the demand for various sizes across different groups. 
           </div>
        </div>
        """, unsafe_allow_html=True)
# ===== TAB 5 =====
    with tab5:
     st.markdown(
            """
         <h2 style="
           color:#d81b60;
           font-weight:700;
           font-family:Arial;
           margin-bottom:10px;
         ">
           THE DATA FRAME
         </h2>
         """,
         unsafe_allow_html=True
        )
     st.dataframe(df, use_container_width=True)
     st.write("Rows:", df.shape[0], "| Columns:", df.shape[1])
