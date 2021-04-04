from openpyxl import load_workbook


wb = load_workbook("sampl_random_append1.xlsx")

ws= wb.active
ws.insert_cols(2,3)# b 번째열 3열  추가

wb.save("sample_insrt_cols.xlsx")