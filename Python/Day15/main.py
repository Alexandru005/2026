# You are given a sorted integer array arr, two integers k and x,
# return the k closest integers to x in the array.
# The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# My solution
def findClosestElement(arr, k, x):
    lista = []
    lungime = 0

    for i in range(len(arr)):
        if lungime < k:
            lista.append([arr[i],abs(x-arr[i])])
            lungime += 1
        else:
            lista.sort(key=lambda x: x[1])
            j = k - 1
            while j >= 0:
                if abs(x-arr[i]) < lista[j][1]:
                    lista[j] = [arr[i],abs(x-arr[i])]
                    break
                if abs(x-arr[i]) == lista[j][1] and arr[i] < lista[j][0]:
                    lista[j] = [arr[i],abs(x-arr[i])]
                    break
                j -= 1

    lista = list(map(lambda x: x[0], lista))
    lista.sort()
    return lista


print(findClosestElement([1,2,3,4,5,6,7,8,9], 3, 8))

