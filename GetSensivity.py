import os.path
import re

class CGetSensitivity:
    def __init__(self):
        # 读取文件
        self.lines = []
        print("开始读取源文件......")
        file = r"D:\test\rxdr1\log_sensivity.txt"
        if os.path.isfile(file):
            with open(file, 'r') as fd:
                self.lines = fd.readlines()
        else:
            print("出现问题，可能是文件不存在")
            quit()

        print("共读取到 ", len(self.lines), " 行......")

        '''
        self.Get_ChI();
        self.Get_CH75();
        self.Get_CH100();
        self.Get_CH150();'''

    def GetMatchs(self, szModal):
        matchs = []
        for line in self.lines:
            res = re.findall(szModal, line)
            if res:
                sensi = re.search(r"Sensitivity:-[\d,'.']*", line).group()
                if sensi:
                    pos = sensi.find(':')
                    if pos >= 0:
                        matchs.append(sensi[pos + 1:])
        return matchs
       # print("共读取到 ", len(matchs), " 个符合条件的值")


    # 第一列：ChI
    def Get_ChI(self):
        # Rate0,p1,chW,T0
        # TestID:37 RF_mod:1 tx_sc:2 rate:1 TX_mod:255  p:0 ChModel:E Trms:75 CFO:0 Sensitivity:-95.29
        matchs = self.GetMatchs(r"rate:0[\s,\S]*p:1 ChModel:W Trms:0")
        print("共读取到 ", len(matchs), " 个符合条件的ChI值")
        return matchs

    # 第二列：CH75
    def Get_CH75(self):
        matchs = self.GetMatchs(r"RF_mod:1 tx_sc:2[\s,\S]*ChModel:E Trms:75")
        print("共读取到 ", len(matchs), " 个符合条件的Ch75值")
        return matchs

    # 第三列：CH100
    def Get_CH100(self):
        matchs = self.GetMatchs(r"RF_mod:1 tx_sc:2[\s,\S]*ChModel:E Trms:100")
        print("共读取到 ", len(matchs), " 个符合条件的Ch100值")
        return matchs

    # 第四列：CH150
    def Get_CH150(self):
        matchs = self.GetMatchs(r"RF_mod:1 tx_sc:2[\s,\S]*ChModel:E Trms:150")
        print("共读取到 ", len(matchs), " 个符合条件的Ch150值")
        return matchs


#ss = CGetSensitivity()
