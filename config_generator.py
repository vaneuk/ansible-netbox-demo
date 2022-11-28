import os

import pynetbox
from plugins.filters.jinja_filters import vlan
from dotenv import load_dotenv


from jinja2 import Environment, FileSystemLoader
environment = Environment(loader=FileSystemLoader("templates/nxos/"), trim_blocks=True, lstrip_blocks=True)
environment.filters["vlan"] = vlan


load_dotenv()

DEVICES = ['site-1-leaf-abc']

def get_netbox_data():
    nb = pynetbox.api(
        os.getenv('NETBOX_API'),
        token=os.getenv('NETBOX_API_KEY'),
    )

    devices = nb.dcim.devices.filter(name=DEVICES)
    result = {}
    for device in devices:
        result[device.name] = device.config_context
        result[device.name].update({"interfaces": []})

    q = nb.dcim.interfaces.filter(device=DEVICES)
    interface_with_ip_addresses = set()
    for i in q:
        result[i.device.name]["interfaces"].append(i.serialize())
        if i.count_ipaddresses > 0:
            interface_with_ip_addresses.add(i.id)

    for i in nb.ipam.ip_addresses.filter(interface_id=interface_with_ip_addresses):
        print(i.serialize())
        print()
        for interface in result[i.assigned_object.device.name]["interfaces"]:
            if interface["name"] == i.assigned_object.name:
                if "ip_addresses" not in interface:
                    interface["ip_addresses"] = []
                    interface["vrf"] = i.vrf
                interface["ip_addresses"].append(i.serialize())
    return result


def render_templates(device_info: dict) -> None:
    template = environment.get_template("main.j2")
    for device, context in device_info.items():
        filename = f"{device}.txt"
        content = template.render(context)
        with open(f"intended_configurations/{filename}", mode="w", encoding="utf-8") as config_file:
            config_file.write(content)
            print(f"completed config render for {device}")


def main():
    device_info = get_netbox_data()
    render_templates(device_info)


if __name__ == "__main__":
    main()