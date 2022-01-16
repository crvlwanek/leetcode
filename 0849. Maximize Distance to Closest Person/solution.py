
def maxDistToClosest(seats: List[int]) -> int:
    occupied = [i for i, value in enumerate(seats) if value]
    
    dist = occupied[0]
    for i in range(1, len(occupied)):
        dist = max(dist, (occupied[i] - occupied[i-1])//2)
    dist = max(dist, len(seats) - 1 - occupied[-1])
    
    return dist