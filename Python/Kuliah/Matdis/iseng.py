def merge(kiri,kanan):
    result = []
    a = b = 0
    while a < len(kiri) and b < len(kanan):
        if kiri[a] <= kanan[b]:
            result.append(kiri[a])
            a+=1
        else :
            result.append(kanan[b])
            b+=1
    while a < len(kiri):
        result.append(kiri[a])
        a+=1 
    
    while b < len(kanan):
        result.append(kanan[b])
        b+=1

    return result

def m_sort(arr):
    if len(arr) <1:
        return arr
    else :
        tengah = len(arr)//2
        kiri = arr[:tengah]
        kanan = arr[tengah:]

        kiri = m_sort(kiri)
        kanan = m_sort(kanan)
        return merge(kiri,kanan)

a = [3, 1, 5, 4, 7, 8, 2, 6]
b = m_sort(a)
print(b)