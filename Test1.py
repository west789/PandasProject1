import pandas as pd
from pandas import *


def DfInitTable():
    dfInitTable = DataFrame(pd.read_csv("./test.csv"))
    return dfInitTable

def DfNameAndAlias(dfInitArg):
    dfNameAndAlias = dfInitArg [["NAME","All_Alias"]]
    return dfNameAndAlias
def Result(dfInitTalbe, dfNameAndAlias):  #进行合并去重操作
    stateDic = {}
    dfColumns = dfInitTable.columns.values
    dfNewTable = DataFrame(columns=[dfColumns[i] for i in range(len(dfColumns))])
    try:
        for i in range(len(dfInitTable)):
            if not ("ixState%d"%i in stateDic.keys() and stateDic["ixState%d"%i] == "true"):
                stateDic["ixState%d"%i] = "true"
                dfNamei = dfNameAndAlias.loc[i, "NAME"]
                dfAliasi = dfNameAndAlias.loc[i, "All_Alias"]
                dfAliasiSet = set(dfAliasi.split("###"))
                replIndexi = dfInitTable.loc[i]
                falgMerge = False
                for j in range (i+1,len(dfInitTable)):
                    dfNamej = dfNameAndAlias.loc[j, "NAME"]
                    dfAliasj = dfNameAndAlias.loc[j, "All_Alias"]
                    dfAliasjSet = set(dfAliasj.split("###"))
                    boolState = "ixState%d"%j not in stateDic
                    if boolState:
                        stateDic["ixState%d"%j] = "false"
                    else:
                        pass 
                    if (stateDic["ixState%d"%j] == "false") and (dfNamei == dfNamej or len(dfAliasiSet & dfAliasjSet) != 0):
                        stateDic["ixState%d"%j] = "true"
                        falgMerge = True
                        seriesMerge = mergeThreeCol(dfInitTable, i, j)
                        dfNewTable.loc[i] = seriesMerge
                    else:
                        break
                if not falgMerge:
                    dfNewTable.loc[i] = replIndexi
            else:
                continue       
    except e:
        print ("错误信息%s"%e)
    return dfNewTable
    
def mergeThreeCol(dfInitTable, i, j): #合并要求的三列数据
    setAliasi = set(dfInitTable.loc[i, "All_Alias"].split("###"))
    setAliasj = set(dfInitTable.loc[j, "All_Alias"].split("###"))
    setCodei = set(dfInitTable.loc[i, "CODE"].split("###"))
    setCodej = set(dfInitTable.loc[j, "CODE"].split("###"))
    setSourcei = set(dfInitTable.loc[i, "SOURCE"].split("###"))
    setSourcej = set(dfInitTable.loc[j, "SOURCE"].split("###"))
    strAliasij = "###".join(setAliasi | setAliasj)
    strCodeij = "###".join(setCodei | setCodej)
    strSourceij = "###".join(setSourcei | setSourcej)
    strSourceij = sortedStrSource(strSourceij)
    replIndexi = dfInitTable.loc[i]
    replIndexi = replIndexi.replace([replIndexi["All_Alias"],replIndexi["CODE"],replIndexi["SOURCE"]],
                        [strAliasij,strCodeij,strSourceij])
    dfInitTable.loc[i] = replIndexi
    return replIndexi
                
def sortedStrSource(strSourceij):
    listSorted = []
    if "###"  in strSourceij:
        listStrSourceij = strSourceij.split("###")
        if "卫计委" in listStrSourceij:
            listSorted.append("卫计委")
        if "MOH" in listStrSourceij:
            listSorted.append("MOH")    
        if "CPA" in listStrSourceij:
            listSorted.append("CPA")   
        if "MUNDI" in listStrSourceij:
            listSorted.append("MUNDI")   
        if "MERCK" in listStrSourceij:
            listSorted.append("MERCK")   
        if "挂号" in listStrSourceij:
            listSorted.append("挂号")   
        if "PFIZER" in listStrSourceij:
            listSorted.append("PFIZER")   
        elif "Haodf" in listStrSourceij:
            listSorted.append("Haodf")   
        return "###".join(listSorted)
    else:
        return strSourceij
    


dfInitTable = DfInitTable()  #加载初始DataFrame 使用EditPlus保存编码格式为UTF-8
print (dfInitTable)
dfNameAndAlias = DfNameAndAlias(dfInitTable) #由Name和Alias组成的DataFrame
dfNewFrameTable = Result(dfInitTable,dfNameAndAlias) #得到一个新的dataframe
dfNewFrameTable.to_csv('./result.csv',index=False)   #输出结果会在result.csv里面
