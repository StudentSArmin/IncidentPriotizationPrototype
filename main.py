import tkinter
import tkinter as tk
from tkinter import filedialog as fd, ttk, DISABLED
import json
from tkinter import Frame
from tkinter.constants import TOP

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import loadExampleNetJSON

import nodeClass
import IncidentClass
import networkx as nx
import matplotlib.pyplot as plt

# new window with a title
main_window = tk.Tk()
main_window.geometry('1350x800')
main_window['background'] = '#65788A'
main_window.title('Incident Priotization App')

main_window.resizable(False, False)
global network_dict
global networkNodeList
global incidentList
incidentList = []
global impact_factor_parameter

tabsystem = ttk.Notebook(main_window)
tab_network = Frame(tabsystem, bg='#65788A')
tab_incident = Frame(tabsystem, bg='#5E8E6C')

tabsystem.add(tab_network, text='Network')
tabsystem.add(tab_incident, text='Incidents')
tabsystem.pack(expand=1, fill="both")

propagation_modi = "default"

##################################################################
# Incident Tab
# Tkinter elements
listbox_incident = tk.Listbox(tab_incident, selectmode='single', width=20, height=15)  # selectmode multiple
listbox_incident.place(x=20, y=400)
Label_list_box_incidents = tk.Label(tab_incident, text="Incident list:",width=20, bg='#3F4C50', fg='white', height=1)
Label_list_box_incidents.place(x=20, y=380)

Label_Incident_configuration_banner = tk.Label(tab_incident, text="Incident Prioritization and configuration",
                                               width=180, foreground="white", bg='#3F4C50', height=1)
Label_Incident_configuration_banner.place(x=1, y=1)

Label_notice_configure_context = tk.Label(tab_incident, text="Configure \nOrganization \n Parameters:",
                                          width=12, bg='#3F4C50', fg='white', height=4)
Label_notice_configure_context.place(x=230, y=30)
Label_background = tk.Label(tab_incident, text="", width=113, bg='#3F4C50', fg='white', height=4)
Label_background.place(x=350, y=30)

Label_context_Confidentiality = tk.Label(tab_incident, text="Confidentiality: ", width=15, bg='black',
                                         fg='white', height=1)
Label_context_Confidentiality.place(x=370, y=40)
Label_context_Integrity = tk.Label(tab_incident, text="Integrity: ", width=15, bg='black', fg='white', height=1)
Label_context_Integrity.place(x=510, y=40)
Label_context_Availability = tk.Label(tab_incident, text="Availability: ", width=15, bg='black', fg='white',
                                      height=1)
Label_context_Availability.place(x=650, y=40)
Label_context_safety = tk.Label(tab_incident, text="Safety: ", width=15, bg='black', fg='white', height=1)
Label_context_safety.place(x=790, y=40)
Label_context_Material = tk.Label(tab_incident, text="Material: ", width=15, bg='black', fg='white', height=1)
Label_context_Material.place(x=930, y=40)

str_cb_confidentiality = tk.StringVar()
cb_parameter_confidentiality = ttk.Combobox(tab_incident, width=13, textvariable=str_cb_confidentiality)
cb_parameter_confidentiality['values'] = ('Undefined', 'Low', 'Medium', 'High')
cb_parameter_confidentiality.current(0)
cb_parameter_confidentiality.place(x=370, y=70)

str_cb_integrity = tk.StringVar()
cb_parameter_integrity = ttk.Combobox(tab_incident, width=13, textvariable=str_cb_integrity)
cb_parameter_integrity['values'] = ('Undefined', 'Low', 'Medium', 'High')
cb_parameter_integrity.current(0)
cb_parameter_integrity.place(x=510, y=70)

str_cb_availability = tk.StringVar()
cb_parameter_availability = ttk.Combobox(tab_incident, width=13, textvariable=str_cb_availability)
cb_parameter_availability['values'] = ('Undefined', 'Low', 'Medium', 'High')
cb_parameter_availability.current(0)
cb_parameter_availability.place(x=650, y=70)

str_cb_safety = tk.StringVar()
cb_parameter_safety = ttk.Combobox(tab_incident, width=13, textvariable=str_cb_safety)
cb_parameter_safety['values'] = ('Undefined', 'Low', 'Medium', 'High')
cb_parameter_safety.current(0)
cb_parameter_safety.place(x=790, y=70)

