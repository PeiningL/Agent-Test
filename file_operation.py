import xlrd
import xlwt
import sys
import csv
from agent import Agent

def create_csv(filepath):
    workbook = xlrd.open_workbook(filepath)
    with open('csvdata.csv','wb') as myFile:
        myWriter = csv.writer(myFile)
        booksheet = workbook.sheet_by_index(0)
        sheet = workbook.sheet_by_index(0)
        for row in range(0, booksheet.nrows):
            rows = sheet.row_values(row)
            myWriter.writerow(rows)
    return

def data_initialize():
    Agentset = []
    with open('csvdata.csv','r') as myFile:
        myReader = csv.DictReader(myFile)
        for row in myReader:
            Agentset.append(Agent(row["Agent_Breed"], row["Policy_ID"], row["Age"], row["Social_Grade"], row["Payment_at_Purchase"],
                      row["Attribute_Brand"], row["Attribute_Price"], row["Attribute_Promotions"], row["Auto_Renew"], row["Inertia_for_Switch"]))
    return Agentset

def export(filename, Agentset):
    with open(filename, 'w') as myFile:
        fieldnames = ["Agent_Breed", "Policy_ID", "Age", "Social_Grade", "Payment_at_Purchase", "Attribute_Brand",
                          "Attribute_Price", "Attribute_Promotions", "Auto_Renew", "Inertia_for_Switch"]

        myWriter = csv.DictWriter(myFile, fieldnames=fieldnames)
        myWriter.writeheader()
        rows = [{
                        "Agent_Breed": agent.Agent_Breed,
                        "Policy_ID": agent.Policy_ID,
                        "Age": str(agent.Age),
                        "Social_Grade": str(agent.Social_Grade),
                        "Payment_at_Purchase": str(agent.Payment_at_Purchase),
                        "Attribute_Brand": str(agent.Attribute_Brand),
                        "Attribute_Price": str(agent.Attribute_Price),
                        "Attribute_Promotions": str(agent.Attribute_Promotions),
                        "Auto_Renew": str(agent.Auto_Renew),
                        "Inertia_for_Switch": str(agent.Inertia_for_Switch)
                } for agent in Agentset]
        myWriter.writerows(rows)









