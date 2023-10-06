
nums = int(input(""))
lst = [None] * nums
for i in range(nums):
    word = str(input(""))

    if(len(word) > 10):
        x = ""
        x += (word[0])
        
        y = ""
        num = str(len(word) - 2)
        
        num += (word[len(word)-1])
        lst[i] = str(x + num)
    else:
        lst[i] = word

for i in lst:
    print(i)