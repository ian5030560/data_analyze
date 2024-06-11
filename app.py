import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import statistics
from db import (
    getAgeMarriage, getUnMarriage, getCPI,
    getFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility,
    alignByYear, getFemaleLabor, getAgeFertility,
    getCorrelationOfAgeFertilityAndFertility, getCorrelationOfFemaleLaborAndFertility
)
#把data_list的值分開兩個list來存
def extract_growth_data(data_list, years_list, values_list):
    for data in data_list:
        years_list.append(data[0])
        values_list.append(data[1])

def count_average(data_list):
    # 確保 data_list 非空
    if not data_list:
        return 0.0
    # 使用 sum() 函數和 float() 確保數據的精確度
    avg = sum(float(data) for data in data_list) / len(data_list)
    return avg

st.title('探討我國生育率下降原因之影響程度')

# Fetch the growth rate data
unmarriage_growth_data = getUnMarriage()
marriage_growth_data = getAgeMarriage()
CPI_growth_data = getCPI()
fertility_growth_data = getFertility()
FemaleLabor_data = getFemaleLabor()
AgeFertility_data = getAgeFertility()

# Initialize lists to store the data
growthRateOfUnMarriageYears = []
growthRateOfUnMarriage = []

growthRateOfMarriageYears = []
growthRateOfMarriage = []

growthRateOfCPIYears = []
growthRateOfCPI = []

growthRateOfFertilityYears = []
growthRateOfFertility = []

growthRateOfFemaleLaborYears = []
growthRateOfFemaleLabor= []

growthRateOfAgeFertilityYears = []
growthRateOfAgeFertility= []

extract_growth_data(unmarriage_growth_data, growthRateOfUnMarriageYears, growthRateOfUnMarriage)
extract_growth_data(marriage_growth_data, growthRateOfMarriageYears, growthRateOfMarriage)
extract_growth_data(CPI_growth_data, growthRateOfCPIYears, growthRateOfCPI)
extract_growth_data(fertility_growth_data,growthRateOfFertilityYears,growthRateOfFertility)
extract_growth_data(FemaleLabor_data,growthRateOfFemaleLaborYears,growthRateOfFemaleLabor)
extract_growth_data(AgeFertility_data,growthRateOfAgeFertilityYears,growthRateOfAgeFertility)
st.write('不婚人數')
# Assuming you want to create a DataFrame and display it
dfUnMarriage = pd.DataFrame({
    'Year': growthRateOfUnMarriageYears,
    'Growth Rate': growthRateOfUnMarriage
})
dfUnMarriage.set_index('Year', inplace=True)

st.line_chart(dfUnMarriage)

st.write('平均結婚年齡')
dfMarriage = pd.DataFrame({
    'Year': growthRateOfMarriageYears,
    'Growth Rate': growthRateOfMarriage
})
dfMarriage.set_index('Year', inplace=True)
st.line_chart(dfMarriage)

st.write('消費者物價指數')
dfCPI = pd.DataFrame({
    'Year': growthRateOfCPIYears,
    'Growth Rate': growthRateOfCPI
})
dfCPI.set_index('Year', inplace=True)
st.line_chart(dfCPI)

st.write('女性勞動參與率')
dfFemaleLabor = pd.DataFrame({
    'Year': growthRateOfFemaleLaborYears,
    'Growth Rate': growthRateOfFemaleLabor
})
dfFemaleLabor.set_index('Year', inplace=True)
st.line_chart(dfFemaleLabor)

st.write('平均生育年齡')
dfAgeFertility = pd.DataFrame({
    'Year': growthRateOfAgeFertilityYears,
    'Growth Rate': growthRateOfAgeFertility
})
dfAgeFertility.set_index('Year', inplace=True)
st.line_chart(dfAgeFertility)



st.write('生育率的年增率(Z-Score Standardization)')
alignValue= alignByYear(getFertility(), getCPI(), getAgeMarriage(), getUnMarriage(), getFertility(),getFemaleLabor(),getAgeFertility())


fertilityGrowthRateStd = []
CPIGrowthRateStd = []
marriageGrowthRateStd = []
unMarriageGrowthRateStd = []
femaleLaborGrowthRateStd= []
ageFertilityGrowthRateStd= []

#Count Fertility Growth Rate Z-Score Standardization
for i in range(len(alignValue['values'][3])):
    fertilityGrowthRateStd.append((float(alignValue['values'][3][i]) - count_average(alignValue['values'][3]))/statistics.stdev(alignValue['values'][3]))
    CPIGrowthRateStd.append((float(alignValue['values'][0][i]) - count_average(alignValue['values'][0]))/statistics.stdev(alignValue['values'][0]))
    marriageGrowthRateStd.append((float(alignValue['values'][1][i]) - count_average(alignValue['values'][1]))/statistics.stdev(alignValue['values'][1]))
    unMarriageGrowthRateStd.append((float(alignValue['values'][2][i]) - count_average(alignValue['values'][2]))/statistics.stdev(alignValue['values'][2]))
    femaleLaborGrowthRateStd.append((float(alignValue['values'][4][i]) - count_average(alignValue['values'][4]))/statistics.stdev(alignValue['values'][4]))
    ageFertilityGrowthRateStd.append((float(alignValue['values'][5][i]) - count_average(alignValue['values'][5]))/statistics.stdev(alignValue['values'][5]))

dfFertility = pd.DataFrame(
    {
        'Year': alignValue['year'],
        'Fertility':fertilityGrowthRateStd,
        'CPI': CPIGrowthRateStd,
        'Marriage': marriageGrowthRateStd,
        'UnMarriage': unMarriageGrowthRateStd,
        'FemaleLabor': femaleLaborGrowthRateStd,
        'AgeFertility': ageFertilityGrowthRateStd,
})
dfFertility.set_index('Year', inplace=True)

# 單選按鈕選項
options = [
    'None',  # 可以選擇不添加
    "消費者物價指數(Z-Score Standardization)",
    "平均結婚年齡(Z-Score Standardization)",
    "不婚人數(Z-Score Standardization)",
    "女性勞動參與率(Z-Score Standardization)",
    "平均生育年齡(Z-Score Standardization)"
]
options_mappings = {
    'None':'None',  # 可以選擇不添加
    "消費者物價指數(Z-Score Standardization)":'CPI',
    "平均結婚年齡(Z-Score Standardization)":'Marriage',
    "不婚人數(Z-Score Standardization)":'UnMarriage',
    "女性勞動參與率(Z-Score Standardization)":'FemaleLabor',
    "平均生育年齡(Z-Score Standardization)":'AgeFertility'
}

selected_option = st.radio("選擇要比對的項目(此為標準化過後的數據)", options)

# 預設顯示 Fertility Growth Rate
columns_to_show = ['Fertility']

# 如果選擇了其他成長率，則添加到顯示的列中
if selected_option != 'None':
    columns_to_show.append(options_mappings[selected_option])

# 顯示選擇的成長率
st.line_chart(dfFertility[columns_to_show])



st.write('生育率的相關係數')
correlationWithFertility = []
# 設置 X 軸標籤
labels = ['平均結婚年齡', '不婚人數', '消費者物價指數','女性勞動參與率','平均生育年齡']
correlationWithFertility.append(abs(getCorrelationWithFertility(getAgeMarriage())))
correlationWithFertility.append(abs(getCorrelationWithFertility(getUnMarriage())))
correlationWithFertility.append(abs(getCorrelationWithFertility(getCPI())))
correlationWithFertility.append(abs(getCorrelationWithFertility(getFemaleLabor())))
correlationWithFertility.append(abs(getCorrelationWithFertility(getAgeFertility())))
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

