import streamlit as st

# Title of the page
st.title(":red[YouTube] Statistics")


# This part of the code is for the navigation tab/dropdown menu
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Please select your tab!", ["Overview", "Global Viewership Data", "Categories By the Popularity", "Viewership Subscribers", "Categories by Average Monthly Earning"])

#Page Overview Code
if page == "Overview":
    st.write("Welcome to ultimate YouTube Statistic App, your ultimate companion for YouTube growth and insights! Unlock the power of data to supercharge your channel’s performance and creativity. This app is designed to empower content creators like you by providing in-depth analytics, actionable insights, and trend-driven recommendations. Whether you're just starting your YouTube journey or striving to take your channel to the next level, we've got everything you need to thrive in the competitive world of content creation. Get ready to transform your ideas into results, uncover hidden opportunities, and connect with your audience like never before. Your next big milestone starts here!")
    st.image("background.1.png", use_column_width=True)

#Page Global Viewership Data Code
elif page == "Global Viewership Data":
    st.write("This provides a comprehensive look at YouTube audience trends across the globe. This feature is perfect for creators who want to expand their reach and create content that resonates with an international audience. What You’ll Discover, Regional Trends: See which types of content perform best in different countries and regions.Audience Insights: Understand global viewer preferences, habits, and engagement patterns. Growth Opportunities: Identify untapped markets and tailor your content to attract diverse audiences worldwide.Whether you're planning to localize your content or broaden your appeal, this tab equips you with the insights to grow your channel on a global scale.")
    st.image("Global Viewership Data.png", caption="Global Viewership Data (World-Wide)", use_column_width=True)
    
    st.write("""
    **What You’ll Discover:**
    - **Regional Trends:** See which types of content perform best in different countries and regions.
    - **Audience Insights:** Understand global viewer preferences, habits, and engagement patterns.
    - **Growth Opportunities:** Identify untapped markets and tailor your content to attract diverse audiences worldwide.
    
      Whether you're planning to localize your content or broaden your appeal, this tab equips you with the insights to grow your channel on a global scale.  
    """)

#Page Categories by the popularity Code
elif page == "Categories By the Popularity":
    st.write("This page gives you a clear view of which YouTube content categories are trending and performing well. This feature is perfect for creators looking to align their content with audience preferences and capitalize on popular trends.")
    st.image("Categories By the Popularity.1.png", caption="Categories By the Popularity", use_column_width=True)
    st.image("Categories By the Popularity.2.png", caption="Categories By the Popularity", use_column_width=True)
    st.image("Categories By the Popularity.3.png", caption="Categories By the Popularity", use_column_width=True)

    st.write("""
    **What You’ll Find:**
    - **Top Performing Categories:** Discover the most popular niches and topics driving engagement and growth on YouTube.
    - **Insights for Strategy:** Understand which categories resonate with viewers and how you can tailor your content to match their interests.
    - **Trend Spotting:** Stay ahead of the curve by identifying rising trends and emerging content themes.
    
        Whether you're brainstorming new video ideas or refining your niche, this tab is your gateway to staying competitive and relevant in the ever-evolving YouTube landscape.
    """)


#Page Viewership Subscribers Code
elif page == "Viewership Subscribers":
    st.write("This page provides valuable insights into the relationship between audience engagement and subscriber growth. This feature is essential for creators looking to understand their viewers better and convert them into loyal subscribers.")
    st.image("Viewership Subscribers.png", caption="describe the photo by text here", use_column_width=True)
    st.image("Viewership Subscribers.2.png", caption="describe the photo by text here", use_column_width=True)
    st.image("Viewership Subscribers.3.png", caption="describe the photo by text here", use_column_width=True)
    st.image("Viewership Subscribers.4.png", caption="describe the photo by text here", use_column_width=True)
    st.image("Viewership Subscribers.5.png", caption="describe the photo by text here", use_column_width=True)
    st.image("Viewership Subscribers.6.png", caption="describe the photo by text here", use_column_width=True)

    st.write("""
    **What You’ll Learn:**
    - **Viewership Trends:** Analyze how views translate into subscriber growth across different content types.
    - **Engagement Insights:** Discover what keeps viewers watching and encourages them to subscribe to your channel.
    - **Optimization Tips:** Get data-driven recommendations to improve your content strategy and boost subscriber numbers.
    
        Whether you're aiming to grow your channel or retain your audience, this tab gives you the tools to turn casual viewers into a thriving community of subscribers.
    """)


#Page Categories by Average Monthly Earning
elif page == "Categories by Average Monthly Earning":
    st.write("This page is your go-to resource for understanding the revenue potential across different YouTube niches. This feature is ideal for creators aiming to maximize their monetization strategy and align their content with high-earning categories.")
    st.image("Monthly Earning.png", caption="describe the photo by text here", use_column_width=True)


    st.write("""
    **What You’ll Discover:**
    - **Earnings Insights by Category:** Explore which content types generate the highest average monthly revenue.
    - **Strategic Content Planning:** Identify profitable niches and adapt your content to capitalize on lucrative opportunities.
    - **Monetization Potential:** Understand how category performance ties to sponsorships, ads, and viewer engagement
    
        Whether you're optimizing your current channel or deciding on a niche to focus on, this tab equips you with the knowledge to make informed, revenue-driven decisions for your YouTube journey.  
    """)