str_cb_material = tk.StringVar()
cb_parameter_material = ttk.Combobox(tab_incident, width=13, textvariable=str_cb_material)
cb_parameter_material['values'] = ('Undefined', 'Low', 'Medium', 'High')
cb_parameter_material.current(0)
cb_parameter_material.place(x=930, y=70)



#########################################################################
# Incident tab functions

global impact_factor_parameter
impact_factor_parameter = {"Low": "0.7", "Medium": "1", "High": "1.3", "Undefined": "1"}


def get_impact_parameter():
    impact_parameter_values = [1.0, 1.0, 1.0, 1.0, 1.0]
    impact_parameter_values[0] = float(impact_factor_parameter[cb_parameter_confidentiality.get()])
    impact_parameter_values[1] = float(impact_factor_parameter[cb_parameter_integrity.get()])
    impact_parameter_values[2] = float(impact_factor_parameter[cb_parameter_availability.get()])
    impact_parameter_values[3] = float(impact_factor_parameter[cb_parameter_safety.get()])
    impact_parameter_values[4] = float(impact_factor_parameter[cb_parameter_material.get()])
    return impact_parameter_values


def get_max_val_incident(incident_type):
    all_affected_nodes = []
    for node in networkNodeList:
        all_affected_nodes.append(node.id)
    max_incident = IncidentClass.IncidentClass("---MAX---", incident_type, all_affected_nodes, None)
    return max_incident


def update_incident_list():
    network_nodes_count = 0
    try:
        if not networkNodeList is None:
            max_incident = get_max_val_incident("Undefined")

            for incident in incidentList:
                if incident.id == "max":
                    incidentList.remove(incident)
            if not max_incident in incidentList:
                incidentList.append(max_incident)
            network_nodes_count = len(networkNodeList)
    except:
        print("nodelist not yet defined")

    listbox_incident.delete(0, tkinter.END)
    score_list = []


    Label_incident_score_overview = tk.Label(tab_incident, width=144, height=1, text="Incident Score Overview:", bg='#3F4C50', fg='white')
    Label_incident_score_overview.place(x=150, y=130)
    text_list_all_incident = tk.Text(tab_incident, height=10, width=120, bg='#1D2325', fg='white')
    text_list_all_incident.place(x=150, y=150)

    text_list_all_incident.insert(tkinter.END,
                                  "Name:             |   Type:    | Impact Score | Propagation Score: | Recoverability Factor: | Score: |Normalized(0-100%)\n")

    max_value = 1
    for incident in incidentList:
        calculate_score(incident)
        score_list.append(incident.score)

        if incident.id =="---MAX---":
            max_value = incident.score
    score_list.sort(reverse=True)


    inc_check_list = []
    for score in score_list:
        for incident in incidentList:
            if incident.score == score and incident not in inc_check_list:
                listbox_incident.insert(tkinter.END, incident.id)
                text_list_all_incident.insert(tkinter.END, incident.list(max_value))
                inc_check_list.append(incident)
    show_box_plot()


def calculate_score(incident):
    affected_nodes_by_incident = []  # contains only ids such as "172.16.41.2"
    for node_id in incident.affected_node_ids:
        for node in networkNodeList:
            if node_id == node.id:
                affected_nodes_by_incident.append(node.id)
    propagation_score = round(
        calculate_propagation_score(affected_nodes_by_incident, incident), 2)
    incident.propagation_score = propagation_score
    incident.impact_score = calculate_impact_score(incident)

    incident_affected_impact_factors = incident
    impact_score_sum = 0
    for i in range(0, len(incident.impact_score)):
        impact_score_sum += incident.impact_score[i]
    incident.impact_score_sum = round(impact_score_sum,2 )
    #impact_score_sum = round(impact_score_sum / len(networkNodeList),2 ) * 100
    incident.score = round((incident.impact_score_sum * incident.recoverability_factor) + (propagation_score * 0.5) , 2)
    # incident.score = incident.propagation_score + incident.impact_score
    return incident


# get list of node objects by node label strings
def node_list_by_ids(nodes_ids):
    nodes = []
    for node_id in nodes_ids:
        for node in networkNodeList:
            if node.id == node_id:
                nodes.append(node)
    return nodes


def aggr_impact_values_from_nodes(node_list, impact_factors):
    impact_parameter = get_impact_parameter()
    impact_score_aggregated_values = [0.0, 0.0, 0.0, 0.0, 0.0]  # aggregated result for every individual impact factor

    for node in node_list:
        for i in range(0, 5):
            if impact_factors[i] == 1:
                impact_score_aggregated_values[i] += (node.impact_values[i] * impact_parameter[i])
            impact_score_aggregated_values[i] = round(impact_score_aggregated_values[i], 2)
    return impact_score_aggregated_values


