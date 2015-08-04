import heapq

def merge_files(output_file, input_files):
	heap = []
	output_fd = open(output_file, 'w+')
	try:
	    # open all files
	    open_files = []
	    [open_files.append(open(file__, 'r')) for file__ in input_files]

	    # 2. Iterate through each file f
	    # enqueue the pair (nextNumberIn(f), f) using the first value as priority key
	    [heapq.heappush(heap, (file__.readline(), file__)) for file__ in open_files] 
	    
	    # 3. While queue not empty
	    # dequeue head (m, f) of queue
	    # output m
	    # if f not depleted
	    # enqueue (nextNumberIn(f), f)
	    while(heap):
		# get the smallest key
		smallest = heapq.heappop(heap)
		# write to output file
		output_fd.write(smallest[0])
		# read next line from current file
		read_line = smallest[1].readline()
		# check that this file has not ended
		if(len(read_line) != 0):
		    # add next element from current file
		    heapq.heappush(heap, (read_line, smallest[1]))
	    # clean up
	    [file__.close() for file__ in open_files]    
	    output_fd.close()
			    
	except Exception, err_msg:
	    print "Error while merging: %s" % str(err_msg)

def test():
	files = ['part_001.txt', 'part_002.txt', 'part_003.txt', 'part_004.txt']
	merge_files('output-file.txt', files)

if __name__ == '__main__':
    test()

