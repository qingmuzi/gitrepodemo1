
# 第一天需求
#  Tempture Change :C and F
#   C = (F -32) /1.8
#   F = C * 1.8 + 32

def Temchange():
    temp = input('Enter the tempture:')
    if temp[-1] in ['f', 'F']:
        C = (eval(temp[:-1]) - 32) / 1.8
#        print('Tempture change %.2f' % (C))
        print ('Tempture change {:.2f}C'.format(C))
    elif temp[-1] in ['c', 'C']:
        F = eval(temp[:-1]) * 1.8 + 32
        print ('Tempture change {:.2f}F'.format(F))
    else:
        print("Input error!!!")




Temchange()