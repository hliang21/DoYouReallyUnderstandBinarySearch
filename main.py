'''
Term Project Exercise 3: Binary Search
Solution for Do you really understand binary search ?
https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/do-you-really-understand-binary-search/
'''

def main():
    num_line = int(input())
    y_ints = input().split()
    
    # convert to int
    y_ints = [int(i) for i in y_ints]
    y_ints.sort()
    
    # read in the points
    num_point = int(input())
    for i in range(num_point):
        x, y = input().split()
        x = int(x)
        y = int(y)
        print(lines_below_binary_search(y_ints, 0, len(y_ints) - 1, x, y, 0))
        
        
# binary search for num line below point        
def lines_below_binary_search(y_ints, left, right, x, y, n):
    while(left <= right):
        mid = int((left + right) / 2)
        if y_at_x(y_ints[mid], x) < y:
            return lines_below_binary_search(y_ints, mid + 1, right, x, y, mid + 1)
        elif y_at_x(y_ints[mid], x) > y:
            return lines_below_binary_search(y_ints, left, mid - 1, x, y, n)
        else:
            return n + 1
    return n
        
def y_at_x(y_int, x):
    m = -1
    b = y_int
    return m * x + b
    
    
if __name__ == '__main__':
    main()