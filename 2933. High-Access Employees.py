class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        employeemap = collections.defaultdict(list)
        res=[]

        for emp,time in access_times:
            minutes_time = int(time[0:2]) * 60 + int(time[2:4]) # convert timestamp to minutes. For example 0530 will ve  (5*60+30)=330 #Another approach is to check 100-minute for 0430-0530.
            employeemap[emp].append(minutes_time)

        for emp,times in employeemap.items():
            flag=False
            employeemap[emp] = sorted(times)
            length = len(employeemap[emp])
            for i in range(length-2): # a window of 3 timestamps
                if employeemap[emp][i+2] - employeemap[emp][i] <60:
                    flag = True
                    break
            if flag:
                res.append(emp)

        return res
