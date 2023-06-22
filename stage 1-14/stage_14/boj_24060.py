# 24060

def m_sort(lst):
    if len(lst) <= 1:
        return lst
    
    center = (len(lst)+1) // 2
    left = m_sort(lst[:center])
    right = m_sort(lst[center:])
    
    i = j = 0
    new_lst = []
    
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            new_lst.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            new_lst.append(right[j])
            ans.append(right[j])
            j += 1
    while i < len(left):
        new_lst.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        new_lst.append(right[j])
        ans.append(right[j])
        j += 1
    return new_lst

n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
m_sort(nums)

if len(ans) <= k:
    print(-1)
else:
    print(ans[k-1])
