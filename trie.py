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
t.add_keyword('app')
t.add_keyword('apple')
t.add_keyword('apart')
t.add_keyword('bag')
t.add_keyword('bang')
t.add_keyword('bangle')
t.get_completions('ap')


