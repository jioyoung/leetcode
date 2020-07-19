def minimumDays(rows, columns, grid):
    # WRITE YOUR CODE HERE
    n = 0

    while (haszero(rows, columns, grid)):
        n+=1
        new_grid = list(grid) # copy grid to new_grid
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    if hasonearound(rows, columns, i, j, grid):
                        new_grid[i][j]=1
        
        grid = list(new_grid) #update grid 
                    
    return n
    
    
def haszero(rows, columns, grid):
    for i in range(rows):
        if sum(grid[i])<columns:
            return True
    return False

def hasonearound(rows, columns, irow, icol, grid):
    #up
    if irow>0:
        if (grid[irow-1][icol]==1):
            return True
    #down
    if irow<(rows-1):
        if (grid[irow+1][icol]==1):
            return True
    #left
    if icol>0:
        if (grid[irow][icol-1]==1):
            return True
    #right
    if icol<(columns-1):
        if (grid[irow][icol+1]==1):
            return True        
    return False


a = [[1,1,0], [0,0,0]]

print(minimumDays(2, 3, a))