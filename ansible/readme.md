## Ansible ad-hoc commands
1. ping servers in vagrant group in inventory
```
ansible vagrant -i inventory -m ping
```

2. Get details of the servers
```
ansible vagrant -i inventory -m setup -a 'filter=ansible_distribution'
```

## Ansible Playbook

1. dry run
```
ansible-playbook -i inventory playbook.yml --check
```

2. passing become password as --extra-vars
```
export ANSIBLE_BECOME_PWD="<pwd>"
ansible-playbook -i inventory playbook.yml -e "ansible_become_password=${ANSIBLE_BECOME_PWD}"
```

## ansible-vault

ansible-vault encrypt --vault-password-file ~/.ansible_vault_key  info.txt
ansible-vault decrypt --vault-password-file ~/.ansible_vault_key  info.txt
## to edit encrypted file
ansible-vault edit --vault-password-file ~/.ansible_vault_key  info.txt
ansible-vault view --view-password-file ~/.ansible_vault_key info.txt
## to update the password used for encryption
ansible-vault rekey info.txt --vault-password-file

## Ref
ansible-galaxy - geerlingguy
