//
//  main.cpp
//  SimpleCpp
//
//  Created by Cyril Foriel on 26/04/2017.
//  Copyright © 2017 FORC. All rights reserved.
//

#include <iostream>
#include <string>
#include "simplecpp.h"

int main(int argc, const char * argv[]) {
    println("coucou !");
    std::string nom = ask("Nom : ");
    println("Hello " + nom + " !");
    fprintln("ll", "w", nom + " est genial");
    std::string texte = fread("ll");
    println(texte);
    return 0;
}
