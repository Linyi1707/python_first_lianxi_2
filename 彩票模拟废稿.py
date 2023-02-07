

# 彩票模拟小游戏

import random

k1 = '开始游戏'
k2 = '结束游戏'
print(k1.center(60, '*'))
data = list()
money = int(input('请输入您的基础金额：'))
print('您现在的余额为%d' % money)
while money >= 0:
	for i in range(0, 6):
		 = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
		data.append()
# print(data)
# break
	while 1:
		if money <= 0:
			money = int(input('余额过少，请充值：'))
		else:
			jiang = int(input('请输入想要投入的金额：'))
			money = money - jiang
			print('您现在的余额为%d.' % money)
			break
# print(money)
	cai = input('请输入你的竞猜号码：')
	cai = list(cai)
	# print(cai, data)
	if cai == data:
		jiang = jiang * 32
		money = jiang + money
		print('恭喜全部猜中！您中了特等奖，奖金为%d的，以为您放入余额中。\n现在您的余额为%d。' % (jiang, money))
	elif cai[0] == data[0]:
		if cai[1] == data[1]:
			if cai[2] == data[2]:
				if cai[3] == data[3]:
					if cai[4] == data[4]:
						jiang = jiang * 16
						money = money + jiang
						print('恭喜猜中5个号码！奖金为%d的，以为您放入余额中。\n现在您的余额为%d。' % (jiang, money))
					else:
						jiang = jiang * 8
						money = money + jiang
						print('恭喜猜中4个号码！奖金为%d的，以为您放入余额中。\n现在您的余额为%d。' % (jiang, money))
				else:
					jiang = jiang * 4
					money = money + jiang
					print('恭喜猜中3个号码！奖金为%d的，以为您放入余额中。\n现在您的余额为%d。' % (jiang, money))
			else:
				jiang = jiang * 2
				money = money + jiang
				print('恭喜猜中2个号码！奖金为%d的，以为您放入余额中。\n现在您的余额为%d。' % (jiang, money))
		else:
			jiang = jiang * 1
			print('恭喜猜中1个号码！奖金为%d的，以为您放入余额中。\n现在您的余额为%d。' % (jiang, money))
	else:
		jiang = 0
		print('很遗憾您全未猜中，奖金为%d。\n现在您的余额为%d。' % (jiang, money))

		print('阳桑，故乡的樱花开了，你有去看吗？:)')