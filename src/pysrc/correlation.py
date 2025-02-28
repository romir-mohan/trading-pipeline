from re import search
from scipy.stats import pearsonr

exp = []
act = []

with open("/home/rmohan/intern-project/src/pysrc/data/test_data.txt") as file:
    for line in file:
        exp_match = search(r"Expected: ([+-]?\d*\.\d+|\d+)", line)
        act_match = search(r"Actual: ([+-]?\d*\.\d+|\d+)", line)

        if exp_match:
            exp.append(float(exp_match.group(1)))

        if act_match:
            act.append(float(act_match.group(1)))

if exp and act:
    r_value, p_value = pearsonr(exp, act)
    print("r-value:", r_value)
    print("p-value:", p_value)
else:
    print("Not enough data for correlation calculation.")
