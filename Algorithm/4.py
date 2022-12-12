def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    ln1 = len(nums1)
    ln2 = len(nums2)
    if ln1 + ln2 % 2:
        m_ind = abs(ln1 - ln2 - 1)//2
        i,j = 0,0
        i_flag = False
        while True:
            if nums1[i] >= nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
                i_flag = True
            if i + j == m_ind:
                return float(nums1[i]) if i_flag else float(nums2[j])
            i_flag = False

if __name__ == '__main__':
    n = [1,3]
    m = [2]
    findMedianSortedArrays(n,m)