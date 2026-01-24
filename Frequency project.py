dictionary={'Football':6,'is':6,'the':7,'best':6,'sport':7,'ever':6}
print('\n\n\nThe original dictionary is'+ str(dictionary))

x=int(input('\nWhat number do you want to check the frequency of in this dictionary?\nEnter a number:  '))

res=0
for key in dictionary:
    if dictionary[key]==x:
        res=res+1

print('The frequency of',x,'is',res,'.\n')