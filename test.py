from db import (
    getAgeMarriage, getUnMarriage, getCPI,
    getFertility, getCorrelationWithFertility, getCorrelationOfUnmarriageAndFertility,
    getCorrelationOfAgeMarriageAndFertility, getCorrelationOfCPIAndFertility,
    alignByYear, getFemaleLabor, getAgeFertility,
    getCorrelationOfAgeFertilityAndFertility, getCorrelationOfFemaleLaborAndFertility
)

if __name__ == '__main__':
    print(getFemaleLabor())
    print(getAgeFertility())
