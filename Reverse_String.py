s = ["h","e","l","l","o"]

# print(list(''.join(s)[::-1]))
#
# print(s.reverse())
# s[:]=s[::-1]
#
# print(s)

left =0
right=len(s)-1

while left<=right:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print(s)