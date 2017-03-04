<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
	</head>

	<body>
		<?php 
			if (!preg_match("#^[a-z0-9._-]+@(hotmail|live|msn).[a-z]{2,4}$#", $mail)) {
    				$passage_ligne = "\r\n";
			}
			else {
    				$passage_ligne = "\n";
			}
			$mail = $_POST["mail"];
			$exp = $_POST["exp"];
			$sujet = $_POST["subject"];
			$message_text = $_POST["message"];

			$boundary = "-----=".md5(rand());
			$boundary_alt = "-----=".md5(rand());

			$header = "From: ".$exp.$passage_ligne;
			$header .= "Reply-to: ".$exp.$passage_ligne;
			$header .= "MIME-Version: 1.0".$passage_ligne;
			$header.= "Content-Type: multipart/mixed;".$passage_ligne." boundary=\"$boundary\"".$passage_ligne;
			
			$message = $passage_ligne."--".$boundary.$passage_ligne;
			$message.= "Content-Type: multipart/alternative;".$passage_ligne." boundary=\"$boundary_alt\"".$passage_ligne;
			$message.= $passage_ligne."--".$boundary_alt.$passage_ligne;
			$message.= "Content-Type: text/plain; charset=\"ISO-8859-1\"".$passage_ligne;
			$message.= "Content-Transfer-Encoding: 8bit".$passage_ligne;
			$message.= $passage_ligne.$message_txt.$passage_ligne;
			$message.= $passage_ligne."--".$boundary.$passage_ligne;

			mail($mail,$sujet,$message,$header);
			echo "message envoyé !";
		?>
	</body>
</html>
