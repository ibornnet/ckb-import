# -*- coding: utf-8 -*-
import sys, csv
import datetime
#   Date ValueDate - 13
#   Payee CounterPartyAccountNumber - 12
#   Reference Textbox103 - 18
#   Description   Description3 - 19
#   Amount 
#         Textbox18 (Debit) - 14
#         Textbox15 (Credit) - 15

SelectList = [13, 12, 18, 19, 14, 15]
#ManagerStatement.write("Date, Payee, Reference, Description, Amount\n")
print("Hello and welcome to the IBORN.NET - ProCredit Bank MK Bank statement processor - version 1.0")
print("Started processing at {0}.".format(datetime.datetime.now()))
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
        amount = 0.00
        if float(managerTransactionList[4].replace(',','')) != 0.00:
            amount = "-"+(managerTransactionList[4].replace(',','').replace(".",","))          
        if float(managerTransactionList[5].replace(',','')) != 0.00:
            amount = (managerTransactionList[5].replace(',','').replace(".",","))
        
        del managerTransactionList[4:6]
        managerTransactionList.append(amount)
        #print managerTransactionList
        manager_writer.writerow(managerTransactionList)
        print("Successfully processed transaction {0}".format(transcation_count))
    print("Successfully processed the bank file {0}".format(sys.argv[1]+'-mng.csv'))
    print("Finished processing at {0}.".format(datetime.datetime.now()))
