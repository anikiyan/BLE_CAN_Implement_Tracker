import pandas as pd

# === CONFIGURATION ===
LOG_FILE = "ipe833_can_log.csv"  # Input CSV file path
OUTPUT_FILE = "implement_usage_summary.csv"
IMPLEMENT_CAN_ID = '0x18FF50E5'  # Your implement CAN message ID

# === LOAD CSV LOG ===
print("Loading CAN log file...")
df = pd.read_csv(LOG_FILE)

# Assumes columns: ['Timestamp', 'CAN_ID', 'Data[0]', ...]
if 'Timestamp' not in df.columns or 'CAN_ID' not in df.columns:
    raise ValueError("CSV must contain 'Timestamp' and 'CAN_ID' columns.")

# === FILTER FOR IMPLEMENT MESSAGES ===
print("Filtering implement messages...")
df_impl = df[df['CAN_ID'].str.upper() == IMPLEMENT_CAN_ID.upper()].copy()

# Decode status from first byte of data
df_impl['Status'] = df_impl['Data[0]'].apply(lambda x: int(str(x), 16) if pd.notna(x) else 0)
df_impl['Implement_Active'] = df_impl['Status'].apply(lambda val: 1 if val == 1 else 0)

# Ensure Timestamp is datetime
df_impl['Timestamp'] = pd.to_datetime(df_impl['Timestamp'])

# Sort and find active periods
df_impl = df_impl.sort_values('Timestamp')
df_impl['Change'] = df_impl['Implement_Active'].diff()

# Find start and stop timestamps
starts = df_impl[df_impl['Change'] == 1]['Timestamp'].reset_index(drop=True)
stops = df_impl[df_impl['Change'] == -1]['Timestamp'].reset_index(drop=True)

# Match lengths
if not stops.empty and starts.iloc[0] > stops.iloc[0]:
    stops = stops.iloc[1:]  # Drop unmatched stop at start
if len(starts) > len(stops):
    starts = starts.iloc[:len(stops)]  # Drop extra start

# Calculate durations
summary = pd.DataFrame({'Start': starts, 'Stop': stops})
summary['Duration_sec'] = (summary['Stop'] - summary['Start']).dt.total_seconds()

# Save to CSV
summary.to_csv(OUTPUT_FILE, index=False)
print(f"Summary saved to {OUTPUT_FILE}")
