from random import randint
restrictionEnzymes = { "AatII" : "GACGTC",
                       "Acc65I" : "GGTACC",
                       "AccI" : "GTMKAC",
                       "AciI" : "CCGC",
                       "Fake" : "TGGAAAC",
                       "AclI" : "AACGTT",
                       "AcuI" : "CTGAAG",
                       "AfeI" : "AGCGCT",
                       "AflII" : "CTTAAG" }


Codon = { "Ala" : ["GCT","GCC","GCA","GCG"],
          "Arg" : ["CGT","CGC","CGA","CGG","AGA","AGG"],
          "Asp" : ["GAT","GAC"],
          "Asn" : ["AAT","AAC"],
          "Cys" : ["TGT","TGC"],
          "Gln" : ["CAA","CAG"],
          "Glu" : ["GAA","GAG"],

          "Gly" : ["GGT","GGC","GGA","GGG"],
          "His" : ["CAT","CAC"],
          "Ile" : ["ATT","ATC","ATA"],
          "Leu" : ["TTA","TTG","CTT","CTC","CTA","CTG"],
          "Lys" : ["AAA","AAG"],

          "Met" : "ATG",
          "Phe" : ["TTT","TTC"],
          "Pro" : ["CCT","CCC","CCA","CCG"],
          "Ser" : ["TCT","TCC","TCA","TCG","AGT","AGC"],
          "Thr" : ["ACT","ACC","ACA","ACG"],
          "Trp" : "TGG",
          "Tyr" : ["TAT","TAC"],
          "Val" : ["GTT","GTC","GTA","GTG"],
          "Stop" : ["TAA","TAG","TGA"]}

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

def SearchTree(Tree, seq, start, location, restrictionIndices):
    
    if "E" in Tree.children:
        restrictionIndices.append([start, location])

    if location == len(seq):
        return restrictionIndices

    if seq[location] not in Tree.children:
        return restrictionIndices
    elif seq[location] == "U":
        if "T" not in Tree.children:
            return restrictionIndices
        else:
            SearchTree(Tree.children["T"], seq, start, location+1, restrictionIndices)
            return restrictionIndices
    else: #seq[location] in Tree.children
        SearchTree(Tree.children[seq[location]], seq, start, location+1, restrictionIndices)
        return restrictionIndices
        

def SearchDNASeq(seq):
    Tree = BuildEnzymeTree()
    restrictionIndices = []
    for i in range(len(seq)):
        restrictionIndices = SearchTree(Tree, seq, i, i, restrictionIndices)
    return Tree, restrictionIndices


#Assumes that the first occurance of ATG is the start of the reading frame
def MutationIntroduction(seq, Tree, restrictionIndices):

    if len(restrictionIndices) == 0:
        return seq

    stopPositions = []
    frameStart = seq.find('ATG')

    for i in Codon['Stop']:
        currentStop = seq.find(i,frameStart)
        if (currentStop > -1) and ((currentStop - frameStart)%3 == 0) :
            stopPositions.append(currentStop)
    if len(stopPositions) == 0 or frameStart == -1:
        #Treat all as non-coding
        return seq #change later

    stopSite = min(stopPositions)
    
    codingRegion = CodingRegionMutations(seq, frameStart, stopSite, Tree, restrictionIndices)
    preCodedMutatedSequence = PreCodingRegionMutations(seq, frameStart, stopSite, restrictionIndices)
    postCodedMutatedSequence = PostCodingRegionMutations(seq, frameStart, stopSite, restrictionIndices)
    seq = preCodedMutatedSequence + codingRegion + postCodedMutatedSequence
    
    return seq

def PreCodingRegionMutations(seq, frameStart, stopSite, restrictionIndices):
    
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


def CodingRegionMutations(seq, frameStart, stopSite, Tree, restrictionIndices):
    validSite = False
    numRestriction = len(restrictionIndices)
    counter = -1
    firstSiteIndex = -1
    lastSiteIndex = numRestriction
    
    while (not validSite) and (counter < (len(restrictionIndices)-1)):
        counter += 1        
        if restrictionIndices[counter][0] >= frameStart and firstSiteIndex == -1:
            firstSiteIndex  = counter
        if restrictionIndices[counter][1] > stopSite + 3:
            lastSiteIndex = counter
            validSite = True

    if firstSiteIndex == lastSiteIndex:
        return seq[frameStart:(stopSite+3)]

    mutatedSeq = seq
    codingRegionRestrictionSites = restrictionIndices[firstSiteIndex:lastSiteIndex]

    for i in codingRegionRestrictionSites:
        mutatedSeq = SilentMutation(mutatedSeq, frameStart, Tree, i)
        
    return mutatedSeq[frameStart:(stopSite+3)]

def SilentMutation(seq, frameStart, Tree, restrictionIndex):

    shift = (restrictionIndex[0] - frameStart) % 3
    codonStart = restrictionIndex[0] - shift
    currentCodon = seq[codonStart:(codonStart + 3)]

    aminoAcid = [key for key, value in Codon.items() if currentCodon in value][0]

    if aminoAcid == 'Met' or aminoAcid == 'Trp':
        if (codonStart + 3) >= restrictionIndex[1]:
            print("Could not resolve Restriction Site")
            return seq
        else:
            return SilentMutation(seq, frameStart, Tree, [(codonStart + 3),restrictionIndex[1]])

    differences = []
    for i in Codon[aminoAcid]:
        if not (i == currentCodon):
            differences.append(sum(1 for a, b in zip(i, currentCodon) if a != b))
        else: 
            differences.append(4)

    minMut = min(differences)
    while minMut < 4:
        position = differences.index(minMut)
        mutatedSeq = seq[:codonStart] + Codon[aminoAcid][position] + seq[(codonStart + 3):]
        numRestrictionSites = 0
        for k in range(Tree.value + 3):
            numRestrictionSites += len(SearchTree(Tree, seq, (codonStart - Tree.value), (codonStart - Tree.value), []))
        if numRestrictionSites == 0 :
            return mutatedSeq
        else:
            differences[position] = 4
            minMut = min(differences)
    print("Could not resolve with one mutation")
    return seq


def PostCodingRegionMutations(seq, frameStart, stopSite, restrictionIndices):

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
        seq = seq[:randomPosition] + "C" + seq[randomPosition+1:]
        j = j + 1
    postCodedMutatedSequence = seq[(stopSite+3):]
    return postCodedMutatedSequence
    

def Main():
    
    seq = 'AAAAAAAAAAAAAAAACCGCAAAAAAAAAAAAATGCCCCCCTGGAAACCCCCGCCCCCCCGCCCCCCCTAAAAAAAAAAAAAA'
    Tree, restrictionIndices = SearchDNASeq(seq)


    codedMutation = MutationIntroduction(seq, Tree, restrictionIndices)
    print(seq)
    print(codedMutation)

Main()
