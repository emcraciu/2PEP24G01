import streamlit as st
import streamlit_authenticator as stauth

from homework.ciprian.StockApp import config_data
from homework.ciprian.StockApp.decorators import log_time_decorator


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

        st.header("Cripto Analytics :bar_chart:")
        st.markdown("# Cripto Analytics")
        st.sidebar.markdown("# Cripto Analytics")

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
    				page_icon=':bar_chart:', layout='wide')

    main()