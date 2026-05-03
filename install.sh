#!/usr/bin/bash
# Installer for the ROGAllyTDP Decky plugin.
# Downloads the latest release from GitHub and drops it into the Decky
# plugins directory. Safe to re-run for updates.

if [ "$EUID" -eq 0 ]
  then echo "Please do not run as root"
  exit
fi

echo "removing previous install if it exists"

cd $HOME

sudo rm -rf $HOME/homebrew/plugins/ROGAllyTDP

echo "installing ROGAllyTDP plugin for TDP control"
# download + install ROGAllyTDP
curl -L $(curl -s https://api.github.com/repos/ThaFridge/ROGAllyTDP/releases/latest | grep "browser_download_url" | cut -d '"' -f 4) -o $HOME/ROGAllyTDP.zip
sudo 7z x ./ROGAllyTDP.zip -o$HOME/homebrew/plugins

# install complete, remove build dir
rm $HOME/ROGAllyTDP.zip
sudo systemctl restart plugin_loader.service

echo "Installation complete"
