// BLE-CAN Gateway Firmware for ESP32
// Reads BLE vibration data (MSV01), sends implement status to CAN logger (IPE833) via MCP2515

#include <BLEDevice.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>

#include <SPI.h>
#include <mcp_can.h>

// CAN Setup (MCP2515 connected to SPI)
const int SPI_CS_PIN = 5;
MCP_CAN CAN(SPI_CS_PIN);

// BLE Setup
BLEScan* pBLEScan;
const int scanTime = 5; // seconds

// BLE Filter Parameters
const char* targetName = "MSV01";  // BLE device name to look for
bool implementActive = false;
uint32_t lastSentTime = 0;
const uint32_t sendInterval = 3000; // Minimum 3s between CAN messages

// CAN Message
const unsigned long CAN_ID = 0x18FF50E5; // Custom CAN ID (29-bit extended frame if needed)

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice advertisedDevice) {
    if (advertisedDevice.haveName() && advertisedDevice.getName() == targetName) {
      // You can refine this further using manufacturer data or RSSI threshold
      Serial.println("Vibration detected from MSV01!");

      unsigned long now = millis();
      if (now - lastSentTime > sendInterval) {
        sendCanMessage(true);
        lastSentTime = now;
      }
    }
  }
};

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Starting BLE to CAN Gateway...");

  // Start CAN
  if (CAN.begin(MCP_ANY, CAN_500KBPS, MCP_8MHZ) == CAN_OK) {
    Serial.println("CAN BUS Shield init OK!");
  } else {
    Serial.println("CAN BUS Shield init FAIL");
    while (1);
  }
  CAN.setMode(MCP_NORMAL);

  // Start BLE
  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);
}

void loop() {
  BLEScanResults foundDevices = pBLEScan->start(scanTime, false);
  pBLEScan->clearResults();
}

// Function to send CAN message
void sendCanMessage(bool active) {
  byte data[8] = {0};
  data[0] = active ? 1 : 0;  // Byte 0: 1 = active, 0 = idle
  data[1] = 0xAB;            // Byte 1-2: BLE device code or ID (example)
  data[2] = 0xCD;

  byte sendResult = CAN.sendMsgBuf(CAN_ID, 0, 8, data);

  if (sendResult == CAN_OK) {
    Serial.println("CAN message sent successfully.");
  } else {
    Serial.println("Error sending CAN message.");
  }
}
