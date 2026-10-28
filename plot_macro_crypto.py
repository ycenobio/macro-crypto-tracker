import matplotlib.pyplot as plt
from datetime import datetime

# 1. Complete 4-year macro data coordinates
dates = [
    "2022-01", "2022-07", "2023-01", "2023-07", 
    "2024-01", "2024-07", "2025-07", "2026-01", "2026-10"
]
btc_prices = [47740, 19228, 16835, 29391, 42124, 67845, 118353, 95310, 81464]
fed_rates = [0.08, 1.58, 4.33, 5.33, 5.33, 5.33, 4.33, 4.33, 3.75]

# Convert date strings to datetime objects
x_dates = [datetime.strptime(d, "%Y-%m") for d in dates]

# 2. Initialize the plot with generous padding
fig, ax1 = plt.subplots(figsize=(11, 6))

# --- LEFT AXIS: Bitcoin Price ---
color = '#1f77b4'
ax1.set_xlabel('Timeline (2022 - 2026)', fontweight='bold', labelpad=12)
ax1.set_ylabel('Bitcoin (BTC) Price in USD', color=color, fontweight='bold', labelpad=12)
line1 = ax1.plot(x_dates, btc_prices, color=color, linewidth=2.5, marker='o', label='Bitcoin Price (USD)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.yaxis.set_major_formatter('${x:,.0f}')
ax1.grid(True, linestyle='--', alpha=0.5)

# --- RIGHT AXIS: Fed Interest Rate ---
ax2 = ax1.twinx()
color = '#d62728'
ax2.set_ylabel('U.S. Federal Funds Interest Rate', color=color, fontweight='bold', labelpad=15)
line2 = ax2.plot(x_dates, fed_rates, color=color, linewidth=2.5, linestyle='--', marker='s', label='Fed Funds Rate (%)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.yaxis.set_major_formatter('{x:.2f}%')

# 3. Add critical annotations
ax1.annotate('Cycle Peak\n$118k', xy=(datetime(2025, 7, 1), 118353), xytext=(datetime(2025, 1, 1), 125000),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))

ax2.annotate('Peak Pause\n5.33%', xy=(datetime(2023, 7, 1), 5.33), xytext=(datetime(2023, 1, 1), 5.8),
             arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6))

# 4. Global layouts and layout preservation
plt.title('Macro Analysis: Bitcoin Price vs. U.S. Interest Rates (4-Year Horizon)', fontsize=13, fontweight='bold', pad=15)
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

plt.tight_layout()

# Save the file and print confirmation
plt.savefig('crypto_macro_chart.png', dpi=300)
print("[+] High-resolution chart saved successfully as 'crypto_macro_chart.png'")
