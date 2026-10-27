class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_heap=[-count for count in freq.values()]
        heapq.heapify(max_heap)
        time=0
        while max_heap:
            temp=[]
            cycles=0
            for _ in range(n+1):
                if max_heap:
                    count=heapq.heappop(max_heap)
                    cycles+=1
                    count+=1
                    if count<0:
                        temp.append(count)
            for count in temp:
                heapq.heappush(max_heap,count)
            if max_heap:
                time+=n+1
            else:
                time+=cycles
        return time