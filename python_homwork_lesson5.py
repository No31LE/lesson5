score_list = list()
people = int(input('''amount of people?
'''))


for i in range(1,people + 1):
    score_list.append(int(input('''score? 1-100
''')))



print ('average:', sum(score_list)/people)
print ('highest',max(score_list))
print ('lowest',min(score_list))