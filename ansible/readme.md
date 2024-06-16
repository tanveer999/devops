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


## Ref
ansible-galaxy - geerlingguy
