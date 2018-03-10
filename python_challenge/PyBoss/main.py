import os
import csv

emp1 = os.path.join('raw_data', 'employee_data1.csv')
emp2 = os.path.join('raw_data', 'employee_data2.csv')

empid = []
first = []
last = []
dob = []
ssn = []
state = []
ssnshort = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# create a new file to write to 
output = os.path.join('newemp.csv')

with open(emp1, 'r') as emp1r:
    csvreader = csv.reader(emp1r, delimiter=',')
    next(csvreader)
    for row in csvreader:
        
        firstnew,lastnew = row[1].split(' ')
        first.append(firstnew)
        last.append(lastnew)
        empid.append(row[0])    
        dob.append(row[2])
        
        ssnshort = "***-**-"+row[3].split('-')[2]
        ssn.append(ssnshort)
#        ssn.append(row[3])
#        state.append(row[4])

        # update state  
        for key in us_state_abbrev:
            if key == row[4]:
                stateAB=us_state_abbrev[key]
#                state.appened(stateAB)


#    for row in csvreader:
#        dob = 
for item in ssn: 
    ssnshort = "***-**" + ssn.split("-")[2]
    ssn.append(ssnshort)

# Zip lists together into tuples
employees = zip(empid, first, last, dob, ssn, state)

# Open the file using "write" mode. Name the headers. 
with open(output, "w", newline="") as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # write header row
    csvwriter.writerow(["EmpID", "First","Last","DOB", "SSN", "State"])
    csvwriter.writerows(employees)
#    
#    csvwriter.writerow([first])
#    csvwriter.writerow([last]) 
#    csvwriter.writerow([dob])
#    csvwriter.writerow([ssn])
#    csvwriter.writerow([state]) 
    

