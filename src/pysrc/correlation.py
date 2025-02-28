from re import search
from scipy.stats import pearsonr

exp = []
act = []

with open("src/pysrc/test_data.txt") as file:
    for line in file:
        exp_match = search(r"Exp: ([+-]?\d*\.\d+|\d+)", line)
        act_match = search(r"Act: ([+-]?\d*\.\d+|\d+)", line)

        if exp_match:
            exp.append(float(exp_match.group(1)))

        if act_match:
            act.append(float(act_match.group(1)))

r_value, p_value = pearsonr(exp, act)

print("r-value: " + str(r_value))
print("p-value: " + str(p_value))
