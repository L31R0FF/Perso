import System.Random

nmax :: Int
nmax = 0

nmin :: Int
nmin = 0

minijeu n ncoups = do
    putStrLn "Nombre : "
    ne <- readLn :: IO Int
    if ne == n
        then do
            putStrLn $ "Vous avez trouvé en " ++ show (ncoups+1) ++ " coups !"
            return ncoups
        else do
            if ne < n
            then do
                putStrLn "Plus grand"
                minijeu n (ncoups + 1)
            else do
                putStrLn "Plus petit"
                minijeu n (ncoups + 1)

preludejeu :: IO Int
preludejeu = do
    putStrLn "Maximum : "
    nmax <- readLn :: IO Int
    putStrLn "Minimum : "
    nmin <- readLn :: IO Int
    n <- randomRIO (nmin,nmax)
    minijeu n 0

main = preludejeu