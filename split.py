from itertools import chain

def split_file(filename, pattern, size):
    """Split a file into multiple output files.

    The first line read from 'filename' is a header line that is copied to
    every output file. The remaining lines are split into blocks of at
    least 'size' characters and written to output files whose names
    are pattern.format(1), pattern.format(2), and so on. The last
    output file may be short.

    """
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

    return output_files

if __name__ == '__main__':
    split_file('inputfile.txt', 'part_{0:03d}.txt', 2)
