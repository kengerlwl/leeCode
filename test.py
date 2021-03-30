import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#str = input()
#print(str)
# print('hello world!')


nums = input().split(' ')
for i in range(len(nums)):
    nums[i] = int(nums[i])
