from .db import CPI, session, AgeFertility, FemaleLabor
from .util import getCorrelationWithFertility
import pandas as pd

def getAgeFertility() -> list[int, float]:
    """計算每年的平均生育年齡
    """
    data = session.query(AgeFertility).all()
    df = pd.DataFrame({
        "year": list(map(lambda x: x.year, data)),
        "age": list(map(lambda x: x.age, data)),
        "value": list(map(lambda x: x.value, data)),
    })
    
    groupby = df.groupby("year")
    keys = groupby.groups.keys()
    
    ages = []
    for key in keys:
        group = groupby.get_group(key)
        valSum = group["value"].sum()
        group.insert(len(group.columns), "rate", group["value"].map(lambda x: x / valSum))
        age = (group["age"] * group["rate"]).sum()
        ages.append((key, age))

    result = []
    # for i in range(1, len(ages)):
    #     result.append((ages[i][0], (ages[i][1] - ages[i - 1][1]) / ages[i - 1][1]))
    for i in range(0, len(ages)):
        result.append((ages[i][0], ages[i][1]))
        
    return result

def getFemaleLabor() -> list[int, float]:
    """計算每年的女性勞動參與率
    """
    data = session.query(FemaleLabor).all()
    
    result = []
    # for i in range(1, len(data)):
    #     result.append((data[i].year, (data[i].value - data[i - 1].value) / data[i - 1].value))
    for i in range(0, len(data)):
        result.append((data[i].year, data[i].value))
        
    return result

getCorrelationOfAgeFertilityAndFertility = lambda: getCorrelationWithFertility(getGrowthRateOfAgeFertility())
getCorrelationOfFemaleLaborAndFertility = lambda: getCorrelationWithFertility(getGrowthRateOfFemaleLabor())