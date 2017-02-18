import os
import unittest

from search import find_word

class FuncTestCase(unittest.TestCase):

    def setUp(self):
	self.current_dir = os.getcwd()
	self.single_file_path = os.path.join(self.current_dir, 'test_function.py')

    	self.single_file_results = find_word(
	    codebase=self.single_file_path, word='positive')

	self.folder_results = find_word(
	    codebase=self.current_dir, word='positive')

    def test_single_file(self):
	self.assertEqual(len(self.single_file_results), 2)

    def test_folder(self):
	number_of_files = len(self.folder_results)
	total_instances = sum(
	    len(file_result) for file_result in self.folder_results) - number_of_files
	self.assertEqual(number_of_files, 3)
    	self.assertEqual(total_instances, 10)

    def test_ext(self):
	results = find_word(codebase=self.current_dir, word='positive', ext='html')
	self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()