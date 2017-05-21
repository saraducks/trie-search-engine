#!/usr/bin/env python
import os
import sys
sys.path.insert(0,os.getcwd()+"/trie")
print(os.getcwd()+"/trie")
import trie
#!/usr/bin/env python3.4

import trie
import time

t = trie.Trie()

# measure the time taken for adding dictionary words to trienode
start  = time.time()

#open the local dictionary file and build the trie node
local_dict = open('/usr/share/dict/words')
for i in local_dict:
    t.add_keyword(i)

finish_import = time.time()

# prints total time taken for opening dictionary file and creating tirenode
print( "time for dictionary import %d seconds"%(finish_import - start))

while(1):
    # prompts for user input
    print("enter query:")
    query = input()
    # measures the total time taken to search for prefix and return the result
    start_query = time.time()
    results = t.get_completions(query)
    print("|".join(results))
    end_query = time.time()
    print("time for search %d seconds" % (end_query - start_query))

