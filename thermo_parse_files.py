import csv

def parse_gas_compounds(path):
    gas_elements=[]
    f = csv.reader(open(path, "rU"), dialect=csv.excel_tab)
    for row in f:
        gas_elements.append(row[0].split(","))
    for i in gas_elements:
        if i[1].find('0') != -1:
            i[1]=i[1].replace(i[1][i[1].find('0')],u'\u2080')
        if i[1].find('1') != -1:
            i[1]=i[1].replace(i[1][i[1].find('1')],u'\u2081')
        if i[1].find('2') != -1:
            i[1]=i[1].replace(i[1][i[1].find('2')],u'\u2082')
        if i[1].find('3') != -1:
            i[1]=i[1].replace(i[1][i[1].find('3')],u'\u2083')
        if i[1].find('4') != -1:
            i[1]=i[1].replace(i[1][i[1].find('4')],u'\u2084')
        if i[1].find('5') != -1:
            i[1]=i[1].replace(i[1][i[1].find('5')],u'\u2085')
        if i[1].find('6') != -1:
            i[1]=i[1].replace(i[1][i[1].find('6')],u'\u2086')
        if i[1].find('7') != -1:
            i[1]=i[1].replace(i[1][i[1].find('7')],u'\u2087')
        if i[1].find('8') != -1:
            i[1]=i[1].replace(i[1][i[1].find('8')],u'\u2088')
        if i[1].find('9') != -1:
            i[1]=i[1].replace(i[1][i[1].find('9')],u'\u2089')
        if i[0].find('_') != -1:
            i[0]=i[0].replace(i[0][i[0].find('_')],',')
    
    gas_mass=[]
    gas_compounds=[]
    for i in gas_elements:
        gas_compounds.append(i[0] + ' == ' + i[1])
        gas_mass.append(float(i[2]))
    gas_compounds = tuple(gas_compounds)
    return gas_compounds
