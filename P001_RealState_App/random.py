import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(0)  # Seed so random arrays do not change on each rerun
n_rows = 1000
random_data = pd.DataFrame( {"A": np.random.random(size=n_rows),
                             "B": np.random.random(size=n_rows)} )

sliders = {
    "A": st.sidebar.slider("Filter A", min_value=0.0, max_value=1.0, value=(0.0, 1.0), step=0.01),
    "B": st.sidebar.slider("Filter B", min_value=0.0, max_value=1.0, value=(0.0, 1.0), step=0.01),
}

filter = np.full(n_rows, True)  # Initialize filter as only True


for feature_name, slider in sliders.items():
    # Here we update the filter to take into account the value of each slider
    filter = ( filter & (random_data[feature_name] >= slider[0])
               & (random_data[feature_name] <= slider[1])         )


st.write(random_data[filter])


