import pandas as pd
import os


df = pd.read_feather('output/input.feather')

summary1 = df.groupby('practice_enrolled')["patient_id"].count()
summary1.to_csv(os.path.join("output","summary1.csv"))
print(summary1)

df = df.loc[df['practice_enrolled']==True]
summary2 = df.groupby('practice_trial_arm')["patient_id"].count()
print(summary2)
summary2.to_csv(os.path.join("output","summary2.csv"))

summary3 = df.groupby('practice_deprivation_pctile')["patient_id"].count()
print(summary3)
summary3.to_csv(os.path.join("output","summary3.csv"))
