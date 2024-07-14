import streamlit as st
from cwe import css

st.write(css, unsafe_allow_html=True)

def main():
    
    try:
        st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    except:
        pass

    st.write("# Welcome, I'm E.D.I.T.H 👋")

    st.image("hero-animation.gif")

if __name__=="__main__":
    main()
