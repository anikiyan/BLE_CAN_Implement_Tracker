import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Implement Usage Dashboard", layout="wide")

st.title("🚜 Implement Usage Dashboard")
st.markdown("This dashboard visualizes usage events from the BLE-to-CAN implement tracking system.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('../data_pipeline/implement_usage_summary.csv')
    df['Start'] = pd.to_datetime(df['Start'])
    df['Stop'] = pd.to_datetime(df['Stop'])
    df['Duration_min'] = df['Duration_sec'] / 60
    return df

df = load_data()

# Summary stats
st.subheader("📊 Summary Statistics")
st.write(df['Duration_min'].describe())

# Timeline plot
st.subheader("🕒 Usage Timeline")
timeline_df = df.copy()
timeline_df['Duration_str'] = timeline_df['Duration_min'].round(2).astype(str) + ' min'

fig = px.timeline(
    timeline_df,
    x_start='Start',
    x_end='Stop',
    y=timeline_df.index,
    color='Duration_min',
    hover_name='Duration_str',
    title="Implement Usage Events Over Time",
    labels={'y': 'Event #'}
)
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# Anomalies
st.subheader("⚠️ Potential Anomalies")
min_thres = st.slider("Min Duration (min)", 0.1, 5.0, 0.5)
max_thres = st.slider("Max Duration (min)", 5.0, 60.0, 10.0)
anomalies = df[(df['Duration_min'] < min_thres) | (df['Duration_min'] > max_thres)]

st.write(f"Detected {len(anomalies)} anomalies")
st.dataframe(anomalies)
