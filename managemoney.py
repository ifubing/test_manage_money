import json
import datetime

import datetimetools

class Person:
    def __init__(self):
        # 读取个人的配置信息
        self.data = self.load_data()
        # 用户的余额
        self.left_money = self.data['left_money']

    def start(self):
        """主要逻辑"""
        # 获取当天的时间
        today = datetimetools.get_now_datetime()
        # 日期时间增量，一天一天的增
        one_day = datetime.timedelta(days=1)

        # 打印输出内容的容器
        change_info_list = list()

        # change_day_list = [9, 15, 26]
        change_day_list = [li[0] for li in self.data['change']]
        print(change_day_list)

        # 获取时间长量是90天
        # for i in range(1, 91):
        for i in range(1, 91):
            # 判断当天是否有扣款行为
            # 获取今天是几号
            day = today.day  # 5   int
            if day not in change_day_list:
                today += one_day
                continue



            # print(day)

            # 看一看今天是否有扣款的行为
            for change_list in self.data['change']:
                # print(change_list)
                # 比较一下当天是否有扣款行为
                if day == change_list[0]:
                    ls = [
                        datetimetools.get_datetime_strftime(today),
                        "扣款前金额：{}".format(self.left_money),
                        "发生变化的金额：{}".format(change_list[1]),
                        "名称：{}".format(change_list[2]),
                        "扣款后的变化:{}".format(self.left_money+change_list[1])
                    ]

                    self.left_money += change_list[1]
                    # print('余额为', self.left_money)
                    change_info_list.append(ls)
                    break


            # 时间往后走一天
            today += one_day
            # print('新的一天开始了', today)



            # 当前天数 + 1天增量
            # # 让时间流动起来
            # 对日期进行判断
            # 如果9号，那么
            # self.left_money += 金额
            # if 余额为负数：
            #     提醒和警告操作
            pass

        for change_info in change_info_list:
            print(change_info)

    def load_data(self):
        with open('money.db', 'r', encoding='utf8') as f:
            content = f.read()
            content = json.loads(content)
        return content


p = Person()

import time

start = time.time()
p.start()
end = time.time()

print('耗时为{}', end - start)
