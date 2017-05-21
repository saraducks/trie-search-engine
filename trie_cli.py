#!/usr/bin/env python3.4

import time

from dictionary_webapp import trie


def func(user_input):
    # measure the time taken for adding dictionary words to trienode
    start  = time.time()
    t = trie.Trie()
    finish_import = time.time()

    # prints total time taken for opening dictionary file and creating tirenode
    print( "time for dictionary import %d seconds"%(finish_import - start))

    # while(1):
        # prompts for user input
        # print("enter query:")
        # query = input()
        # measures the total time taken to search for prefix and return the result
    query = user_input
    start_query = time.time()
    res = t.get_completions(query)
    print(res)
    end_query = time.time()
    print("time for search %d seconds" % (end_query - start_query))


func("appl")