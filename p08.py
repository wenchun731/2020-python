a=input('輸入職級')

if a in ['A','B']:
    print('年終6個月')
elif a in ['C','D']:
    print('年終4個月')
elif a in ['E','F']:
    print('年終3個月')
else:
    print('年終2個月')