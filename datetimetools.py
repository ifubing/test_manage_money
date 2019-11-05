"""
日期时间模块与时间柜块的综合工具
"""
import datetime
import time


# 获取当前时间
def get_now_datetime():
    """返回当前的datetime对象"""
    return datetime.datetime.now()


def get_now_timestamp():
    """返回当前的时间戳"""
    return time.time()


def get_now_strftime(fmt="%Y-%m-%d"):
    """
    返回当前的格式化时间字符串
    :param fmt: 格式化字符串
    :return:
    """
    now_time = get_now_datetime()
    return now_time.strftime(fmt)

# 获取指定时间的字符串显示
def get_datetime_strftime(dateteime_obj, fmt="%Y-%m-%d"):
    return dateteime_obj.strftime(fmt)

# 模块对象的转换
def timestamp2datetime(timestamp_obj):
    """
    时间戳转为日期时间对象
    :param timestamp_obj: 时间戳
    :return: 日期时间对象
    """
    return datetime.datetime.fromtimestamp(timestamp_obj)


def datetime2timestamp(datetime_obj):
    """
    日期时间对象转为字符串
    :param datetime_obj: 日期时间对象
    :return: 时间戳
    """
    return datetime_obj.timestamp()


def timedelta2second(timedelta_obj):
    """
    时间增量转秒数
    :param timedelta_obj: 时间增量对象
    :return: 秒数
    """
    return timedelta_obj.total_seconds()


# 获取指定的时间
def get_zero_datetime(datetime_obj):
    """
    获取日期时间对象对应的零点时间对象
    :param datetime_obj: 日期时间对象
    :return: 零点的日期时间对象
    """
    return datetime_obj.replace(hour=0, minute=0, second=0, microsecond=0)


def get_zero_timestamp(timestamp_obj):
    """
    获取时间戳对应的当天零点的时间戳
    :param timestamp_obj: 时间戳
    :return: 零点时间戳
    """
    # 时间戳转时间对象
    datetime_obj = timestamp2datetime(timestamp_obj)
    # 调用上面的方法，得到一个0点的时间象
    zero_datetime_obj = get_zero_datetime(datetime_obj)
    # 0点时间对象转时间戳
    zero_timestamp_obj = datetime2timestamp(zero_datetime_obj)
    # 返回
    return zero_timestamp_obj


def get_timestamp_by_str(year=2000, month=0, day=0, hour=0, minute=0, second=0, fmt="%Y-%m-%d"):
    """
    获取时间戳，根据时间字符串
    :param str_time: 时间字符串
    :param fmt: 格式
    :return: None 或者 时间戳
    """
    if fmt=="%Y-%m-%d":
        str_time = "{year}-{month}-{day}".format(year=year,month=month,day=day)
    elif fmt == "%Y-%m-%d %H:%M":
        str_time = "{year}-{month}-{day} {hour}:{minute}".format(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute
        )
    print(str_time)
    try:
        time_tuple = time.strptime(str_time, fmt)
    except:
        timestamp = None
    else:
        timestamp = time.mktime(time_tuple)
    return timestamp

def get_datetime_by_str(year=2000, month=1, day=1, hour=1, minute=1, second=1):
    res = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    return res


# 时间的比较
def compare_is_one_day_by_timestamp(timestamp_obj1, timestamp_obj2):
    """
    比较两个时间戳，判断是否是同一天
    :param timestamp_obj1: 第一个时间戳
    :param timestamp_obj2: 第二个时间戳
    :return:
    """
    is_one_day = False
    z1 = get_zero_timestamp(timestamp_obj1)
    z2 = get_zero_timestamp(timestamp_obj2)
    if z1 == z2:
        is_one_day = True
    return is_one_day

def compare_is_one_day_by_datetime(datetime_obj1, datetime_obj2):
    """
    比较两个datetime对象，判断是否是同一天
    :param datetime_obj1: 日期时间对象1
    :param datetime_obj2: 日蜞时间对象2
    :return:
    """
    is_one_day = False

    z1 = get_zero_datetime(datetime_obj1)
    z2 = get_zero_datetime(datetime_obj2)
    if z1 == z2:
        is_one_day = True

    return is_one_day



if __name__ == '__main__':

    # 测试
    # t1 = time.time()
    # time.sleep(3)
    # t2 = time.time()
    #
    # res = compare_is_one_day_by_timestamp(t1, t2)
    #
    # print(res)

    pass