lists = list(input().split())

print(lists)

power = len(lists)

powerset = 2** power

print("Tong so tap hop : ", 2**power)

for counter in range(powerset):
    for mask in range(power):
        if counter & (1 << mask ) > 0:
            print(lists[mask], end=" ")
    print(" ")




        
