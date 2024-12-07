import streamlit as st

# Title of the page
st.title(":red[YouTube] Statistics")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["Global Viewership Data", "Categories By the Popularity", "Viewership to Subscriber Ratio by Country", "Section 4"])

if page == "Global Viewership Data":
    st.write("This website is a showcase and indepth view of Youtube Stats from many different variables, the insight that can be found in the different tabs can help someone who already has a youtube channel or someone who wants to take there youtube channel to the next level.")
    st.image("Map.png", caption="Global Viewership Data (World-Wide)", use_column_width=True)
    st.write("This is the World Global Viewship Data, in this data you can find the following ...")

elif page == "Categories By the Popularity":
    st.image("Categories By the Popularity.png", caption="Categories By the Popularity", use_column_width=True)
    st.write("With the popularity")

elif page == "Viewership to Subscriber Ratio by Country":
    st.image("https://picsum.photos/800/402", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.33333333333
    """)

elif page == "Section 4":
    st.image("https://picsum.photos/800/403", caption="describe the photo by text here", use_column_width=True)
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero.444444444444444
    """)
