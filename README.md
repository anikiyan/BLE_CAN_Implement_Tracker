# BLE-CAN Smart Implement Tracker

A complete edge-to-cloud system to track and log farm implement usage in real-time using BLE vibration sensors, ESP32-based gateways, and CAN-bus integration with the IPETronik IPE833 logger. Built for precision agriculture, this project enables automatic detection of implement activity (idle vs active) and logs usage patterns for analytics, reporting, and predictive maintenance.

## 🚀 Overview

This system combines:
- **BLE vibration sensors (MSV01)** to detect implement activity.
- **ESP32 BLE-to-CAN gateway** using MCP2515 transceiver for message transmission.
- **IPE833 CAN logger** to record implement status with tractor data.
- **Cloud-based analysis** of usage trends, anomalies, and utilization reports.

## 📊 Use Case

Designed for smart farming machinery where knowing when and how long an implement is used can improve:
- Energy efficiency
- Fleet utilization
- Maintenance planning
- Operator behavior analysis

---

## 📂 Repository Structure

```plaintext
BLE_CAN_Implement_Tracker/
├── esp32_firmware/                  # ESP32 BLE-to-CAN firmware
│   └── ble_to_can_gateway.ino
├── hardware_design/                # Wiring and hardware schematics
│   ├── mcp2515_wiring.png
│   └── sensor_mount_schematic.pdf
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
│   ├── architecture_diagram.png
│   └── presentation_slides.pdf
├── .gitignore
├── LICENSE
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
- Streamlit-based dashboard for visualization
- Data pipeline automation and signal alignment
- Cloud integration (AWS-ready architecture)

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
