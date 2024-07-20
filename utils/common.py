import base64
import psycopg2
import streamlit as st
import pandas as pd
from .credentials import db_dbname, db_user, db_password, db_host, db_port
def replace_image(file_path, file_type):
    """Read and convert image files to base64-encoded strings."""
    if file_type == "svg":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        with open(file_path, "rb") as file:
            return f"data:image/jpeg;base64,{base64.b64encode(file.read()).decode('utf-8')}"
# Fungsi untuk memuat data dari database
def load_data(query):
    try:
        connection = psycopg2.connect(
            dbname=db_dbname,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(records, columns=columns)
        return df
    except psycopg2.Error as e:
        st.error(f"Error connecting to PostgreSQL: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()