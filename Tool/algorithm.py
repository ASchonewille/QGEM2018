from random import randint

restrictionEnzymes = { "AatII" : "GACGTC",
                       "Acc65I" : "GGTACC",
                       "AccI" : "GTMKAC",
                       "AciI" : "CCGC",
                       "Fake" : "AACGTTA",
                       "AclI" : "AACGTT",
                       "AcuI" : "CTGAAG",
                       "AfeI" : "AGCGCT",
                       "AflII" : "CTTAAG" }

Codon = { "Ala" : ["GCU","GCC","GCA","GCG"],
          "Arg" : ["CGU","CGC","CGA","CGG","AGA","AGG"],
          "Asp" : ["GAU","GAC"],
          "Asn" : ["AAU","AAC"],
          "Cys" : ["UGU","UGC"],
          "Gln" : ["CAA","CAG"],
          "Glu" : ["GAA","GAG"],
          "Gly" : ["GGU","GGC","GGA","GGG"],
          "His" : ["CAU","CAC"],
          "Ile" : ["AUU","AUC","AUA"],
          "Leu" : ["UUA","UUG","CUU","CUC","CUA","CUG"],
          "Lys" : ["AAA","AAG"],
          "Met" : ["AUG"],
          "Phe" : ["UUU","UUC"],
          "Pro" : ["CCU","CCC","CCA","CCG"],
          "Ser" : ["UCU","UCC","UCA","UCG","AGU","AGC"],
          "Thr" : ["ACU","ACC","ACA","ACG"],
          "Trp" : ["UGG"],
          "Tyr" : ["UAU","UAC"],
          "Val" : ["GUU","GUC","GUA","GUG"],
          "Stop" : ["UAA","UAG","UGA"]}
          
                                                                                  

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
        treeString = "|"*Counter + str(self.value) + '\n'
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

def AddRestrictionSite(Tree, site):
    if (not site):
        Tree.addChild("E")
    else:
        if (site[0] == "A" or site[0] == "D" or site[0] == "H" or site[0] == "M" or site[0] == "N" or site[0] == "R" or site[0] == "V" or site[0] == "W"):

            if ("A" not in Tree.children):
                Tree.addChild("A")
            Tree.children["A"] = AddRestrictionSite(Tree.children["A"], site[1:])
            
        if (site[0] == "C" or site[0] == "B" or site[0] == "H" or site[0] == "M" or site[0] == "N" or site[0] == "S" or site[0] == "V" or site[0] == "Y"):
            if ("C" not in Tree.children):
                Tree.addChild("C")                        
            Tree.children["C"] = AddRestrictionSite(Tree.children["C"], site[1:])
            
        if (site[0] == "G" or site[0] == "B" or site[0] == "D" or site[0] == "K" or site[0] == "N" or site[0] == "R" or site[0] == "S" or site[0] == "V"):
            if ("G" not in Tree.children):
                Tree.addChild("G")                        
            Tree.children["G"] = AddRestrictionSite(Tree.children["G"], site[1:])
             
        if (site[0] == "T" or site[0] == "B" or site[0] == "D" or site[0] == "H" or site[0] == "K" or site[0] == "N" or site[0] == "W" or site[0] == "Y"):
            if ("T" not in Tree.children):
                Tree.addChild("T")                        
            Tree.children["T"] = AddRestrictionSite(Tree.children["T"], site[1:])
   
    return Tree 

def BuildEnzymeTree():
    Tree = node(0)

    for i in restrictionEnzymes:
        currentLen = len(restrictionEnzymes[i])
        if currentLen > Tree.value:
            Tree.value = currentLen
        Tree = AddRestrictionSite(Tree, restrictionEnzymes[i])
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
        else:
            SearchTree(Tree.children["T"], seq, start, location+1)
            return
    else: #seq[location] in Tree.children
        SearchTree(Tree.children[seq[location]], seq, start, location+1)
        return
        

def SearchDNASeq(seq):
    Tree = BuildEnzymeTree()
    for i in range(len(seq)):
        SearchTree(Tree, seq, i, i)
    return Tree


#Assumes that the first occurance of ATG is the start of the reading frame
def SilentMutationIntroduction(seq):
    stopPositions = []
    frameStart = seq.find('ATG')

    for i in Codon['Stop']:
        print (i)
        stopPositions.append(seq.find(i,frameStart))
    print(stopPositions)    
    stopSite = min(stopPositions)
    
    codingRegion = CodingRegionMutations(seq, frameStart, stopSite)
    preCodedMutatedSequence = PreCodingRegionMutations(seq, frameStart, stopSite)
    postCodedMutatedSequence = PostCodingRegionMutations(seq, frameStart, stopSite)
    seq = preCodedMutatedSequence + codingRegion + postCodedMutatedSequence
    
    return seq

def CodingRegionMutations(seq, frameStart, stopSite):
    #FIX THIS
    filler = "FILLER"
    return filler


def PostCodingRegionMutations(seq, frameStart, stopSite):

    i = 0
    validPostSites = []
    for i in range(len(restrictionIndices)):
        validPostSites.append(restrictionIndices[i]) 
        i= i + 1
    j = 0
    for j in range(len(validPostSites)):
        tempSite = []
        tempSite.append(validPostSites[j][0])
        tempSite.append(validPostSites[j][1])
        randomPosition = randint(tempSite[0],tempSite[1])    
        seq = seq[:randomPosition] + "C" + seq[randomPosition:]
        j = j + 1
    postCodedMutatedSequence = seq[stopSite:]
    return postCodedMutatedSequence
    

def PreCodingRegionMutations(seq, frameStart, stopSite):
    
    i = 0
    validPreSites = []
    while restrictionIndices[i][0] < frameStart:
        validPreSites.append(restrictionIndices[i])
        i= i + 1       
    j = 0
    for j in range(len(validPreSites)):
        tempSite = []
        tempSite.append(validPreSites[j][0])
        tempSite.append(validPreSites[j][1])
        randomPosition = randint(tempSite[0],tempSite[1])
        seq = seq[:randomPosition] + "C" + seq[randomPosition:]
        j = j + 1
    preCodedMutatedSequence = seq[:frameStart]
    return preCodedMutatedSequence
    
def Main(): 
    
    seq = 'ACTGAAGAAGATGCCGCAAAUAAGAATAA'
    stopSite = 23
    frameStart = seq.find('ATG')
    Tree = SearchDNASeq(seq)
    print(Tree)
    print(restrictionIndices)
    
    post = PostCodingRegionMutations (seq, frameStart, stopSite)
    pre = PreCodingRegionMutations (seq, frameStart, stopSite)
    print (pre)
    print (post)

Main()
