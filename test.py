from db import (
    getGrowthRateOfAgeMarriage, getGrowthRateOfUnMarriage, getGrowthRateOfCPI,
    getGrowthRateOfFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility,
    alignByYear
)

if __name__ == '__main__': 
    print(alignByYear(getGrowthRateOfFertility(), getGrowthRateOfCPI(), getGrowthRateOfAgeMarriage(), getGrowthRateOfUnMarriage()))