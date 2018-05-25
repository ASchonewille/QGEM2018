<!DOCTYPE html>
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

    <form class="ui form segment" id="RestrictionEliminationForm" action="./RestrictionSubmit.py" method="get" >
        <h1>Restriction Site Elimination</h1>
        <p>How to use this tool</p>  
        <div class="ui segment">
            <div class="field">
                    <label>Target Sequence</label>
                    <textarea name="sequence"></textarea> 
            </div>
            
				<label for="sequenceFile" class="ui button">
					<i class="ui file icon"></i> 
					Upload File
				</label>
				<input type="file" (change)="fileEvent($event)" class="inputfile" name="sequenceFile" style="display: none" id="sequenceFile"/>

				<div class='ui right floated submit button' id='submitButton' onclick='document.getElementById("RestrictionEliminationForm").submit();'>Submit
				</div>
		</div>
    </form>  
  
</div>
</div>  

</body>

</html>