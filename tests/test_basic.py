import unittest
from nose.tools import *
from dictionary_webapp import trie

test_trie = trie.Trie()
class TestTrieWordCompletion(unittest.TestCase):
    # check if all packages are installed and working properly
    # check if the code works as expected
      #1. You can pass the simple value, and check if the result is list and displays the correct result.
      #2. Result to be compared against is stored locally as a list

    #1. pass the random word not in dictionary and see if condition pass
    def test_trie_not_in_dictionary(self):
        result_list = test_trie.get_completions('vic')
        #check each and every word in the result_list
        for iter in range(0,len(result_list)):
            self.assertTrue(result_list[iter][:3] == 'vic')

    #2. Pass the null, it should return NONE
    def test_trie_for_none(self):
        result_list = test_trie.get_completions('')
        self.assertIsNotNone(result_list, "")

    #3. matches the exact word
    def test_get_exact_match(self):
        result_list = test_trie.get_completions("victory")
        for iter in range(0, len(result_list)):
            self.assertTrue(result_list[iter][:7] == "victory")


if __name__ == '__main__':
    unittest.main()