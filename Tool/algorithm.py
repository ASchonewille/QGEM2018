restrictionEnzymes = { "AatII" : "GACGTC",
                       "Acc65I" : "GGTACC",
                       "AccI" : "GTMKAC",
                       "AciI" : "CCGC",
                       "AclI" : "AACGTT",
                       "AcuI" : "CTGAAG",
                       "AfeI" : "AGCGCT",
                       "AflII" : "CTTAAG" }

class node:
    def __init__(self, value, childList):
        self.value = value
        self.children = setChildren(childList)

    def setChildren(childList):
        for i in childList:
            self.addChild(i)
        return

    def addChild(self, childValue):
        placed = False
        i = 0
        while i < range(self.children) || !placed:
            if childValue < self.children[i]:
                self.children.insert(i, node(childValue, [])
                placed = True
            i += 1
        return                 

def BuildEnzymeTree(enzymes):
    Tree = node("Root", [])
    for i in enzymes: 

def Main():
    enzymes = ["AatII", "AciI", "AfeI"]
    Tree = BuildEnzymeTree(enzymes)
    

Main()