def node_has_vulnerability(node_id, incident):
    check = False
    if incident.vulnerabilities is not None:
        for vulnerability in incident.vulnerabilities:
            for node in networkNodeList:
                if node.firmware == vulnerability and node_id == node.id:
                    check = True

    return check


def aggr_propagation_values_from_nodes(layer_nodes, incident):
    impact_factors = incident.get_affected_impact_factors()
    impact_parameter = get_impact_parameter()
    impact_score_aggregated_values = [0.0, 0.0, 0.0, 0.0, 0.0]  # aggregated result for every individual impact factor

    for node in layer_nodes:
        # If node has known vulnerability, then the weight should increase by the factor 5
        vulnerability_weight = 1.0
        if node_has_vulnerability(node.id, incident) is True:
            vulnerability_weight = 5.0
        for i in range(0, 5):
            if impact_factors[i] == 1:
                impact_score_aggregated_values[i] += (float(node.impact_values[i]) * float(impact_parameter[i]) * vulnerability_weight)
            impact_score_aggregated_values[i] = round(impact_score_aggregated_values[i], 2)
    return impact_score_aggregated_values


def calculate_impact_score(incident):
    affected_nodes = node_list_by_ids(incident.affected_node_ids)
    impact_score_aggregated_values = aggr_impact_values_from_nodes(affected_nodes,
                                                                   incident.get_affected_impact_factors())
    return impact_score_aggregated_values


def load_example_incidents():
    global incidentList
    incidentList = IncidentClass.load_predefined_incidents()
    update_incident_list()


def show_box_plot():
    # First create a figure
    fig = Figure(figsize=(2.5, 2.5), dpi=70)
    # Create a plot on that figure
    plot = fig.add_subplot()

    # Plot the values on the figure
    values = []

    for incident in incidentList:
        values.append(incident.score)
    # box_plot_data = (values)
    plot.boxplot(values, autorange=True)

    # Create a canvas widget from the figure
    canvas = FigureCanvasTkAgg(fig, master=tab_incident)
    canvas.draw()
    # And then `.pack` it
    canvas.get_tk_widget().place(x=1120, y=150)


def get_nodeList_with_vulnerabilites(incident):
    node_with_vulnerability_list = []
    if incident.vulnerabilities is not None:
        for vulnerability in incident.vulnerabilities:
            for node in networkNodeList:
                if node.firmware == vulnerability:
                    node_with_vulnerability_list.append(node)

    return node_with_vulnerability_list


def calculate_propagation_score(affected_node_ids, incident):
    # List of node arrays structured by communication distance; layer_list[0] = affected nodes!
    layer_list = analyze_topology(affected_node_ids)
    layer_result_list = []
    score = 0.0
    layer_distance = 0.0

    # for every layer all impact factors from the nodes are aggregated
    for layer_number in range(1, len(layer_list)):
        # get node objects by node_ids
        layer_nodes = node_list_by_ids(layer_list[layer_number])
        # aggregate values for node array
        layer_result_list.append(aggr_propagation_values_from_nodes(layer_nodes, incident))

    for i in range(0, len(layer_result_list)):
        denominator = 2 + i # first distance layer is weighted as 2²
        if (i < 3):
            for layer_result in layer_result_list[i]:
                score += (layer_result /  (denominator*denominator))
    return score


# Layers represent the distance from all affected nodes to all other unaffected nodes in the network.
# For each affected node, all directly connected nodes are stored in an array corresponding to layer 1,
# then the same is done for all nodes of the first layer, which are then defined as layer 2, and so on.
def analyze_topology(incident_id_list):
    list_connection_layers = [incident_id_list]  # affected nodes are represented in Layer 0
    list_connection_layers = traverse_layer(list_connection_layers, incident_id_list)

    counter = 0
    for i in list_connection_layers:
        counter += 1
    return list_connection_layers


