
def get_exampleNetJson():
    netJson = {
        "type": "NetworkGraph",
        "protocol": "olsr",
        "version": "0.6.6",
        "revision": "5031a799fcbe17f61d57e387bc3806de",
        "metric": "etx",
        "label": "Test Network",
        "nodes": [
            {
                "id": "172.16.40.24",
                "label": "SwiftSensor_1",
                "properties": {
                    "Confidentiality importance": "Low",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.40.25",
                "label": "SwiftSensor_2",
                "properties": {
                    "Confidentiality importance": "Low",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.40.26",
                "label": "SwiftSensor_3",
                "properties": {
                    "Confidentiality importance": "Low",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.40.2",
                "label": "SwiftGateway SG3-1010",
                "properties": {
                    "Firmware":"swift 6.47.2",
                    "Confidentiality importance": "Low",
                    "Availability importance": "High",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Medium"
                }
            },
            {
                "id": "172.16.41.2",
                "label": "Vigor2960Gateway SG3-1010",
                "properties": {
                    "Firmware" : "SG3-1010",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "High",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Medium"
                }
            },
            {
                "id": "172.16.42.3",
                "label": "EZVIZCamera_1",
                "properties": {
                    "Firmware" : "V5.3.0",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "Medium",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.42.4",
                "label": "EZVIZCamera_2",
                "properties": {
                    "Firmware" : "V5.3.0",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "Medium",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.41.50",
                "label": "TOTOLINKRouter",
                "properties": {
                    "Firmware" : "t-1234",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "High",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Medium"
                }
            },
            {
                "id": "172.16.41.3",
                "label": "MQTTServer",
                "properties": {
                    "Firmware" : "MQTT 5.010",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "High",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Medium"
                }
            },
            {
                "id": "172.16.52.2",
                "label": "wearable_1",
                "properties": {
                    "Firmware" : "wea_1212",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.52.3",
                "label": "wearable_2",
                "properties": {
                    "Firmware" : "wea_1212",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.52.4",
                "label": "wearable_3",
                "properties": {
                    "Firmware" : "wea_1212",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "None",
                    "Material importance": "Low"
                }
            },
            {
                "id": "172.16.55.2",
                "label": "AGVArduino_1",
                "properties": {
                    "Firmware" : "AGV2.5.0",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "Low",
                    "Material importance": "High"
                }
            },
            {
                "id": "172.16.55.3",
                "label": "AGVArduino_2",
                "properties": {
                    "Firmware" : "AGV2.5.0",
                    "Confidentiality importance": "Medium",
                    "Availability importance": "Medium",
                    "Integrity importance": "High",
                    "Safety importance": "Low",
                    "Material importance": "High"
                }
            }
        ],
        "links": [
            {
                "source": "172.16.40.24",
                "target": "172.16.40.2",
                "cost": 1.000
            },
            {
                "source": "172.16.40.25",
                "target": "172.16.40.2",
                "cost": 1.000
            },
            {
                "source": "172.16.40.26",
                "target": "172.16.40.2",
                "cost": 1.000
            },
            {
                "source": "172.16.41.2",
                "target": "172.16.40.2",
                "cost": 1.000
            },
            {
                "source": "172.16.40.2",
                "target": "172.16.41.2",
                "cost": 1.000
            },
            {
                "source": "172.16.41.3",
                "target": "172.16.41.2",
                "cost": 1.000
            },
            {
                "source": "172.16.41.2",
                "target": "172.16.41.3",
                "cost": 1.000
            },
            {
                "source": "172.16.41.2",
                "target": "172.16.42.3",
                "cost": 1.000
            },
            {
                "source": "172.16.42.3",
                "target": "172.16.41.2",
                "cost": 1.000
            },
            {
                "source": "172.16.42.4",
                "target": "172.16.41.2",
                "cost": 1.000
            },
            {
                "source": "172.16.41.2",
                "target": "172.16.42.4",
                "cost": 1.000
            },
            {
                "source": "172.16.41.50",
                "target": "172.16.41.2",
                "cost": 1.000
            },
            {
                "source": "172.16.41.2",
                "target": "172.16.41.50",
                "cost": 1.000
            },
            {
                "source": "172.16.41.50",
                "target": "172.16.52.2",
                "cost": 1.000
            },
            {
                "source": "172.16.52.2",
                "target": "172.16.41.50",
                "cost": 1.000
            },
            {
                "source": "172.16.41.50",
                "target": "172.16.52.4",
                "cost": 1.000
            },
            {
                "source": "172.16.52.4",
                "target": "172.16.41.50",
                "cost": 1.000
            },
            {
                "source": "172.16.41.50",
                "target": "172.16.52.3",
                "cost": 1.000
            },
            {
                "source": "172.16.52.3",
                "target": "172.16.41.50",
                "cost": 1.000
            },
            {
                "source": "172.16.41.50",
                "target": "172.16.55.2",
                "cost": 1.000
            },
            {
                "source": "172.16.55.2",
                "target": "172.16.41.50",
                "cost": 1.000
            },
            {
                "source": "172.16.41.50",
                "target": "172.16.55.3",
                "cost": 1.000
            },
            {
                "source": "172.16.55.3",
                "target": "172.16.41.50",
                "cost": 1.000
            }
        ]
    }

    return netJson