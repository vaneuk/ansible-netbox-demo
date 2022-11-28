def vlan(value: list) -> str:
    if len(value) == 0:
        return "none"

    vlans = sorted(value)
    vlan_ranges = [[vlans[0]]]
    previous = vlans[0]
    for v in vlans[1:]:
        if v == previous + 1:
            if len(vlan_ranges[-1]) == 1:
                vlan_ranges[-1].append(v)
            else:
                vlan_ranges[-1][1] = v
        else:
            vlan_ranges.append([v])
        previous = v
    formatted_result = ",".join(["-".join([str(v) for v in vlan_range]) for vlan_range in vlan_ranges])
    return formatted_result
