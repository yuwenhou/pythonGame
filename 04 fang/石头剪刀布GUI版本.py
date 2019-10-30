import random
import easygui as G

# 出拳
punches = ['石头','剪刀','布']
computer = random.choice(punches)
user = G.enterbox('请出拳：（石头、剪刀、布）')  # 请用户输入选择

while user not in punches:  # 当用户输入错误，提示错误，重新输入
    G.msgbox('输入有误，请重新出拳')
    user = G.enterbox('请出拳：（石头、剪刀、布）')

# 亮拳
def show(U,C):
    G.msgbox('————战斗过程————\n   电脑出了：%s \n   你出了：%s\n'% (C, U))

# 胜负

def competition(U,C):
    '''使用if进行条件判断'''
    
    if ((U == '石头' and C == '剪刀') 
          or (U == '剪刀' and C == '布') 
          or (U == '布' and C == '石头')):
        G.msgbox('—————结果—————\n\t你赢了！')
    elif U == C:  
        G.msgbox('—————结果—————\n\t平局！')
    else:
        G.msgbox('—————结果—————\n\t你输了！')

show(user,computer)
competition(user,computer)
