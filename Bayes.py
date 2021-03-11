import pandas as pd
import numpy as np


class Bayes():
    # def __init__(self):
    #     self.A = self.create_A()

    def create_A(self):
        A = {}
        n = input('请输入划分数: ')
        for i in range(1, int(n) + 1):
            description = input('请输入A' + str(i) + '的描述: ')
            p = input('请估计A' + str(i) + '发生的概率: ')
            A[description] = float(p)
        self.A = A
        self.save_records_A(self.A)
        print('创建完成!')

    def display_A(self):
        for key, value in self.A.items():
            print(key + ': ' + str(round(value, 5) * 100)[:7] + '%')

    def add_B(self):
        a = []
        description = input('请输入事件B的描述: ')
        pb = 0
        self.save_records('\n')
        for key, value in self.A.items():
            text = '在' + key + '成立的条件下, ' + description + '的概率是: '
            p = input(text)
            # 保存在日志中
            self.save_records(text + p)
            # 全概率公式，累加 P(A)P(B|A)
            pb += value * float(p)
            a.append(value * float(p))
        # 根据贝叶斯公式计算出后验概率，覆盖先验概率
        i = 0
        for key in self.A.keys():
            self.A[key] = a[i] / pb
            i += 1
        self.save_records_A(self.A)
        print('先验概率已被校正!')

    def save(self, filename):
        df = pd.Series(self.A)
        df.to_csv(filename)
        print('保存成功!')

    def load(self, filename):
        df = pd.Series()
        df.read_csv(filename)
        self.A = df.to_dict()

    def save_records(self, text, filename='record.txt'):
        with open(filename, 'a') as ob:
            ob.write(text + '\n')

    def save_records_A(self, A, filename='record.txt'):
        with open(filename, 'a') as ob:
            for key, value in A.items():
                text = key + ': ' + str(round(value, 5) * 100)[:7] + '%\n'
                ob.write(text)


A1 = Bayes()
a = input('1. 创建 \n2. 添加事件 \n3. 输出 \n4. 保存 \n5. 读取\n6. 退出\n请输入要进行的操作: ')
while a != '6':
    if (a == '1'):
        A1.create_A()
    elif (a == '2'):
        A1.add_B()
    elif (a == '3'):
        A1.display_A()
    elif (a == '4'):
        filename = input('请输入文件名: ')
        A1.save(filename + '.csv')
    elif (a == '5'):
        filename = input('请输入文件名: ')
        A1.load(filename + '.csv')
    a = input('\n1. 创建 \n2. 添加事件 \n3. 输出 \n4. 保存 \n5. 读取\n6. 退出\n请输入要进行的操作: ')