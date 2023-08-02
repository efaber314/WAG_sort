#Wag matching software
#emily Faber - efaber1@umbc.edu
#Spring 2023

import pandas as pd

filename = ('TEST_SPREADSHEET.csv')

df = pd.read_csv(filename, low_memory = False)
print(df)
print(df.keys())
leaders = df[df['Would you like to lead a group?'] == 'Yes']
remaining_wagers = df[df['Would you like to lead a group?'] == 'No']
print(leaders)
print(remaining_wagers)
# remaining_wagers_names = list(remaining_wagers['Name'])
def group_divide(list, number):
    for i in range(0, len(list), number):
        yield list[i:i+number]
groups_suggestion = list(group_divide(list(remaining_wagers['Name']),5))
print(groups_suggestion)

f  = open("SuggestedGroups.txt", "w+")
f.write('LEADERS')
f.write(str(leaders))
f.write('SUGGESTED GROUPS')
f.write(str(groups_suggestion))
f.close()
# TimeOfDayGroups = remaining_wagers.groupby(by = 'What time of day do you prefer?')
# # print(TimeOfDayGroups)
# for Name,Pronouns in TimeOfDayGroups:
#    print(Name)
#    print(Pronouns)

# list_of_groups = zip(*(iter(list(df['Name and pronouns'])),) * 5)
# print(str(list_of_groups))
# print(zip(*(iter(df['Name and pronouns']),) * 3))
# inPerson = df.loc[df['I would prefer to meet in person.'] == 'No']
# print(inPerson)
# inPerson = df.groupby(by = ['I would prefer to meet in person.']).reset_index()
# inPerson = inPerson.reset_index()
# print(inPerson)
# LongGroups = df.groupby(by = ['Pick times that work for you', 'Pick places that work for you'])['Email Address'].size().reset_index()
# # print(LongGroups.head())
# # LongGroups.reset_index()
# # LongGroups.reset_index(inplace = True).to_csv('Groups' + filename + '.csv')
# # print(LongGroups)
# LongGroups.to_csv('Groups' + filename + '.csv')

# LongGroups.to_csv('Groups' + filename + '.csv')
