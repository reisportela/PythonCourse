# Setup Stata
import stata_setup
stata_setup.config("C:/Program Files/Stata17", "se")

# Import json data
from pandas.io.json import json_normalize
import json
with open("did.json") as json_file:
    data = json.load(json_file)
data = json_normalize(data, 'records', ['hospital_id', 'month'])

# Load data to Stata
from pystata import stata
stata.pdataframe_to_data(data, True)

# Run block of Stata code 
stata.run('''
destring satisfaction_score, replace
destring hospital_id, replace
destring month, replace

gen proc = 0
replace proc = 1 if procedure == "New"
label define procedure 0 "Old" 1 "New"
drop procedure
rename proc procedure
label value procedure procedure
''', quietly=True)

stata.run('''
didregress (satisfaction_score) (procedure), group(hospital_id) time(month)
''', echo=True)

# Load Stata results to Python
r = stata.get_return()['r(table)']

# Use Stata results in Python
print("The treatment hospitals had a %4.2f-point increase." 
      % (r[0][0]), end=" ") 
print("The result is with 95%% confidence interval [%4.2f, %4.2f]." 
      % (r[4][0], r[5][0]))

# Generate Stata graph 
stata.run("estat trendplots", quietly=True)
stata.run("graph export did.svg, replace", quietly=True)
