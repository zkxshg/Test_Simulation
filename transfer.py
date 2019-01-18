import numpy as np
from fangzhen import Test
import matplotlib.pyplot as plt
#生成语数外/语数总分，并给出考生总人数和上锚点和下锚点
#输入真实成绩，计算转换后分布
def test_real(danke,a ,b ):
    danke.sort()
    A_o = []
    B_o = []
    C_o = []
    D_o = []
    E_o = []
    for n in danke:
        if n>=91:
            A_o.append(n)
        elif n>=76:
            B_o.append(n)
        elif n>=61:
            C_o.append(n)
        elif n>=41:
            D_o.append(n)
        else:
            E_o.append(n)
    #print(A_f)
    print ("%.4f"%(len(A_o)/len(danke)))
    #print(B_f)
    print ("%.4f"%(len(B_o)/len(danke)))
    #print(C_f)
    print ("%.4f"%(len(C_o)/len(danke)))
    #print(D_f)
    print ("%.4f"%(len(D_o)/len(danke)))
    #print(E_f)
    print ("%.4f"%(len(E_o)/len(danke)))

    uppoint = int(len(danke)*(1-a))+1
    downpoint = int(len(danke)*b)+1
    A_value = danke[uppoint]
    E_value = danke[downpoint]
    print (len(danke))
    print(A_value)
    print(E_value)
    A=[]
    E=[]
    other = []
    for n in danke :
        if n >= A_value:
            A.append(n)
        else:
            if n <= E_value:
                E.append(n)
            else:
                other.append(n)
    A_f=[]
    for n in A:
        n = 100-(100-n)*(100-91)/(100-A_value)
        A_f.append(int(n))
    #print(E)
    E_f = []
    for n in E:
        n = 41 * n/ E_value
        E_f.append(int(n))
    #print(E_f)
    other_new = []
    for n in other:
        n = 91-50*(A_value-n)/(A_value-E_value)
        other_new.append(int(n))
    #print(A_value)
    #print(other)
    #print(other_new)
    B_f = []
    C_f = []
    D_f = []
    for n in other_new:
        if n>=76:
            B_f.append(n)
        else:
            if n>=61:
                C_f.append(n)
            else:
                D_f.append(n)
    #print(A_f)
    print ("%.4f"%(len(A_f)/len(danke)))
    #print(B_f)
    print ("%.4f"%(len(B_f)/len(danke)))
    #print(C_f)
    print ("%.4f"%(len(C_f)/len(danke)))
    #print(D_f)
    print ("%.4f"%(len(D_f)/len(danke)))
    #print(E_f)
    print ("%.4f"%(len(E_f)/len(danke)))
    plot_test(danke)
    p_p = []
    p_p.extend(A_f)
    p_p.extend(other_new)
    p_p.extend(E_f)
    plot_test(p_p)
    '''
    plot_test(A_f)
    plot_test(B_f)
    plot_test(C_f)
    plot_test(D_f)
    plot_test(E_f)
    '''
#输入单个学生成绩score、真实单科成绩记录dake，上锚点a和下锚点b，输出转换后成绩
def test_realdata_singe(score,danke,a,b):
    danke.sort()
    uppoint = int(len(danke) * (1 - a)) + 1
    downpoint = int(len(danke) * b) + 1
    A_value = danke[uppoint]
    E_value = danke[downpoint]
    print(A_value)
    print(E_value)
    print(len(danke))
    A = []
    E = []
    other = []
    for n in danke:
        if n >= A_value:
            A.append(n)
        else:
            if n <= E_value:
                E.append(n)
            else:
                other.append(n)
    A_f = []
    for n in A:
        n = 100 - (100 - n) * (100 - 91) / (100 - A_value)
        A_f.append(int(n))
    # print(E)
    E_f = []
    for n in E:
        n = 41 * n / E_value
        E_f.append(int(n))
    # print(E_f)
    other_new = []
    for n in other:
        n = 91 - 50 * (A_value - n) / (A_value - E_value)
        other_new.append(int(n))
    # print(A_value)
    # print(other)
    # print(other_new)
    B_f = []
    C_f = []
    D_f = []
    for n in other_new:
        if n >= 76:
            B_f.append(n)
        else:
            if n >= 61:
                C_f.append(n)
            else:
                D_f.append(n)
    # print(A_f)
    print("%.4f" % (len(A_f) / len(danke)))
    # print(B_f)
    print("%.4f" % (len(B_f) / len(danke)))
    # print(C_f)
    print("%.4f" % (len(C_f) / len(danke)))
    # print(D_f)
    print("%.4f" % (len(D_f) / len(danke)))
    # print(E_f)
    print("%.4f" % (len(E_f) / len(danke)))
    p_p = []
    p_p.extend(A_f)
    p_p.extend(other_new)
    p_p.extend(E_f)
    print(np.mean(p_p))
    if score >= A_value:
        n1 = 100 - (100 - score) * (100 - 91) / (100 - A_value)
    else:
        if score <= E_value:
            n1 = 41 * score/ E_value
        else:
            n1 = 91 - 50 * (A_value - score) / (A_value - E_value)
    return  n1

def step_one():
    sum_ysw = Test.get_sample(225, 150000, 450, 225)
    #return sum_ysw
    ysw = sum_ysw
    p_95 = 450 * 0.95
    p_5 = 450* 0.05
    ysw.sort()
    l = len(ysw)
    # print(ysw)
    i = 0
    j = 0
    for n in ysw:
        if n >= p_95:
            i += 1
        if n <= p_5:
            j += 1
    return i/l,j/l

#绘出单科成绩分布图
def plot_test(array):
    x_c = []
    y_c = []
    for i in range(0,100):
        j = 0
        for n in array:
            if n==i:
                j+=1
        x_c.append(i)
        y_c.append(j)
    plt.plot(x_c, y_c)
    #print (x_c)
    #print (y_c)
    plt.show()

