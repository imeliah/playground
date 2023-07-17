from datetime import datetime

time_layout = "%Y-%m-%d %H:%M:%S"

# 获取时间戳（浮点数）
timestamp = datetime.timestamp(datetime.now())
print(timestamp)

# 时间戳转时间字符串
datetime_obj = datetime.fromtimestamp(timestamp)
print(datetime_obj)

# 时间字符串转时间戳
datetime_str = "2022-01-01 12:00:00"
datetime_obj = datetime.strptime(datetime_str, time_layout)
print(datetime_obj.timestamp())

# 获取指定格式的时间字符串
datetime_str = datetime.now().strftime(time_layout)
print(datetime_str)
