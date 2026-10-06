import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# CSCE 735 - HW1
# Part 2: Distributed-Memory Programming with MPI
# Questions 5 and 7
# ============================================================


# ============================================================
# QUESTION 5
# n = 10^8
# p = 1, 2, 4, 8, 16, 32, 64
# ntasks-per-node = 4
# ============================================================

processes = np.array([
    1, 2, 4, 8, 16, 32, 64
])

q5_time = np.array([
    0.15191767,
    0.07799947,
    0.08077565,
    0.17282820,
    0.15872939,
    0.65974204,
    0.04658476
])


# Speedup = T1 / Tp
q5_speedup = q5_time[0] / q5_time

# Efficiency = Speedup / p
q5_efficiency = q5_speedup / processes


# ------------------------------------------------------------
# Q5.1 Execution Time vs Number of Processes
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    processes,
    q5_time,
    marker='o',
    linewidth=2
)

plt.xscale('log', base=2)

plt.xlabel('Number of Processes (p)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Processes, n = $10^8$')

plt.xticks(processes, processes)
plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q5_1_execution_time.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Q5.2 Speedup vs Number of Processes
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    processes,
    q5_speedup,
    marker='o',
    linewidth=2
)

plt.xscale('log', base=2)

plt.xlabel('Number of Processes (p)')
plt.ylabel('Speedup')
plt.title('Speedup vs Number of Processes, n = $10^8$')

plt.xticks(processes, processes)
plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q5_2_speedup.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Q5.3 Efficiency vs Number of Processes
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    processes,
    q5_efficiency,
    marker='o',
    linewidth=2
)

plt.xscale('log', base=2)

plt.xlabel('Number of Processes (p)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Number of Processes, n = $10^8$')

plt.xticks(processes, processes)
plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q5_3_efficiency.png', dpi=300)
plt.show()


# ============================================================
# QUESTION 7
# n = 10^2, 10^4, 10^6, 10^8
#
# Speedup on p=64 relative to p=1:
#
# Speedup(n) = T1(n) / T64(n)
#
# For n = 10^8, reuse the Q5 p=1 and p=64 measurements.
# ============================================================

n_values = np.array([
    1e2,
    1e4,
    1e6,
    1e8
])


# p = 1 execution times
q7_time_p1 = np.array([
    0.00001183,     # n = 10^2
    0.00002763,     # n = 10^4
    0.00152663,     # n = 10^6
    0.15191767      # n = 10^8, reused from Q5
])


# p = 64 execution times
q7_time_p64 = np.array([
    0.02088889,     # n = 10^2
    0.01005510,     # n = 10^4
    0.01922262,     # n = 10^6
    0.04658476      # n = 10^8, reused from Q5
])


# Speedup
q7_speedup = q7_time_p1 / q7_time_p64


# Relative error for p = 64
q7_relative_error = np.array([
    2.65e-6,        # n = 10^2
    2.65e-10,       # n = 10^4
    2.63e-14,       # n = 10^6
    0.00e0          # n = 10^8
])


# ------------------------------------------------------------
# Q7.1 Speedup vs n
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    n_values,
    q7_speedup,
    marker='o',
    linewidth=2
)

# plt.xscale('log', base=10)

plt.xlabel('Number of Intervals (n)')
plt.ylabel('Speedup on 64 Processes')
plt.title('Speedup vs Problem Size on 64 Processes')

plt.xticks(
    n_values,
    [r'$10^2$', r'$10^4$', r'$10^6$', r'$10^8$']
)

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q7_1_speedup_vs_n.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Q7.2 Relative Error vs n
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    n_values,
    q7_relative_error,
    marker='o',
    linewidth=2
)

# plt.xscale('log', base=10)

plt.xlabel('Number of Intervals (n)')
plt.ylabel('Relative Error')
plt.title('Relative Error vs Number of Intervals, p = 64')

plt.xticks(
    n_values,
    [r'$10^2$', r'$10^4$', r'$10^6$', r'$10^8$']
)

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q7_2_relative_error_vs_n.png', dpi=300)
plt.show()


# ============================================================
# PRINT RESULTS
# ============================================================

print("\n==========================================")
print("QUESTION 5 RESULTS")
print("==========================================")

print(
    f"{'p':>8} "
    f"{'Time(s)':>14} "
    f"{'Speedup':>14} "
    f"{'Efficiency':>14}"
)

for p, t, s, e in zip(
    processes,
    q5_time,
    q5_speedup,
    q5_efficiency
):
    print(
        f"{p:8d} "
        f"{t:14.8f} "
        f"{s:14.6f} "
        f"{e:14.6f}"
    )


# Q5.4 minimum runtime
q5_min_index = np.argmin(q5_time)

print("\nQ5.4")
print(
    f"Minimum runtime = {q5_time[q5_min_index]:.8f} seconds"
)
print(
    f"Number of processes = {processes[q5_min_index]}"
)


print("\n==========================================")
print("QUESTION 7 RESULTS")
print("==========================================")

print(
    f"{'n':>12} "
    f"{'T1(s)':>14} "
    f"{'T64(s)':>14} "
    f"{'Speedup':>14} "
    f"{'Relative Error':>18}"
)

for n, t1, t64, s, err in zip(
    n_values,
    q7_time_p1,
    q7_time_p64,
    q7_speedup,
    q7_relative_error
):
    print(
        f"{n:12.0f} "
        f"{t1:14.8f} "
        f"{t64:14.8f} "
        f"{s:14.6f} "
        f"{err:18.4e}"
    )