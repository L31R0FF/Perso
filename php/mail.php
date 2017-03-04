<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
	</head>

	<body>
		<title>Mail</title>
		<h1>Mail</h1>
		<form method="post" action="mailCible.php">
			<p>Expéditeur : <input type="mail" name="exp" /></p>
			<p>Envoyer à :  <input type="mail" name="mail" /></p>
			<p>Sujet :      <input type="mail" name="subject" /></p>
			<p>Message :</p>
			<p>
				<textarea name="message" rows="16" cols="60" spellcheck="false">
				</textarea>
			</p>
			<input type="submit" value="Envoyer" />
		</form>
	</body>

</html>