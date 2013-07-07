# -*- coding: cp936 -*-
import xlrd



sheet=xlrd.open_workbook("d:\\recommendation\\recommendation\\recommendation\\ratings.xls").sheet_by_index(0)

def buildCritics_user(sheet):
    critics={}
    for irow in range(sheet.nrows):
        user="%d" % sheet.cell(irow, 1).value
        film="%d" % sheet.cell(irow, 0).value
        critics.setdefault(user, {})
        critics[user].setdefault(film, 0)
        critics[user][film]=sheet.cell(irow, 2).value
    return critics

def buildCritics_item(sheet):
    critics={}
    for irow in range(sheet.nrows):
        user="%d" % sheet.cell(irow, 2).value
        film="%d" % sheet.cell(irow, 1).value
        critics.setdefault(film, {})
        critics[film].setdefault(user, 0)
        critics[film][user]=sheet.cell(irow, 2).value
    return critics
#print len(critics)
#n = 0
#for item in critics:
#    n = n+len(item)
#print n