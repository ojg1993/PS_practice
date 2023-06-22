eq = input()
temp = []
if '+' in eq:
  a = eq.split('+')
  for i in a[0]:
    if i.isdigit():
      temp.append(i)
  temp = ''.join(temp)
  x = (int(a[1]) * -1)/int(temp)
else:
  a = eq.split('-')
  for i in a[0]:
    if i.isdigit():
      temp.append(i)
  temp = ''.join(temp)
  x = (int(a[1]))/int(temp)


print(format(x, '.2f'))
