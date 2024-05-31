import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from db import (
    getGrowthRateOfAgeMarriage, getGrowthRateOfUnMarriage, getGrowthRateOfCPI,
    getGrowthRateOfFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility,alignByYear
)
#把data_list的值分開兩個list來存
def extract_growth_data(data_list, years_list, values_list):
    for data in data_list:
        years_list.append(data[0])
        values_list.append(data[1])

st.title('探討我國生育率下降原因之影響程度')

# Fetch the growth rate data
unmarriage_growth_data = getGrowthRateOfUnMarriage()
marriage_growth_data = getGrowthRateOfAgeMarriage()
CPI_growth_data = getGrowthRateOfCPI()
fertility_growth_data = getGrowthRateOfFertility()

# Initialize lists to store the data
growthRateOfUnMarriageYears = []
growthRateOfUnMarriage = []

growthRateOfMarriageYears = []
growthRateOfMarriage = []

growthRateOfCPIYears = []
growthRateOfCPI = []

growthRateOfFertilityYears = []
growthRateOfFertility = []

extract_growth_data(unmarriage_growth_data, growthRateOfUnMarriageYears, growthRateOfUnMarriage)
extract_growth_data(marriage_growth_data, growthRateOfMarriageYears, growthRateOfMarriage)
extract_growth_data(CPI_growth_data, growthRateOfCPIYears, growthRateOfCPI)
extract_growth_data(fertility_growth_data,growthRateOfFertilityYears,growthRateOfFertility)
st.write('不婚人數的年增率')
# Assuming you want to create a DataFrame and display it
dfUnMarriage = pd.DataFrame({
    'Year': growthRateOfUnMarriageYears,
    'Growth Rate': growthRateOfUnMarriage
})
dfUnMarriage.set_index('Year', inplace=True)

st.line_chart(dfUnMarriage)

st.write('平均結婚年齡的年增率')
dfMarriage = pd.DataFrame({
    'Year': growthRateOfMarriageYears,
    'Growth Rate': growthRateOfMarriage
})
dfMarriage.set_index('Year', inplace=True)
st.line_chart(dfMarriage)

st.write('消費者物價指數的年增率')
dfCPI = pd.DataFrame({
    'Year': growthRateOfCPIYears,
    'Growth Rate': growthRateOfCPI
})
dfCPI.set_index('Year', inplace=True)
st.line_chart(dfCPI)

st.write('生育率的年增率')
alignValue= alignByYear(getGrowthRateOfFertility(), getGrowthRateOfCPI(), getGrowthRateOfAgeMarriage(), getGrowthRateOfUnMarriage(),getGrowthRateOfFertility())
checkBoxCPI = st.checkbox("消費者物價指數的年增率(10倍)")
checkBoxMarriage = st.checkbox("平均結婚年齡的年增率(10倍)")
checkBoxUnMarriage = st.checkbox("不婚人數的年增率(10倍)")



dfFertility = pd.DataFrame(
    {
        'Year': alignValue['year'],
        'Fertility Growth Rate':alignValue['values'][3],
        'CPI Growth Rate': [i*10 for i in alignValue['values'][0]],
        'Marriage Growth Rate': [i*10 for i in alignValue['values'][1]],
        'UnMarriage Growth Rate': [i*10 for i in alignValue['values'][2]],
})
dfFertility.set_index('Year', inplace=True)

columns_to_show = ['Fertility Growth Rate']  # 預設顯示 Fertility Growth Rate
if checkBoxCPI:
    columns_to_show.append('CPI Growth Rate')
if checkBoxMarriage:
    columns_to_show.append('Marriage Growth Rate')
if checkBoxUnMarriage:
    columns_to_show.append('UnMarriage Growth Rate')

if columns_to_show:
    st.line_chart(dfFertility[columns_to_show])



st.write('生育率的相關係數')
correlationWithFertility = []
# 設置 X 軸標籤
labels = ['平均結婚年齡的年增率', '不婚人數的年增率', '消費者物價指數年增率']
correlationWithFertility.append(abs(getCorrelationWithFertility(getGrowthRateOfAgeMarriage())))
correlationWithFertility.append(abs(getCorrelationWithFertility(getGrowthRateOfUnMarriage())))
correlationWithFertility.append(abs(getCorrelationWithFertility(getGrowthRateOfCPI())))
# 將數據轉換為 DataFrame
dfCorrelationWithFertility = pd.DataFrame({
    'Category': labels,
    'Correlation': correlationWithFertility,
})

# 使用 Altair 創建橫向長條圖
chart = alt.Chart(dfCorrelationWithFertility).mark_bar().encode(
    x='Correlation:Q',
    y=alt.Y('Category:N', sort='-x')  # 按照值進行排序
).configure_axis(
    labelAngle=0  # 將標籤方向設為水平
)
st.altair_chart(chart, use_container_width=True)

