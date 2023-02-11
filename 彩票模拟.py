# 彩票模拟小游戏
import random
k1 = '开始游戏'
k2 = '结束游戏'
print(k1.center(60, '*'))
try:
	money = int(input('请输入您的基础金额：'))
	print('您现在的余额为%d' % money)
	while 1:
		data = list()
		for i in range(0, 6):
			s = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
			data.append(s)
		while 1:
			data1 = money
			if money <= 0:
				money = int(input('余额过少，请充值：')) + money
			else:
				data3 = jiang = int(input('请输入想要投入的金额：'))
				money = money - jiang
				jiang = data2 = jiang * 2 // 3
				print('您现在的余额为%d.' % money)
				break
		if jiang < 0:
			money = money + data3
			break
		if money < 0:
			print('请输入小于余额的金额！')
			money = data1
			break
		cai = list(input('请输入你的竞猜号码：'))
		a = int()
		x = int(2)
		for i in range(0, len(data)):
			if cai[i] == data[i]:
				a = a + 1
		for b in range(1, a):
			data2 = data2 * x
		if a == 0:
			jiang = 0
		else:
			jiang = data2
		money = jiang + money
		print('中奖号码为\n%s\n您猜中了%d个号码，奖金为%d，奖金已为您放入余额。\n您的余额为%d' % (data, a, jiang, money))
		if str(1) == input("请问还要继续竞猜么？如果不想请请按1,继续请任意输入字符："):
			break
except (ValueError, IndexError):
	print('请输入正确字符！')
else:
	print("你的余额为：%d元" % money)
print(k2.center(60, "*"))
