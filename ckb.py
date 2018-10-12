#Convert CKB bank statement
import sys, codecs
import datetime
#open the file. read everything except line with totals
BankStatement = codecs.open(sys.argv[1], 'r', 'cp1251')
TransactionsList = BankStatement.readlines()[:-1]


#open file for writing; append header line.
ManagerStatement = codecs.open(sys.argv[1]+"mng.csv", 'a+', 'utf-8')
ManagerStatement.write("Date, Description, Amount\n")

#list to select just the needed elements
SelectList = [1, 5 ,6, 9]
print("IBORN.NET - Central Cooperative Bank MK Bank statement processor - version 1.0")
print("Started processing at {0}.".format(datetime.datetime.now()))
for Transaction in TransactionsList:

    DateDescriptionAmmoutList = []
    TransactionElements=(Transaction.split("\t"))

    #Remove elements from list. Keep only 1, 5, 6, and 9.
    NewList = [TransactionElements[i] for i in SelectList]

    DateDescriptionAmmoutList.append(NewList[0])
    DateDescriptionAmmoutList.append(NewList[3].replace(","," "))

    #Make 5 from SelectList to be a negative number.
    #Format numbers with comma for decimal value

    if float(NewList[1]) != 0:
        DateDescriptionAmmoutList.append("-"+(NewList[1].replace(".",",")))

    if float(NewList[2]) != 0:
        DateDescriptionAmmoutList.append(NewList[2].replace(".",","))

    #convert list to string in order to write to file
    SaveString = ",".join(DateDescriptionAmmoutList)
    ManagerStatement.write(SaveString + "\n")

#close files
BankStatement.close()
ManagerStatement.close()
print("Successfully processed the bank file {0}".format(sys.argv[1]+'-mng.csv'))
print("Finished processing at {0}.".format(datetime.datetime.now()))
