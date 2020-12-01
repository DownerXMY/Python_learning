a = 100
while True:
    num = int(input('请猜测一个结果'))
    if num == a:
        print('恭喜您，猜对了')
        break
    elif num < a:
        print('很遗憾，您的猜测结果偏小')
    else:
        print('很遗憾，您的猜测结果偏大')

######################################
a = 97
n = 0
while True:
    num = int(input('请猜测一个结果'))
    n = n + 1
    if num == a and n == 1:
        print('恭喜您，一猜就中！')
        break
    elif num == a and 1 < n <= 5:
        print('恭喜您，经过不懈努力终于猜对了')
        break
    elif num < a and n <= 5:
        print('很遗憾，您猜测的结果偏小')
    elif num > a and n <= 5:
        print('很遗憾，您猜测的结果偏大')
    else:
        print('省省吧，就您这智商猜一万年也没戏！')
        break
################################################
