from next_fit import next_fit
from first_fit import first_fit
from first_fit import first_fit_decreasing
from best_fit import best_fit, merge_sort
from best_fit import best_fit_decreasing
from zipzip_tree import ZipZipTree, Rank



# Rank is a container representing each node's rank, both geometric and uniform.
#           If using an earlier form of Python, you can use a named tuple instead.
# ZipZipTree(): constructs the zip-zip tree with a specific capacity.
# get_random_rank(): returns a random node rank, chosen independently from:
#           a geometric distribution of mean 1 and,
#           a uniform distribution of integers from 0 to log(capacity)^3 - 1 (log capacity cubed minus 1).
# insert(): inserts item with parameter key, value, and rank into tree.
#           if rank is not provided, a random rank should be selected by using get_random_rank().
# remove(): removes item with parameter key from tree.
#           you can assume that the item exists in the tree.
# find(): returns the value of item with parameter key.
#         Assuming that the item exists in the tree.
# get_size(): returns the number of nodes in the tree.
# get_height(): returns the height of the tree.
# get_depth(): returns the depth of the item with parameter key.
#              Assuming that the item exists in the tree.


# For all bin packing functions:
# params:
# 	items: the items to assign to the bins
# 	assignment: the assignment of the ith item to the jth bin for all i items.
# 	            bin numbers start from 0.
# 	            assume len(assignment) == len(items).
# 	            Not adding any new elements to this list - modify list elements to indicate the assignment
#
# 	free_space: the amount of space left in the jth bin for all j bins created by the algorithm.
# 	            Add one element for each bin that the algorithm creates.
# 	            when the function returns, this should indicate the final free space available in each bin.