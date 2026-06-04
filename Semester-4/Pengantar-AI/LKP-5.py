from aima3.csp import *

variables = [
'Tenjo','ParungPanjang','Jasinga','Cigudeg','Rumpin', 
'Sukajaya','Leuwisadeng','Nanggung','Leuwiliang', 
'Cibungbulang','Pamijahan','Ciampea','Tenjolaya','Dramaga' 
]

colors = ['Merah','Hijau','Biru', 'kuning']
domains = {v: colors for v in variables}

neighbors = { 
'Tenjo':['Jasinga','ParungPanjang','Cigudeg'], 
'ParungPanjang':['Tenjo','Rumpin','Cigudeg'], 
'Jasinga':['Tenjo','Cigudeg','Sukajaya'], 
'Cigudeg':['Tenjo','ParungPanjang','Jasinga','Rumpin','Sukajaya','Nanggung','Leuwisadeng'], 
'Rumpin':['ParungPanjang','Cigudeg','Leuwisadeng','Leuwiliang','Cibungbulang'], 
'Sukajaya':['Jasinga','Cigudeg','Nanggung'], 
'Leuwisadeng':['Cigudeg','Nanggung','Leuwiliang','Rumpin'], 
'Nanggung':['Sukajaya','Cigudeg','Leuwisadeng','Leuwiliang'], 
'Leuwiliang':['Nanggung','Leuwisadeng','Rumpin','Pamijahan','Cibungbulang'], 
'Cibungbulang':['Rumpin','Leuwiliang','Pamijahan','Ciampea','Tenjolaya'], 
'Pamijahan':['Leuwiliang','Cibungbulang','Ciampea','Tenjolaya'], 
'Ciampea':['Cibungbulang','Pamijahan','Tenjolaya','Dramaga'], 
'Tenjolaya':['Cibungbulang','Pamijahan','Ciampea','Dramaga'], 
'Dramaga':['Ciampea','Tenjolaya'] 
} 

def constraint(A, a, B, b):
    return a != b

csp = CSP(variables, domains, neighbors, constraint)
solution = backtracking_search(csp)
print(solution)