"""
@brief: 求和 ∑f(xk) : xk表示等距节点的第k个节点，不包括端点
        xk = a + kh (k = 0, 1, 2, ...)
        积分区间为[a, b]
         
@param: xk      积分区间的等分点x坐标集合（不包括端点）
@param: func    求积函数
@return: 返回值为集合的和
"""
def sum_fun_xk(xk, func):
    return sum([func(each) for each in xk])


"""
@brief: 求func积分 :
         
@param: a  积分区间左端点
@param: b  积分区间右端点
@param: n  积分分为n等份（复化梯形求积分要求）
@param: func  求积函数
@return: 积分值
"""  
def integral(a, b, n, func):
    h = (b - a)/float(n)
    xk = [a + i*h for i in range(1, n)]
    return h/2 * (func(a) + 2 * sum_fun_xk(xk, func) + func(b))

if __name__ == "__main__":
     
    func = lambda x: x**2
    a, b = -1, 1
    n = 20
    print(integral(a, b, n, func))
     
    ''' 画图 '''
    import matplotlib.pyplot as plt
    plt.figure("play")
    ax1 = plt.subplot(111)
    plt.sca(ax1)
     
    tmpx = [a + float(b-a) /50 * each for each in range(50+1)]
    plt.plot(tmpx, [func(each) for each in tmpx], linestyle = '-', color='black')
     
    for rang in range(n):
        tmpx = [a + float(b-a)/n * rang, a + float(b-a)/n * rang, a + float(b-a)/n * (rang+1), a + float(b-a)/n * (rang+1)]
        tmpy = [0, func(tmpx[1]), func(tmpx[2]), 0]
        c = ['r', 'y', 'b', 'g']
        plt.fill(tmpx, tmpy, color=c[rang%4])
    plt.grid(True)
    plt.show()