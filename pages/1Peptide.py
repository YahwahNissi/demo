# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:04:17 2023

@author: Yahwah Nissi
"""

import streamlit as st
import pandas as pd
import numpy as np
from peptideUtilities import *


#User input for pep sequnces
pep_list = list(map(str, st.text_input('Enter pep seq:').split(sep= ',')))
st.write('Entered seq :',(pep_list),unsafe_allow_html=True)
st.button('Search')

#st.text(get_norm_bscore(peptide))
#st.text(get_abs_logP(get_long_sequence(peptide)))
#st.text(get_logP(get_long_sequence(peptide))[1])
#st.text(get_abs_logP(peptide))

fp_col = ["norm_bscore","logP","abs_logP"]

df = pd.DataFrame(
    {
       "pep": [st.text(peptide) for peptide in pep_list],
      "norm_bscore": [st.text(get_norm_bscore(peptide)) for peptide in pep_list],
      'logP': [st.text(get_logP(get_long_sequence(peptide))[1]) for peptide in pep_list],
      'abs_logP': [st.text(get_abs_logP(get_long_sequence(peptide))) for peptide in pep_list]
    }
)


st.dataframe(data = df)
#st.table(pd.DataFrame([df]))
#st.write(data)
