
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

from applicationResults import print_action_summary
from county import print_county_summary, get_county_summary
from disparate_rates import compute_disparate_approval_rates, plot_disparate_approval_rates
from race import print_race_codes, print_race_summary, get_race_summary

# Read
hmda = pd.read_csv('datasets/2017nj.csv', low_memory=False, na_values=["NA", "Exempt", ""])
hmda = hmda.apply(pd.to_numeric, errors='ignore')

# Drop cols w/ missing values > 50%
threshold = len(hmda) * 0.5
hmda = hmda.dropna(thresh=threshold, axis=1)

# Drop rows missing key variables
hmda = hmda.dropna(subset=["loan_amount_000s", "applicant_income_000s"])

##############
print()
print()
print()
#############





print_action_summary(hmda)
print_county_summary(hmda, county_column='county_name')  # or 'county' if different
print_race_summary(hmda)


##############
print()
print()
print()
#############


# Analyze approval rates by race
race_summary = compute_disparate_approval_rates(hmda, group_col='applicant_race_1')
plot_disparate_approval_rates(race_summary, group_col='applicant_race_1')

# You can repeat this for other groupings too:
# sex_summary = compute_disparate_approval_rates(hmda, group_col='applicant_sex')
# plot_disparate_approval_rates(sex_summary, group_col='applicant_sex')