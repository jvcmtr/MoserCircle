
def main():
    for i in range(1, 20):
        print(f"{i} : {solveForPoints(i)}")


# Incremental aproach to the problem
def solveForPointsIncremental(n_points):
    if n_points <= 1:
        return 1

    last_computed = 1
    for i in range(2, n_points+1):
        last_computed = last_computed + getExtraRegions(i)
        
    return last_computed

# Recursive aproach to the problem
def solveForPoints(n_points):
    if n_points <= 1:
        return 1
    
    prev = solveForPoints(n_points-1)
    return prev + getExtraRegions(n_points)


def getExtraRegions(nth_point):
    """returns how many new regions are created when a new point is added"""
    on_right = nth_point - 2
    on_left = 0
    extraRegions = 0

    while(on_right >= 0):
        extraRegions += drawLine(on_left, on_right)
        on_left += 1
        on_right -= 1
    return extraRegions
        

def drawLine(left, right):
    """returns how many new regions a line creates, given how many points there are to the left and to the right of the given line"""
    return (left*right)+1


if __name__ == '__main__':
    main()
    