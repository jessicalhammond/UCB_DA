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
        #append EMPID 
        empid.append(row[0]) 
        
        #split f/l and append
        firstnew,lastnew = row[1].split(' ')
        first.append(firstnew)
        last.append(lastnew)
        
        #format date and append
        year,month,day = row[2].split('-')
        date = (month + "/" + day + "/" + year)
        dob.append(date)
        
        #format SSN and append
        one,two,three = row[3].split('-')
        ssnnew = ("***-**-" + three)
        ssn.append(ssnnew)
        
        # update state  
        for key in us_state_abbrev:
            if key == row[4]:
                row[4] = us_state_abbrev[key]
                state.append(row[4])
with open(emp2, 'r') as emp2r:
    csvreader = csv.reader(emp2r, delimiter=',')
    next(csvreader)
    for row in csvreader:
        #append EMPID 
        empid.append(row[0]) 
        
        #split f/l and append
        firstnew,lastnew = row[1].split(' ')
        first.append(firstnew)
        last.append(lastnew)
        
        #format date and append
        year,month,day = row[2].split('-')
        date = (month + "/" + day + "/" + year)
        dob.append(date)
        
        #format SSN and append
        one,two,three = row[3].split('-')
        ssnnew = ("***-**-" + three)
        ssn.append(ssnnew)
        
        # update state  
        for key in us_state_abbrev:
            if key == row[4]:
                row[4] = us_state_abbrev[key]
                state.append(row[4])
                
# Zip lists together into tuples
employees = zip(empid, first, last, dob, ssn, state)

# Open the file using "write" mode. Name the headers. 
with open(output, "w", newline="") as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # write header row
    csvwriter.writerow(["EmpID", "First","Last","DOB", "SSN", "State"])
    #write zip employee rows
    csvwriter.writerows(employees)


