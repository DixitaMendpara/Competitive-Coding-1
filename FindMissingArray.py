
# Online Python - IDE, Editor, Compiler, Interpreter

def missing(nums):
    low=0
    high=len(nums)-1
    while low<high:
        mid = low+(high-low)//2
        if abs(nums[low]-low) != abs(nums[mid]-mid):
            high=mid-1
        else:
            low=mid+1
    return nums[low]+1        

a = [1,2,3,4,6,7]
print(missing(a))
