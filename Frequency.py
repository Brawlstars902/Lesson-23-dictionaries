dictionary={'Football':6,'is':6,'the':7,'best':6,'sport':7,'ever':6}
print('\n\n\nThe original dictionary is'+ str(dictionary))

res=0
for key in dictionary:
    if dictionary[key]==6:
        res=res+1

print('The frequency of 6 is',res,'.\n')