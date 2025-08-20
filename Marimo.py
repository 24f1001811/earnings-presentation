# 24f1001811@ds.study.iitm.ac.in
# Interactive Data Analysis Notebook demonstrating variable dependencies

import marimo as mo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cell 1: Data generation and parameters
sample_size = mo.ui.slider(10, 1000, value=100, label="Sample Size")
noise_level = mo.ui.slider(0.1, 2.0, value=0.5, step=0.1, label="Noise Level")

mo.md(f"""
# Interactive Data Analysis Dashboard
**Email:** 24f1001811@ds.study.iitm.ac.in

## Data Parameters
- Sample Size: {sample_size.value}
- Noise Level: {noise_level.value}
""")

# Cell 2: Generate synthetic data (depends on sample_size and noise_level)
np.random.seed(42)  # For reproducibility
x = np.linspace(0, 10, sample_size.value)
y = 2 * x + 1 + noise_level.value * np.random.normal(0, 1, sample_size.value)

# Create DataFrame for analysis
data = pd.DataFrame({
    'x_variable': x,
    'y_variable': y,
    'residuals': y - (2 * x + 1)
})

# Cell 3: Statistical calculations (depends on data from Cell 2)
correlation = np.corrcoef(data['x_variable'], data['y_variable'])[0, 1]
mean_y = np.mean(data['y_variable'])
std_y = np.std(data['y_variable'])

# Cell 4: Dynamic visualization (depends on data and statistics)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Scatter plot
ax1.scatter(data['x_variable'], data['y_variable'], alpha=0.6, color='blue')
ax1.plot(x, 2 * x + 1, 'r--', label='True relationship: y = 2x + 1')
ax1.set_xlabel('X Variable')
ax1.set_ylabel('Y Variable')
ax1.set_title(f'Scatter Plot (n={sample_size.value})')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Residuals histogram
ax2.hist(data['residuals'], bins=20, alpha=0.7, color='green', edgecolor='black')
ax2.set_xlabel('Residuals')
ax2.set_ylabel('Frequency')
ax2.set_title('Residual Distribution')
ax2.grid(True, alpha=0.3)

plt.tight_layout()

# Cell 5: Dynamic markdown output based on widget state and calculations
correlation_strength = "strong" if abs(correlation) > 0.8 else "moderate" if abs(correlation) > 0.5 else "weak"
noise_description = "high" if noise_level.value > 1.0 else "moderate" if noise_level.value > 0.5 else "low"

mo.md(f"""
## Statistical Analysis Results

### Data Flow Documentation:
1. **Cell 1:** User input parameters (sample_size={sample_size.value}, noise_level={noise_level.value})
2. **Cell 2:** Generated synthetic dataset with {sample_size.value} observations
3. **Cell 3:** Calculated correlation coefficient: **{correlation:.3f}**
4. **Cell 4:** Created visualizations based on current data
5. **Cell 5:** Dynamic summary based on all previous calculations

### Key Findings:
- **Sample Size:** {sample_size.value} data points
- **Correlation:** {correlation:.3f} ({correlation_strength} relationship)
- **Mean Y:** {mean_y:.2f} ± {std_y:.2f}
- **Noise Level:** {noise_description} ({noise_level.value})

### Interactive Features:
- 🔄 **Reactive Cells:** Changing sliders updates all dependent calculations automatically
- 📊 **Real-time Visualization:** Charts update instantly with parameter changes
- 📈 **Statistical Updates:** All metrics recalculate based on current data

### Variable Dependencies:
```
sample_size, noise_level → data → statistics → visualization → summary
```

*Adjust the sliders above to see how data relationships change in real-time!*
""")

# Cell 6: Data summary table (depends on data from Cell 2)
summary_stats = data.describe()
mo.ui.table(summary_stats, label="Dataset Summary Statistics")
