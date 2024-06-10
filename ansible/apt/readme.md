# Command to run the ansible script with sudo:

    sudo ansible-playbook -i inventory main.yaml --verbose

# Command to run the ansible script with become parameter:

    ansible-playbook main.yaml -b --ask-become-pass