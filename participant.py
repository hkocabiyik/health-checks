# Define a list of participant
participant= ['Monalisa', 'Akbar Hossain', 'Jakir Hasan', 'Zahadur Rahman', 'Zenifer Lopez']
# Define the function to filters selected candidates
def SelectedPerson(participant):
    selected = ['Akbar Hossain', 'Zillur Rahman', 'Monalisa']
    if(participant in selected):
        return True
selectedList = filter(SelectedPerson, participant)
print('The selected candidates are:')
for candidate in selectedList:
    print(candidate)
print('The unselected candidates are:')
print('The statement is for the new Branch -Refactor-')
