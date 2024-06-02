from db import (
    getGrowthRateOfAgeMarriage, getGrowthRateOfUnMarriage, getGrowthRateOfCPI,
    getGrowthRateOfFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility,
    alignByYear
)

if __name__ == '__main__':
    # aa = alignByYear(getGrowthRateOfFertility(), getGrowthRateOfCPI(), getGrowthRateOfAgeMarriage(), getGrowthRateOfUnMarriage())
    # print(len(aa['year'])) 
    # print(len(aa['values'][0]))
    # print(list(map(lambda x: (x[0], x[1] * 100), getGrowthRateOfFertility())))
    print(getCorrelationOfAgeMarriageAndFertility())
    print(getCorrelationOfCPIAndFertility())
    print(getCorrelationOfUnmarriageAndFertility())