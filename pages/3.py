import streamlit as st
import pandas as pd
from peptideUtilities import *

#User input for pep sequnces
pep_list = list(map(str, st.text_input('Enter pep seq:').split(sep= ',',maxsplit=3)))
st.write('Entered seq :',(pep_list),unsafe_allow_html=True)

# Get fp values 

#for peptide in pep_list:
 #   st.text(get_norm_bscore(peptide))
 #   st.text(get_abs_logP(get_long_sequence(peptide)))
#st.text(get_logP(get_long_sequence(peptide))[1])
#st.text(get_abs_logP(peptide))

fp_data ={
    'norm_bscore': [st.text(get_norm_bscore(peptide)) for peptide in pep_list],
    'abs_logP': [st.text(get_abs_logP(get_long_sequence(peptide))) for peptide in pep_list]
}

st.dataframe(pd.DataFrame(fp_data,columns= ["bscore","logP"]),hide_index=True)
