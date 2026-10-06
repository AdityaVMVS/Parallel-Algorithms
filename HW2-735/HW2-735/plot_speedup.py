# usage: python3 plot_speedup.py output.<jobid>
import re, sys, collections
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
pat = re.compile(r"List Size = (\d+), Threads = (\d+), error = (\d), time \(sec\) =\s+([\d.]+)")
t = collections.defaultdict(dict)
for line in open(sys.argv[1]):
    m = pat.search(line)
    if m: t[int(m[1]).bit_length()-1][int(m[2])] = float(m[4])
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
print("k, p, time, speedup, efficiency")
for k in (12, 20, 28):
    if k not in t or 1 not in t[k]: continue
    ps = sorted(t[k]); T1 = t[k][1]
    sp = [T1/t[k][p] for p in ps]; ef = [s/p for s, p in zip(sp, ps)]
    for p, s, e in zip(ps, sp, ef): print(k, p, t[k][p], round(s, 3), round(e, 3))
    ax[0].plot(ps, sp, "o-", label=f"k={k}"); ax[1].plot(ps, ef, "o-", label=f"k={k}")
ax[0].set(xscale="log", yscale="log", xlabel="threads p", ylabel="speedup", title="Speedup"); ax[0].legend()
ax[1].set(xscale="log", xlabel="threads p", ylabel="efficiency", title="Efficiency"); ax[1].legend()
plt.tight_layout(); plt.savefig("speedup_efficiency.png", dpi=150)
