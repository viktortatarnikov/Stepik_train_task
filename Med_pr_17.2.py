file = open('nums.txt', 'r', encoding='utf-8')
nums = map(int, file.read().split())
print(sum(nums))

file.close()

# В одну строчку
# print(sum(map(int, open('numbers.txt').read().split())))