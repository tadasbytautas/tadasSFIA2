#!/bin/bash

# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
## install ansible with pip
pip3 install --user ansible
# check that ansible has been installed
ansible --version

#run ansible-playbook to install dependencies
ansible_playbook -i inventory.cfg playbook.yml

