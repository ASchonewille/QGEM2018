restrictionEnzymes = { "AatII" : "GACGTC",
                       "Acc65I" : "GGTACC",
                       "AccI" : "GTMKAC",
                       "AciI" : "CCGC",
                       "AclI" : "AACGTT",
                       "AcuI" : "CTGAAG",
                       "AfeI" : "AGCGCT",
                       "AflII" : "CTTAAG" }

class node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        return

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __iter__(self):
        return self

    def printChildren(self):
        childString = ""
        for i in self.children:
            childString += self.children[i] + '/'
        print(childString)
        return
    
    def addChild(self, value):
        if (value not in self.children):
            self.children[value] = node(value)
        else:
            print("Already in child set")
        return

def addRestrictionSite(Tree, site):
    if (not site):
        Tree.addChild("E")
    else:
        if (site[0] == "A" or site[0] == "D" or site[0] == "H" or site[0] == "M" or site[0] == "N" or site[0] == "R" or site[0] == "V" or site[0] == "W"):

            if ("A" not in Tree.children):
                Tree.addChild("A")                        
            Tree.children = addRestrictionSite(Tree.children["A"], site[1:])
            
        if (site[0] == "C" or site[0] == "B" or site[0] == "H" or site[0] == "M" or site[0] == "N" or site[0] == "S" or site[0] == "V" or site[0] == "Y"):
            if ("C" not in Tree.children):
                Tree.addChild("C")                        
            Tree.children = addRestrictionSite(Tree.children["C"], site[1:])
            
        if (site[0] == "G" or site[0] == "B" or site[0] == "D" or site[0] == "K" or site[0] == "N" or site[0] == "R" or site[0] == "S" or site[0] == "V"):
            if ("G" not in Tree.children):
                Tree.addChild("G")                        
            Tree.children = addRestrictionSite(Tree.children["G"], site[1:])
             
        if (site[0] == "T" or site[0] == "B" or site[0] == "D" or site[0] == "H" or site[0] == "K" or site[0] == "N" or site[0] == "W" or site[0] == "Y"):
            if ("T" not in Tree.children):
                Tree.addChild("T")                        
            Tree.children = addRestrictionSite(Tree.children["T"], site[1:])
   
    return Tree 

def BuildEnzymeTree(enzymes):
    Tree = node("Root")
    print(Tree.value)
    print(Tree.children)
    Tree = addRestrictionSite(Tree, "ATCG")
    Tree.printChildren()
    

def Main():    
    enzymes = ["AatII", "AciI", "AfeI"]
    Tree = BuildEnzymeTree(enzymes)
    
    

Main()
