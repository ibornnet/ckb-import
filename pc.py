# -*- coding: utf-8 -*-
import sys, csv
#   Date ValueDate - 13
#   Payee Textbox64 - 0
#   Reference Textbox103 - 18
#   Description   Description3 - 19
#   Amount Textbox33 - 5
SelectList = [13, 0, 18, 19, 5]
#ManagerStatement.write("Date, Payee, Reference, Description, Amount\n")
print("Hello and welcome to the IBORN.NET - ProCredit Bank MK Bank statement processor") 
with open(sys.argv[1]+'-mng.csv', mode='wb') as manager_csv, open(sys.argv[1]) as csvfile:
    manager_writer = csv.writer(manager_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    manager_writer.writerow(['Date', 'Payee', 'Reference', 'Description', 'Amount'])
    bankstatement = csv.reader(csvfile, delimiter=',')
    next(bankstatement, None)     
    transcation_count = 0
    for transaction in bankstatement:
        transcation_count = transcation_count+1
        print("Processing transaction {0}".format(transcation_count))  
        if not (transaction):
            print("Detected empty transaction. Skipping.")  
            continue   
        managerTransactionList = [transaction[i] for i in SelectList]
        managerTransactionList = [x.strip(' ').replace(',','').replace('"','') for x in managerTransactionList]
        manager_writer.writerow(managerTransactionList)
        print("Successfully processed transaction {0}".format(transcation_count))
print("Successfully processed the bank file {0}".format(sys.argv[1]+'-mng.csv'))
