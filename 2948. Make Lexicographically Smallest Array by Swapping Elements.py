class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        a=[]
        for i,n in enumerate(nums):
            a.append((n, i)) # (1)tuples including (value,index)
        
        a.sort(key=lambda x:x[0]) # (2)sort tuples based on values 
        #print(a)
        groups=[[a[0]]] #(3) make groups
        for i in range(1,len(a)):
            if a[i][0] - a[i-1][0]<=limit:
                groups[-1].append(a[i]) #append to already existing group
            else: 
                groups.append([a[i]]) #make a new group
        #print(groups) # [[(1, 0), (3, 2), (5, 1)], [(8, 4), (9, 3)]]

        # for each group sort its indices, and then use those indices to update original array. 
        # In each group, smallest index should be used to put smallest value in that position in original array
        # e.g; for group: [(1, 0), (3, 2), (5, 1)], a[0] should be replace by least value of this group which is at first place(1). a[1] should be replaced by second value which is "3" here, and a[2] should be replaced by third value which is "5"
        for group in groups:
            indx = []
            for _,index in group:  
                indx.append(index)
            indx.sort() 
            for i in range(len(indx)): 
                a[indx[i]] =  group[i][0]
        return a
            


        
