import tkinter

incident_types =  {
        "Malware": [1, 1, 1, 1, 1],
        "DDoS": [0, 0, 1, 1, 0],
        "DoS": [0, 0, 1, 1, 0],
        "PDoS": [0, 0, 1, 1, 0],
        "Spyware": [1, 0, 0, 0, 0],
        "WirelessDoS": [0, 0, 1, 0, 0],
        "Undefined": [1, 1, 1, 1, 1]
    }

incident_recoverability_factors = {
        "Malware": 1.2,
        "DDoS": 1.2,
        "DoS": 0.8,
        "Spyware": 1.2,
        "WirelessDoS": 1.0,
        "Undefined": 1.0
    }


class IncidentClass:
    def __init__(self, id, type, affected_node_ids, vulnerabilities):
        self.id = id
        self.type = type
        self.affected_node_ids = affected_node_ids
        self.vulnerabilities = vulnerabilities
        self.propagation_score = 0
        self.recoverability_factor = 1.0
        self.impact_score = [0, 0, 0, 0, 0]
        self.impact_score_sum = 0.0
        self.score = 0

    def __str__(self):
        return f"Id: {self.id} Type: {self.type} Functional_I: " \
               f"affectedNodes: {self.affected_node_ids} \n Score: {self.impact_score}"

    def str_results(self):
        return f"" + self.id + ": Type: " + self.type + "\ Score: " + str(self.score)

    def str_results_old(self):
        return f"" + self.id + ": Type: " + self.type + "\ PropagationScore: " + str(self.propagation_score) +\
               "\ ImpactScore: " + str(self.impact_score) + "\ Score: " + str(self.score)

    def list(self, max_value):
        name = self.id +"               "
        name = name[0:18]
        type = self.type+"         "
        type = type[0:12]

        impact_score_aggr = 0
        for i in range(0, 5):
            impact_score_aggr += self.impact_score[i]

        # impact_score_aggr =  round(impact_score_aggr/ len(networkNodeList), 2) * 100

        impact_score_aggr = "                       " +str(round(impact_score_aggr,2 ))
        impact_score_aggr = impact_score_aggr[-12:]

        propagation_score = "                        " +str(self.propagation_score)
        propagation_score = propagation_score[-20:]


        recoverability_factor = "                    "+ str(self.recoverability_factor)
        score = "     " + str(self.score)
        score = score[-7:]
        score_normalized = round(self.score/max_value * 100, 2)

        return f"" + name + "|"+ type  + "| "+ impact_score_aggr +" |"+ propagation_score +"| "+ recoverability_factor +"| "+ score + "|  "+ str(score_normalized) +"\n"


    def get_affected_impact_factors(self):
        return incident_types[self.type]

    def get_affected_impact_factors_labels(self):
        string_affected_factors = "|"
        if(incident_types[self.type][0] == 1):
            string_affected_factors += " Con |"
        if(incident_types[self.type][1] == 1):
            string_affected_factors += " Int |"
        if(incident_types[self.type][2] == 1):
            string_affected_factors += " Ava |"
        if(incident_types[self.type][3] == 1):
            string_affected_factors += " Saf |"
        if(incident_types[self.type][4] == 1):
            string_affected_factors += " Mat |"
        return string_affected_factors

    def print_incident_impact_sum(self):
        affected_factors = self.get_affected_impact_factors()
        impact_score =  self.impact_score
        string_affected_factors = "| "

        if(affected_factors[0] == 1):
            string_affected_factors +=  ("  "+ (str(impact_score[0])))[-4:]+"| "
        if(affected_factors[1] == 1):
            string_affected_factors +=  (" "+ (str(impact_score[1])))[-4:]+ "| "
        if(affected_factors[2] == 1):
            string_affected_factors +=  (" "+ (str(impact_score[2])))[-4:]+ "| "
        if(affected_factors[3] == 1):
            string_affected_factors +=  (" "+ (str(impact_score[3])))[-4:]+ "| "
        if(affected_factors[4] == 1):
            string_affected_factors += (" "+ (str(impact_score[4])))[-4:]+ "|"
        return (string_affected_factors)

    def update_recoverability_factor_for_incident(self):
        for incident_type in incident_recoverability_factors:
            if incident_type == self.type:
                self.recoverability_factor = incident_recoverability_factors[incident_type]


def define_listbox_incident_types(Listbox):
    incident_types_names = []
    for incident_type in incident_types:
        Listbox.insert(tkinter.END, incident_type)
    return incident_types_names


def load_predefined_incidents():
    incidents = []

    incidents.append(IncidentClass("BotenaGO", "Malware",  ["172.16.41.2"], ["t-1234", "SG3-1010"]))
    incidents.append(IncidentClass("DDoS", "DDoS", ["172.16.40.2"], None))

    incidents.append(IncidentClass("MQTTDoS_Server", "DoS",  ["172.16.41.3"], None))
    incidents.append(IncidentClass("CamerasSpyware", "Spyware",  ["172.16.42.3", "172.16.42.4"], None))
    #incidents.append(IncidentClass("AGVRemoteControl", "Malware",  ["172.16.55.2", "172.16.55.3"], "2.5.0"))
    incidents.append(IncidentClass("AGVRemoteControl", "Malware",  ["172.16.55.2"], "2.5.0"))

    incidents.append(IncidentClass("NodeCaptureAttack", "WirelessDoS",  ["172.16.40.24", "172.16.40.25", "172.16.52.2"], None))

    for incident_obj in incidents:
        incident_obj.update_recoverability_factor_for_incident()
    return incidents


