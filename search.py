import os
from os.path import splitext

def main():
    print 'What is the path of the codebase folder:'
    codebase = raw_input()
    print 'What is the search term:'
    search_term = raw_input()
    print 'What file type you like to search (.py, .js etc or leave empty):'
    file_ext = raw_input()

    search_word(codebase, search_term, file_ext)


def search_word(codebase, search_term, file_ext):
    if file_ext:
	if file_ext[0] != '.':
	    file_ext = '.{}'.format(file_ext)

    results = []

    for subdir, dirs, files in os.walk(codebase):
	for file in files:
	    if splitext(file)[1] == file_ext or file_ext == '':
		file_path = os.path.join(subdir, file)
		f = open(file_path)
		file_result = []
	    	for i, line in enumerate(f):
		    if search_term in line:
		    	file_result.append('\t{line_num}: {line}'.format(
			    line_num=i, line=line.strip()))
		if len(file_result) > 0:
		    file_result.insert(0, file_path)
		    results.append(file_result)

    for result in results:
	print '"""'
	print '\n'.join(result)

if __name__ == '__main__':
    main()
