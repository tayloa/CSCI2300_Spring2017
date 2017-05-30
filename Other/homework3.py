# Calculates the minimum of 2 arrays

def smallest(a,b,k):
    larger = max(len(a),len(b))
    i = 0
    j = 0
    count = 0
    small = 0
    while i < larger:
        if i+j == k: return small
        if a[i] < b[j]:
            small = a[i]
            i+=1
        elif a[i] > b[j]:
            small = b[i]
            j+=1
            
if __name__ == "__main__":
    a = [-1,1,2,3,3,5]
    b = [-2,2,2,15,16]
    print(smallest(a,b,1))
    print(smallest(a,b,2))
    print(smallest(a,b,3))
