import heapq

class Solution:

    def get_distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            print(heap)
            if len(heap) < k:
                heapq.heappush(heap, (-self.get_distance(point), point))
            else:
                cur_distance, ele = heapq.heappop(heap)
                if (-cur_distance) > self.get_distance(point):
                    cur_distance, ele = -self.get_distance(point), point
                heapq.heappush(heap, (cur_distance, ele))
        res = []
        for _, point in heap:
            res.append(point)
        return res
