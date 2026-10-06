import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Input data
# ---------------------------------------------------------

# q values
q = np.array([0, 1, 2, 4, 6, 8, 10])

# Number of threads = 2^q
threads = 2 ** q

# Execution times for each k
times = {
    12: np.array([
        0.0005,
        0.0004,
        0.0009,
        0.0012,
        0.0030,
        0.0113,
        0.0494
    ]),

    20: np.array([
        0.1402,
        0.0732,
        0.0395,
        0.0170,
        0.0101,
        0.0240,
        0.0686
    ]),

    28: np.array([
        49.8663,
        26.3009,
        13.4490,
        3.7316,
        1.8297,
        1.7543,
        2.1018
    ])
}


# ---------------------------------------------------------
# Calculate speedup and efficiency
# ---------------------------------------------------------

speedup = {}
efficiency = {}

for k in times:

    # Single-thread execution time
    T1 = times[k][0]

    # Speedup = T1 / Tp
    speedup[k] = T1 / times[k]

    # Efficiency = Speedup / Number of threads
    efficiency[k] = speedup[k] / threads


# ---------------------------------------------------------
# Create plots
# ---------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(15, 6))


# =========================================================
# Speedup Plot
# =========================================================

for k in times:

    axes[0].plot(
        q,
        speedup[k],
        marker='o',
        markersize=7,
        linewidth=2,
        label=f'k = {k}'
    )

    # Add actual speedup value above each point
    for x, y in zip(q, speedup[k]):

        axes[0].annotate(
            f'{y:.2f}',
            xy=(x, y),
            xytext=(0, 8),
            textcoords='offset points',
            ha='center',
            va='bottom',
            fontsize=8
        )


axes[0].set_xlabel(
    'q  (Number of Threads = 2^q)',
    fontsize=11
)

axes[0].set_ylabel(
    'Speedup',
    fontsize=11
)

axes[0].set_title(
    'Speedup vs Number of Threads',
    fontsize=13
)


# X-axis labels show both q and number of threads
axes[0].set_xticks(q)

axes[0].set_xticklabels(
    [f'{qi}\n({p})'
     for qi, p in zip(q, threads)]
)


# Log-scale speedup axis so all k values are visible
axes[0].set_yscale('log')

axes[0].set_ylim(
    0.008,
    50
)


# Grid for both major and minor log ticks
axes[0].grid(
    True,
    which='both',
    linestyle='--',
    alpha=0.5
)

axes[0].legend()


# =========================================================
# Efficiency Plot
# =========================================================

for k in times:

    axes[1].plot(
        q,
        efficiency[k],
        marker='o',
        markersize=7,
        linewidth=2,
        label=f'k = {k}'
    )


axes[1].set_xlabel(
    'q  (Number of Threads = 2^q)',
    fontsize=11
)

axes[1].set_ylabel(
    'Efficiency',
    fontsize=11
)

axes[1].set_title(
    'Efficiency vs Number of Threads',
    fontsize=13
)


axes[1].set_xticks(q)

axes[1].set_xticklabels(
    [f'{qi}\n({p})'
     for qi, p in zip(q, threads)]
)


# Keep efficiency on linear scale
axes[1].set_ylim(
    0,
    1.05
)

axes[1].set_yticks(
    np.arange(0, 1.1, 0.1)
)


axes[1].grid(
    True,
    linestyle='--',
    alpha=0.5
)

axes[1].legend()


# ---------------------------------------------------------
# Final formatting
# ---------------------------------------------------------

plt.tight_layout()


# Save high-resolution image
plt.savefig(
    'speedup_efficiency.png',
    dpi=300,
    bbox_inches='tight'
)


plt.show()


# ---------------------------------------------------------
# Print calculated values
# ---------------------------------------------------------

for k in times:

    print(f"\nk = {k}")

    print(
        "q\tThreads\tTime(sec)\tSpeedup\t\tEfficiency"
    )

    for i in range(len(q)):

        print(
            f"{q[i]}\t"
            f"{threads[i]}\t"
            f"{times[k][i]:.6f}\t"
            f"{speedup[k][i]:.4f}\t\t"
            f"{efficiency[k][i]:.4f}"
        )