#!/bin/bash

set -x

echo "Installing required packages"
pacman -Sy
pacman -Sy flatpak fastfetch firefox less git code docker minikube ntfs-3g tmux stow fzf

echo "Configuring git"
git config --global user.name "Tanveer Ahmed"
git config --global user.email "tanveerahmed2619@gmail.com"