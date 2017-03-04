<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
	</head>

	<body>
		<title>Biblio</title>
		<h1>Biblio</h1>
		<form method="post" action="biblio.php">
            <label>Auteur : <input type="text" name="auteur" /></label><br />
            <label>Titre : <input type="text" name="titre" /></label><br />
            <label>date : <input type="text" name="date_edition" /></label><br />
            <label>Maison : <input type="text" name="edition" /></label><br />
            <label>Collection : <input type="text" name="collection" /></label><br />
            <label>Genre : <input type="text" name="genre" /></label><br />
            <label>Commentaire : <input type="text" name="commentaire" /></label><br />
            <input type="hidden" name="foo" value="ok" />
            <input type="submit" value="Rechercher" name="send" />
        </form>
        <?php
            if (isset($_POST["foo"]))
            {
                try
                {
                    $db = new PDO('mysql:host=localhost;dbname=TDB;charset=utf8','root','grigou');
                    $debut = 0;
                    if (isset($_POST["auteur"]) and $debut == 0)
                    {
                        $auteur = $_POST["auteur"];
                        $mysql_commande = " WHERE auteur='" . $auteur . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["auteur"]) and $debut == 1)
                    {
                        $auteur = $_POST["auteur"];
                        $mysql_commande = $mysql_commande . " AND auteur='" . $auteur . "'";
                    }

                    elseif (isset($_POST["titre"]) and $debut == 0)
                    {
                        $titre = $_POST["titre"];
                        $mysql_commande = " WHERE titre='" . $titre . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["titre"]) and $debut == 1)
                    {
                        $titre = $_POST["titre"];
                        $mysql_commande = $mysql_commande . " AND titre='" . $titre . "'";
                    }

                    elseif (isset($_POST["date_edition"]) and $debut == 0)
                    {
                        $date_edition = $_POST["date_edition"];
                        $mysql_commande = " WHERE date_edition='" . $date_edition . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["date_edition"]) and $debut == 1)
                    {
                        $date_edition = $_POST["date_edition"];
                        $mysql_commande = $mysql_commande . " AND date_edition='" . $date_edition . "'";
                    }

                    elseif (isset($_POST["edition"]) and $debut == 0)
                    {
                        $edition = $_POST["edition"];
                        $mysql_commande = " WHERE edition='" . $edition . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["edition"]) and $debut == 1)
                    {
                        $edition = $_POST["edition"];
                        $mysql_commande = $mysql_commande . " AND edition='" . $edition . "'";
                    }

                    elseif (isset($_POST["collection"]) and $debut == 0)
                    {
                        $collection = $_POST["collection"];
                        $mysql_commande = " WHERE collection='" . $collection . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["collection"]) and $debut == 1)
                    {
                        $collection = $_POST["collection"];
                        $mysql_commande = $mysql_commande . " AND collection='" . $collection . "'";
                    }

                    elseif (isset($_POST["genre"]) and $debut == 0)
                    {
                        $genre = $_POST["genre"];
                        $mysql_commande = " WHERE genre='" . $genre . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["genre"]) and $debut == 1)
                    {
                        $genre = $_POST["genre"];
                        $mysql_commande = $mysql_commande . " AND genre='" . $genre . "'";
                    }

                    elseif (isset($_POST["commentaire"]) and $debut == 0)
                    {
                        $commentaire = $_POST["commentaire"];
                        $mysql_commande = " WHERE commentaire='" . $commentaire . "'";
                        $debut = 1;
                    }
                    elseif (isset($_POST["commentaire"]) and $debut == 1)
                    {
                        $commentaire = $_POST["commentaire"];
                        $mysql_commande = $mysql_commande . " AND commentaire='" . $commentaire . "'";
                    }
                    $my_query = 'SELECT * FROM Livres' . $mysql_commande;
                    $reponse = $db->query($my_query);    
                    while ($donnees = $reponse->fetch())
                    {
                    ?>
                        <p>
                            <strong>Titre :</strong> <?php echo $donnees['titre']; ?><br />
                            <strong>Auteur :</strong> <?php echo $donnees['auteur']; ?><br />
                            <strong>Edition/Collection :</strong> <?php echo $donnees['edition']; echo ", " . $donnees['collection']; ?><br />
                            <strong>Imprimé en :</strong> <?php echo $donnees['date_edition']; ?><br />
                            <strong>Genre :</strong> <?php echo $donnees["genre"]; ?><br />
                            <strong>Commentaires :</strong><br />
                            <em>"<?php echo $donnees['commentaire']; ?>"</em>
                        </p>
                    <?php
                    }                
                    $reponse->closeCursor(); 
                }   
                catch (Exception $e)
                {
                    die('Erreur : ' . $e->getMessage());
                }
            }
            else
            {

            }
        ?>
	</body>

</html>