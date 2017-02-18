import os

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
	if file_ext[0] == '.':
	    file_ext = file_ext[1:]

    for subdir, dirs, files in os.walk(codebase):
	for file in files:
	    file_text = open(os.path.join(subdir, file)).read()


if __name__ == '__main__':
    main()
