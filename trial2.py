def findNumber(arr, k):
    # Write your code here
    for i in range(1, arr[0]+1):
        if arr[i]==k:
            return "YES"
    return "NO"

print(findNumber([5,1,2,3,4,5],5))