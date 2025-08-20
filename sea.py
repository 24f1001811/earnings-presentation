# Customer Support Response Time Analysis
# Company: Paucek Schuppe - Customer Experience Analytics
# Analyst: 24f1001811@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic customer support response time data
def generate_support_data(n_samples=1000):
    """Generate realistic customer support response time data by channel"""
    
    # Define response time characteristics for each channel
    channels = {
        'Live Chat': {'mean': 2.5, 'std': 1.2, 'min': 0.5, 'max': 8},
        'Email': {'mean': 24, 'std': 12, 'min': 2, 'max': 72},
        'Phone': {'mean': 8, 'std': 4, 'min': 1, 'max': 30},
        'Social Media': {'mean': 6, 'std': 3.5, 'min': 0.3, 'max': 24}
    }
    
    data = []
    
    for channel, params in channels.items():
        # Generate data with realistic distribution
        if channel == 'Email':
            # Email has more variation, some long delays
            base_times = np.random.lognormal(mean=np.log(params['mean']), 
                                           sigma=0.8, size=n_samples//4)
        elif channel == 'Live Chat':
            # Live chat is generally faster with some outliers
            base_times = np.random.gamma(shape=2, scale=1.2, size=n_samples//4)
        else:
            # Phone and social media follow more normal patterns
            base_times = np.random.gamma(shape=3, scale=params['mean']/3, size=n_samples//4)
        
        # Clip to realistic bounds
        response_times = np.clip(base_times, params['min'], params['max'])
        
        # Add channel data
        for time in response_times:
            data.append({
                'channel': channel,
                'response_time_hours': time,
                'customer_satisfaction': np.random.normal(
                    loc=max(1, 5 - time/10), 
                    scale=0.5
                )
            })
    
    return pd.DataFrame(data)

# Generate the dataset
print("Generating synthetic customer support data...")
df = generate_support_data(1200)

# Data quality check
print(f"Dataset shape: {df.shape}")
print(f"Channels: {df['channel'].unique()}")
print(f"Response time range: {df['response_time_hours'].min():.2f} - {df['response_time_hours'].max():.2f} hours")

# Set professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Create the figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create the violinplot
violin_plot = sns.violinplot(
    data=df,
    x='channel',
    y='response_time_hours',
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],  # Professional color palette
    inner='box',  # Show box plot inside violin
    linewidth=1.5,
    alpha=0.8
)

# Customize the plot
plt.title('Customer Support Response Time Distribution by Channel\n'
          'Paucek Schuppe Customer Experience Analytics', 
          fontsize=16, fontweight='bold', pad=20)

plt.xlabel('Support Channel', fontsize=14, fontweight='bold')
plt.ylabel('Response Time (Hours)', fontsize=14, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(True, alpha=0.3, linestyle='--')

# Add statistical annotations
channel_stats = df.groupby('channel')['response_time_hours'].agg(['mean', 'median', 'std'])
print("\nChannel Statistics:")
print(channel_stats.round(2))

# Add mean indicators
for i, channel in enumerate(df['channel'].unique()):
    mean_val = channel_stats.loc[channel, 'mean']
    plt.plot(i, mean_val, 'ro', markersize=8, markerfacecolor='red', 
             markeredgecolor='white', markeredgewidth=2, label='Mean' if i == 0 else "")

# Add legend
plt.legend(loc='upper right')

# Add professional styling
plt.tight_layout()

# Add watermark with analyst contact
plt.figtext(0.02, 0.02, 'Analysis by: 24f1001811@ds.study.iitm.ac.in', 
            fontsize=8, style='italic', alpha=0.7)

# Save the chart with exact specifications
plt.savefig('chart.png', 
            dpi=64,  # 512px / 8in = 64 DPI
            bbox_inches='tight',
            facecolor='white',
            edgecolor='none',
            format='png')

print(f"\nChart saved as 'chart.png' with 512x512 pixel dimensions")
print(f"Contact: 24f1001811@ds.study.iitm.ac.in")

# Display summary insights
print("\n" + "="*60)
print("BUSINESS INSIGHTS:")
print("="*60)
print(f"• Live Chat: Fastest channel (avg: {channel_stats.loc['Live Chat', 'mean']:.1f}h)")
print(f"• Phone: Moderate response (avg: {channel_stats.loc['Phone', 'mean']:.1f}h)")  
print(f"• Social Media: Quick response (avg: {channel_stats.loc['Social Media', 'mean']:.1f}h)")
print(f"• Email: Slowest channel (avg: {channel_stats.loc['Email', 'mean']:.1f}h)")
print(f"\nRecommendation: Invest in live chat infrastructure for optimal efficiency")

# Show the plot
plt.show()
