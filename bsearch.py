def binarySearch(arr, target):
    Low=0
    high=len(arr)-1

    while Low<=high:
         mid=(Low+high)//2

    if arr[mid]==target:
        return mid

    elif arr[mid]>target:
        high= mid-1

    else : Low=mid+1

    return -1

arr=[1,2,3,4,5,6,7,8,9]
target = 7

result=binarySearch(arr,target)

if result != -1:
    print(f"Elemnt found at index {result}")
else:
    print("Element not found in array")