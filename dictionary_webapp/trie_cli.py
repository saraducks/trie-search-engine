#!/usr/bin/env python3.4

import time
import trie


def func(user_input):
    # measure the time taken for adding dictionary words to trienode
    start  = time.time()
    t = trie.Trie()
    finish_import = time.time()

    # prints total time taken for opening dictionary file and creating tirenode
    print( "time for dictionary import %d seconds"%(finish_import - start))

    res = []
    query = user_input
    start_query = time.time()
    # res should intialize to empty list before invoking the get_completions
    res = t.get_completions(query)

    #prints the res list
    #print(res)
    end_query = time.time()
    print("time for search %d seconds" % (end_query - start_query))



func("vic")

