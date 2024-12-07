#!/bin/bash

set -x

echo "Installing required packages"
pacman -Sy
pacman -Sy flatpak fastfetch firefox less git code docker minikube ntfs-3g tmux

git config --global user.name "Tanveer Ahmed"