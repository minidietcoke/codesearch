import os
import sys
from os.path import splitext


def main():
    print 'What is the path of the codebase folder:'
    codebase = raw_input()
    try:
	os.stat(codebase)
    except:
	print 'Invalid path, please start again'
	sys.exit()
    print 'What is the search term:'
    word = raw_input()
    print 'What file type you like to search (.py, .js etc or leave empty):'
    ext = raw_input()

    results = find_word(codebase, word, ext)
    print_results(results)

def find_word(codebase, word, ext=''):
    if ext and ext[0] != '.':
	ext = '.{}'.format(ext)

    results = []

    try:
	file = open(codebase)
	results.extend(find_word_in_file(word, file))
    except IOError:
	for subdir, dirs, files in os.walk(codebase):
	    for file in files:
		if is_matching_file_ext(file, ext):
		    file_path = os.path.join(subdir, file)
		    f = open(file_path)
		    file_result = find_word_in_file(word, f)
		    if len(file_result) > 0:
			file_result.insert(0, file_path)
			results.append(file_result)

    return results

def find_word_in_file(word, file):
    file_result = []
    for i, line in enumerate(file):
	if word in line:
	    file_result.append(
		'\t{line_num}: {line}'.format(line_num=i, line=line.strip()))
    return file_result

def is_matching_file_ext(file, file_ext):
    return splitext(file)[1] == file_ext or file_ext == ''

def print_results(results):
    for result in results:
	print '"""'
	print '\n'.join(result)

if __name__ == '__main__':
    main()
