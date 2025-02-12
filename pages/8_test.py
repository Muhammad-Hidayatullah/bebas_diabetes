#return bytes(pdf.output())

#return pdf.output(dest="S").encode("latin1")

import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Class": ["10A", "11B", "12C"],
    "Student ID": [101, 102, 103],
    "Birthdate": ["2005-01-01", "2004-02-15", "2003-03-22"],
    "Birthcity": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Drop unnecessary columns
df_cleaned = df.drop(columns=["Birthdate", "Birthcity"])

# Custom CSS for styling
table_style = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
            font-size: 16px;
        }
        th {
            background-color: green;
            color: white;
            padding: 10px;
            text-align: left;
        }
        td {
            background-color: white;
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        tr:nth-child(even) td {
            background-color: #f9f9f9; /* Light gray for alternating rows */
        }
    </style>
"""

# Convert DataFrame to HTML
table_html = df_cleaned.to_html(index=False, escape=False)

# Display in Streamlit
st.markdown(table_style + table_html, unsafe_allow_html=True)
