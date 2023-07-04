file = open('numbers.txt', 'r', encoding='utf-8')
nums = [int(num) for num in file.readlines()]
print(sum(nums))

file.close()

# Красивое решение
# print(sum(map(int, file)))