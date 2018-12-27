
def max_heapify(heap, heap_size, root):
    left  = 2 * root + 1
    right = 2 * root + 2
    larger = root

    if left < heap_size and heap[larger] < heap[left]:
        larger = left

    if right < heap_size and heap[larger] < heap[right]:
        larger = right

    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, heap_size, larger)


def build_max_heap(heap):
    heap_size = len(heap)
    for i in range((heap_size - 2)//2 , -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(heap):
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0],heap[i] = heap[i],heap[0]
        max_heapify(heap, i, 0)
    return heap


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)

            if k > pos + 1:
                return self.findKthLargest(nums[pos+1:], k-pos-1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            return nums[pos]

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]

        return low



if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    heap_sort(a)
    print(a)