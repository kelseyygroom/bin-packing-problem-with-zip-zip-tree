from zipzip_tree import BestFitZipZipTree

def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    # BEST_FIT:
    # we can just binary search through the tree. starting w first node. i should inherit the zipzip tree??
    # and add my best_fit methods to the existing zipzip tree functionality??.
    # ok so the keys for the bst should be the (remaining bin capacity, index) -- tuples are compared l-r lexicographically. 
    # value should be best brc in subtree .??????
    # geometric and uniform rank remain unchanged; only care about bst properties/functionality
    # ranks are left to class to handle for balancing properties
    tree = BestFitZipZipTree(len(items))        # capacity is the number of items (because worst case each item has it's own bin)
    # go thru items list
    for i, size in enumerate(items):
        # find the best fit
        bin = tree.find_best_node(size)
        if bin == None:                     # means bin wasn't found, need to create new bin. add item
            ind = tree.get_size()
            tree.add_node((round(1-size,2), ind))
            assignment[i] = ind                      # because tree size is number of nodes.
            free_space.append(round(1-size,2))
        else:
            # a bin with best fit was found.
            # we want to remove the node from the tree. update the capacity update the lists. reinsert it into the tree
            rc = round(bin.key[0] - size, 2)         # remaining capacity after adding item to bin
            b_index = bin.key[1]            # index of bin. need to save
            free_space[b_index] = rc        # update the bin capacity in free_space list
            assignment[i] = b_index         # assign item to bin in assignment list

            tree.remove(bin.key)
            tree.add_node((rc,b_index))
    return free_space


def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    # order items from largest to smalles and then call best_fit(sorted_items, assignment, free_space)
    best_fit(merge_sort(items), assignment, free_space)
    return free_space

# modified from project 1 to sort in descending order
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