import pymysql as sql
import pandas as pd
import re

conn = sql.connect(
    user="root",
    host="localhost",
    port=3306,
    # password="ucdw6eak",
    database="data_analyze",
)
cusor = conn.cursor()


def injectAgeMarriage():
    df = pd.read_excel("raw/age_marrige.xlsx")
    (rows, cols) = df.shape

    def extractGroup(value: str):
        regex = r"國籍別總計_(.*)歲"
        result = re.search(regex, str(value))
        return result.group(1) if result is not None else None

    age_group = list(map(extractGroup, df.iloc[0].values))

    for i in range(1, rows):
        year = df.iloc[i, 0].replace("年", "")
        for j in range(1, cols):
            group = age_group[j]
            data = df.iloc[i, j]
            cusor.execute(
                "INSERT INTO `age_marrige` VALUES (%s, '%s', %d);" % (year, group, data)
            )
            conn.commit()

    cusor.close()
    conn.close()


def injectCPI():
    df = pd.read_excel("raw/cpi.xlsx")
    filtered = df[df["統計期"].notna() & df["統計期"].str.contains("年")]
    (rows, _) = filtered.shape

    for row in range(rows):
        year, value = filtered.iloc[row, 0], filtered.iloc[row, 1]
        cusor.execute(
            "INSERT INTO `cpi` VALUES (%s, %f)" % (year.replace("年", ""), value)
        )
        conn.commit()

    cusor.close()
    conn.close()


def injectFertility():
    df = pd.read_excel("raw/age_fertility.xlsx")
    (rows, _) = df.shape
    for row in range(rows):
        year, value = df.iloc[row, 0], df.iloc[row, 1]
        cusor.execute(
            "INSERT INTO `fertility` VALUES (%s, %d)" % (year.replace("年", ""), value)
        )
        conn.commit()

    cusor.close()
    conn.close()


def injectUnmarriage():
    df = pd.read_excel("raw/unmarrige.xlsx")
    (rows, _) = df.shape

    for row in range(1, rows):
        year, value = df.iloc[row, 0], df.iloc[row, 1]
        cusor.execute(
            "INSERT INTO `unmarrige` VALUES (%s, %d)" % (year.replace("年", ""), value)
        )
        conn.commit()

    cusor.close()
    conn.close()

def injectAgeFertility():
    df = pd.read_excel("raw/age_fertility.xlsx")
    (rows, _) = df.shape

    ages = df.columns
    for row in range(0, rows):
        (cols, ) = df.iloc[row].shape
        year = int(df.iloc[row, 0][0: -1])
        for col in range(1, cols):
            age = int(ages[col][0: -1])
            value = int(df.iloc[row, col])
            cusor.execute("INSERT INTO `age_fertility` VALUES (%d, %d, %d)"%(year, age, value))
            conn.commit()
            
    cusor.close()
    conn.close()

def injectFemaleLabor():
    df = pd.read_excel("raw/female_labor.xlsx")
    (rows, _) = df.shape

    for row in range(1, rows):
        year, value = df.iloc[row, 0], df.iloc[row, 1]
        year = int(year.replace("年平均", ""))
        cusor.execute("INSERT INTO `female_labor` VALUES (%d, %f)"%(year, value))
        conn.commit()
        
    cusor.close()
    conn.close()
    
# if __name__ == "__main__":
#     injectFemaleLabor()

