import pandas as pd
import numpy as np

###
# 专业组
# 复旦1：法学, 历史学类, 社会科学试验班, 新闻传播学类, 英语, 中国语言文学类, 哲学类 (7)
# 复旦2：工科试验班, 软件工程, 数学类, 自然科学试验班, 技术科学试验班, 计算机科学与技术(拔尖人才试验班，本研贯通), 航空航天类 (7)
# 复旦3：经济学类, 经济管理试验班 (2)
# 复旦4：数学英才试验班 (1)
# 复医1：临床医学(8年制本博连读), 临床医学(5年制) (2)
# 复医2：药学, 公共事业管理, 口腔医学, 预防医学 (4)
###

MajorGroup = {'复旦1': ['法学', '历史学类', '社会科学试验班', '新闻传播学类', '英语', '中国语言文学类', '哲学类'],
         '复旦2': ['工科试验班(新工科本研贯通)', '软件工程', '数学类', '自然科学试验班', '技术科学试验班', '计算机科学与技术(拔尖人才试验班，本研贯通)', '航空航天类'],
         '复旦3': ['经济学类', '经济管理试验班'],
         '复旦4': ['数学英才试验班'],
         '复医1': ['临床医学(8年制本博连读)', '临床医学(5年制)'],
         '复医2': ['药学', '公共事业管理', '口腔医学', '预防医学']}

majors = {
    '法学': '法学(卓越法律人才基地)', '历史学类': '历史学类(拔尖学生培养基地)', '社会科学试验班': '社会科学试验班(含政治及行政学、国政等专业)', 
    '新闻传播学类': '新闻传播学类(卓越新闻人才计划)', '英语': '英语(含英语，翻译2个专业)', '中国语言文学类': '中国语言文学类(拔尖学生培养基地)', 
    '哲学类': '哲学类(拔尖学生培养基地)', '工科试验班(新工科本研贯通)': '工科试验班(新工科本研贯通)', '软件工程': '软件工程(国家示范性软件学院)', 
    '数学类': '数学类(拔尖学生培养基地)', '自然科学试验班': '自然科学试验班(物理化学方向，拔尖学生培养基地)', '技术科学试验班': '技术科学试验班(拔尖学生培养基地)',
    '计算机科学与技术(拔尖人才试验班，本研贯通)': '计算机科学与技术(拔尖人才试验班，本研贯通)', '航空航天类': '航空航天类', '经济学类': '经济学类(拔尖学生培养基地)', 
    '经济管理试验班': '经济管理试验班', '数学英才试验班': '数学英才试验班', '临床医学(8年制本博连读)': '临床医学(8年制本博连读)', '临床医学(5年制)': '临床医学(5年制)', 
    '药学': '药学(拔尖学生培养基地)', '公共事业管理': '公共事业管理', '口腔医学': '口腔医学', '预防医学': '预防医学'
}

admissionTable = pd.read_excel('招生计划表.xlsx', sheet_name=0)
scoreTable = pd.read_excel('报名成绩统计.xlsx', sheet_name=0)

grouped = scoreTable.groupby(scoreTable.iloc[:, 2])
scoreGrouped, admittedNum, admittedStu, adjustStu, failedStu = {}, {}, {}, {}, {}
for name, table in grouped:
    scoreGrouped[name] = table.values
    admittedNum[name] = 0
    admittedStu[name], adjustStu[name], failedStu[name] = [], [], []

admission = admissionTable.set_index('专业名称')['计划数'].to_dict()

quotaNum = {}
for g, m in MajorGroup.items():
    sum = 0
    for i in m:
        sum += admission[majors[i]]
    quotaNum[g] = sum

for groupName, groupScoreTable in scoreGrouped.items():  # 对每个专业组
    # print('*********************')
    # print(key)
    # print(value)
    # 录取过程
    adjusting = []
    for stu in groupScoreTable:
        preference = stu[4].split('、')
        # print(preference)
        admitted = False
        for p in preference:  # 顺序考虑每个志愿
            if (admission[majors[p]] > 0):  # 尚有空位，录取成功
                admitted = True
                admission[majors[p]] -= 1   # 该专业空位减一
                admittedNum[groupName] += 1  # 该专业组录取人数加1
                admittedStu[groupName].append(stu)  # 记录此学生
                break
        if (admitted == False):   # 录取失败
            if (stu[5] == '是'):  # 服从调剂
                adjusting.append(stu)  # 添加到本专业等待调剂List
            else:
                failedStu[groupName].append(stu)  # 添加到落榜名单

    # 计算可调剂的名额
    adjustQuota = quotaNum[groupName] - admittedNum[groupName]
    # 进行调剂
    for stu in adjusting:
        if (adjustQuota > 0):
            adjustStu[groupName].append(stu)
            admittedNum[groupName] += 1
            adjustQuota -= adjustQuota
        else:
            failedStu[groupName].append(stu)
     
# print(admittedStu)
# print('****************************')
# print(adjusting)
                
# print(scoreGrouped['复旦1'][0][4])
# print(admission)

# 输出为XLSX文件
for _, table in admittedStu.items():
    # TODO HERE
    df=pd.DataFrame(table)
    print(df)
    print('************************************')
    pass
            