# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations

from typing import TypeVar
from dataclasses import dataclass
import random
import math

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

@dataclass
class Rank:
	geometric_rank: int
	uniform_rank: int

class ZipNode:
	def __init__(self, key, value, rank: Rank):
		self.key = key
		self.rank = rank
		self.value = value 		# for any add'l data to be stored in the nodes???
		self.left = None
		self.right = None

class ZipZipTree:
	def __init__(self, capacity: int):
		self.capacity = capacity			# initialize capacity, height and depth to 0
		self.size = 0
		self.root = None	
	
	def get_random_rank(self) -> Rank:
		"""
		Calculates and assigns a Rank where:
		Rank.geometric_rank is a geometric distribution of mean 1
        Rank.uniform_ranks is a uniform distribution of integers from 0 to log(capacity)^3 - 1
		"""
		g_rank = 0
		while True:
			if random.random() < 0.5 :		# essentially a coin flip
				break
			else:
				g_rank += 1
		
		i = int((math.log2(self.capacity)**3))-1
		if i < 0:				# in case log capacity is < 1,, rank will be 0 instead of error
			u_rank = 0
		else:
			u_rank = random.randint(0, i)
		
		return Rank(geometric_rank=g_rank, uniform_rank=u_rank)

	def insert(self, key: KeyType, val: ValType, rank: Rank = None):

		# basically just change it so uniform_rank is the same as testing for key; geometric_rank is the test for uniform. if they 
		# r still equal then check the key.

		# need to update so it still follows bst properties. so it adds it in the correct spot lexographically.
		# and THEN it checks the uniform_rank. 
		#	1. if node.u_rank < parent.u_rank, leave it where it is.
		# 	2. if node.u_rank > parent.u_rank. THEN do the fixing shit while loop
		#	3. if node.u_rank == parent.u_rank, CHECK geo rank (steps 1-2 above). if equal then check the key value, favoring smaller keys 
		
		if rank == None:						# generate a Rank for the node if not provided
			rank = self.get_random_rank()
		
		node = ZipNode(key, val, rank)
		cur = self.root
		prev = None

		# translated pseudocode from Zip Zip paper
		while(cur != None and ((rank.geometric_rank < cur.rank.geometric_rank) or 
						 (rank.geometric_rank == cur.rank.geometric_rank and rank.uniform_rank < cur.rank.uniform_rank) or 
						 (rank.geometric_rank == cur.rank.geometric_rank and rank.uniform_rank == cur.rank.uniform_rank and key > cur.key))):
			prev = cur
			if key < cur.key:
				cur = cur.left
			else:
				cur = cur.right
		
		self.size += 1			# node was added; update the size of the tree.

		if cur == self.root:
			self.root = node
		elif key < prev.key:
			prev.left = node
		else:
			prev.right = node
		
		if cur == None:
			node.left = None
			node.right = None
			return node

		if key < cur.key:
			node.right = cur		
		else:
			node.left = cur
		
		prev = node
	
		while(cur != None):
			fix = prev
			if cur.key < key:
				while(cur != None and cur.key < key):
					prev = cur
					cur = cur.right
			else:
				while(cur != None and cur.key > key):
					prev = cur
					cur = cur.left
			if fix.key > key or (fix == node and prev.key > key):
				fix.left = cur
			else:
				fix.right = cur
		return node
	
	def remove(self, key: KeyType):
		self.size -= 1
		cur = self.root
		while(key != cur.key):		# basically traversing tree to find the node with provided key
			prev = cur
			if key < cur.key:
				cur = cur.left
			else:
				cur = cur.right
		node = cur					# save node to remove
		
		left = cur.left
		right = cur.right
		
		if left == None:
			cur = right
		elif right == None:
			cur = left
		elif (left.rank.geometric_rank >= right.rank.geometric_rank) or (left.rank.geometric_rank == right.rank.geometric_rank and left.rank.uniform_rank >= right.rank.uniform_rank):
			cur = left
		else:
			cur = right

		if self.root == node:
			self.root = cur
		elif key < prev.key:
			prev.left = cur
		else:
			prev.right = cur

		while(left != None and right != None):
			if left.rank.geometric_rank >= right.rank.geometric_rank:
				while(left != None and left.rank.geometric_rank >= right.rank.geometric_rank):
					prev = left
					left = left.right
				prev.right = right

			else:
				while(right != None and left.rank.geometric_rank < right.rank.geometric_rank):
					prev = right
					right = right.left
				prev.left = left
		return node

	def find_node(self, key: KeyType) -> ZipNode:
		cur = self.root
		while(cur != None):				# keep searching until key is found; guaranteed to be in tree.
			if cur.key == key:
				return cur
			elif cur.key < key:			# key is greater than current key, traverse right
				cur = cur.right
			else:						# otherwise key is less than current key, traverse left
				cur = cur.left
		
		return None				# key is guaranteed to be in tree but just in case

	def find(self, key: KeyType) -> ValType:
		node = self.find_node(key)
		return node.value if node != None else None

	def get_size(self) -> int:
		return self.size
	
	def height(self, node):
		"""Recursively finds height of tree starting at the root; only called by self.get_height()"""
		if node == None:
			return -1		# to negate the +1 in recursive calls (only count leaf)
		left = 1 + self.height(node.left)
		right = 1 + self.height(node.right)
		return max(left, right)

	def get_height(self) -> int:
		return self.height(self.root)

	def depth(self, k, node: ZipNode) -> int:
		"""Recursively searches for the node with key k -- KEY GUARANTEED TO BE IN TREE"""
		if k == node.key:
			return 0		# base case
		
		if k < node.key:
			return 1 + self.depth(k, node.left)
		else:
			return 1 + self.depth(k, node.right)
	
	def get_depth(self, key: KeyType):
		return self.depth(key, self.root)

	def print_tree(self, node, level=0, prefix="Root: "):
		if node is not None:
			print(" " * (level * 4) + prefix + str(node.key) + ", " + str(node.value))
			if node.left is not None:
				self.print_tree(node.left, level + 1, "Left: ")
			if node.right is not None:
				self.print_tree(node.right, level + 1, "Right: ")


