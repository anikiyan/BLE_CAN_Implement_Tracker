# BLE-CAN Smart Implement Tracker
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-ff4b4b?logo=streamlit)


A complete edge-to-cloud system to track and log farm implement usage in real-time using BLE vibration sensors, ESP32-based gateways, and CAN-bus integration with the IPETronik IPE833 logger. Built for precision agriculture, this project enables automatic detection of implement activity (idle vs active) and logs usage patterns for analytics, reporting, and predictive maintenance.

## 🚀 Overview

This system combines:
- **BLE vibration sensors (MSV01)** to detect implement activity.
- **ESP32 BLE-to-CAN gateway** using MCP2515 transceiver for message transmission.
- **IPE833 CAN logger** to record implement status with tractor data.
- **Cloud-based analysis** of usage trends, anomalies, and utilization reports.

## 📊 Use Case

Designed for smart farming machinery, this system tracks when implements (e.g., seeders, ploughs) are actively used, enabling:
- Enhanced power efficiency
- Operator behavior analytics
- Maintenance scheduling
- Remote cloud-based monitoring

---

## 📂 Repository Structure

```plaintext
BLE_CAN_Implement_Tracker/
├── esp32_firmware/                  # ESP32 BLE-to-CAN firmware
│   └── ble_to_can_gateway.ino
├── hardware_design/                # Wiring and hardware schematics
│   └── mcp2515_wiring.png
├── data_pipeline/                  # CAN parsing and time alignment tools
│   ├── can_parser.py
│   └── event_alignment_tool.ipynb
├── analytics/                      # Vibration pattern EDA & anomaly detection
│   ├── vibration_feature_extraction.ipynb
│   └── anomaly_detection_demo.ipynb
├── dashboard/                      # Streamlit dashboard
│   └── streamlit_usage_dashboard.py
├── docs/                           # Documentation and reports
│   ├── README.md
│   └── architecture_diagram.png
├── .gitignore
├── requirements.txt
└── environment.yml
```

---

## 🧠 Core Skills Demonstrated

- Predictive Modelling, Feature Engineering & EDA
- BLE signal processing & vibration pattern detection
- CAN Bus integration with ESP32 and MCP2515
- Time-Series Forecasting and Anomaly Detection
- ML Frameworks: Scikit-learn, TensorFlow-ready structure
- Real-time Edge Gateway Development (ESP32)
- Interactive Dashboard (Streamlit + Plotly)
- Data pipeline automation, signal alignment and Anomaly Detection
- Cloud integration (AWS-ready architecture)
- Git-based Project Management & Automation


## 📦 Project Components

    Component	                            Purpose
    ✅ README.md	                            Clean, branded summary with badges, visuals, and links
    ✅ ble_to_can_gateway.ino	            ESP32 firmware for BLE-to-CAN message injection
    ✅ can_parser.py	                    Extract implement usage sessions from CAN logs
    ✅ vibration_feature_extraction.ipynb	    EDA on usage duration & anomaly thresholds
    ✅ anomaly_detection_demo.ipynb	            ML-based detection using Z-score and Isolation Forest
    ✅ event_alignment_tool.ipynb	            Aligns implement status with external telemetry (e.g., engine load)
    ✅ streamlit_usage_dashboard.py	            Interactive usage + anomaly dashboard
    ✅ architecture_diagram.png	            System flow: Sensor → Gateway → Logger → Cloud → Dashboard
    ✅ sensor_mount_schematic.pdf	            BLE sensor hardware mounting plan
    ✅ requirements.txt / environment.yml	    Python & Conda environment setup

---

## 📡 System Architecture

```plaintext
[MSV01 BLE Sensor]
    ↓ BLE
[ESP32 BLE-WiFi Gateway + MCP2515]
    ↓ CAN Bus
[IPE833 Data Logger]
    ↓ USB / Cloud
[AWS S3 + Analytics + Dashboard]
```

---

## 🔮 Future Enhancements

- Edge AI on ESP32 for local inference
- MQTT-based live streaming to cloud
- Alert system for abnormal usage
- Mobile dashboard for real-time tracking

---

## 🔗 Related Projects

Looking for predictive failure analytics? See my [Predictive Maintenance Project](https://github.com/anikiyan/Predictive_Maintenance_Project) — a portfolio-ready time-series diagnostic and forecasting platform built for electric farming machinery.
