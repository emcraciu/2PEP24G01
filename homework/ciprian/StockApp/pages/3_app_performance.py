import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

import streamlit_authenticator as stauth
from homework.ciprian.StockApp import config_data
from homework.ciprian.tests.run_pylint import run_pylint_test

def main() -> None:
    config = config_data.Users(), config_data.Cookies(), config_data.Preauthorized()
    authenticator = stauth.Authenticate(
        config[0]['credentials'],
        config[1]['cookie'].get('csporea', {}).get('name', 'user_name'),
        config[1]['cookie'].get('csporea', {}).get('key', 'user_key'),
        config[1]['cookie'].get('csporea', {}).get('expiry_days', 30),
        config[2]['pre-authorized']
    )
    authenticator.login()

    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.header("App Performance :bar_chart:")
        # st.markdown("# App Performance")
        st.sidebar.markdown("# App Performance")

        df_logs = pd.read_csv('./StockApp/logfile.csv')
        func_list = df_logs[df_logs['funcname'].str.contains('[a-zA-Z]')]['funcname'].sort_values().unique()

        col1, col2, col3, col4 = st.columns([0.8, 0.1, 0.5, 0.5])
        choose_func = col1.selectbox('Choose function name to analyse it\'s execution time', func_list,
                                    help='')

        st.subheader('**time performance**')

        df = df_logs.loc[df_logs['funcname'] == choose_func]
        df.insert(df.shape[1], 'id', np.array(np.arange(1, df.shape[0] + 1)))

        total_time_card = df
        col3.metric(
            "Total time of execution",
            f"{total_time_card['executiontime'].sum():.4f} ",
            f"sec",
                    )

        col4.metric(
            "Total # executions",
            f"{df.shape[0]} ",
            f"func calls",
        )


        fig = px.scatter(df, x='id', y='executiontime')
        st.plotly_chart(fig, key="iris", on_select="rerun")

        with st.expander("View your data as a Dataframe"):
            st.write(df)

        st.subheader('**unit test performance**')
        col1a, col2a, col3a, col4a = st.columns([0.8, 0.1, 0.5, 0.5])
        dir_URL = Path(r"C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\\")
        filename_list = [file.name for file in dir_URL.glob("*.py")]
        choose_test_file = col1a.selectbox('Choose python file to run pylint test', filename_list, help='')

        total_time_card = df
        col3a.metric(
            "Total time of execution",
            f"{run_pylint_test(str(choose_test_file))} ",
            f"sec",
        )


    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')


if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
    				page_icon=':bar_chart:', layout='wide')

    main()