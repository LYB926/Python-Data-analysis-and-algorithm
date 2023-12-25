import pandas as pd

###
# split-apply-combine
###
# 专业组
# 复旦1：法学, 历史学类, 社会科学试验班, 新闻传播学类, 英语, 中国语言文学类, 哲学类 (7)
# 复旦2：工科试验班, 软件工程, 数学类, 自然科学试验班, 技术科学试验班, 计算机科学与技术(拔尖人才试验班，本研贯通), 航空航天类 (7)
# 复旦3：经济学类, 经济管理试验班 (2)
# 复旦4：数学英才试验班 (1)
# 复医1：临床医学(8年制本博连读), 临床医学(5年制) (2)
# 复医2：药学, 公共事业管理, 口腔医学, 预防医学 (4)
###

# 用于查询专业组中专业的字典，Key为专业组名称，对应的Value为专业组包含的专业的列表
# 例：MajorGroup['复医1'] = ['临床医学(8年制本博连读)', '临床医学(5年制)']
MajorGroup = {'复旦1': ['法学', '历史学类', '社会科学试验班', '新闻传播学类', '英语', '中国语言文学类', '哲学类'],
              '复旦2': ['工科试验班(新工科本研贯通)', '软件工程', '数学类', '自然科学试验班', '技术科学试验班', '计算机科学与技术(拔尖人才试验班，本研贯通)', '航空航天类'],
              '复旦3': ['经济学类', '经济管理试验班'],
              '复旦4': ['数学英才试验班'],
              '复医1': ['临床医学(8年制本博连读)', '临床医学(5年制)'],
              '复医2': ['药学', '公共事业管理', '口腔医学', '预防医学']}

# 用于查询专业全称的字典，Key为专业简称，对应的Value为专业的全称
MajorName = {
    '法学': '法学(卓越法律人才基地)', '历史学类': '历史学类(拔尖学生培养基地)', '社会科学试验班': '社会科学试验班(含政治及行政学、国政等专业)',
    '新闻传播学类': '新闻传播学类(卓越新闻人才计划)', '英语': '英语(含英语，翻译2个专业)', '中国语言文学类': '中国语言文学类(拔尖学生培养基地)',
    '哲学类': '哲学类(拔尖学生培养基地)', '工科试验班(新工科本研贯通)': '工科试验班(新工科本研贯通)', '软件工程': '软件工程(国家示范性软件学院)',
    '数学类': '数学类(拔尖学生培养基地)', '自然科学试验班': '自然科学试验班(物理化学方向，拔尖学生培养基地)', '技术科学试验班': '技术科学试验班(拔尖学生培养基地)',
    '计算机科学与技术(拔尖人才试验班，本研贯通)': '计算机科学与技术(拔尖人才试验班，本研贯通)', '航空航天类': '航空航天类', '经济学类': '经济学类(拔尖学生培养基地)',
    '经济管理试验班': '经济管理试验班', '数学英才试验班': '数学英才试验班', '临床医学(8年制本博连读)': '临床医学(8年制本博连读)', '临床医学(5年制)': '临床医学(5年制)',
    '药学': '药学(拔尖学生培养基地)', '公共事业管理': '公共事业管理', '口腔医学': '口腔医学', '预防医学': '预防医学'
}

# 从两个文件中读取招生计划和报名成绩统计
quotaTable = pd.read_excel('招生计划表.xlsx', sheet_name=0)
scoreTable = pd.read_excel('报名成绩统计.xlsx', sheet_name=0)


#################################################
################## 拆分 Split ###################
#################################################

# 用于储存学生成绩、各专业名额和录取情况的字典，对每个字典内容说明如下：
# scoreGrouped: Key为专业组名称，对应的Value为包含该专业组学生成绩单的二维数组
# quotaNum: Key为专业全称，对应的Value为该专业招生名额余量
# admittedNum：Key为专业组名称，Value为该专业组已录取的学生数量
# admittedStu：Key为专业组名称，Value为该专业组志愿录取的学生名单（不包含调剂生）
# adjustStu：Key为专业组名称，Value为该专业组调剂录取的学生名单
# failedStu：Key为专业组名称，Value为落榜学生名单
scoreGrouped, quotaNum, admittedNum, admittedStu, adjustStu, failedStu ={}, {}, {}, {}, {}, {}

# 按照专业组对学生的报名成绩表进行分组拆分
grouped = scoreTable.groupby(scoreTable.iloc[:, 2])
for group, table in grouped: 
    # 初始化每个专业组的学生成绩单、已录取的学生数量和名单、调剂和落榜的学生名单数据
    scoreGrouped[group] = table.values
    admittedNum[group] = 0 
    admittedStu[group], adjustStu[group], failedStu[group] = [], [], []

# 计算各专业的招生名额余量
quota = quotaTable.set_index('专业名称')['计划数'].to_dict()
for group, major in MajorGroup.items():
    sum = 0
    for i in major:
        sum += quota[MajorName[i]]
    quotaNum[group] = sum


