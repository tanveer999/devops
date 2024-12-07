#!/bin/bash
set -x

FONT_DIR="$HOME/.local/share/fonts"
TMP_DIR="$HOME/tmp"

mkdir -p TMP_DIR

echo "Installing required packages........"

sudo pacman -Sy
sudo pacman -Sy --noconfirm flatpak fastfetch firefox less git code docker minikube ntfs-3g tmux stow fzf tree unzip

echo "Installing flatpaks............."
flatpak install --noninteractive -y flathub org.kde.okular
flatpak install --noninteractive -y flathub md.obsidian.Obsidian
flatpak install --noninteractive -y flathub com.brave.Browser

echo "Configuring git........"
git config --global user.name "Tanveer Ahmed"
git config --global user.email "tanveer@test.com"

echo "Starting services......"
sudo systemctl enable bluetooth

echo "starship setup ........."
mkdir -p $FONT_DIR
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/CodeNewRoman.zip -o $TMP_DIR/codenewroman.zip
unzip $TMP_DIR/codenewroman.zip -d $FONT_DIR
rm $TMP_DIR/codenewroman.zip
curl -sS https://starship.rs/install.sh | sh