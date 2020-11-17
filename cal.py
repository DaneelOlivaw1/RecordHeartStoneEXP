import pandas as pd
from datetime import timedelta

data = pd.read_csv("/Users/wangboyi/Documents/GitHub/RecordHeartStoneEXP/data.csv", parse_dates=['时间'])
level = pd.read_csv("/Users/wangboyi/Documents/GitHub/RecordHeartStoneEXP/level.csv", index_col=['等级'])

def GetNeedExp(level, p):
    return level.loc[p]["升级所需经验"]

def cal(data, level, p):
    data.时间[p]
    delta_time = pd.to_datetime(data.时间[p]) - pd.to_datetime(data.时间[p-1])
    totalExp = 0
    if (int(data.等级[p]) == int(data.等级[p-1])):
        totalExp = int(data.已刷经验[p]) - int(data.已刷经验[p-1])
    elif (int(data.等级[p]) == int(data.等级[p-1]) + 1):
        totalExp = GetNeedExp(level, int(data.等级[p-1])) - int(data.等级[p-1]) + int(data.等级[p])
    else:
        totalExp = totalExp + int(data.已刷经验[p])
        for i in range(int(data.等级[p-1]), int(data.等级[p])):
            totalExp = totalExp + GetNeedExp(level, i)
    return totalExp / delta_time.total_seconds() * 60 * 60

# 算全部的效率
# for i in range(1, len(data)):
#     data.loc[i, "效率（exp/h）"] =  cal(data, level, i)

a = int(input("请输入当前等级："))
b = int(input("请输入现在的经验："))
print(pd.datetime.now())

a = {"时间":pd.datetime.now(),"等级":a, "已刷经验":b, "效率（exp/h）":0}
data = data.append(a,ignore_index=True)
data.loc[len(data) - 1, "效率（exp/h）"] =  cal(data, level, len(data) - 1)

print(data.loc[len(data) - 1, "效率（exp/h）"])
data.to_csv("/Users/wangboyi/Documents/GitHub/RecordHeartStoneEXP/data.csv", index=0)