
class TrieNode:

  def __init__(self, rootNode=None, childNode=None):
      self.rootNode = None
      self.childNode = []

  def add_child(self, chnode):
      self.childNode.append(chnode)


class Trie:

 def __init__(self):
     self.TrieNode = TrieNode()

 #add the word to the trie dictionary and store whole words at the end of the tree
 def addKeyword(self, word):
      head = TrieNode.rootNode
      for iter in word:
          if(iter in head.childNode):
              head = head.childNode[iter]
          if iter not in head:
              head.add_child(iter)
              head = head.childNode[iter]
      head.childNode[word]

 #get complete words for the prefix
 def getCompleteWords(self, prefix):
      endOfprefix = False
      head = TrieNode.rootNode
      for iter in range(prefix):
          if(prefix in head.childNode):
              head = head.childNode[prefix]
      prefixhead = head
      endOfprefix = True

      while endOfprefix:
          while prefixhead != None:
              temp = prefixhead.childNode
              print prefixhead.childNode
              prefixhead = prefixhead.childNode[temp]

 def print_tree(self, tree):
      head = TrieNode.rootNode
      if tree == None:
        return

      for res in range(TrieNode.chilNode):
          temp = TrieNode.chilNode[res]
          head = head.childNode[temp]
          print temp


t = Trie()
t.addKeyword('app')
t.addKeyword('bag')
t.print_tree(t)


