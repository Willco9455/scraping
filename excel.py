import xlsxwriter

class ExcelHandle:
    def __init__(self):
        self.row = 1
        self.workbook = xlsxwriter.Workbook('output.xlsx')
        self.worksheet = self.workbook.add_worksheet()

        bold = self.workbook.add_format({'bold': True})

        self.worksheet.set_column('A:L', 25)
        self.worksheet.write('A1', 'First Names', bold)
        self.worksheet.write('B1', 'Last Name', bold)
        self.worksheet.write('C1', 'Address', bold)
        self.worksheet.write('D1', 'Email', bold)
        self.worksheet.write('E1', 'URL', bold)
        self.worksheet.write('F1', 'Tel', bold)
        self.worksheet.write('G1', 'Fax', bold)
        
    
    def addRow(self, data):
        col = 0
        for i in data:
            self.worksheet.write(self.row, col, i)
            col += 1
        self.row += 1
                
    def close(self):
        self.workbook.close()
        
excelHandle = ExcelHandle()

excelHandle.close()