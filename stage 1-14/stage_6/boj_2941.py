# 2941

a = input()

tmp = ''
cro = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cro:
    if c in a:
        a = a.replace(c, 'a')
        
print(len(a))