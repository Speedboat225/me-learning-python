

student_data= { 
    "id1": {"name":['Aarav'],"class":["grade5"],"subject":["English","Math","Science"]},

"id2" : {"name":["william shakesphere"], "class":["graduated"], "subject":["english", "english literature"]
         },

"id3" : {"name":["little timmy"], "class":["kindergarten"], "subject":["maff", "engish"]
         },

"id4" : {"name":["Rohan"], "class":["6"], "subject":["Economics", "History","French"]
         }}  

result= {}

for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)