# Recursive function that searches for all nearest nodes of a collection of
# nodes and stores the results in an array which is then passed on to a new function call
# until no more nodes are available.
def traverse_layer(list_layers, list_last_layer):
    new_layer_list = []
    for src_id in list_last_layer:
        src_node = None
        for node in networkNodeList:
            if node.id == src_id:
                src_node = node
        for target_id in src_node.node_links:
            if not check_if_in_list(list_layers, target_id) and target_id not in new_layer_list:
                new_layer_list.append(target_id)
    if len(new_layer_list) > 0:
        list_layers.append(new_layer_list)
        return traverse_layer(list_layers, new_layer_list)
    else:
        return list_layers  # break: no more nodes found


def show_propagation_details(incident):
    Label_propagation_details = tk.Label(tab_incident, text="Topology information of incident:", width=80, bg='#3F4C50', fg='white',
                                        height=1)
    Label_propagation_details.place(x=690, y=380)
    text_incident_propagation_details = tk.Text(tab_incident, height=12, width=80, bg='#1D2325', fg='white')
    text_incident_propagation_details['state'] = 'normal'
    text_incident_propagation_details.place(x=690, y=400)


    affected_nodes_by_incident = []  # contains only ids such as "172.16.41.2"
    for node_id in incident.affected_node_ids:
        for node in networkNodeList:
            if node_id == node.id:
                affected_nodes_by_incident.append(node.id)
    layer_list = analyze_topology(affected_nodes_by_incident)


    count = 1
    text_space = ""
    for i in range(1, len(layer_list)):
        text_space += "  "
        header_text = "Prop. distance: " + str(count) + "                  "
        header_text = header_text[0: 20] + str(incident.get_affected_impact_factors_labels())
        text_incident_propagation_details.insert(tk.END, text_space + header_text +"\n")
        for node_id in layer_list[i]:
            for node in networkNodeList:
                if node.id == node_id:
                    if node_has_vulnerability(node_id, incident):
                        text_incident_propagation_details.insert(tk.END, text_space + node.print_node_impact_factors_2(
                            incident.get_affected_impact_factors()) + " vuln\n")
                    else:
                        text_incident_propagation_details.insert(tk.END, text_space + node.print_node_impact_factors_2(incident.get_affected_impact_factors())+ "\n")

        text_incident_propagation_details.insert(tk.END,"\n")
        count += 1
    text_incident_propagation_details['state'] = 'disabled'


def show_vulnerabilites_nodes(incident):
    Label_incident_impact_details_vulnerabilites = tk.Label(tab_incident, text="Nodes with vulnerabilites related to incident:", width=80, bg='#3F4C50',
                                         fg='white',
                                         height=1)
    Label_incident_impact_details_vulnerabilites.place(x=690, y=630)
    text_incident_vulnerabilites = tk.Text(tab_incident, height=6, width=80, bg='#1D2325', fg='white')
    text_incident_vulnerabilites['state'] = 'normal'
    text_incident_vulnerabilites.place(x=690, y=650)

    # text_incident_vulnerabilites.insert(tk.END, "")
    if incident.vulnerabilities is not None:
        for vulnerability in incident.vulnerabilities:
            for node in networkNodeList:
                if node.firmware == vulnerability:
                    text_incident_vulnerabilites.insert(tk.END, (str(node.label)+ "                ")[0:25] + " Impact values: " + str(
                        node.impact_values) + "\n")


def show_affected_nodes(incident):
    Label_incident_impact_details = tk.Label(tab_incident, text="Impact details of incident:", width=60, bg='#3F4C50',
                                         fg='white',
                                         height=1)
    Label_incident_impact_details.place(x=210, y=380)
    text_incident_impact_details = tk.Text(tab_incident, height=21, width=58, bg='#1D2325', fg='white')
    text_incident_impact_details.place(x=210, y=400)
    text_incident_impact_details.insert(tk.END, "                    | affected impact factors \n")
    text_incident_impact_details.insert(tk.END,
                                        "Affected nodes      " + incident.get_affected_impact_factors_labels() + "\n\n")


    affected_nodes = node_list_by_ids(incident.affected_node_ids)
    for i in range(0, len(affected_nodes)):
        text_incident_impact_details.insert(tk.END, affected_nodes[i].print_node_impact_factors_2(
            incident.get_affected_impact_factors()) + " \n")

    impact_factor_parameter = get_impact_parameter()
    impact_factors = incident.get_affected_impact_factors()
    text_incident_impact_details.insert(tk.END, "\n_________________________________________________________")
    text_incident_impact_details.insert(tk.END, "\nImpact weight:      | ")
    for i in range(0, 5):
        if(impact_factors[i] == 1):
            text_incident_impact_details.insert(tk.END, "x" + str(impact_factor_parameter[i]) +"| ")
    text_incident_impact_details.insert(tk.END, "\n")
    text_incident_impact_details.insert(tk.END,
                                        "Result:             " + incident.print_incident_impact_sum() +" = " + str(incident.impact_score_sum)+ "\n\n")



