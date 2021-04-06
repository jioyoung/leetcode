```python
def combination_no_duplicate(candidates, k):
    # 组合 无重复
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    getCombination(candidates, k, 0, res, [])
    return res

def getCombination(candidates, k, start, res, rec_res):
    if len(rec_res) == k:
        res.append(list(rec_res))
        return
    for i in range(start, len(candidates)):
        rec_res.append(candidates[i])
        getCombination(candidates, k, i+1, res, rec_res)
        rec_res.pop()
    return
```


```python
candidates = [1,2,3,4,5]
combination_no_duplicate(candidates, 2)
```




    [[1, 2],
     [1, 3],
     [1, 4],
     [1, 5],
     [2, 3],
     [2, 4],
     [2, 5],
     [3, 4],
     [3, 5],
     [4, 5]]




```python
def combination_duplicate(candidates, k):
    # 组合 重复
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    res = []
    getCombination_duplicate(candidates, k, 0, res, [])
    return res

def getCombination_duplicate(candidates, k, start, res, rec_res):
    if len(rec_res) == k:
        res.append(list(rec_res))
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        rec_res.append(candidates[i])
        getCombination_duplicate(candidates, k, i+1, res, rec_res)
        rec_res.pop()
    return
```


```python
candidates = [1,1,3,4,5]
combination_duplicate(candidates, 2)
```

    [[1, 1], [1, 3], [1, 4], [1, 5], [3, 4], [3, 5], [4, 5]]

