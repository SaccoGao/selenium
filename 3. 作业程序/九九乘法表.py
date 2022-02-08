for i in range(1, 10):
    for j in range(1, i+1):
        a = '{0}*{1} = {2}  '.format(j, i, i*j)
        print(a, end = '')
    print('')
