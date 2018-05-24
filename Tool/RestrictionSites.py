#!"C:/Users/Abigael/AppData/Local/Programs/Python/Python36-32/python.exe"
print("Content-Type: text/html\n")

print("""
<html>
<head>
    <!-- Standard Meta -->
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

    <!-- Site Properties -->
    <title>QGEM</title>
    <link rel="stylesheet" type="text/css" href=   "https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.0/semantic.css">
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
        <a class='active item blue' href='./RestrictionSites.php'>
            Restriction Sites
        </a>

    </div>
	
  <div class="ui segment">
    <h1>Restriction Site Elimination</h1>
    <p>How to use this tool</p>
  </div>
  
  <div class="ui segment">  
	<form class="ui form">
		<div class="field">
			<label>Target Sequence</label>
			<textarea name="sequence"></textarea> 
		</div>
		
		<div class="ui right labeled input">
			<input type="text" name="inputFile" placeholder="Choose a file">
			<label for="sequenceFile" class="ui button">
				Browse Files
			</label>
			<input type="file" name="sequenceFile" style="display: none">
		</div>
	</form>  
  </div>
  
</div>
</div>  

</body>

</html>""")
