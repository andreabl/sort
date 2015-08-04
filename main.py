#!/usr/bin/python


import argparse, os

from quicksort import sort
from split import split_file
from merge import merge_files


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Sort a huge file.')
	parser.add_argument('--input', help='File to sort')
	parser.add_argument('--output', help='Output file')
	parser.add_argument('--tempfile', help='Temporarily output pattern prefix (default: output)', default='output')
	parser.add_argument('--splitsize', help='Number of lines in each split (default: 10000)', type=int, default=10000)

	args = parser.parse_args()

	splitted_files = split_file(args.input, '%s_{0:04d}.txt' % args.tempfile, args.splitsize)	

	for split_file in splitted_files:
		sort(split_file, "%s_sorted" % split_file)	
	
	splitted_files_sorted =  ["%s_sorted" % filename for filename in splitted_files]

	merge_files(args.output, splitted_files_sorted)

	# cleanup
	for filename in splitted_files + splitted_files_sorted:
		os.remove(filename)

	print "success"

