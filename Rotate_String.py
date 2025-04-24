s = "abcde"
goal = "abced"

match =''
unmatch =''

for i in range(len(s)):
    if s[i] == goal[0]:
        unmatch = s[i:]
        match = s[:i]

if unmatch+match == goal:
    print("match",True)
print("unmatch",False)


print(len(s)==len(goal) and s in goal+goal)