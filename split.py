from itertools import chain

def split_file(filename, pattern, size):
	try:
		output_files = []
		with open(filename, 'rb') as f:
			for index, line in enumerate(f, start=1):
				with open(pattern.format(index), 'wb') as out:
					output_files.append(out.name)
					n = 0
					for line in chain([line], f):
						out.write(line)
						n += len(line)
						if n >= size:
							break

	except Exception, err_msg:
		print "Error while splitting: %s" % str(err_msg)

	return output_files
