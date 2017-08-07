#!/bin/bash

cols=$(tput cols)
title=" MENU "
let wgth="($cols - 6) / 2"
i=0
str=""
choice=""

for ((i = 1; i <= $wgth; i++))
do
    str="$str#"
done

while true
do
    clear
    echo "$str$title$str"
    echo ""
    echo " [1] Text editor"
    echo " [2] File navigator"
    echo " [3] Internet navigator"
    echo " [4] Terminal"
    echo " [5] Python IDE"
    echo " [6] Games"
    echo " [7] Volume"
    echo " [8] Exit to shell"
    echo " [9] Shutdown"
    echo ""
    read -p "choice [1-9] : " choice

    if [ $choice = "1" ]
    then
        nano
    elif [ $choice = "2" ]
    then
        mc -b
    elif [ $choice = "3" ]
    then
        links2 lite.qwant.com
    elif [ $choice = "4" ]
    then
        bash term.sh
    elif [ $choice = "5" ]
    then
        bash pyde.sh
    elif [ $choice = "6" ]
    then
        bash xdos.sh
    elif [ $choice = "7" ]
    then
        alsamixer -g
    elif [ $choice = "8" ]
    then
        exit
    elif [ $choice = "9" ]
    then
        sudo shutdown -h now
    fi
done