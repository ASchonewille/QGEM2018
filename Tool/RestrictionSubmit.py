#!"C:/Users/Abigael/AppData/Local/Programs/Python/Python36-32/python.exe"

print("Content-Type: text/html\r\n")

import cgi
import algorithm
from colorama import Fore, Back, Style

print("""
<html>
<head>
    <!-- Standard Meta -->
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

    <!-- Site Properties -->
    <title>QGEM</title>
    <link rel="icon" href="QGEMLogo.jpg">
    <link rel="stylesheet" type="text/css" href=   "https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.0/semantic.css">
    <link rel="stylesheet" type="text/css" href=   "./QGEM.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.0/semantic.min.js"></script>

    <style>
        .wrapper {
            margin-top: 20px;
        }
    </style>
	
</head>

<body>
<div class="wrapper">
<div class="ui container">
    <div class='ui pointing menu'>
	<div class= "ui tiny image">
            <img src="QGEMLogo.jpg">
        </div>
        <a class='item' href='./home.php'>
            Home
        </a>
        <a class='active item green' href='./RestrictionSites.php'>
            Restriction Sites
        </a>

    </div>

    	
    <div class="ui segment">
        <h1>Restriction Site Elimination</h1> 

    <form class="ui form segment" id="RestrictionSubmitForm">
        <div class='field'>
            <p class="detail ow">
            
""")

form = cgi.FieldStorage()

if "sequence" not in form and "sequenceFile" not in form:
    print("No sequence was provided")
elif "sequence" in form and "sequenceFile" not in form:
    seq = (form["sequence"].value)
    
    Tree, restrictionIndices = algorithm.SearchDNASeq(seq)

    codedMutation = algorithm.MutationIntroduction(seq, Tree, restrictionIndices)
    if len(restrictionIndices) > 0 :
        original = seq[:restrictionIndices[0][0]]
        mutated = codedMutation[:restrictionIndices[0][0]]
        for i in range(len(restrictionIndices)):
            if i+1 == len(restrictionIndices):
                original = original + '<span class="cutSite">' + seq[restrictionIndices[i][0]:restrictionIndices[i][1]] + '</span>' + seq[restrictionIndices[i][1]:]
                mutated = mutated + '<span class="cutSite">' + codedMutation[restrictionIndices[i][0]:restrictionIndices[i][1]] + '</span>' + codedMutation[restrictionIndices[i][1]:]
            else:
                original = original + '<span class="cutSite">' + seq[restrictionIndices[i][0]:restrictionIndices[i][1]] + '</span>' + seq[restrictionIndices[i][1]:restrictionIndices[i+1][0]]
                mutated = mutated + '<span class="cutSite">' + codedMutation[restrictionIndices[i][0]:restrictionIndices[i][1]] + '</span>' + codedMutation[restrictionIndices[i][1]:restrictionIndices[i+1][0]]

        frameStart = original.find('ATG')
        stopPositions = []
        if not frameStart == -1:
            for i in algorithm.Codon['Stop']:
                currentStop = original.find(i,frameStart)
                if (currentStop > -1) and ((currentStop - frameStart)%3 == 0) :
                    stopPositions.append(currentStop)
            if len(stopPositions) > 0:
                stop = min(stopPositions)
                original = original[:frameStart] + '<span class="startSite">' + original[frameStart:frameStart+3] + '</span>' + original[frameStart+3:stop] + '<span class="stopSite">' + original[stop:stop+3] + '</span>' + original[stop+3:]
                mutated = mutated[:frameStart] + '<span class="startSite">' + mutated[frameStart:frameStart+3] + '</span>' + mutated[frameStart+3:stop] + '<span class="stopSite">' + mutated[stop:stop+3] + '</span>' + mutated[stop+3:]


    print("Original: <br>", original)
    print("<br>")
    print("Mutated: <br>", mutated)
else:
    print("File section")
        
print ("""
            </p>
        </div>
        
    </div>
    </form>
</div>
</div>
</body>
</html>
""")
