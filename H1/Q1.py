# 生成邮箱地址：邮箱名形式为“用户名@域名.后缀”,
# 用户名和域名分别由6-12位和3-6位数字、字母、下划线组成，
# 后缀包含.com, .org, .net, .cn四种情况。

import string, random

def randomEmail():
    charList = string.digits + string.ascii_letters + '_'
    suffixList = ['.com', '.org', '.net', '.cn']
    name = domain = ''
    for i in range(0, random.randint(6,12)): name = name + random.choice(charList)
    for i in range(0, random.randint(3,6)):  domain = domain + random.choice(charList)
    return name + '@' + domain + random.choice(suffixList)
    
for i in range(0,6):
    mailAddr = randomEmail()
    print(mailAddr)