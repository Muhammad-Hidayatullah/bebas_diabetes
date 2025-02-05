from base64 import b64encode
from fpdf import FPDF
import streamlit as st
import pandas as pd
from assets import database as db
import numpy as np


st.dataframe(db.cek_get_diagnosis_penyakit("PS002"))