import time
import streamlit as st
import numpy as np
import pandas as pd
from db import (
    getGrowthRateOfAgeMarriage, getGrowthRateOfUnMarriage, getGrowthRateOfCPI,
    getGrowthRateOfFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility
)

st.title('探討我國生育率下降原因之影響程度')
st.write('不婚人數的年增率')

# Fetch the growth rate data
unmarriage_growth_data = getGrowthRateOfUnMarriage()

# Initialize lists to store the data
growthRateOfUnMarriageYears = []
growthRateOfUnMarriage = []

# Iterate through the fetched data and append to the lists
for data in unmarriage_growth_data:
    growthRateOfUnMarriageYears.append(data[0])
    growthRateOfUnMarriage.append(data[1])  # Assuming second value in tuple

# Display the data in Streamlit
st.write(growthRateOfUnMarriageYears)
st.write(growthRateOfUnMarriage)

# Assuming you want to create a DataFrame and display it
df = pd.DataFrame({
    'Year': growthRateOfUnMarriageYears,
    'Growth Rate': growthRateOfUnMarriage
})

st.line_chart(df)