def incident_selected(filler):
    selected_incident_element = listbox_incident.selection_get()
    incident_obj = None
    for incident in incidentList:
        if incident.id == selected_incident_element:
            incident_obj = incident

    show_affected_nodes(incident_obj)
    show_propagation_details(incident_obj)
    show_vulnerabilites_nodes(incident_obj)


def graph_generator_affected_nodes():
    selected_incident_element = listbox_incident.selection_get()
    incident_obj = None
    for incident in incidentList:
        if incident.id == selected_incident_element:
            incident_obj = incident

    affected_nodes = incident_obj.affected_node_ids
    affected_nodes_list = node_list_by_ids(affected_nodes)

    affected_nodes_labels = []
    for nodes in affected_nodes_list:
        affected_nodes_labels.append(nodes.label)
    nodes_not_yet_exploited = []
    if incident_obj.vulnerabilities is not None:
        for vulnerability in incident_obj.vulnerabilities:
            for node in networkNodeList:
                if node.firmware == vulnerability and node.label not in affected_nodes_labels:
                    nodes_not_yet_exploited.append(node.label)

    g = nx.Graph()
    for node in networkNodeList:
        for node_connection in node.node_links:
            g.add_edge(node.label, get_node_from_list_by_id(node_connection).label)

    color_map = []
    for node in g:
        if node in affected_nodes_labels:
            color_map.append('red')
        elif node in nodes_not_yet_exploited:
            color_map.append('purple')
        else:
            color_map.append('lightgreen')

            # values = [affected_nodes_labels.get(node, 0.25) for node in g.nodes()]
    nx.draw(g, font_size=10, node_color=color_map, node_size=400, with_labels=True)
    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("off")
    plt.show()


def get_node_from_list_by_str(node_label_str):
    for node in networkNodeList:
        if node.label == node_label_str:
            return node


def add_new_incident():
    root = tkinter.Toplevel()
    root.geometry("500x700")
    root['background'] = '#65788A'
    label = tk.Label(root, text="Enter the property for the new incident", foreground="white", bg='#3F4C50')
    label.grid(row=0, column=0, sticky='w')

    label_new_incident_id = tk.Label(root, text="Type in Incident Id", foreground="white", bg='#3F4C50')
    label_new_incident_id.grid(row=1, column=0, sticky='w')
    text_new_incident_id = tk.Text(root, height=1, width=20, bg='#1D2325', fg='white')
    text_new_incident_id.grid(row=1, column=1)

    full_type_list = IncidentClass.incident_types
    incident_type_list = []
    for type in full_type_list:
        incident_type_list.append(type)
    print(incident_type_list)
    label_incident_type = tk.Label(root, text="Incident Type", foreground="white", bg='#3F4C50')
    label_incident_type.grid(row=2, column=0, sticky='w')
    incident_type_str_var = tk.StringVar()
    cb_incident_type = ttk.Combobox(root, textvariable=incident_type_str_var)
    cb_incident_type['values'] = incident_type_list
    cb_incident_type.grid(row=2, column=1, sticky='w')

    label_affected_nodes = tk.Label(root, text="select affected nodes", foreground="white", bg='#3F4C50')
    label_affected_nodes.grid(row=3, column=0, sticky='w')
    listbox_affected_nodes = tk.Listbox(root, selectmode='multiple', width=20, height=10)
    listbox_affected_nodes.grid(row=3, column=1)
    for node in networkNodeList:
        listbox_affected_nodes.insert(tkinter.END, node.label)

    def add_incident():
        id = text_new_incident_id.get(1.0, "end-1c")
        type = cb_incident_type.get()
        affected_nodes = []
        for i in listbox_affected_nodes.curselection():
            affected_nodes.append(get_node_from_list_by_str(listbox_affected_nodes.get(i)).id)
        new_incident = IncidentClass.IncidentClass(id, type, affected_nodes, None)
        new_incident.update_recoverability_factor_for_incident()
        incidentList.append(new_incident)
        update_incident_list()
        root.destroy()

    button_confirm_new_incident = tk.Button(root, text='Add new incident', width=20, command=add_incident)
    button_confirm_new_incident.grid(row=4, column=1, sticky='w')
    root.mainloop()


