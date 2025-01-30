#!/usr/bin/env python3

import re
import datetime
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def main():
    # -- 1) Start in XKCD style (hand-drawn look)
    plt.xkcd()

    # -- 2) File path to the README
    readme_path = "/Users/danielsmith/Documents/1-RL/ASU/research/20Sim2RealSurvey/git/AwesomeSim2Real/README.md"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine year range: 2001..current year
    current_year = datetime.datetime.now().year
    min_year, max_year = 2001, current_year

    # Find 4-digit years in [2001..max_year]
    all_years = re.findall(r"\b(20\d{2})\b", content)
    valid_years = [int(y) for y in all_years if min_year <= int(y) <= max_year]

    # Tally
    year_counts = Counter(valid_years)
    all_range = list(range(min_year, max_year + 1))
    counts_in_order = [year_counts[y] for y in all_range]

    # -- 3) Make the bar chart
    fig, ax = plt.subplots(figsize=(10, 5))

    # X-values for bar chart
    x_positions = np.arange(len(all_range))
    x_labels = [str(y) for y in all_range]

    ax.bar(x_positions, counts_in_order, color="dodgerblue", width=0.6)

    # -- 4) Add a fitted curve (polynomial fit) on top
    # Convert counts to float for fitting
    yvals = np.array(counts_in_order, dtype=float)
    # Fit a polynomial of degree 3 (feel free to change degree)
    z = np.polyfit(x_positions, yvals, deg=3)
    p = np.poly1d(z)
    y_fit = p(x_positions)

    ax.plot(x_positions, y_fit, color="tomato", linewidth=2, label="Trend")

    # -- 5) Format the plot
    ax.set_title(f"Yearly Paper Count ({min_year} - {max_year})", fontsize=14, pad=20)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Number of Papers", fontsize=12)
    plt.xticks(x_positions, x_labels, rotation=45, ha='right')
    ax.legend(loc="upper left")

    plt.tight_layout()

    # -- 6) Save figure
    out_fig = "./assets/year_distribution.png"
    plt.savefig(out_fig, dpi=150)
    print(f"Done! Figure saved as '{out_fig}'.")

if __name__ == "__main__":
    main()
