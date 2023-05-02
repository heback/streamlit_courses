# 인터넷 연결 오류시
# pip install --upgrade certifi

import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, \
    AgGrid, GridUpdateMode, DataReturnMode
import sqlite3

con = sqlite3.connect('user.db')
cur = con.cursor()

data = pd.read_sql('SELECT * FROM users', con)

gb = GridOptionsBuilder.from_dataframe(data)
gb.configure_default_column(editable=True)
# Add pagination
gb.configure_pagination(paginationAutoPageSize=True)
# Add a sidebar
gb.configure_side_bar()
# Enable multi-row selection
gb.configure_selection(
    'multiple',
    use_checkbox=True,
    groupSelectsChildren="Group checkbox select children"
)
gridOptions = gb.build()

grid_response = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT',
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=False,
    # Add theme color to the table
    theme='blue',
    enable_enterprise_modules=True,
    height=350,
    reload_data=False,

)

data = grid_response['data']
selected = grid_response['selected_rows']
# Pass the selected rows to a new dataframe df
df = pd.DataFrame(selected)
st.write(df)

