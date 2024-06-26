import streamlit as st
import numpy as np
import pandas as pd



def main() -> None:
    st.header("Cripto Analytics :bar_chart:")
    st.markdown("# Cripto Analytics")
    st.sidebar.markdown("# Cripto Analytics")



if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
    				page_icon=':bar_chart:', layout='wide')

    main()