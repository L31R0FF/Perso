import System.IO

lecture inp = do
    eof <- hIsEOF inp
    if eof
        then return ()
        else do
            ligne <- hGetLine inp
            putStrLn ligne
            lecture inp
            
ecriture outp texte = do
    if texte == "EOF"
        then return ()
        else do
            hPutStrLn outp texte
            texte <- getLine
            ecriture outp texte    

main = do
    putStrLn "Nom du fichier"
    nfichier <- getLine
    inp <- openFile nfichier ReadMode
    lecture inp
    hClose inp
    putStrLn " "
    putStrLn "----------------------------------------"
    putStrLn " "
    outp <- openFile nfichier WriteMode
    ecriture outp ""
    hClose outp