#################################################
################## 应用 Apply ###################
#################################################
# 对每个专业组进行志愿录取和调剂操作
for group, table in scoreGrouped.items():
    table = sorted(table, key=lambda x: x[1], reverse=True)  # 对学生按成绩进行排序
    adjusting = []  # 存放该专业组志愿未录取但接受调剂的学生名单
    for stu in table:  # 遍历专业组中每个学生
        preference = stu[4].split('、')  # 包含当前同学志愿的列表
        # print(preference)
        admitted = False
        for p in preference:  # 顺序考虑每个志愿
            if (quota[MajorName[p]] > 0):  # 尚有空位，录取成功
                admitted = True
                quota[MajorName[p]] -= 1     # 该专业空位减一
                admittedNum[group] += 1  # 该专业组录取人数加1
                stu[4] = p  # 记录学生最终录取志愿
                admittedStu[group].append(stu)  # 记录此学生
                break
        if (admitted == False):   # 录取失败
            if (stu[5] == '是'):  # 服从调剂
                adjusting.append(stu)  # 添加到本专业等待调剂List
            else:
                stu[4] = '未录取'  # 记录学生落榜 
                failedStu[group].append(stu)  # 添加到落榜名单

    # 报名专业志愿录取完成，进行调剂
    # 计算当前专业组可调剂的名额
    adjustQuota = quotaNum[group] - admittedNum[group]
    # 顺序考察待调剂学生，进行调剂操作
    for stu in adjusting:
        if (adjustQuota > 0):  # 专业组内还有名额，记录为调剂
            stu[4] = '专业组内调剂'  # 标记录取状态为调剂
            adjustStu[group].append(stu)  # 添加到调剂名单
            admittedNum[group] += 1
            adjustQuota -= adjustQuota
        else:
            stu[4] = '未录取'  # 落榜
            failedStu[group].append(stu)


#################################################
################# 合并 Combine ##################
#################################################

# dfAdmitted：存放已录取学生名单的DataFrame 
dfAdmitted = pd.DataFrame()
# 添加各专业组志愿录取的学生名单
for _, table in admittedStu.items():  
    df = pd.DataFrame(table)
    dfAdmitted = pd.concat([dfAdmitted, df])
# 添加各专业组志愿调剂的学生名单
for _, table in adjustStu.items():
    df = pd.DataFrame(table)
    dfAdmitted = pd.concat([dfAdmitted, df])

# dfAdmitted：存放未录取学生名单的DataFrame 
dfFailed = pd.DataFrame()
# 添加各专业组未录取的学生名单
for _, table in failedStu.items():
    df = pd.DataFrame(table)
    dfFailed = pd.concat([dfFailed, df])

# dfAll：完整的志愿录取情况名单
dfAll = pd.concat([dfAdmitted, dfFailed]) 
dfAll = dfAll.sort_values(by=0)  # 按报名号进行排序
# 对DataFrame进行格式处理
dfAll.drop(5, axis=1, inplace=True) 
dfAll.columns = ['报名号', '综合成绩', '专业组', '排名', '录取情况']
dfAll['报名号'] = dfAll['报名号'].apply(lambda x: '{:06}'.format(x))

# 计算每个专业组的招生计划名额、实际录取名额、录取成绩的最高/低分以及录取比例
print('各个专业组的招生统计信息:')
print('\t 专业组 \t 计划名额 \t 录取名额 \t 录取最高分 \t 录取最低分 \t 录取比例')
stat = []
for group, qn in quotaNum.items():
    maxScore = admittedStu[group][0][1]
    minScore = admittedStu[group][-1][1]
    admitRatio = admittedNum[group] / quotaNum[group]
    # 格式化打印数据
    print('\t {:<8} \t {:<8} \t {:<8} \t {:.2f} \t {:.2f} \t {:.2%}'
          .format(group, qn, admittedNum[group], maxScore, minScore, admitRatio))
    stat.append([group, qn, admittedNum[group], maxScore, minScore, admitRatio])
# 将统计数据保存到DataFrame，便于写入文件
dfStat = pd.DataFrame(stat, columns = ['专业组', '计划名额', '录取名额', '录取最高分', '录取最低分', '录取比例'])
dfStat['录取比例'] = dfStat['录取比例'].apply(lambda x: '{:.2%}'.format(x))

# 将结果写入文件，录取结果和录取数据统计分别写入到两个Sheet
file_name = 'ScoreStat.xlsx'
with pd.ExcelWriter(file_name) as f:
    dfAll.to_excel(f, sheet_name='志愿录取情况', index=False)
    dfStat.to_excel(f, sheet_name='录取数据统计', index=False)

print('\n志愿录取结果已经写入到文件{}: '.format(file_name))
print('\t- 每位考生的志愿录取情况(录取专业、调剂、未录取)已经写入到工作表：“志愿录取情况”。')
print('\t- 每个专业组的录取数据分析(计划名额、录取名额、最高/最低分和录取比率)已经写入到工作表: “录取数据统计”。')