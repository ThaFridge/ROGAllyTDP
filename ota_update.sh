#!/usr/bin/bash
# OTA update for the ROGAllyTDP Decky plugin.
# Expects /tmp/ROGAllyTDP.tar.gz to already be present (downloaded by the
# plugin itself).

if [ ! -f '/tmp/ROGAllyTDP.tar.gz' ]; then
  echo "Failed to find downloaded plugin"
  exit -1
fi

DECKY_DIR="$HOME/homebrew/plugins"

if [ ! -d $DECKY_DIR ]; then
  echo "Failed to find DECKY_DIR at: "
  echo $DECKY_DIR
  exit -1
fi

rm -rf $DECKY_DIR/ROGAllyTDP

tar -xzf /tmp/ROGAllyTDP.tar.gz -C $DECKY_DIR

# install complete, remove files
rm -rf /tmp/ROGAllyTDP.tar.gz

systemctl restart plugin_loader.service
