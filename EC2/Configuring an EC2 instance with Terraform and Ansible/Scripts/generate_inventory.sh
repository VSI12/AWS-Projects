#!/bin/bash

cd Terraform 
IP=$(terraform output -raw public_ip)

cd ../
cat > Ansible/inventory <<EOF
[web]
$IP 
EOF

echo "[+] Inventory generated with IP $IP"
