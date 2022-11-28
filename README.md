# DEMO

## Installation
Follow instruction to run netbox via docker https://github.com/netbox-community/netbox-docker#quickstart


```bash
pip install -r requirements.txt
ansible-galaxy collection install netbox.netbox
ansible-galaxy collection install cisco.nxos
ansible-galaxy collection install cisco.ios
```

```bash
pip install -r requirements.txt
```

Copy ntc templates:
```bash
git clone git@github.com:networktocode/ntc-templates.git
```

Build docker image for ansible
```bash
docker build . -t ansible
```

## Usage
Please check Makefile for command meaninig.

Populate netbox:
```bash
make setup_initial
make setup_context
```

Create NX-OS Device and assign IP address to it.

Add Serial number information and MAC address information to netbox.
```bash
make state_collector
```

Generate device configuration:
```bash
make generate
```

Show pending commands:
```bash
make check_diff
```

Show pending commands:
```bash
make apply_config
```