def add_incident_types():
    root = tkinter.Toplevel()
    root.geometry("500x700")
    root['background'] = '#65788A'
    label = tk.Label(root, text="Add new Incident Types ", foreground="white", bg='#3F4C50')
    label.grid(row=0, column=0, sticky='w')


    listbox_incident_types = tk.Listbox(root, selectmode='single', width=30, height=17)  # selectmode multiple
    listbox_incident_types.grid(row=3, column=0)
    IncidentClass.define_listbox_incident_types(listbox_incident_types)
    label_incident_type_name = tk.Label(root, text="Define Incident Type name", foreground="white", bg='#3F4C50')
    label_incident_type_name.grid(row=1, column=0, sticky='w')
    text_incident_name= tk.Text(root, height=1, width=20, bg='#1D2325', fg='white')
    text_incident_name.grid(row=1, column=1)


#
#
#
# var_activate_propagation_risk = tk.IntVar()
# checkbox_activate_propagation_probability = tk.Checkbutton(tab_incident, text='Activate Propagation by Probability',variable=var_activate_propagation_risk, onvalue=1, offvalue=0, command=update_incident_list())
# checkbox_activate_propagation_probability.place(x=250, y=350)



listbox_incident.bind('<<ListboxSelect>>', incident_selected)
################################################################
# Incident tab buttons
button_edit_incident_types = tk.Button(tab_incident, text='Configure Incident Types', bg='#2e383b', fg='white', width=20,
                                 command=add_incident_types)
button_edit_incident_types.place(x=10, y=30)

button_add_incident = tk.Button(tab_incident, text='add incident', bg='#2e383b', fg='white', height=1, width=12,
                                command=add_new_incident)
button_add_incident.place(x=10, y=155)


button_load_incident = tk.Button(tab_incident, text='Load example \n incidents', bg='#2e383b', fg='white', height=2, width=12,
                                 command=load_example_incidents)
button_load_incident.place(x=10, y=195)

button_show_affected_nodes_graph = tk.Button(tab_incident, text='show network Graph \n with affected nodes', bg='#2e383b', fg='white',
                                             width=20, height=2, command=graph_generator_affected_nodes)
button_show_affected_nodes_graph.place(x=10, y=650)
button_update_parameter = tk.Button(tab_incident, text='update Parameter', bg='#2e383b', fg='white',
                                    width=20, command=update_incident_list)
button_update_parameter.place(x=1070, y=70)

######################################################################################
# network tab
# tkinter elements
Label_network_configuration_banner = tk.Label(tab_network, text="Configuration of Network nodes and their impact factors",
                                               width=165, foreground="white", bg='#3F4C50', height=2)
Label_network_configuration_banner.place(x=1, y=1)

Label_network_configuration_banner = tk.Label(tab_network, text="Defined Network nodes overview:",
                                               width=165, foreground="white", bg='#3F4C50', height=2)
Label_network_configuration_banner.place(x=1, y=265)

Label_node_list = tk.Label(tab_network, width=30, height=2, text="List of all defined nodes:", bg='#3F4C50', fg='white')
Label_node_list.place(x=50, y=330)

guide_text = "Tool Guid: \n" \
             "1. Define your network by importing a NetJSON File\n" \
             "2. Edit the impact factors of the listed nodes below if necessary\n" \
             "3. Switch to the incident tab to import or add Incidents "
text_guide_text = tk.Text(tab_network, height=8, width=68, bg='#3F4C50', fg='white')
text_guide_text.place(x=50, y=55)
text_guide_text.insert(tk.END, guide_text)
text_guide_text['state'] = DISABLED

Label_node_list = tk.Label(tab_network, width=70, height=2, text="Node properties:", bg='#3F4C50', fg='white')
Label_node_list.place(x=330, y=330)

listbox_nodes = tk.Listbox(tab_network, selectmode='single', width=30, height=17)  # selectmode multiple
listbox_nodes.place(x=50, y=370)
text_node_details = tk.Text(tab_network, height=14, width=70, bg='#1D2325', fg='white', state=DISABLED)
text_node_details.place(x=330, y=370)

Label_node_counter = tk.Label(tab_network, height=2, width=30, text="Node Count: 0", bg='#3F4C50', fg='white')
Label_node_counter.place(x=50, y=690)



############################################################


