import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# CSCE 735 - HW1
# Part 1: Shared-Memory Programming with Threads
# ============================================================


# ------------------------------------------------------------
# Question 1
# n = 10^8
# p = 2^k, k = 0,...,13
# ------------------------------------------------------------

threads = np.array([
    1, 2, 4, 8, 16, 32, 64,
    128, 256, 512, 1024, 2048, 4096, 8192
])

time_n1e8 = np.array([
    0.9368,
    0.4858,
    0.2424,
    0.1255,
    0.0639,
    0.0329,
    0.0305,
    0.0258,
    0.0264,
    0.0300,
    0.0328,
    0.0650,
    0.1319,
    0.2699
])


# ------------------------------------------------------------
# Calculate speedup and efficiency
# ------------------------------------------------------------

speedup = time_n1e8[0] / time_n1e8
efficiency = speedup / threads


# ------------------------------------------------------------
# Question 1.1
# Execution Time vs Number of Threads
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    threads,
    time_n1e8,
    marker='o',
    linewidth=2
)

plt.xscale('log', base=2)

plt.xlabel('Number of Threads (p)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Threads, n = $10^8$')

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.xticks(threads, threads, rotation=45)

plt.tight_layout()
plt.savefig('Q1_1_execution_time.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Question 1.2
# Speedup vs Number of Threads
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    threads,
    speedup,
    marker='o',
    linewidth=2
)

plt.xscale('log', base=2)

plt.xlabel('Number of Threads (p)')
plt.ylabel('Speedup')
plt.title('Speedup vs Number of Threads, n = $10^8$')

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.xticks(threads, threads, rotation=45)

plt.tight_layout()
plt.savefig('Q1_2_speedup.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Question 1.3
# Efficiency vs Number of Threads
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    threads,
    efficiency,
    marker='o',
    linewidth=2
)

plt.xscale('log', base=2)

plt.xlabel('Number of Threads (p)')
plt.ylabel('Efficiency')
plt.title('Efficiency vs Number of Threads, n = $10^8$')

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.xticks(threads, threads, rotation=45)

plt.tight_layout()
plt.savefig('Q1_3_efficiency.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Question 2
# n = 10^10
# Used to find the thread count with minimum runtime
# ------------------------------------------------------------

time_n1e10 = np.array([
    93.4157,
    47.6087,
    24.5045,
    12.4658,
    6.3081,
    3.1582,
    2.4358,
    2.2209,
    2.2242,
    2.2166,
    2.2232,
    2.2277,
    2.2622,
    2.3616
])


# ------------------------------------------------------------
# Question 4
# Error vs n
# p = 48
# ------------------------------------------------------------

n_values = np.array([
    1e3,
    1e4,
    1e5,
    1e6,
    1e7,
    1e8,
    1e9
])

errors = np.array([
    4.76e-2,
    1.01e-2,
    4.29e-3,
    1.21e-3,
    1.29e-3,
    2.08e-4,
    8.04e-6
])


plt.figure(figsize=(8, 5))

plt.plot(
    n_values,
    errors,
    marker='o',
    linewidth=2
)

# plt.xscale('log', base=10)

plt.xlabel('Number of Points (n)')
plt.ylabel('Relative Error')
plt.title('Relative Error vs Number of Points, p = 48')

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('Q4_error_vs_n.png', dpi=300)
plt.show()


# ------------------------------------------------------------
# Print numerical results
# ------------------------------------------------------------

q1_min_index = np.argmin(time_n1e8)
q2_min_index = np.argmin(time_n1e10)

print("\n========================================")
print("PART 1 RESULTS")
print("========================================")

print("\nQuestion 1:")
print("Minimum runtime =", time_n1e8[q1_min_index], "seconds")
print("Threads giving minimum runtime =", threads[q1_min_index])

print("\nQuestion 2:")
print("Minimum runtime =", time_n1e10[q2_min_index], "seconds")
print("Threads giving minimum runtime =", threads[q2_min_index])


# ------------------------------------------------------------
# Print Q1 table
# ------------------------------------------------------------

print("\n========================================")
print("QUESTION 1 DATA")
print("========================================")
print(f"{'p':>8} {'Time(s)':>12} {'Speedup':>12} {'Efficiency':>12}")

for p, t, s, e in zip(threads, time_n1e8, speedup, efficiency):
    print(f"{p:8d} {t:12.4f} {s:12.4f} {e:12.6f}")


# ------------------------------------------------------------
# Print Question 2 data
# ------------------------------------------------------------

print("\n========================================")
print("QUESTION 2 DATA")
print("========================================")
print(f"{'p':>8} {'Time(s)':>12}")

for p, t in zip(threads, time_n1e10):
    print(f"{p:8d} {t:12.4f}")


# ------------------------------------------------------------
# Print Question 4 data
# ------------------------------------------------------------

print("\n========================================")
print("QUESTION 4 DATA")
print("========================================")
print(f"{'n':>15} {'Relative Error':>20}")

for n, error in zip(n_values, errors):
    print(f"{n:15.0f} {error:20.6e}")