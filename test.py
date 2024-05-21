from db import (
    getGrowthRateOfAgeMarriage, getGrowthRateOfUnMarriage, getGrowthRateOfCPI,
    getGrowthRateOfFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility
)

import math

if __name__ == '__main__':
    print(getGrowthRateOfUnMarriage())
