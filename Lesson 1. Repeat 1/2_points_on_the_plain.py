n = int(input())
points = [tuple(map(int, input().split())) for i in range(n)]

parts = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}

for point in points:
    if 0 in point:
        print(point)
    elif point[0] > 0 and point[1] > 0:
        parts['I'] += 1
    elif point[0] > 0 > point[1]:
        parts['IV'] += 1
    elif point[0] < 0 and point[1] < 0:
        parts['III'] += 1
    else:
        parts['II'] += 1

print(', '.join(list(map(lambda x: f'{x}: {parts[x]}', parts))) + '.')
