//
//  simplecpp.cpp
//  SimpleCpp
//
//  Created by Cyril Foriel on 26/04/2017.
//  Copyright © 2017 FORC. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include "simplecpp.h"

void print(std::string text) {
    std::cout << text;
}

void println(std::string text) {
    std::cout << text << std::endl;
}

std::string ask(std::string text) {
    std::cout << text;
    std::string reponse;
    std::getline(std::cin, reponse);
    return reponse;
}

void fprint(std::string nom, std::string mode, std::string text) {
    if(mode == "w") {
        std::ofstream monFlux(nom.c_str());
        if(monFlux) {
            monFlux << text;
        }
        else {
            std::cout << "ERROR: file " << nom << " cannot be open" << std::endl;
        }
    }
    else {
        std::ofstream monFlux(nom.c_str(), std::ios::app);
        if(monFlux) {
            monFlux << text;
        }
        else {
            std::cout << "ERROR: file " << nom << " cannot be open" << std::endl;
        }
        
    }
}

void fprintln(std::string nom, std::string mode, std::string text) {
    if(mode == "w") {
        std::ofstream monFlux(nom.c_str());
        if(monFlux) {
            monFlux << text << std::endl;
        }
        else {
            std::cout << "ERROR: file " << nom << " cannot be open" << std::endl;
        }
    }
    else {
        std::ofstream monFlux(nom.c_str(), std::ios::app);
        if(monFlux) {
            monFlux << text << std::endl;
        }
        else {
            std::cout << "ERROR: file " << nom << " cannot be open" << std::endl;
        }
    }
    
}

std::string fread(std::string nom) {
    std::ifstream monFlux(nom.c_str());
    std::string text;
    std::string line;
    
    while (getline(monFlux, line)) {
        text = text + line;
    }
    return text;
}