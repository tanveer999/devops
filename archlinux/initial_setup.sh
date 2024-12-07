#!/bin/bash

set -x

echo "Installing required packages........"

sudo pacman -Sy
sudo pacman -Sy flatpak fastfetch firefox less git code docker minikube ntfs-3g tmux stow fzf

echo "Installing flatpaks............."
flatpak install --noninteractive -y flathub org.kde.okular
flatpak install --noninteractive -y flathub md.obsidian.Obsidian
flatpak install --noninteractive -y flathub com.brave.Browser

echo "Configuring git........"
git config --global user.name "Tanveer Ahmed"
git config --global user.email "tanveer@test.com"

echo "Starting services......"
sudo systemctl enable bluetooth