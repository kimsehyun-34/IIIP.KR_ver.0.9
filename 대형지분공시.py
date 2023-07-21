import OpenDartReader
import csv, time, pandas as pd

api_key = 'b450cf721bdcf41b18581e862c341289b26be197'

dart = OpenDartReader(api_key) 

def 지분공시():
    with open('지분공시\coper.txt', "r", encoding='utf-8') as f: #txt읽기
        coper = f.read()
        f.close()
        
    now = time
    d = str(now.localtime().tm_mday)
    h = str(now.localtime().tm_hour)
    mi = str(now.localtime().tm_min)

    mol_P=dart.major_shareholders(coper)
    print(coper)
    
    mol_P=str(mol_P)
    mol_P = mol_P.replace('                                ', '&')
    mol_P = mol_P.replace('                               ', '&')
    mol_P = mol_P.replace('                              ', '&')
    mol_P = mol_P.replace('                             ', '&')
    mol_P = mol_P.replace('                            ', '&')
    mol_P = mol_P.replace('                           ', '&')
    mol_P = mol_P.replace('                          ', '&')
    mol_P = mol_P.replace('                         ', '&')
    mol_P = mol_P.replace('                        ', '&')
    mol_P = mol_P.replace('                       ', '&')
    mol_P = mol_P.replace('                      ', '&')
    mol_P = mol_P.replace('                     ', '&')
    mol_P = mol_P.replace('                    ', '&')
    mol_P = mol_P.replace('                   ', '&')
    mol_P = mol_P.replace('                  ', '&')
    mol_P = mol_P.replace('                 ', '&')
    mol_P = mol_P.replace('                ', '&')
    mol_P = mol_P.replace('               ', '&')
    mol_P = mol_P.replace('              ', '&')
    mol_P = mol_P.replace('             ', '&')
    mol_P = mol_P.replace('            ', '&')
    mol_P = mol_P.replace('           ', '&')
    mol_P = mol_P.replace('          ', '&')
    mol_P = mol_P.replace('         ', '&')
    mol_P = mol_P.replace('        ', '&')
    mol_P = mol_P.replace('       ', '&')
    mol_P = mol_P.replace('      ', '&')
    mol_P = mol_P.replace('     ', '&')
    mol_P = mol_P.replace('    ', '&')
    mol_P = mol_P.replace('   ', '&')
    mol_P = mol_P.replace('  ', '&')
    
    with open('mil_file\mol_P.txt', "w", encoding='utf-8') as f:
        data = mol_P
        f.write(data)
        
    xf=d+h+mi+'mol_P.xlsx'

    df = pd.read_csv('mil_file\mol_P.txt',sep='&',encoding='utf-8')
    df.to_excel(xf,index=True)