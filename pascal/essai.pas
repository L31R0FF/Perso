Program Salut;
Var nom : String;
Var prenom : String;
BEGIN
    Write('Prenom : ');
    ReadLn(prenom);
    Write('Nom : ');
    ReadLn(nom);
    Writeln('Bonjour ', prenom, ' ', nom, ' !');
END.