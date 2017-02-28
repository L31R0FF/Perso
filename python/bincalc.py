#!/usr/bin/env python  
# -*- coding: utf-8 -*-

entreeA = raw_input("nombreA : ")
entreeB = raw_input("nombreB : ")
entreeC = raw_input("retenueC: ")
entreeD = raw_input("nombreD : ")
entreeE = raw_input("nombreE : ")
entreeF = raw_input("nombreF : ")
entreeG = raw_input("nombreG : ")

entreeA = int(entreeA)
entreeB = int(entreeB)
entreeC = int(entreeC)
entreeD = int(entreeD)
entreeE = int(entreeE)
entreeF = int(entreeF)
entreeG = int(entreeG)

if entreeA == 0 and entreeB == 1 or entreeA == 1 and entreeB == 0 :
	sommeA = 1
else :
	sommeA = 0

if entreeA == 1 and entreeB == 1 :
	retenueA = 1
else :
	retenueA = 0

####################################

if retenueA == 0 and entreeC == 1 or retenueA == 1 and entreeC == 0 :
	sommeB = 1
else :
	sommeB = 0

if retenueA == 1 and entreeC == 1 :
	retenueB = 1
else :
	retenueB = 0

####################################

if sommeB == 1 or retenueB == 1 :
	retenueC = 1
else :
	retenueC = 0

#############################################
#############################################

if retenueC == 0 and entreeD == 1 or retenueC == 1 and entreeD == 0 :
	sommeC = 1
else :
	sommeC = 0

if retenueC == 1 and entreeD == 1 :
	retenueD = 1
else :
	retenueD = 0

####################################

if retenueD == 0 and entreeE == 1 or retenueD == 1 and entreeE == 0 :
	sommeD = 1
else :
	sommeD = 0

if retenueD == 1 and entreeE == 1 :
	retenueE = 1
else :
	retenueE = 0

####################################

if sommeD == 1 or retenueE == 1 :
	retenueF = 1
else :
	retenueF = 0

#############################################
#############################################

if retenueF == 0 and entreeF == 1 or retenueF == 1 and entreeF == 0 :
	sommeE = 1
else :
	sommeE = 0

if retenueF == 1 and entreeF == 1 :
	retenueG = 1
else :
	retenueG = 0

####################################

if retenueG == 0 and entreeG == 1 or retenueG == 1 and entreeG == 0 :
	sommeF = 1
else :
	sommeF = 0

if retenueG == 1 and entreeG == 1 :
	retenueH = 1
else :
	retenueH = 0

####################################

if sommeF == 1 or retenueH == 1 :
	retenueI = 1
else :
	retenueI = 0

print("somme : " + str(sommeA))
print("somme2 : " + str(sommeC))
print("somme3 : " + str(sommeE))
print("retenue : " + str(retenueI))