import time

class TrieNode:
    def __init__(self, node_char="$"):
        self.trie_node_char = node_char
        self.childNodeList = []
        self.endOfWord = False

    def is_char_in_trienode(self, character):
        for iter in self.childNodeList:
            if character == iter.trie_node_char:
                return iter
        return None

    def print_trie(self, temp = ""):
        print(temp+self.trie_node_char)
        for iter in self.childNodeList:
            iter.print_trie(temp+self.trie_node_char)

    def print_prefix(self, prefix, temp =""):
        #prints the word only if endOfWord is set to True
        if self.endOfWord == True:
            print(temp+prefix)
        #recursivly call the print_prefix
        for i in self.childNodeList:
            i.print_prefix(prefix+temp+i.trie_node_char)


class Trie:
    # initialize the root node with '$'
    def __init__(self):
        self.root = TrieNode()

    def add_keyword(self, input_string):
        current_node = self.root
        # iterate through the input_string
        for each_character in input_string:
            # Check each character in the input_string with the childNodeList
            # If character is in childNodeList then update root to the current character
            result = current_node.is_char_in_trienode(each_character)
            if result is not None:
                current_node = result
            # else create a new node, append it to the current node and update the current node to new node
            else:
                new_child_node = TrieNode(each_character)
                current_node.childNodeList.append(new_child_node)
                current_node = new_child_node
        # once we reach the end of the input_string set the endOfWord to True
        new_end_node = TrieNode()
        new_end_node.endOfWord = True
        current_node.childNodeList.append(new_end_node)

    # initialize to the root and call the print function in TrieNode
    def print_trie(self):
        self.root.print_trie()

    #get the completeness of the given prefix
    def get_completions(self, prefix):
        #initialize to the root node
        head = self.root
        isEndOfPrefix = False
        counter = 0
        #Itereate through the character in prefix with childNodeList
        while counter < len(prefix):
            result = head.is_char_in_trienode(prefix[counter])
            if result is not None:
                counter = counter + 1
                head = result
            else:
                print("No such prefix")
                break
        
        isEndOfPrefix = True if counter == len(prefix) else False

        if isEndOfPrefix:
           TrieNode.print_prefix(head, prefix)



t = Trie()

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
    query = raw_input()
    # measures the total time taken to search for prefix and return the result
    start_query = time.time()
    t.get_completions(query)
    end_query = time.time()
    print("time for search %d seconds" % (end_query - start_query))

