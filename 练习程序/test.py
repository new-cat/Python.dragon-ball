#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# '''
# 1. 给定一个非空整数数组，用位运算求其唯一值
# '''
# def Single(s):
#     num = s[0];
#     i = 1;
#     while (i < len(s)):
#         num = num ^ s[i];
#         i += 1;
#     return num;
# s = [3, 2, 9, 2, 3, 4, 7, 7, 4]
# print(Single(s))


# '''
# 2. 编写一个Python程序来查找那些可以被7除余5的整数的数字，介于1500和2700之间。
# '''
# def Search():
#     x = [i for i in range(1500,2700,1) if (i % 7) == 5]
#     print(x)
# Search();



# '''
# 3. 龟兔赛跑，给定v1,v2,t,s,l，预测结果
# (v1,v2< =100;t< =300;s< =10;l< =10000且为v1,v2的公倍数)
# 输出包含两行:
# 第一行输出比赛结果——一个大写字母“T”或“R”或“D”，分别表示乌龟获胜，兔子获胜，或者两者同时到达终点。
# 第二行输出一个正整数，表示获胜者（或者双方同时）到达终点所耗费的时间（秒数）。
# '''
# def Forecast():
#     v1,v2,s,t,l = map(int,input('请分别输入兔子速度,乌龟速度,兔子领先阈值,兔子休息时间,赛道长度').split(' '))
#     sec = 0;    #时间变量
#     tmp = 0;    #兔子休息次数
#     while not ((v2*sec>=l) or (v1 * (sec - tmp*sec)>=l)):
#         if((v1 * (sec - tmp*sec) - v2 *sec) >= s):
#             tmp += 1;
#             sec += t;
#         else:
#             sec += 1;
#     else:
#         if (v2*sec>=l) > (v1 * (sec - tmp*sec)) :
#             print('D');
#         elif (v2*sec>=l) < (v1 * (sec - tmp*sec)) :
#             print('R');
#         else :
#             print('T');
#         print(sec);
# Forecast();



# '''
# 4. 猜数字游戏，异常处理结构try-except语句
# '''
# import random
# guess=random.randint(0,100)
# i = 1;
# print('猜测一个0到100之间的整数')
# while True:
#     try:
#         temp=int(input('第' +str(i)+ '次猜，请输入一个整型数字：'))
#         i += 1;
#     except ValueError :
#         print ("输入无效")
#         continue;
#     if temp==guess:
#         print ("恭喜你猜对了，就是这个数",guess)
#         break;
#     elif (temp>guess):
#         print ("太大")
#     elif (temp<guess):
#         print ("太小")

