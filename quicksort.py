#!/usr/bin/env python

import sys

def partition(A, start, end):
	pivot = A[start]
	left = start+1
	right = end
	done = False
	while not done:
		while left <= right and A[left] <= pivot:
			left += 1
		while A[right] >= pivot and right >=left:
			right -= 1
		if right < left:
			done = True
		else:
			# swap places
			A[left],A[right] = A[right],A[left]
	# swap start with A[right]
	A[start],A[right] = A[right],A[start]
	return right

def quicksort(A, start, end):
	if start < end:
		# partition the list
		pivot = partition(A, start, end)
		# sort both halves
		quicksort(A, start, pivot-1)
		quicksort(A, pivot+1, end)

    

def sort(input_file, output_file):
	try:
		with open(input_file) as f:
			content = f.readlines()
			
			quicksort(content,0,len(content)-1)

			with open(output_file, "w") as output:
				for line in content:
					output.write(line)

        except Exception, err_msg:
            print "Error while sorting: %s" % str(err_msg)

	
if __name__ == "__main__":

	if len(sys.argv) != 3:
		print "missing arguments"
			
	else:
		input_file = sys.argv[1]
		output_file = sys.argv[2]

		with open(input_file) as f:
			content = f.readlines()
			
			quicksort(content,0,len(content)-1)

			with open(output_file, "w") as output:
				for line in content:
					output.write(line)
		

