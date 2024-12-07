import streamlit as st

# Title of the page
st.title(":red[YouTube] Statistics")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["**Overview**", "**Global Viewership Data**", "**Categories By the Popularity**", "**Viewership Subscribers**", "**Categories by Average Monthly Earning**"])

if page == "**Overview**":
    st.write("
Welcome to my app, your ultimate companion for YouTube growth and insights! Unlock the power of data to supercharge your channel’s performance and creativity. This app is designed to empower content creators like you by providing in-depth analytics, actionable insights, and trend-driven recommendations. Whether you're just starting your YouTube journey or striving to take your channel to the next level, we've got everything you need to thrive in the competitive world of content creation. Get ready to transform your ideas into results, uncover hidden opportunities, and connect with your audience like never before. Your next big milestone starts here!")
    st.image("background.1.png", use_column_width=True)

elif page == "**Global Viewership Data**":
    st.write("This website is a showcase and indepth view of Youtube Stats from many different variables, the insight that can be found in the different tabs can help someone who already has a youtube channel or someone who wants to take there youtube channel to the next level.")
    st.image("Global Viewership Data.png", caption="Global Viewership Data (World-Wide)", use_column_width=True)
    st.write("This is the World Global Viewship Data, in this data you can find the following ...")

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
