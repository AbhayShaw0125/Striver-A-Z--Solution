class Solution:
    def findUnion(self, a, b):
        # code here
        lst3 = a + b
        s1 = sorted(set(lst3))
        return s1
###another solution
class Solution:
    def findUnion(self, a, b):
        # code here
        union_list = []

        for i in a:
            if i not in union_list:
                union_list.append(i)
        for i in b:
            if i not in union_list:
                union_list.append(i)

        return sorted(union_list)
###Since the above code is O(N^2) Solution it gives TLE
###if i not in union_list is an O(n) operation — Python has to scan the entire list each time.