def check_if_in_list(node_lists, node):
    for list_item in node_lists:
        if node in list_item:
            return True
    return False


def network_details_window():
    window_network_details = tkinter.Toplevel()
    window_network_details.geometry("500x400")
    window_network_details['background'] = '#65788A'

    text_networkdetail = tk.Label(window_network_details, text="network details", bg='#3F4C50', fg='white')
    text_networkdetail.pack(padx=10, pady=10, expand=True)
    text_netjson = tk.Text(window_network_details)
    text_netjson.pack(padx=10, pady=10)
    display_network(text_netjson, networkNodeList)


def display_network(text_netjson, networkNodeList):
    str_alert = 'Network nodes \n'
    for node in networkNodeList:
        str_alert += '\n'
        str_alert += f"Label: {node.label} \n Id: {node.id} \n {node.node_links} \n"
    text_netjson.delete("1.0", "end")
    text_netjson.insert(tk.END, str_alert)


def list_all_nodes(networkNodeList):
    listbox_nodes.delete(0, tkinter.END)
    for node in networkNodeList:
        listbox_nodes.insert(tkinter.END, node.label)


def node_selected(iwas):
    text_node_details['state'] = 'normal'

    text_node_details.delete('1.0', tkinter.END)
    node_selected = listbox_nodes.selection_get()
    for node in networkNodeList:
        if node.label == node_selected:
            text_node_details.insert(tk.END, str(node))
    text_node_details['state'] = 'disabled'


def graph_generator():
    g = nx.Graph()
    for node in networkNodeList:
        for node_connection in node.node_links:
            g.add_edge(node.label, get_node_from_list_by_id(node_connection).label)

            # values = [affected_nodes_labels.get(node, 0.25) for node in g.nodes()]
    nx.draw(g, font_size=10, node_color="lightgreen", node_size=400, with_labels=True)
    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("off")
    plt.show()


def get_node_from_list_by_id(node_label_str):
    for node in networkNodeList:
        if node.id == node_label_str:
            return node



def edit_node_factors():
    rootnew = tkinter.Toplevel()
    rootnew.geometry("450x180")
    rootnew['background'] = '#65788A'

    label_impact_factors = tk.Label(rootnew, width=30, text="Define the node impact factors: \n", foreground="white", bg='#3F4C50')
    label_impact_factors.grid(row=0, column=0, sticky='w')

    label_confidentiality = tk.Label(rootnew, height=1, width=30, text="Confidentiality factor:", foreground="white", bg='#3F4C50')
    label_confidentiality.grid(row=2, column=0, sticky='w')

    label_integrity = tk.Label(rootnew, width=30, text="Integrity factor:", foreground="white", bg='#3F4C50')
    label_integrity.grid(row=3, column=0, sticky='w')

    label_availability = tk.Label(rootnew, width=30, text="Availability factor:", foreground="white", bg='#3F4C50')
    label_availability.grid(row=4, column=0, sticky='w')

    label_safety = tk.Label(rootnew, width=30, text="Safety factor:", foreground="white", bg='#3F4C50')
    label_safety.grid(row=5, column=0, sticky='w')

    label_material = tk.Label(rootnew, width=30, text="Material factor:", foreground="white", bg='#3F4C50')
    label_material.grid(row=6, column=0, sticky='w')

    index_listbox_selected = listbox_nodes.curselection()
    node = get_node_from_list_by_str(listbox_nodes.get(index_listbox_selected))

    str_var_confidentiality = tk.StringVar()
    cb_confidentiality = ttk.Combobox(rootnew, textvariable=str_var_confidentiality)
    cb_confidentiality['values'] = ('Undefined', 'Low', 'Medium', 'High')
    cb_confidentiality.current(cb_confidentiality['values'].index(node.confidentiality_factor))
    cb_confidentiality.grid(row=2, column=1, sticky='w')

    str_var_integrity = tk.StringVar()
    cb_integrity = ttk.Combobox(rootnew, textvariable=str_var_integrity)
    cb_integrity['values'] = ('Undefined', 'Low', 'Medium', 'High')
    cb_integrity.current(cb_integrity['values'].index(node.integrity_factor))
    cb_integrity.grid(row=3, column=1, sticky='w')

    str_var_availability = tk.StringVar()
    cb_availability = ttk.Combobox(rootnew, textvariable=str_var_availability)
    cb_availability['values'] = ('Undefined', 'Low', 'Medium', 'High')
    cb_availability.current(cb_availability['values'].index(node.availability_factor))
    cb_availability.grid(row=4, column=1, sticky='w')

    str_var_safety = tk.StringVar()
    cb_safety = ttk.Combobox(rootnew, textvariable=str_var_safety)
    cb_safety['values'] = ('Undefined', 'None', 'Low', 'High')
    cb_safety.current(cb_safety['values'].index(node.safety_factor))
    cb_safety.grid(row=5, column=1, sticky='w')

    str_var_material = tk.StringVar()
    cb_material = ttk.Combobox(rootnew, textvariable=str_var_material)
    cb_material['values'] = ('Undefined', 'Low', 'Medium', 'High')
    cb_material.current(cb_material['values'].index(node.material_factor))
    cb_material.grid(row=6, column=1, sticky='w')

    def apply_changes():
        node.availability_factor = cb_availability.get()
        node.integrity_factor = cb_integrity.get()
        node.confidentiality_factor = cb_confidentiality.get()
        node.safety_factor = cb_safety.get()
        node.material_factor = cb_material.get()
        node.get_impact_values()
        rootnew.destroy()

        text_node_details['state'] = 'normal'
        text_node_details.insert(tk.END, str(node))
        text_node_details['state'] = 'disabled'

        listbox_nodes.selectedindex = index_listbox_selected

    # text_networkdetail = tk.Label(rootnew, text="network details")
    button_apply_changes = tk.Button(rootnew, text='Apply changes', width=20, command=apply_changes, foreground="white", bg='#2e383b')
    button_apply_changes.grid(row=7, column=1, sticky='w')
    rootnew.mainloop()


