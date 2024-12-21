#!/bin/bash
set -x

FONT_DIR="$HOME/.local/share/fonts"
TMP_DIR="$HOME/tmp"

mkdir -p $TMP_DIR

echo "Installing required packages........"

sudo pacman -Sy
sudo pacman -Sy --noconfirm flatpak fastfetch firefox less git docker minikube kubectl ntfs-3g tmux stow tree unzip okular obsidian xclip zsh qbittorrent neovim fzf

echo "Configure yay ......"
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si

echo "Installing flatpaks............."
flatpak install --noninteractive -y flathub org.kde.okular
flatpak install --noninteractive -y flathub md.obsidian.Obsidian
flatpak install --noninteractive -y flathub com.brave.Browser

echo "Configuring git........"
git config --global user.name "Tanveer Ahmed"
git config --global user.email "tanveer@test.com"

echo "Starting services......"
sudo systemctl enable bluetooth
sudo systemctl enable docker containerd

echo "starship setup ........."
mkdir -p $FONT_DIR
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/CodeNewRoman.zip -o $TMP_DIR/codenewroman.zip
unzip $TMP_DIR/codenewroman.zip -d $FONT_DIR
rm $TMP_DIR/codenewroman.zip
curl -sS https://starship.rs/install.sh | sh

echo "Configuring tmux.........."
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
tmux source ~/.tmux.conf

echo "Aur packages"
# yay -S blesh
yay -S visual-studio-code-bin
yay -S oh-my-posh
# ysy -S google-chrome

#echo "Configuring fzf .........."
#git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
#~/.fzf/install
