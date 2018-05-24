#!"C:/Users/Abigael/AppData/Local/Programs/Python/Python36-32/python.exe"

print("Content-Type: text/html\r\n")


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
        <a class='active item green' href='./RestrictionSites.php'>
            Restriction Sites
        </a>

    </div>
</div>
</div>
</html>
""")
