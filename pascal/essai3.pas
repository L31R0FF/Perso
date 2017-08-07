Program rkey;
Uses Crt;
Var touche : Char;
BEGIN
    repeat
        touche := ReadKey;
        Write(touche, ':');
    until touche = 'q'; 
END. 