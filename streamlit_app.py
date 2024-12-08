import streamlit as st

# Title of the page
st.title(":red[YouTube] Statistics")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["**Overview**", "**Global Viewership Data**", "**Categories By the Popularity**", "**Viewership Subscribers**", "**Categories by Average Monthly Earning**"])

if page == "**Overview**":
    st.write("Welcome to ultimate YouTube Statistic App, your ultimate companion for YouTube growth and insights! Unlock the power of data to supercharge your channel’s performance and creativity. This app is designed to empower content creators like you by providing in-depth analytics, actionable insights, and trend-driven recommendations. Whether you're just starting your YouTube journey or striving to take your channel to the next level, we've got everything you need to thrive in the competitive world of content creation. Get ready to transform your ideas into results, uncover hidden opportunities, and connect with your audience like never before. Your next big milestone starts here!")
    st.image("background.1.png", use_column_width=True)

elif page == "**Global Viewership Data**":
    st.write("This provides a comprehensive look at YouTube audience trends across the globe. This feature is perfect for creators who want to expand their reach and create content that resonates with an international audience. What You’ll Discover, Regional Trends: See which types of content perform best in different countries and regions.Audience Insights: Understand global viewer preferences, habits, and engagement patterns. Growth Opportunities: Identify untapped markets and tailor your content to attract diverse audiences worldwide.Whether you're planning to localize your content or broaden your appeal, this tab equips you with the insights to grow your channel on a global scale.")
    st.image("Global Viewership Data.png", caption="Global Viewership Data (World-Wide)", use_column_width=True)
    st.write("""
    **What You’ll Discover:**
    - Regional Trends: See which types of content perform best in different countries and regions.
    - Audience Insights: Understand global viewer preferences, habits, and engagement patterns.
    - Growth Opportunities: Identify untapped markets and tailor your content to attract diverse audiences worldwide.
    
      Whether you're planning to localize your content or broaden your appeal, this tab equips you with the insights to grow your channel on a global scale.  
    """)

elif page == "**Categories By the Popularity**":
    st.image("Categories By the Popularity.png", caption="Categories By the Popularity", use_column_width=True)
    st.write("With the popularity")

elif page == "**Viewership Subscribers**":
    st.image("https://picsum.photos/800/402", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.33333333333
    """)

elif page == "**Categories by Average Monthly Earning**":
    st.image("https://picsum.photos/800/403", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.444444444444444
    """)
