import heapq

class Solution:

    def get_distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #return heapq_sol(points, k)
        return self.quick_select(points, k)

    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:

        def partition(left, right):
            pivot = points[right]
            pivot_index = left
            for i in range(left, right):
                if self.get_distance(points[i]) < self.get_distance(pivot):
                    points[pivot_index], points[i] = points[i], points[pivot_index]
                    pivot_index += 1
            points[right], points[pivot_index] = points[pivot_index], points[right]
            return pivot_index

        def quick_select(left, right):
            if left >= right:
                return
            pivot_index = partition(left, right)
            if pivot_index + 1 == k:
                return
            elif pivot_index + 1 > k:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
            quick_select(left, right)
        
        quick_select(0, len(points) - 1)

        return points[:k] 

    def heapq_sol(self, points: List[List[int]], k: int) -> List[List[int]]:
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
