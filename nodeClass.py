import tkinter
from tkinter import *

impact_factor_values =  {
        "confidentiality": { "Low": "0.5", "Medium": "1", "High": "3", "Undefined": "1" },
        "integrity": {"Low": "0.5", "Medium": "1", "High": "3", "Undefined": "1"},
        "availability": { "Low": "0.5", "Medium": "1", "High": "3", "Undefined": "1" },
        "safety": { "None": "0", "Low": "3", "High": "10", "Undefined": "0" },
        "material": { "Low": "0.5", "Medium": "1", "High": "3", "Undefined": "1" },
    }


class NetworkNode:
    def __init__(self, id, label, confidentiality_factor, integrity_factor, availability_factor,
                 safety_factor, material_factor, firmware):
        self.id = id
        self.label = label
        self.confidentiality_factor = confidentiality_factor
        self.integrity_factor = integrity_factor
        self.availability_factor = availability_factor
        self.safety_factor = safety_factor
        self.material_factor = material_factor
        self.firmware = firmware
        self.impact_values = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.node_links = []

    def __str__(self):
        return f"Label: {self.label} \n\n Id: {self.id} " \
               f"\n Confidentiality factor: {self.confidentiality_factor}" \
               f"\n Integrity factor:       {self.integrity_factor}" \
               f"\n Availability factor:    {self.availability_factor}" \
               f"\n Safety Factor:          {self.safety_factor} \n " \
               f"Material factor:        {self.material_factor} \n\n " \
               f"Firmware:               {self.firmware} \n " \
               f"\n Connection links: {self.node_links}"

    def print_node_impact_factors(self, affected_factors):
        string_affected_factors = ""
        if(affected_factors[0] == 1):
            string_affected_factors += " Con: " + str({self.confidentiality_factor})
        if(affected_factors[1] == 1):
            string_affected_factors += " Int: " + str({self.integrity_factor})
        if(affected_factors[2] == 1):
            string_affected_factors += " Ava: " + str({self.availability_factor})
        if(affected_factors[3] == 1):
            string_affected_factors += " Saf: " + str({self.safety_factor})
        if(affected_factors[4] == 1):
            string_affected_factors += " Mat: " + str({self.material_factor})
        return f"{self.label}" + string_affected_factors

    def print_node_impact_factors_2(self, affected_factors):
        impact_values = self.impact_values
        string_affected_factors = "|  "
        label = self.label + "          "
        label = label[0:20]

        if(affected_factors[0] == 1):
            string_affected_factors +=  str(impact_values[0]) + "|  "
        if(affected_factors[1] == 1):
            string_affected_factors +=  str(impact_values[1])+ "|  "
        if(affected_factors[2] == 1):
            string_affected_factors +=  str(impact_values[2])+ "|  "
        if(affected_factors[3] == 1):
            string_affected_factors +=  str(impact_values[3])+ "|  "
        if(affected_factors[4] == 1):
            string_affected_factors +=  str(impact_values[4])+ "|  "
        return (label + string_affected_factors)

    def get_impact_values(self):
        new_impact_values = [0.0,0.0,0.0,0.0,0.0]
        new_impact_values[0] = float(impact_factor_values['confidentiality'][self.confidentiality_factor])
        new_impact_values[1] = float(impact_factor_values['integrity'][self.integrity_factor])
        new_impact_values[2] = float(impact_factor_values['availability'][self.availability_factor])
        new_impact_values[3] = float(impact_factor_values['safety'][self.safety_factor])
        new_impact_values[4] = float(impact_factor_values['material'][self.material_factor])
        self.impact_values = new_impact_values


def network_dict_to_network_nodes(network_dict):
    network_nodes = []
    list_nodes = network_dict['nodes']
    list_links = network_dict['links']

    confidentiality = "Undefined"
    integrity = "Undefined"
    availability = "Undefined"
    safety = "Undefined"
    material = "Undefined"
    firmware = "Undefined"

    for node in list_nodes:
        try:
            firmware = node['properties']['Firmware']

        except KeyError:
            print()
        try:
            confidentiality = node['properties']['Confidentiality importance']

        except KeyError:
            print()

        try:
            availability = node['properties']['Availability importance']
        except KeyError:
            print()

        try:
            integrity  = node['properties']['Integrity importance']
        except KeyError:
            print()

        try:
            safety = node['properties']['Safety importance']
        except KeyError:
            print()

        try:
            material = node['properties']['Material importance']
        except KeyError:
            print()

        net_node = NetworkNode(node['id'], node['label'], confidentiality, integrity, availability, safety, material, firmware)
        add_node_connections(list_links, net_node)
        net_node.get_impact_values()
        network_nodes.append(net_node)
    return network_nodes


def add_node_connections(links_dict, net_node):
    network_nodes = []

    for link in links_dict:
        if link['source'] == net_node.id:
            network_nodes.append(link['target'])

    net_node.node_links = network_nodes


# Table class
class popup_impact_factors_details:
    # Initialize a constructor

    def __init__(self, root):
        window_impact_factors_details = tkinter.Toplevel()
        window_impact_factors_details.geometry("800x200")
        window_impact_factors_details['background'] = '#65788A'

        label_impact_factors = Label(window_impact_factors_details, text="impact factor details")
        label_impact_factors.pack(padx=10, pady=10, expand=True)
        text_impact_factors = Text(window_impact_factors_details, width=90)
        text_impact_factors.pack(padx=10, pady=10, expand=True)
        for impact_factor in impact_factor_values:
            text_impact_factors.insert(END,  str(impact_factor) + ": " + str(impact_factor_values[impact_factor]) + "\n")