<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
	</head>

	<body>
		<title>Biblio</title>
		<h1>Biblio</h1>
		<?php
            try
            {
                $db = new PDO('mysql:host=localhost;dbname=TDB;charset=utf8','root','grigou');
            }
            catch (Exception $e)
            {
                die('Erreur : ' . $e->getMessage());
            }
        ?>
	</body>

</html>