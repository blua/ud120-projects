#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Number of POIs

print "Number of POIs:"

count = 0
for i in enron_data:
    if enron_data[i]['poi'] == True:
        count += 1
   
print count

#Total value of the stock belonging to James Prentice

print "Total value of the stock belonging to James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]

#Email messages from Wesley Colwell to persons of interest

print "Email messages from Wesley Colwell to persons of interest:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#Value of stock options exercised by Jeffrey K Skilling

print "Value of stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#See all fields

# print enron_data["PRENTICE JAMES"]

#Largest payment

x = {"Skilling":enron_data["SKILLING JEFFREY K"]["total_payments"], "Lay":enron_data["LAY KENNETH L"]["total_payments"],\
"Fastow":enron_data["FASTOW ANDREW S"]["total_payments"]}

biggest_crook = max(x, key=x.get)

print "Total payments:", biggest_crook, x[biggest_crook]

#How many have salary

count_sal = 0
    
for i in enron_data:
    if enron_data[i]["salary"] != 'NaN':
        count_sal += 1

print "People with numerical salaries:", count_sal

#How many have emails

count_ea = 0

for i in enron_data:
    if enron_data[i]["email_address"] != 'NaN':
        count_ea += 1

print "People with known email address:", count_ea

#NaN total payments

count_tp = 0

for i in enron_data:
    if enron_data[i]["total_payments"] == 'NaN':
        count_tp += 1
        
total_ppl = len(enron_data) * 1.00

print "People with NaN total payments:", count_tp, " - ", count_tp / total_ppl, " of the dataset"

#POIs with Nan total payments

count_poi = 0
count_ptp = 0

for i in enron_data:
    if enron_data[i]["poi"] == True:
        count_poi += 1
        if enron_data[i]["total_payments"] == 'NaN':
            count_ptp += 1
        
ratio = 1.0 * count_ptp / count_poi

print "POIs with NaN total payments:", count_ptp, " - ", ratio, " of the dataset"

#Plus 10 ppl

print "Total:", len(enron_data) + 10, count_tp + 10, "without total payments"


