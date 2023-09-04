peoples = input().split(' -> ')
n = int(input())
for i in range(n):
    people = input()
    index = peoples.index(people)
    peoples_to_print = []
    if 0 <= index - 1 < len(peoples):
        peoples_to_print.append(peoples[index - 1])
    peoples_to_print.append(people)
    if 0 <= index + 1 < len(peoples):
        peoples_to_print.append(peoples[index + 1])
    print(*peoples_to_print, sep=' -> ')
