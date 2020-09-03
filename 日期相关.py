import datetime
# 无法显示今天以外的日期
today = datetime.date.today()
print(today)

# 另一种方式显示日期，可指定只显示年份，月份，日期中的任意数值，同时可指定任意顺序
# strftime格式化时间时可在其中加入分隔符，但是之后无法计算
formatted_today = today.strftime('%y%m%d')
print(formatted_today)
print(int(formatted_today)-1)

# 跨月份时，先获取今天的信息，然后使用datetime的timedetla对象，这个对象表示两个时间差值
# datetime.timedelta(days=-1)表示往前一天的时间，3月1日往前一天就是2月28日。
# 最后用strftime转换时间格式
yesterday = (datetime.date.today() + datetime.timedelta(days = -1)).strftime('%y%m%d')
print(yesterday)

# 显示当前时间
# 时间戳表示从特定时间开始经过的时间，一般用来计算程序运行的时间

import time
ticks = time.time()
print(f'当前时间戳为：{ticks}')

# 获取当前时间需要从时间戳开始转换，时间戳参数可取消
localtime = time.localtime(ticks)
print(f'本地时间为：',localtime)

# 获取格式化的时间
localtime = time.asctime(localtime)
print(f'本地时间为：',localtime)

# 格式化日期，需注意时间的大小写
# 该情况的第一种最常用

print(f'本地时间为：',time.strftime('%y-%m-%d %H:%M:%S',time.localtime()))
print(f'本地时间为：',time.strftime('%a %b %d %H:%M:%S %Y',time.localtime()))
