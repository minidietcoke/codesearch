import unittest
from search import search_word
from some_module import MySetupClass

class FuncTestCase(unittest.TestCase):

    def setUp(self):
        self.object = MySetupClass()

    def tearDown():
        self.object.dealloc()

    def test_true_positive(self):
        ...
        pass

    def test_false_posiive(self):
        ...
        pass

    def test_true_negative(self):
        ...
        pass

    def test_false_negative(self):
        ...
        pass

    def test_boundary_values(self):
        ...
        pass

    def test_performance(self):

        with self.object.context() as _e:
            positive = search_word()
            ...
            ...
            pass
