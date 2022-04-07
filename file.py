f1 = open('pd.txt', 'r')
f2 = open('arabe.pyw', 'w')

for line in f1:
    line = line.replace('nameeftp', 'NIQUETAMERE')
    line = line.replace('usernameftp', "FILSDEPUTE")
    line = line.replace('passwordftp', 'SALEFILSDEPUTE')
    line = line.replace('temps', '60')
    f2.write(line)
f1.close()
f2.close()