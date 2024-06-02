from .db import CPI, session, AgeMarrige, Unmarrige, Fertility
import pandas as pd

def getGrowthRateOfAgeMarriage() -> list[tuple[int, float]]:
    """計算每年的結婚年齡成長率
    """
    data: list[AgeMarrige] = session.query(AgeMarrige).all()
    data_dict = {"year": [], "age_group": [], "num": []}
    
    for dt in data:
        data_dict["year"].append(dt.year)
        data_dict["age_group"].append(dt.age_group)
        data_dict["num"].append(dt.num)
        
    df = pd.DataFrame(data_dict)
    
    def convertToAverage(val: str):
        start, end = list(map(int, val.split("-")))
        group = [i for i in range(start, end + 1)]
        return sum(group) / len(group)
    
    df["age_group"] = df["age_group"].map(convertToAverage)
    groupByYear = df.groupby("year")
    groupKeys = groupByYear.groups.keys()
   
    ages = []
    for key in groupKeys:
        group = groupByYear.get_group(key)
        numSum = group["num"].sum()
        group.insert(len(group.columns), "rate", group["num"].map(lambda v: v / numSum))
        age = (group["age_group"] * group["rate"]).sum()
        ages.append((key, age))
    
    result = []
    for i in range(1, len(ages)):
        result.append((ages[i][0], (ages[i][1] - ages[i - 1][1]) / ages[i - 1][1]))
    
    return result

def getCorrelationWithFertility(data: list[tuple[int, float]]) -> float:
    """計算資料與生育率之年增率的相關係數 (使用pearson相關係數)

    Args:
        data (list[tuple[int, float]]): 輸入之資料

    Returns:
        float: 相關係數
    """
    data_dict = {"year": [], "value1": []}
    for age in data:
        data_dict["year"].append(age[0])
        data_dict["value1"].append(age[1])
    
    fertilities = getGrowthRateOfFertility()
    fertility_dict = {"year": [], "value2": []}
    for ferality in fertilities:
        fertility_dict["year"].append(ferality[0])
        fertility_dict["value2"].append(ferality[1])
        
    data_df = pd.DataFrame(data_dict)
    ferality_df = pd.DataFrame(fertility_dict)
    merge = pd.merge(data_df, ferality_df, how="inner", on=["year"])
    neccess = merge[["value1", "value2"]]
    
    return neccess.corr("pearson").iloc[0, 1]

def getGrowthRateOfUnMarriage() -> list[tuple[int, float]]:
    """取得每年未結婚人數的成長率
    """
    data: list[Unmarrige] = session.query(Unmarrige).all()
    
    result = []
    for i in range(1, len(data)):
        result.append((data[i].year, (data[i].num - data[i - 1].num) / data[i - 1].num))
        
    return result

def getGrowthRateOfCPI() -> list[tuple[int, float]]:
    """取得每年消費者物價指數(CPI)的成長率
    """
    data: list[CPI] = session.query(CPI).all()
    
    result = []
    for i in range(0, len(data)):
        result.append((data[i].year, data[i].value / 100))
        
    return result

def getGrowthRateOfFertility() -> list[tuple[int, float]]:
    """取得每年生育率的成長率
    """
    data: list[Fertility] = session.query(Fertility).all()
    
    result = []
    for i in range(1, len(data)):
        result.append((data[i].year, (data[i].value - data[i - 1].value) / data[i - 1].value))
        
    return result


getCorrelationOfAgeMarriageAndFertility = lambda: getCorrelationWithFertility(getGrowthRateOfAgeMarriage())
getCorrelationOfUnmarriageAndFertility = lambda: getCorrelationWithFertility(getGrowthRateOfUnMarriage())
getCorrelationOfCPIAndFertility = lambda: getCorrelationWithFertility(getGrowthRateOfCPI())

Year = int
Value = float
def alignByYear(major: list[tuple[Year, Value]], *data: list[tuple[Year, Value]]) -> dict["year": list[Year], "values": list[list[Value]]]:
    """對齊資料們的年份
    ex: from util import alignByYear\n
        data1 = getGrowthRateOfFertility()\n
        data2 = getGrowthRateOfCPI()\n
        data3 = getGrowthRateOfAgeMarriage()\n
        data4 = getGrowthRateOfUnMarriage()\n
        
        print(alignByYear(data1, data2, data3, data4))\n
    Args:
        major (list[tuple[Year, Value]]): 被對照的資料，年分以它為準
        *data (...list[tuple[Year, Value]]): 需對齊的資料
    Returns:
        {year: list[Year], values: list[list[Value]]}: year: 所有年分，values: 為二維陣列, 其中包含所有對齊過的值, 長度依*data的數量為準
    """
    years = list(map(lambda x: x[0], major))
    
    values: list[list[Value]] = []
    fn = lambda x: x[0] in years
    for d in data:
        value: list[Value] = []
        ys = list(map(lambda x: x[0], d))
        vs = list(map(lambda x: x[1], d))
        
        for year in years:
            if year in ys:
                value.append(vs[ys.index(year)])
            else:
                value.append(0)
        values.append(value)
        
    return {
        "year": years,
        "values": values,
    }