##if even number of odd numbers --> yes or sum is even
## if odd sum --> which means even number of odd numbers, then no

nums = int(input(""))
lst = []
for i in range(nums):
    num = int(input(""))
    for j in range(num):
        line = input("").split()
        lst.append(line)

print(lst)
