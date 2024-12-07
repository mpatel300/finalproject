import streamlit as st

# Title of the page
st.title(":red[YouTube] Statistics")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["Global Viewership Data", "Section 2", "Section 3", "Section 4"])

if page == "Overview":
    st.write("Welcome to my app, your ultimate companion for YouTube growth and insights! This app is designed to empower content creators by providing in-depth analytics and actionable insights. Whether you're just starting your YouTube journey or looking to take your channel to the next level.")
    
elif page == "Global Viewership Data":
    st.write("This website is a showcase and indepth view of Youtube Stats from many different variables, the insight that can be found in the different tabs can help someone who already has a youtube channel or someone who wants to take there youtube channel to the next level.")
    st.image("Map.png", caption="Global Viewership Data (World-Wide)", use_column_width=True)
    st.write("This is the World Global Viewship Data, in this data you can find the following ...")


elif page == "Categories By the Popularity":
    st.image("https://picsum.photos/800/401", caption="describe the photo by text here", use_column_width=True)
    st.write("")

elif page == "Section 3":
    st.image("https://picsum.photos/800/402", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.33333333333
    """)

elif page == "Section 4":
    st.image("https://picsum.photos/800/403", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.444444444444444
    """)
