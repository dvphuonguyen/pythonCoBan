def bineary_search ( lists, mem):
    l = 0
    r = len(lists) - 1
    while (l <= r):
        m = (l + r)//2
        if lists[m] == mem:
            return True
        elif lists[m] < mem:
            l = m + 1
        else:
            r = m - 1
    else:
        return False
    


if __name__ == "__main__":
    numbers = int(input())
    for index in range(numbers):
        first = list(map(int,input().split(' ')))
        second = list(map(int,input().split(' ')))
        count = 0
        second.sort()
        while(len(second) != 0):
            mem = first[1] - second[0]
            second.pop(0)
            if bineary_search(second, mem) == True:
                count += 1
        print (count)

    
        