#!/bin/bash

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y build-essential

sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt install -y tmux xclip curl alacritty neovim ntfs-3g git stow zsh gnome-shell-extension-manager nvtop transmission python3-venv python3-pip ripgrep fd-find fastfetch

# tmux plugin
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# oh my posh
curl -s https://ohmyposh.dev/install.sh | bash -s

# vlc
sudo snap install vlc

# git
echo "Configuring git........"
git config --global user.name "Tanveer Ahmed"
git config --global user.email "tanveer@test.com"

