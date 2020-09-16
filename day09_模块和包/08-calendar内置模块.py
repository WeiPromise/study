#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 15:06

# 用来显示一个日历

import calendar


# 设置每周起始日期。周一到周日分别对应 0-6
calendar.setfirstweekday(calendar.TUESDAY)

# 返回当前每周其实日期的设置。默认情况下。首次载入calendar模块时返回0，即周一
print(calendar.firstweekday())

# 生成2019年的日历，并且一周日为起始日期
c = calendar.calendar(2019)
# print(c)

# 闰年返回TRUE
print(calendar.isleap(2020))

#获取1996年到2020年一种有几个闰年
print(calendar.leapdays(1996,2020))

# 打印2019年3月的日历
print(calendar.month(2019,3))