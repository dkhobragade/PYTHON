haystack = "sadbutsad"
needle = "sad"
#
# print(haystack.find(needle))
#
# print(haystack.index(needle))

for i in range(len(haystack)):
    # print(haystack[i:i+len(needle)])
    if haystack[i:i+len(needle)] == needle:
        print(i)
        break
