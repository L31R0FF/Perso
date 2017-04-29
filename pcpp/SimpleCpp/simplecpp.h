//
//  simplecpp.h
//  SimpleCpp
//
//  Created by Cyril Foriel on 26/04/2017.
//  Copyright © 2017 FORC. All rights reserved.
//
#ifndef simplecpp_h
#define simplecpp_h

#include <string>
#include <sstream>

/**
* \brief Fonction qui affiche un texte à l'écran
* \param text Le texte affiché
*/
void print(std::string text);

/**
* \brief Fonction qui affiche un texte à l'écran avec un retour à la ligne
* \param text Le texte affiché
*/
void println(std::string text);

/**
* \brief Fonction qui demande une saisie à l'utilisateur
* \param text Le texte affiché avant la saisie
* \return reponse
*/
std::string ask(std::string text);

/*
* \brief Fonction qui écrit une chaîne dans un fichier
* \param nom Le nom du fichier
* \param mode Le mode d'ouverture ("a" append ou "w" write)
* \param text La chaîne à écrire
*/
void fprint(std::string nom, std::string mode, std::string text);

/*
* \brief Fonction qui écrit une chaîne dans un fichier avec retour à la ligne
* \param nom Le nom du fichier
* \param mode Le mode d'ouverture ("a" append ou "w" write)
* \param text La chaîne à écrire
*/
void fprintln(std::string nom, std::string mode, std::string text);

/*
* \brief Fonction qui lit un fichier entièrement
* \param nom Le nom du fichier
* \return text
*/
std::string fread(std::string nom);

/*
* \brief Fonction qui convertit n'importe quel type en string
* \param element L'element à convertir 
* \return str
*/
template <typename T>
std::string atos(T element) {
    std::stringstream ss;
    ss << element;
    std::string str = ss.str();
    return str;
}

#endif /* simplecpp_h */