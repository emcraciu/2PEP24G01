import streamlit as st
import streamlit_authenticator as stauth
import numpy as np

from homework.ciprian.StockApp import config_data


def main() -> None:

    st.header("User Account Management :bar_chart:")
    # st.markdown("# App Performance")
    st.sidebar.markdown("# User Account Management")

    config = config_data.Users(), config_data.Cookies(), config_data.Preauthorized()
    authenticator = stauth.Authenticate(
        config[0]['credentials'],
        config[1]['cookie'].get('csporea', {}).get('name', 'user_name'),
        config[1]['cookie'].get('csporea', {}).get('key', 'user_key'),
        config[1]['cookie'].get('csporea', {}).get('expiry_days', 30),
        config[2]['pre-authorized']
    )

    # new user registration widget
    try:
        existing_users = list(config[0]['credentials']['usernames'].keys())
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
            pre_authorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')

            new_user = np.setdiff1d(list(config[0]['credentials']['usernames'].keys()), existing_users)[0]
            username1 = new_user
            password1 = config[0]['credentials']['usernames'][new_user]['password']
            email1 = config[0]['credentials']['usernames'][new_user]['email']
            name1 = config[0]['credentials']['usernames'][new_user]['name']
            config_data.insertUser(username1, password1, email1, name1)
    except Exception as e:
        st.error(e)

    # reset password widget
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(st.session_state["username"]):
                st.success('Password modified successfully')
        except Exception as e:
            st.error(e)

    # forgot password widget
    try:
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
        if username_of_forgotten_password:
            st.success('New password to be sent securely')
            # The developer should securely transfer the new password to the user.
        elif username_of_forgotten_password == False:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    # forgot username widget
    try:
        username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
        if username_of_forgotten_username:
            st.success('Username to be sent securely')
            # The developer should securely transfer the username to the user.
        elif username_of_forgotten_username == False:
            st.error('Email not found')
    except Exception as e:
        st.error(e)

    # update user details widget
    if st.session_state["authentication_status"]:
        try:
            if authenticator.update_user_details(st.session_state["username"]):
                st.success('Entries updated successfully')
        except Exception as e:
            st.error(e)



if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
    				page_icon=':bar_chart:', layout='wide')

    main()