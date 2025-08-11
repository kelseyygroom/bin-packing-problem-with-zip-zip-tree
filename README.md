# Bin Packing Problem Using a Zip Zip Tree

## Overview

This project implements a Zip Zip Tree, which is a variant of a binary search tree, and extends it for use in bin packing problems.

A Zip Zip Tree assigns two independent random ranks to each node:
* Geometric rank: controls tree balancing (like in Treaps but from a geometric distribution)
* Uniform rank: controls ordering for equal geometric ranks (uniformly distributed in a fixed range)

**Goals:** Use Zip Zip trees to store and quickly retrieve bins based on remaining capacity, remain near-balanced search times for bin insertion and retrieval, and support fast "best-fit" or "first-fit" strategies for incoming items.

## Bin Packing
**The Bin Packing Problem:** Given a set of items with sizes in the range (0, 1], pack them into the fewest number of bins of capacity 1.

Common strategies include:
* First Fit: Place each item into the first bin that has enough space
* Best Fit: Place each item into the bin with the least remaining space that can still fit the item
* Next Fit: Keep filling the current bin until it overflows, then start a new bin.

In this bin packing context, each tree node of the Zip Zip Tree represents a bin with a certain amount of remaining capacity. Given the Zip Zip properties, this implementation enables O(log n) insertion and retrieval.

## What I Did

I implemented the Zip Zip Tree from scratch, handling insertion, removal, and searching while maintaining the balanced properties of the tree. I then used the Zip Zip Tree as the data structure to represent the bins in the bin packing problem. I created algorithms for First Fit, Best Fit, and Next Fit bin packing, plotting and mapping the data to determine the most efficient algorithm.
