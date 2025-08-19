n1 = float(input('digite sua nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 +n2)/2
print('sua média é {}'.format(m))
if m >= 7.0:
    print('você passou de ano!')
else:
    print('você não passou de ano')