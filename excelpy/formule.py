from openpyxl import Workbook

formule = {
    "SUM": "=SUM(A1:A10)",
    "AVERAGE": "=AVERAGE(A1:A10)",
    "MIN": "=MIN(A1:A10)",
    "MAX": "=MAX(A1:A10)",
    "COUNT": "=COUNT(A1:A10)",
    "COUNTA": "=COUNTA(A1:A10)",
    "IF": '=IF(A1>10,"Yes","No")',
    "IFERROR": "=IFERROR(A1/B1,0)",
    "VLOOKUP": "=VLOOKUP(A2,Sheet2!A:B,2,FALSE)",
    "INDEX": "=INDEX(A1:A10,5)",
    "MATCH": '=MATCH("apple",A1:A10,0)',
    "TODAY": "=TODAY()",
    "NOW": "=NOW()",
    "YEAR": "=YEAR(TODAY())",
    "MONTH": "=MONTH(TODAY())",
    "DAY": "=DAY(TODAY())",
    "TEXT": '=TEXT(A1,"0.00")',
    "ROUND": "=ROUND(A1,2)",
    "ROUNDUP": "=ROUNDUP(A1,2)",
    "ROUNDDOWN": "=ROUNDDOWN(A1,2)",
    "ABS": "=ABS(A1)",
    "POWER": "=POWER(A1,2)",
    "SQRT": "=SQRT(A1)",
    "SUMIF": '=SUMIF(A1:A10,">10")',
    "COUNTIF": '=COUNTIF(A1:A10,">10")',
    "AVERAGEIF": '=AVERAGEIF(A1:A10,">10")',
    "SUMIFS": '=SUMIFS(A1:A10,A1:A10,">10")',
    "COUNTIFS": '=COUNTIFS(A1:A10,">10")',
    "AVERAGEIFS": '=AVERAGEIFS(A1:A10,A1:A10,">10")',
    "LEFT": "=LEFT(A1,3)",
    "RIGHT": "=RIGHT(A1,3)",
    "MID": "=MID(A1,2,3)",
    "LEN": "=LEN(A1)",
    "CONCAT": "=CONCAT(A1,B1)",
    "CONCATENATE": "=CONCATENATE(A1,B1)",
    "TRIM": "=TRIM(A1)",
    "UPPER": "=UPPER(A1)",
    "LOWER": "=LOWER(A1)",
    "PROPER": "=PROPER(A1)",
    "SUBTOTAL": "=SUBTOTAL(9,A1:A10)",
    "NETWORKDAYS": "=NETWORKDAYS(A1,B1)",
    "EDATE": "=EDATE(A1,3)",
    "EOMONTH": "=EOMONTH(A1,1)",
    "DATEDIF": '=DATEDIF(A1,B1,"Y")',
    "HLOOKUP": "=HLOOKUP(A1,Sheet2!A1:E5,2,FALSE)",
    "XLOOKUP": "=XLOOKUP(A1,Sheet2!A:A,Sheet2!B:B)",
    "FILTER": "=FILTER(A1:A10,A1:A10>10)",
    "UNIQUE": "=UNIQUE(A1:A10)",
    "SEQUENCE": "=SEQUENCE(5)",
    "CHOOSE": '=CHOOSE(2,"A","B","C")',
}

wb = Workbook()
ws = wb.active

ws['A1'] = 158
ws['A2'] = 45
ws['A3'] = "=SUM(A1:A2)" # formule["SUM"]

wb.save("./excelpy/formula.xlsx")