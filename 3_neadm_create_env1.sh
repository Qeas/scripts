#!/bin/bash
#version 1.2

echo "Start 3_neadm_create_env1.sh"
echo 

source utils.sh

node_hostname=$(read_conf "node01_hostname")
license=$(read_conf "license")

echo "---"
echo
echo "Arguments passed in:"
echo
echo "node_hostname=$node_hostname"
echo "license=$license"
echo
echo "---"
echo

echoe "neadm system version"
echoe "neadm system status"
echoe "neadm system init -s"
echoe "neadm system license set online $license"

echo
echo "End 3_neadm_create_env1.sh"
echo
