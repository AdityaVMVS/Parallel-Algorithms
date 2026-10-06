import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# QUESTION 6
# n = 10^10
# p = 64
# ============================================================

ntasks_per_node = np.array([
    4, 8, 16, 32
])

q6_time = np.array([
    0.26946154,
    0.27876676,
    0.26692614,
    0.26790406
])


plt.figure(figsize=(8, 5))

plt.plot(
    ntasks_per_node,
    q6_time,
    marker='o',
    linewidth=2
)

plt.xlabel('Tasks per Node')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Tasks per Node, n = $10^{10}$, p = 64')

plt.xticks(ntasks_per_node)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q6_time_vs_ntasks_per_node.png', dpi=300)
plt.show()


# Find minimum runtime
min_index = np.argmin(q6_time)

print("Question 6:")
print(
    f"Minimum runtime = {q6_time[min_index]:.8f} seconds"
)
print(
    f"ntasks-per-node = {ntasks_per_node[min_index]}"
)