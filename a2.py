import matplotlib.pyplot as plt
import csv
import sys

REJECTED_SAMPLE = '-1'
R_EQUALS_T_SAMPLE = '1'
R_EQUALS_F_SAMPLE = '2'

def run():
    if len(sys.argv) > 1:
        if sys.argv[1] == "p1":
            run_rejection_sampling()
        elif sys.argv[1] == "p2":
            run_likelihood_weighting()
    print("Usage: \npython3 a2.py \"p1\" \t to run rejection sampling\npython3 a2.py \"p2\" \t to run likelihood weighting")


# Parse rs_1.csv and plot p(r|s,w) across samples using rejection sampling
def run_rejection_sampling():
    x = []
    y = []
    num_samples = 0
    num_accepted_samples = 0
    num_r = 0

    with open('rs_1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            num_samples += 1
            if row[0] != REJECTED_SAMPLE:
                num_accepted_samples += 1

                if row[0] == R_EQUALS_T_SAMPLE:
                    num_r += 1

                if num_accepted_samples > 0:    # guard against division by 0
                    p_r_given_s_w = num_r / num_accepted_samples
                    x.append(num_samples)
                    y.append(p_r_given_s_w)

    plot(x, y, 'Rejection Sampling')
    sys.exit()

def run_likelihood_weighting():
    x = []
    y = []
    num_samples = 0
    total_weight = 0

    with open('lw_1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            num_samples += 1
            total_weight += float(row[1])

            p_r_given_s_w = total_weight / num_samples
            x.append(num_samples)
            y.append(p_r_given_s_w)

    plot(x, y, 'Likelihood Weighting')
    sys.exit()

# Plots the given x, y into a graph
def plot(x, y, title):
    plt.semilogx(x,y, label='P(r|s,w)')
    plt.xlabel('Number of samples')
    plt.ylabel('P(r|s,w)')
    plt.title(title)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    run()
