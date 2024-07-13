import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

import streamlit_authenticator as stauth
from homework.ciprian.StockApp import config_data


def main() -> None:
    config = config_data.Users(), config_data.Cookies(), config_data.Preauthorized()
    authenticator = stauth.Authenticate(
        config[0]['credentials'],
        config[1]['cookie']['csporea']['name'],
        config[1]['cookie']['csporea']['key'],
        config[1]['cookie']['csporea']['expiry_days'],
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
        func_list = df_logs['funcname'].unique()

        col1, col2, col3, col4 = st.columns([0.8, 0.1, 0.5, 0.5])
        choose_func = col1.selectbox('Choose function name to analyse it\'s execution time', func_list,
                                    help='')

        st.subheader('**time performance**')

        df = df_logs.loc[df_logs['funcname'] == choose_func]
        df.insert(df.shape[1], 'id', np.array(np.arange(1, df.shape[0] + 1)))

        total_time_card = df.iloc[-1:].groupby('funcname', as_index=False).sum()
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


    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')


if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
    				page_icon=':bar_chart:', layout='wide')

    main()