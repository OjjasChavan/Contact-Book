contacts = []
cont_count = 0

while cont_count == 0:
    contNumber = int(input('Enter the contat number:\n'))
    contName = input('Enter the contat name:\n')
    cont_count = cont_count + 1
    contacts.append([contNumber, contName])
    print("Your contact number and name is: ", contacts)
    
    x = input('Do you want to add another contact? Enter yes or no:\n')
    if x == 'yes':
        cont_count = 0
    elif x == 'no':
        cont_count = 1
    else:
        print('Invalid input')
        cont_count = 1

    if len(contacts) > 1:
        print('Your contact numbers and names are: ', contacts)
    else:
        print('Your contact number and name is: ', contacts)

    x = len(contacts) 

    if x > 1:
        print('your list of contacts are: ', x)
    else:
        print('your list of contacts is: ', x)
