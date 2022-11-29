# DEMO

## Installation
Follow instruction to run netbox via docker https://github.com/netbox-community/netbox-docker#quickstart


Install requirements
```bash
pip install -r requirements.txt
```

Copy ntc templates:
```bash
git clone git@github.com:networktocode/ntc-templates.git
```

We are going to use ansile docker image. Let's build it:
```bash
docker build . -t ansible
```

Copy and update environment variables:
```bash
cp .env.docker.example .env.docker
cp .env.example .env
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

Apply commands:
```bash
make apply_config
```
