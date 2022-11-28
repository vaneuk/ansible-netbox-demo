DIR := ${CURDIR}

setup_initial: $(DIR)
	 docker run -it --rm -v $(DIR):/opt/app --env-file .env.docker ansible ansible-playbook 00_setup_initial.yaml

setup_context: $(DIR)
	docker run -it --rm -v $(DIR):/opt/app --env-file .env.docker ansible ansible-playbook 01_setup_context.yaml

state_collector: $(DIR)
	docker run -it --rm -v $(DIR):/opt/app --env-file .env.docker ansible ansible-playbook 02_state_collector.yaml -i netbox_inventory.yaml

append_to_config: $(DIR)
	docker run -it --rm -v $(DIR):/opt/app --env-file .env.docker ansible ansible-playbook 03_append_to_config.yaml -i netbox_inventory.yaml

check_diff: $(DIR)
	docker run -it --rm -v $(DIR):/opt/app --env-file .env.docker ansible ansible-playbook 03_check_diff.yaml -i netbox_inventory.yaml

apply_config: $(DIR)
	docker run -it --rm -v $(DIR):/opt/app --env-file .env.docker ansible ansible-playbook 03_apply_config.yaml -i netbox_inventory.yaml

config_generator:
	python config_generator.py


generate: $(DIR) config_generator append_to_config

generate_and_validate: $(DIR) config_generator append_to_config check_diff
