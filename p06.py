a=input('請輸入性別(M/F):')
if a == 'M':
    print("男")

if a=='M'or a=='m':
    print('男')

if a in ['M','m']:
    print('男')
else:
    print('女')

if a in ['F','f']:
    print('女')
elif a in ['m','M']:
    print('男')
else:
    print('輸入錯誤')

