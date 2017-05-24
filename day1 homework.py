#_*_coding:utf-8_*_
import sys
retry_limit=3
retry_count=0
account_file='accounts.txt'
lock_file='account.txt'

while retry_count<retry_limit:   #只要重试不超过三次就不跳出循环
    username=raw_input('pelase input your username:')
    lock_check=file(lock_file)   #当用户输入用户名之后，打开lock文件检查是否此用户已经lock
    for line in lock_check.readlines():  #循环lock文件
        if username in line:
            sys.exit('User %s is locked' %username) #如果lock了就直接退出
    password=raw_input('password:')
    f=file(account_file,'rb') #打开账号文件
    match_flag=False  #默认为false，如果用户match上了，就设置为Ture
    for line in f.readlines():
        user,passwd=line.strip('\n').split()
        #去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user，passwd两个变量
        if username==user and password==passwd:
             print 'Match',username
             match_flag=True
             break
    f.close()
    if match_flag==False:
        print 'user ummatched'
        retry_count+=1
    else:
        print'your account is locked'
        f.write(username)
        f.close()