# 25206

my_dict={
    'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,
    'F':0.0
    }

s_t = 0
c_t = 0

for _ in range(20):
    subject, credit, grade = input().split()
    if grade != 'P':
        s_t += float(credit) * my_dict[grade]
        c_t += float(credit)

print(format(s_t/c_t, '.6f'))


