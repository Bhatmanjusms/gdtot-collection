#!/bin/bash

#This is a bash script to install all known ttf-fonts for Archlinu
#
#
# Run this script with sudo : sudo ./Installttf.sh

pacman -Ss ttf- | sed -e's/\s.*//' >> x.txt

yay -S `cat x.txt`
