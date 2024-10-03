#!/bin/bash
echo 'Initializing...'
echo 'Updating drivers'
sudo apt update > /dev/null 2>&1
echo 'Drivers updated'
echo 'Installing firefox'
sudo apt install -y firefox > /dev/null 2>&1
echo 'Firefox installed'
echo 'version'
firefox --version
echo 'Installing dependencies'
pip install -r requirements.txt > /dev/null
echo 'Successfully installed'