#!/bin/bash

sudo apt install ansible -y
ansible_playbook -i inventory.cfg playbook.yml