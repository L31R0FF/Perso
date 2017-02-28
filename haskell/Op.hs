module Op (plus, moins, fois, divise) where

plus :: Real a => a -> a -> a
plus n1 n2 = n1 + n2

moins :: Real a => a -> a -> a
moins n1 n2 = n1 - n2

fois :: Real a => a -> a -> a
fois n1 n2 = n1 * n2

divise :: Fractional a => a -> a -> a
divise n1 n2 = n1 / n2