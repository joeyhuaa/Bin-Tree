# ECS 36A - Joey Hua - Matt Bishop
# Homework 5

class Node():

    def __init__(self, data=0, count=1):
        self.data = data
        self.count = count
        self.lnode = None
        self.rnode = None

    def __str__(self):
        return str(self.data) + ' (' + str(self.count) + ')'


##### ~~~~~~~~ END OF NODE CLASS ~~~~~~~~ #####


### main execution
import re

def getwords():

    # ask user for input of file
    filename = input('Enter a text file that you want to turn into a binary tree: ')

    # open the file
    try:
        with open(filename) as f:
            fcontents = f.read()

        # split file based on everything except for alphanumerics
        wordlist = re.split('[\W]', fcontents)

        # delete blanks strings
        for word in wordlist:
            if word == '':
                wordlist.remove(word)

        # start with the root and create the tree
        rootnode = Node(wordlist[0])
        for word in wordlist:
            if word is not rootnode.data:
                newnode = Node(word)
                createtree(rootnode, newnode)

        # print the tree
        printtree(rootnode)
    except FileNotFoundError:
        print('Either the file does not exist or you entered the wrong pathname.')

# add words to tree
def createtree(root=Node(), node=Node()):

    # go down the tree and compare words
    if node.data == root.data:
        root.count += 1

    elif node.data < root.data:

        if root.lnode is None:
            root.lnode = node
        else:
            createtree(root.lnode, node)

    elif node.data > root.data:

        if root.rnode is None:
            root.rnode = node
        else:
            createtree(root.rnode, node)

# print the tree
def printtree(node=Node(), level=0):

    if node is not None:
        printtree(node.lnode, level+1)
        print('  ' * (level) + str(node))
        printtree(node.rnode, level+1)

def main():
    getwords()

main()
