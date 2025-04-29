from collections import Counter

s = "loveleetcode"
# s = "aabb"

# for i in range(len(s)):
#     if s.count(s[i])==1:
#         print(s[i],i)
#         break
# print(-1)

count = Counter(s)

for key,value in count.items():
    print(key,value)
    if value==1:
        print(s.index(key))