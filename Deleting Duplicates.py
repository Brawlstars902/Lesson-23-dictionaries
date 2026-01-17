student_data={'Identity_1':{
    'Name':'Lucas'
    ,'Age':'16'
    ,'Class':'10'
    ,'Subjects':['P.E.','Maths','Chinese','Science']
    },
    'Identity_2':{
        'Name':'Eddie'
        ,'Age':'11'
        ,'Class':'6'
        ,'Subjects':['P.E','Geography','History','English']
    },
    'Identity_3':{
        'Name':'Lucas'
        ,'Age':'16'
        ,'Class':'10'
        ,'Subjects':['P.E.','Maths','Chinese','Science']
    },
    'Identity_4':{
        'Name':'Eddie'
        ,'Age':'11'
        ,'Class':'6'
        ,'Subjects':['P.E','Geography','History','English']
    },

}

result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)