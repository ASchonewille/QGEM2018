restrictionEnzymes = { "AatII" : "GACGTC",
                       "Acc65I" : "GGTACC",
                       "AccI" : "GTMKAC",
                       "AciI" : "CCGC",
                       "Fake" : "AACGTTA",
                       "AclI" : "AACGTT",
                       "AcuI" : "CTGAAG",
                       "AfeI" : "AGCGCT",
                       "AflII" : "CTTAAG" }

Codon = { "Ala" : [GCU,GCC,GCA,GCG],
          "Arg" : [CGU,CGC,CGA,CGG,AGA,AGG],
          "Asp" : [GAU,GAC],
          "Asn" : [AAU,AAC],
          "Cys" : [UGU,UGC],
          "Gln" : [CAA,CAG],
          "Glu" : [GAA,GAG],
          "Gly" : [GGU,GGC,GGA,GGG],
          "His" : [CAU,CAC],
          "Ile" : [AUU,AUC,AUA],
          "Leu" : [UUA,UUG,CUU,CUC,CUA,CUG],
          "Lys" : [AAA,AAG],
          "Met" : [AUG],
          "Phe" : [UUU,UUC],
          "Pro" : [CCU,CCC,CCA,CCG],
          "Ser" : [UCU,UCC,UCA,UCG,AGU,AGC],
          "Thr" : [ACU,ACC,ACA,ACG],
          "Trp" : [UGG],
          "Tyr" : [UAU,UAC],
          "Val" : [GUU,GUC,GUA,GUG],
          "Stop" : [UAA,UAG,UGA]}
          
          

restrictionIndices = []

class node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        return

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return self.printTreeHelper(0)

    def __hash__(self):
        return hash(self.value)

    def __iter__(self):
        return self

    def printTreeHelper(self, Counter):
        treeString = "|"*Counter + str(self.value + '\n')
        for i in self.children:
            childString = self.children[i].printTreeHelper(Counter+1)
            treeString += childString
        return treeString

    def printChildren(self):
        childString = ""
        for i in self.children:
            childString = childString + str(self.children[i].value) + "|"
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
            Tree.children["A"] = addRestrictionSite(Tree.children["A"], site[1:])
            
        if (site[0] == "C" or site[0] == "B" or site[0] == "H" or site[0] == "M" or site[0] == "N" or site[0] == "S" or site[0] == "V" or site[0] == "Y"):
            if ("C" not in Tree.children):
                Tree.addChild("C")                        
            Tree.children["C"] = addRestrictionSite(Tree.children["C"], site[1:])
            
        if (site[0] == "G" or site[0] == "B" or site[0] == "D" or site[0] == "K" or site[0] == "N" or site[0] == "R" or site[0] == "S" or site[0] == "V"):
            if ("G" not in Tree.children):
                Tree.addChild("G")                        
            Tree.children["G"] = addRestrictionSite(Tree.children["G"], site[1:])
             
        if (site[0] == "T" or site[0] == "B" or site[0] == "D" or site[0] == "H" or site[0] == "K" or site[0] == "N" or site[0] == "W" or site[0] == "Y"):
            if ("T" not in Tree.children):
                Tree.addChild("T")                        
            Tree.children["T"] = addRestrictionSite(Tree.children["T"], site[1:])
   
    return Tree 

def BuildEnzymeTree():
    Tree = node("Root")

    for i in restrictionEnzymes:
        Tree = addRestrictionSite(Tree, restrictionEnzymes[i])
    return Tree

def SearchTree(Tree, seq, start, location):
    
    if "E" in Tree.children:
        restrictionIndices.append([start, location])

    if location == len(seq):
        return

    if seq[location] not in Tree.children:
        return
    elif seq[location] == "U":
        if "T" not in Tree.children:
            return
        else
            SearchTree(Tree.children["T"], seq, start, location+1)
            return
    else: #seq[location] in Tree.children
        SearchTree(Tree.children[seq[location]], seq, start, location+1)
        return
        

def SearchDNASeq(seq):
    Tree = BuildEnzymeTree()
    for i in range(len(seq)):
        SearchTree(Tree, seq, i, i)
    return

def SilentMutationIntroduction(seq, startSite):
    

def Main(): 
    seq = 'GACGTCCGCCCCCCCCCCCCCGCCCCCGCCCCGCCCCCCAACGTTA'
    SearchDNASeq(seq)
    print(restrictionIndices)
    

Main()
