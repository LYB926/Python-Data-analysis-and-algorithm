'''
2.	给定一组足球比赛的视频片段，视频片段涵盖了不同时间段的比赛内容，且能够覆盖完整的比赛内容。请计算能覆盖完整内容的最小的视频数量与所选的视频集合。
要求测试下例：
（1）[1,2], [2,3], [3,10], N =10
（2）[1,2], [1,10], [2,4], [2,10], [3,4], [3,12], N=12
'''
# clips = [[1, 2], [2, 3], [3, 10]]
# N = 10
clips = [[1,2], [1,10], [2,4], [2,10], [3,4], [3,12]]
N = 12
print('Clips = ', clips, '\nN = ', N)

# 使用二进制穷举法
num_clips = len(clips)
min_len = float('inf')
min_dura = float('inf')
selected_clips = []

for i in range(0, (1 << num_clips)):
    tmp_clips = []
    for j in range(0, num_clips):
        if (i & (1 << j)):
            tmp_clips.append(clips[j])

    # 判定穷举得到的片段是否合法
    tmp_len = len(tmp_clips)
    if (tmp_len == 0):
        continue
    tmp_clips.sort()
    flag = True
    if (tmp_clips[0][0] != 1) or (tmp_clips[tmp_len-1][1] < N):
        flag = False
    for k in range(0, tmp_len-1):
        if (tmp_clips[k][1] < (tmp_clips[k+1][0]-1)):
            flag = False

    # 如果序列合法，检查视频数量是否最少且时长（dura）最短
    if flag == True:
        lenc = tmp_len
        dura = 0
        for u in range(0, tmp_len):
            dura = dura + (tmp_clips[u][1] - tmp_clips[u][0])
        if (lenc < min_len):
            min_len, min_dura, selected_clips = lenc, dura, tmp_clips
        if ((lenc == min_len) and (dura < min_dura)):
            min_len, min_dura, selected_clips = lenc, dura, tmp_clips

print ('\n最小的视频数量: {}'.format(len(selected_clips)))
print (selected_clips)
        