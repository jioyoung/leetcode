def medianofmedian(nums, k):
    sublists = [nums[j:j+5] for j in range(0,len(nums), 5)]
    medians = [sorted(list)[len(list)//2] for list in sublists]
    if len(medians)<=5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        pivot = medianofmedian(medians, len(medians)//2)
    low = []
    high = []
    for i in range(len(nums)):
        if nums[i]<pivot:
            low.append(nums[i])
        else:
            high.append(nums[i])
    n = len(low)
    if k<n:
        return medianofmedian(low, k)
    elif k>n:
        return medianofmedian(high, k-n-1)
    else: 
        return pivot
        
print(medianofmedian([1,4,2,5,6,3,9],2))