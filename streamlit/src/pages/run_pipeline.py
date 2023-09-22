import streamlit as st
import numpy as np
import pandas as pd
import validators
#import papermill as pm
import time



def app():

    def execute_notebook():
        st.text("Running..... Please wait....")
        #time.sleep(2)
        # pm.execute_notebook(
        #         'Pipeline_Tool_Notebook.ipynb',
        #         'Pipeline_Tool_Notebook_Output.ipynb',
        #         parameters=dict(github_link=user_github_link)
        #     )
        return True


    st.markdown("**For demonstrative purposes only. Results displayed are exclusively representative of Dropwizard, owing to the constrained capabilities of online public hosting services, irrespective of the input URL.**")

    user_github_link = st.text_input('GitHub URL', '')
    if validators.url(user_github_link) is True and 'github' in user_github_link:
        if st.button('Run Tool.'):
            completed = execute_notebook()
            if completed:
                st.markdown('Completed!')
                
                st.markdown('Please view results via the "View Results tab from the left panel.')

                st.markdown('**Gentle Reminder! Due to limited capabilities of online public hostin services, the results shown are specifically for Dropwizard regardless of input URL.**')
        
            
        
    else:
        st.info(
            f"""
                👆 Please input a valid Github URL.
                """
        )

        st.stop()