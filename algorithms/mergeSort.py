import unittest


def merge(nums1, nums2):
    returnArr = []
    c1,c2 = 0,0

    while c1 < len(nums1) and c2 < len(nums2):
        if nums1[c1] < nums2[c2]:
            returnArr.append(nums1[c1])
            c1 += 1
        else:
            returnArr.append(nums2[c2])
            c2 += 1

    while c1 < len(nums1):
        returnArr.append(nums1[c1])
        c1 += 1

    while c2 < len(nums2):
        returnArr.append(nums2[c2])
        c2 += 1

    return returnArr

def mergeSort(nums):
    if len(nums)<2:
        return nums
    else:
        mid = len(nums)//2
        return merge(mergeSort(nums[:mid]), mergeSort(nums[mid:]))


class TestMergeSort(unittest.TestCase):
    unsortedIn = [3,1,8,3,500,5,9,10,21,6,100,17,19]
    sortedOut = [1, 3, 3, 5, 6, 8, 9, 10, 17, 19, 21, 100, 500]

    def test_sort(self):
        self.assertEqual(mergeSort(self.unsortedIn), self.sortedOut)


    def test_sort2(self):
        self.assertNotEqual(mergeSort(self.unsortedIn), self.unsortedIn)

    def test_sort3(self):
        self.assertEqual(mergeSort([3,4,1,6,7]), [1,3,4,6,7])
    
    def test_sort4(self):
        self.assertEqual(mergeSort([]), [])

    def test_sort5(self):
        self.assertEqual(mergeSort([4]), [4])


if __name__ == '__main__':
    unittest.main()