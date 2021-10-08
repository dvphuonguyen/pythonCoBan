def merge_sort(l):
    if len(l) > 1:
        mid = len(l)//2
        left_arr = l[:mid]
        right_arr = l[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        left = 0
        right =0 
        now = 0
        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left] < right_arr[right]:
                l[now] = left_arr[left]
                left += 1
                now += 1
            else :
                l[now] = right_arr[right]
                right += 1
                now +=1
        while left < len(left_arr):
            l[now] = left_arr[left]
            left += 1
            now += 1
        while right < len(right_arr):
            l[now] = right_arr[right]
            right += 1
            now += 1
    return l
if __name__ == "__main__":
    lists = list(map(int,input().split()))
    print(lists)
    print(merge_sort(lists))       
        



