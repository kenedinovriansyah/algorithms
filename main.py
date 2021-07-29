def _(context):
    if context % 2:
        print(False)
    else:
        print(True)

# Output:
#     True
#     False
#     True


array = ["k","e","n","e","d","y"]

_d = ""
for i in array:
    _d += i

print(_)

# Output:
#     kenedy

_m = [1,9,3,2,3,5,4]
     
print(max(_m))

print(min(_m)) 
   
# # Output:
#     max -> 9
#     min -> 1



def first(data):
    return data[0]
_ = [1,2,3,4,5,6,7]

first(_)

def linear_search(d,v):
    for i in range(len(d)):
        if v == _[i]:
            return i
    raise ValueError("Value not found")
    
linear_search(_,2)


def heap_p(d,n):
    if n == 1:
        print(d)
        return
    for i in range(n):
        heap_p(d,n - 1)
    if n % 2 == 0:
          d[i], d[n-1], d[i]
    else:
        d[0], d[n-1], d[0]

heap_p(_m,len(_m))

# Output:
#     [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]

def m_f(d):
    f = d[0]
    for i in d:
        print(i)
    
    for x in d:
        for y in d:
            print(x,y)


# Output:
#     7 3
# 7 4
# 7 5
# 7 6
# 7 7

def missing(d):
    n = len(d)
    total = (n+1) * (n+2) / 2
    sum_f_d = sum(d)
    return int(total - sum_f_d)
    
_mf = [1,2,4,5]
missing(_mf)

# Output:
#     3
