import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

def gsheet_auth():
    creds = {
        'type': st.secrets["type"],
        'project_id': st.secrets["project_id"],
        'private_key_id': st.secrets["private_key_id"],
        'private_key': st.secrets["private_key"].replace('\\n', '\n'),
        'client_email': st.secrets["client_email"],
        'client_id': st.secrets["client_id"],
        'auth_uri': st.secrets["auth_uri"],
        'token_uri': st.secrets["token_uri"],
        'auth_provider_x509_cert_url': st.secrets["auth_provider_x509_cert_url"],
        'client_x509_cert_url': st.secrets["client_x509_cert_url"]
    }

    scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_info(creds, scopes=scope)

    client = gspread.authorize(creds)

    return client