#输入考生单科成绩，模拟转换流程，给出转化后成绩
def test_stu(score,diff_wuli, per_wuli,a,b):
    mean_score = int(100 * diff_wuli)
    stu_num = int(150000 * per_wuli)
    wuli = Test.get_sample(mean_score, stu_num, 100, mean_score / 2)
    wuli.sort()
    for i in wuli:
        if i>101:
            print("wo cao")
    uppoint = int(len(wuli) * (1 - a)) + 1
    downpoint = int(len(wuli) * b) + 1
    A_value = wuli[uppoint]
    E_value = wuli[downpoint]
    print(A_value)
    print(E_value)
    print(len(wuli))
    A = []
    E = []
    other = []
    for n in wuli:
        if n >= A_value:
            A.append(n)
        else:
            if n <= E_value:
                E.append(n)
            else:
                other.append(n)
    A_f = []
    for n in A:
        n = 100 - (100 - n) * (100 - 91) / (100 - A_value)
        A_f.append(int(n))
    # print(E)
    E_f = []
    for n in E:
        n = 41 * n / E_value
        E_f.append(int(n))
    # print(E_f)
    other_new = []
    for n in other:
        n = 91 - 50 * (A_value - n) / (A_value - E_value)
        other_new.append(int(n))
    # print(A_value)
    # print(other)
    # print(other_new)
    B_f = []
    C_f = []
    D_f = []
    for n in other_new:
        if n >= 76:
            B_f.append(n)
        else:
            if n >= 61:
                C_f.append(n)
            else:
                D_f.append(n)
    # print(A_f)
    print("%.4f" % (len(A_f) / len(wuli)))
    # print(B_f)
    print("%.4f" % (len(B_f) / len(wuli)))
    # print(C_f)
    print("%.4f" % (len(C_f) / len(wuli)))
    # print(D_f)
    print("%.4f" % (len(D_f) / len(wuli)))
    # print(E_f)
    print("%.4f" % (len(E_f) / len(wuli)))
    p_p = []
    p_p.extend(A_f)
    p_p.extend(other_new)
    p_p.extend(E_f)
    print(np.mean(p_p))
    if score >= A_value:
        n1 = 100 - (100 - score) * (100 - 91) / (100 - A_value)
    else:
        if score <= E_value:
            n1 = 41 * score/ E_value
        else:
            n1 = 91 - 50 * (A_value - score) / (A_value - E_value)
    return  n1

#根据给出的难易度和参与率，模拟单科成绩分布，给出各分段人数比例
def test_wuli(diff_wuli, per_wuli,a ,b ):
    mean_score = int(100*diff_wuli)
    stu_num = int(150000*per_wuli)
    wuli = Test.get_sample(mean_score, stu_num, 100, mean_score / 2)
    wuli.sort()


    A_o = []
    B_o = []
    C_o = []
    D_o = []
    E_o = []
    for n in wuli:
        if n>=91:
            A_o.append(n)
        elif n>=76:
            B_o.append(n)
        elif n>=61:
            C_o.append(n)
        elif n>=41:
            D_o.append(n)
        else:
            E_o.append(n)
    #print(A_f)
    print ("%.4f"%(len(A_o)/len(wuli)))
    #print(B_f)
    print ("%.4f"%(len(B_o)/len(wuli)))
    #print(C_f)
    print ("%.4f"%(len(C_o)/len(wuli)))
    #print(D_f)
    print ("%.4f"%(len(D_o)/len(wuli)))
    #print(E_f)
    print ("%.4f"%(len(E_o)/len(wuli)))

    uppoint = int(len(wuli)*(1-a))+1
    downpoint = int(len(wuli)*b)+1
    A_value = wuli[uppoint]
    E_value = wuli[downpoint]
    print (len(wuli))
    print(A_value)
    print(E_value)
    A=[]
    E=[]
    other = []
    for n in wuli :
        if n >= A_value:
            A.append(n)
        else:
            if n <= E_value:
                E.append(n)
            else:
                other.append(n)
    A_f=[]
    for n in A:
        n = 100-(100-n)*(100-91)/(100-A_value)
        A_f.append(int(n))
    #print(E)
    E_f = []
    for n in E:
        n = 41 * n/ E_value
        E_f.append(int(n))
    #print(E_f)
    other_new = []
    for n in other:
        n = 91-50*(A_value-n)/(A_value-E_value)
        other_new.append(int(n))
    #print(A_value)
    #print(other)
    #print(other_new)
    B_f = []
    C_f = []
    D_f = []
    for n in other_new:
        if n>=76:
            B_f.append(n)
        else:
            if n>=61:
                C_f.append(n)
            else:
                D_f.append(n)
    #print(A_f)
    print ("%.4f"%(len(A_f)/len(wuli)))
    #print(B_f)
    print ("%.4f"%(len(B_f)/len(wuli)))
    #print(C_f)
    print ("%.4f"%(len(C_f)/len(wuli)))
    #print(D_f)
    print ("%.4f"%(len(D_f)/len(wuli)))
    #print(E_f)
    print ("%.4f"%(len(E_f)/len(wuli)))
    plot_test(wuli)
    p_p = []
    p_p.extend(A_f)
    p_p.extend(other_new)
    p_p.extend(E_f)
    plot_test(p_p)
    '''
    plot_test(A_f)
    plot_test(B_f)
    plot_test(C_f)
    plot_test(D_f)
    plot_test(E_f)
    '''

(a, b) = step_one()
#test_wuli(0.7, 0.4, a, b)
sco = test_stu(80,0.7,0.4,a,b)
print(sco)
#不同难度系数和不同学生人数
