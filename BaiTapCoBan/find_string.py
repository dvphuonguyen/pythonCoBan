def count_substring(string, sub_string):
    count = 0
    for index in range(0, len(string) - len(sub_string) + 1):
        print(string[index : index + len(sub_string)])
        if sub_string == (string[index : index + len(sub_string)]):
            count += 1
    return count

if __name__ == '__main__':
    string = input()
    sub_string = input()
    count = count_substring(string, sub_string)
    print(count)