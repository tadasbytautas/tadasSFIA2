#!/bin/bash
source /var/lib/jenkins/.env
ansible-playbook -i invetory.cfg playbook.yml