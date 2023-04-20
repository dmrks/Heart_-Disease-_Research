# import libraries
import codecademylib3
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

#1
chol_hd =yes_hd.chol

#2 AVG 251.4748201438849, higher than 240 mg/dl
print(chol_hd.mean())
chol_mean = chol_hd.mean()

#3 +4 0.0035411033905155707 < 0.05 => Significant, mean Patients have a higher Cholestrol Level than 240 mg/dl
from scipy.stats import ttest_1samp

tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

#5 0.0035411033905155707 < 0.05 => Significant, mean Patients have a higher Cholestrol Level than 240 mg/dl

no_chol_hd =no_hd.chol

#5 AVG 242.640243902439, higher than 240 mg/dl
no_chol_mean = no_chol_hd.mean()
print(no_chol_mean)

#5.26397120232220506 > 0.05 => UNSignificant, mean Patients have a lower Cholestrol Level than 240 mg/dl

tstat, pval = ttest_1samp(no_chol_hd, 240)
print(pval/2)

#6 303 = number of patients
num_patients = len(heart)
print(num_patients)

#7 45.0 = the number of patients with fasting blood sugar greater than 120

num_highfbs_patients = np.sum(heart.fbs)
print(num_highfbs_patients)

#7 24.0 = the number of patients with fasting blood sugar greater than 120 in the population

pop_high_blood_sugar = 0.08*303
print(pop_high_blood_sugar)

#8+9+10 4.689471951449078e-05 = tThis is less than 0.05, indicating that this sample likely comes from a population where more than 8% of people have fbs > 120 mg/dl.

from scipy.stats import binom_test

p_val = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(p_val)