def import_netjson_file():
    netjson_file = fd.askopenfilename(
        initialdir='/home/woba/Desktop/JSON',
        filetypes=[("Json File", "*.json")],
        title="Open NetJson File"
    )
    content = open(netjson_file)
    data = content.read()

    global network_dict
    network_dict = json.loads(data)

    process_netjson_file(network_dict)


def process_netjson_file(network_dict):
    global networkNodeList
    networkNodeList = nodeClass.network_dict_to_network_nodes(network_dict)
    list_all_nodes(networkNodeList)
    Count = len(networkNodeList)
    Label_node_counter.config(text=f"Node Count: + {Count}")


def open_example_netjson_file():
    global network_dict
    network_dict = loadExampleNetJSON.get_exampleNetJson()
    print(network_dict)
    process_netjson_file(network_dict)


def show_impact_factors_details():
    window_impact_factor = nodeClass.popup_impact_factors_details(tab_network)


# create the widgets
NetJson_Label = tk.Label(tab_network, height=2, text='Define Network by \n importing NetJson File: ', bg='#3F4C50', fg='white')
# start_topology_Analysis_button = tk.Button(window, text='Analyze Topology', width=20, command=)
open_file_button = tk.Button(tab_network, text='Import NetJson file', bg='#2e383b', fg='white', width=20,
                             command=import_netjson_file)
show_graph_button = tk.Button(tab_network, text='show network graph', bg='#2e383b', fg='white', width=20,
                              command=graph_generator)
# add_incident_button = tk.Button(window, text='Add new Incident', width=20, command=add_incident)

button_load_exampleNetJSON = tk.Button(tab_network, text='Load example Network', bg='#2e383b', fg='white', width=20,
                                       command=open_example_netjson_file)
button_load_exampleNetJSON.place(x=1000, y=70)

button_edit_node = tk.Button(tab_network, text='Edit Impact Factors', bg='#2e383b', fg='white', width=20,
                             command=edit_node_factors)
button_edit_node.place(x=708, y=583)
# using grid layout
NetJson_Label.place(x=620, y=66)
open_file_button.place(x=800, y=70)
# start_topology_Analysis_button.grid(row=2, column=0)
show_graph_button.place(x=1000, y=335)
# add_incident_button.grid(row=7, column=7)


listbox_nodes.bind('<<ListboxSelect>>', node_selected)

# button_network_details = tk.Button(tab_network, text='See Network details', bg='#3F4C50', fg='white', width=20,
#                                    command=network_details_window)
# button_network_details.place(x=10, y=100)

button_open_impact_facto_details = tk.Button(tab_network, text='Load impact factors', bg='#2e383b', fg='white',
                                             width=20,
                                             command=show_impact_factors_details)
button_open_impact_facto_details.place(x=1000, y=380)
# start the app

main_window.mainloop()
