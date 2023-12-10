def solveForPoints(n_points):
    if n_points <= 1:
        return 1
    
    prev = solveForPoints(n_points-1)
    return prev + getExtraRegions(n_points)

def getExtraRegions(nth_point):
    on_right = nth_point - 2
    on_left = 0
    extraRegions = 0

    while(on_right >= 0):
        extraRegions += drawLine(on_left, on_right)
        on_left += 1
        on_right -= 1
    return extraRegions
        

def drawLine(left, right):
    return (left*right)+1


for i in range(1, 20):
    print(f"{i} : {solveForPoints(i)}")

    