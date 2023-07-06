# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:55:20 2023

@author: Yahwah Nissi
"""

import streamlit as st
import io
import pandas as pd
import numpy as np
from streamlit import session_state
from streamlit_extras.add_vertical_space import add_vertical_space


import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
#import matplotlib.pyplot as pltst.title(‘Upoading master data’)

#def load_train(nrows):
cols = ['AP','norm_AP','logP','norm_logP','norm_abs_logP','norm_bscore','net_chg',
        'abs_chg','patterning','class_label','IR_score']
#train_file_reading
#def train_data():
df_train = pd.read_csv('train_full_data.csv',index_col=0)
 #   return None#st.write(df_train)
#df_train = df_train(df_train(cols))
#session_state.df_train = df_train

def filter_columns():
    col_names = list()
    categorical_detail = df_train.dtypes
    for i in range(len(categorical_detail)):
        if (categorical_detail[i] != "object"):
            col_names.append(df_train.columns[i])
    return col_names

def show_graph(x_column, y_columns):
    fig, ax = plt.subplots()
    for i in range(len(y_columns)):
        ax.scatter(df_train[x_column],
                   df_train[y_columns[i]], label=y_columns[i])
    ax.legend()
    ax.grid(True)
    plt.title("Scatter plot")
    plt.xlabel(x_column)
    plt.ylabel(y_columns)
    st.pyplot(fig)
        
    
def show_correlation_matrix(columns, filtered_col):
    if (len(columns) == 0):
        st.write("Please select a column")
    else:

        if "All" not in columns:
            correlation = df_train[columns].corr()
        else:
            correlation = df_train[filtered_col].corr()

        fig = plt.figure(figsize=(20, 20))
        sns.heatmap(correlation, xticklabels=correlation.columns,
                    yticklabels=correlation.columns, annot=True)
        st.write(fig)


def show_visualization_page():
    filtered_col = cols

    # Title
    st.write("<h1 style = 'text-align : center;'>Experimental Data Visualization</h1>",
             unsafe_allow_html=True)
    st.markdown("---")

    # Scatter plot
    st.subheader("Graphical correlation plot")
    graphical_correlation_plot_x_column = st.selectbox(
        "**Select column for horizontal axis**", filtered_col
    )

    graphical_correlation_plot_y_columns = st.multiselect(
        "**Select columns for vertical axis**", filtered_col, filtered_col[1]
    )

    show_graph(graphical_correlation_plot_x_column,
               graphical_correlation_plot_y_columns)

    st.markdown("---")
    
if __name__ == "__main__":
    #train_data()
    show_visualization_page()
#if chart_select == 'Scatterplots':
#    st.sidebar.subheader ('Scatterplot settings')
#    x_values = st.sidebar.selectbox('X axis', options = cols)
#    y_values = st.sidebar.selectbox('Y axis', options = cols)
 #   plot = px.scatter(data_frame=train_data, x= x_values, y =y_values)
 #   st.plotly_chart(plot)