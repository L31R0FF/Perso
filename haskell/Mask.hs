import System.IO

ask prompt = do
    hSetBuffering stdout NoBuffering
    hSetBuffering stdin NoBuffering
    putStr prompt
    texte <- getLine
    return texte

sayln sentence = do
    putStrLn sentence
    return ()

say sentence = do
    hSetBuffering stdout NoBuffering
    hSetBuffering stdin NoBuffering
    putStr sentence
    return ()

fread file = do
    text <- readFile file
    putStrLn text
    return () 

fappend file text = do
    appendFile file text
    return ()

fwrite  file text = do
    writeFile file text
    return ()   