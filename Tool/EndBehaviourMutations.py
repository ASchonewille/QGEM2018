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
