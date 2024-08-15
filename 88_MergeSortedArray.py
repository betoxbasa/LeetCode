from typing import List

class Solution:
    def merge(self,nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        aux = nums1[0:m:] + nums2[0:n:]            
        for x in range(n):
            nums1[m+x] = aux[x]
        nums1.sort()

    def multiplicarElementos(self,lista, numero):
        for indice, elemento in enumerate(lista):
            lista[indice] = elemento * numero


a = Solution()
nums1 =[1,2,3,0,0,0]
m = 3
nums2 =[2,5,6]
n = 3

print(nums1)

a.merge(nums1,m,nums2,n)
print(nums1)

