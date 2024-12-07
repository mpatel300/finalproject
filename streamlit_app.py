import streamlit as st

# Title of the page
st.title("YouTube Statistics")

# This shows the websites desc. along with a message.
st.write(" This website is a showcase and indepth view of Youtube Stats from many different variables, the insight that can be found in the different tabs can help someone
who already has a youtube channel or someone who wants to take there youtube channel to the next level.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to section:", ["Global Viewership Data", "Section 2", "Section 3", "Section 4"])

if page == "Global Viewership Data":
    st.image("Map.png", caption="Global Viewership Data (World-Wide)", use_column_width=True)
    st.write(" This is the World Global Viewship Data, in this data you can find the following ...
        ")
