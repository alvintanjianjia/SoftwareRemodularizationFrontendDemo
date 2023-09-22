import streamlit as st
import numpy as np
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################

from PIL import Image


###################################

def app():

    
    # def _max_width_():
    #     max_width_str = f"max-width: 1800px;"
    #     st.markdown(
    #         f"""
    #     <style>
    #     .reportview-container .main .block-container{{
    #         {max_width_str}
    #     }}
    #     </style>    
    #     """,
    #         unsafe_allow_html=True,
    #     )

    closest_results = pd.read_csv('closest_results.csv')
    #print(closest_results.head())
    closest_results = closest_results.astype(object)
    #st.text("Project Details")
    #st.table(closest_results)
    st.text("Best clustering algorithm & its parameters")
    st.table(closest_results[['cluster_division','affinity','linkage']])

    st.text("ESC4R: Project is trained on ")
    st.table(closest_results[['project_name']])
    
    #image = Image.open('../images/combined_algorithm_spread.png')
    import os
    print(os.getcwd())
    image = Image.open(os.getcwd() + '/streamlit/src/combined_algorithm_spread.png')

    st.image(image, caption='Algorithm Visualisation') 

    c29, c30, c31 = st.columns([1, 6, 1])

    from st_aggrid import GridUpdateMode, DataReturnMode
    shows = pd.read_csv('pipeline_prediction_output.csv')
    shows = shows.astype(object)
    shows = shows[['predicted_time', 'class_name', 'file', 'class', 'Current_Package', 'New_Destination_Package']]
    gb = GridOptionsBuilder.from_dataframe(shows[['predicted_time', 'class_name', 'file', 'class', 'Current_Package', 'New_Destination_Package']])
    
    # enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
    gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    #gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
    #gb.configure_auto_height(10)
    gb.configure_pagination(paginationPageSize=10)
    
    gridOptions = gb.build()

    st.success(
        f"""
            💡 Tip! Hold the shift key when selecting rows to select multiple rows at once!
            """
    )

    response = AgGrid(
        shows,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=True,
    )

    df = pd.DataFrame(response["selected_rows"])
    df = df.astype(object)

    st.subheader("Filtered data will appear below 👇 ")
    st.text("")

    st.table(df)

    st.text("")

    try:
        total_predicted_time = df['predicted_time'].sum()
        st.text("Total predicted time: " + str(total_predicted_time))
    except:
        st.text("Please select a refactoring operation.")

    c29, c30, c31 = st.columns([1, 1, 2])

    with c29:

        CSVButton = download_button(
            df,
            "File.csv",
            "Download to CSV",
        )

    with c30:
        CSVButton = download_button(
            df,
            "File.csv",
            "Download to TXT",
        )