class BestFitZipZipTree(ZipZipTree):
	#class that inherits ZipZipTree functionality with added functions

	def find_best_node(self, item: float) -> ZipNode:
		"""Given an item (float correlating to size of the item), finds and returns the node in ZipZipTree that
		best fits the item."""

		bf = 1.0					# save bf = 1.0 (there will never be 1 remaining capacity since bin sizes are 1.0)
		bf_node = None				# node with the best remaining capacity
		cur = self.root

		while(cur != None):
			key = cur.key[0]		# brc
			if key < item:
				cur = cur.right
			elif key >= item:
				# calculate the remaining capacity if item added and save the node if better than bf
				if key - item < bf:
					bf = key-item
					bf_node = cur
				cur = cur.left

		return bf_node
	
	def add_node(self, key):
		node = self.insert(key, 0)				# arbitrary value for creating node bc position and best subtree brc is unknown
		# now calculate brc based on node returned. basically assume that all children have appropriately calculated brc
		if node.left == None and node.right == None:
			node.value = node.key[0]
		elif node.left == None:
			node.value = node.right.value
		elif node.right == None:
			node.value = node.left.value
		else:
			node.value = max(node.left.value, node.right.value)

class FirstFitZipZipTree(ZipZipTree):
	# FIRST FIT:: 
	# keys = (bin index, item capacity)
	# so nodes are sorted by their order in free_space list
	def find_first_node(self, node: ZipNode, item: float) -> ZipNode:
		# traverses all the way to the left; where the smallest index will be.
		# recursively finds the smallest earliest bin with largest remaining capacity
		if node == None:
			return None
		rc = node.key[1]
		if rc >= item:
			left = self.find_first_node(node.left, item)
			return left if left != None else node 				# if left_subtree is none, return cur node
		left = self.find_first_node(node.left, item)
		right = self.find_first_node(node.right, item)
		if (left == None):
			return right
		else:
			return left
