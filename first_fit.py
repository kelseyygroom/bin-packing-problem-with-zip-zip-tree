
from zipzip_tree import FirstFitZipZipTree
# For all bin packing functions:
# params:
# 	items: the items to assign to the bins
# 	assignment: the assignment of the ith item to the jth bin for all i items.
# 	            bin numbers start from 0.
# 	            assume len(assignment) == len(items).
# 	            you should not add any new elements to this list.
# 	            you must modify this list's elements to indicate the assignment.
# 	            see comment below for first-fit decreasing and for best-fit decreasing.
#
# 	free_space: the amount of space left in the jth bin for all j bins created by the algorithm.
# 	            you should add one element for each bin that the algorithm creates.
# 	            when the function returns, this should indicate the final free space available in each bin.

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    tree = FirstFitZipZipTree(len(items))
    for i, size in enumerate(items):
        bin = tree.find_first_node(tree.root, size)
        if bin == None:
            ind = tree.get_size()
            tree.insert((ind, round(1-size,2)), 0)
            assignment[i] = ind
            free_space.append(round(1-size, 2))
        else:
            rc = round(bin.key[1]-size, 2)
            b_index = bin.key[0]
            free_space[b_index] = rc
            assignment[i] = b_index

            tree.remove(bin.key)
            tree.insert((b_index, rc), 0)
    return free_space

    # FIRST FIT: keys should be (index of bin, rc)
    # values should be BRC

def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    sorted_items = merge_sort(items)
    first_fit(sorted_items, assignment, free_space)
    return free_space

def merge_sort(nums: list[int]):
    length = len(nums)

    if length > 1:
        nums1 = nums[:length//2]
        nums2 = nums[length//2:]
        merge_sort(nums1)
        merge_sort(nums2)
        nums[:] = merge(nums1, nums2)
    return nums

def merge(nums1: list[int], nums2: list[int]):
    nums = []
    i = 0           # i -> nums1
    j = 0           # j -> nums2
    n1 = len(nums1)
    n2 = len(nums2)
    while (i < n1 and j < n2):
        if nums1[i] >= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    # fill in the rest of the nums if any is left
    nums += nums1[i:]
    nums += nums2[j:]
    return nums