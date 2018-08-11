index = 0
i = 0
l = 0
c = 0
temp = ''
st = ''
while index < (len(s)-1):
    i = index

    l = 0
    while s[i] <= s[i + 1] and i < (len(s)-2):
        l += 1
        temp += s[i]
        i += 1
    temp += s[i]
    if l > c:
        c = l
        st = temp
        
    temp = ''
    l = 0
    index += 1
if c == 0:
    st = s[0]
print("Longest substring in alphabetical order is: "+st)
