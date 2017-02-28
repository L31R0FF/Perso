import Op
{-
    Ce programme à été écrit par Félix Foriel le 24/02/2017
-}
periCercle r = 2 * pi * r -- calcule le périmètre d'un cercle
periRect long larg = 2.0*(long+larg) -- calcule le périmètre d'un rectangle
b = a -- Test d'une déclaration récursive
a = 1

x |& y = (x || y) && not (x && y)
grter x y = if x > y then True else False -- vrai si x est plus grand que y 
lower x y = if x < y then True else False -- vrai si x est plus petit que y

grter2 x y = x > y -- la même chose que les deux avant simplifié
lower2 x y = x < y

inLetters x = case x of
    0 -> "Zero"
    1 -> "One"
    2 -> "Two"
    3 -> "Three"
    4 -> "Four"
    5 -> "Five"
    6 -> "Six"
    7 -> "Seven"
    8 -> "Eight"
    9 -> "Nine"
    _ -> "Too great !"

fonct x = 2*x-1

myMin x y = if x > y then y
            else x

myMax x y = if x > y then x
            else y

head' (x:_) = x

phonum nom = case nom of
    "papa" -> Just "06 36 95 84 63"
    "maman" -> Just "06 79 87 09 77"
    "moi" -> Just "07 68 40 36 23"
    _ -> Nothing

fois Nothing _ = Nothing
fois _ Nothing = Nothing
fois (Just a) (Just b) = Just (a * b)

monprenom :: [Char]
monprenom = "Felix"

monnom :: String
monnom = "Foriel"

numero :: Maybe Integer
numero = Just 123

fac 1 = 1
fac n = n * fac (n-1)

plus 1 1 = 2
plus 3 3 = 6
plus a b = plus a b

indent i    -- Essai de récursion
    | i > 1000000 = "Nombre trop grand !"
    | i == 1000000 = "Fini" 
    | otherwise = indent (i+1)

f :: Floating a => a -> a
f x = x+2.0

f2 = (+2.0)

type Coords = (Double, Double, Double)

c1 :: Coords
c1 = (1.0,1.0,1.0)

data Etat = Mort | Vivant

type Tel = [(Int,Int)]

data Personne = Personne String String Tel String
    deriving Show

newPers :: String -> String -> Tel -> String -> Personne
newPers nom prenom tel mail = Personne nom prenom tel mail

data Personne2 = Personne2 {
    nom :: String,
    prenom :: String,
    tel :: Tel,
    mail :: String
    } deriving Show 

newPers2 :: String -> String -> Tel -> String -> Personne2
newPers2 mynom myprenom mytel mymail = Personne2 { nom = mynom,
                                           prenom = myprenom,
                                           tel = mytel,
                                           mail = mymail
                                         }
