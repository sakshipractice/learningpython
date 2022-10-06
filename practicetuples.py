T = (1,2)
print(T)
T2 = tuple('string')
print(T2)
T3= (1,2,3,['hello',6],'string', {'name':'steve'})
print(T3)
print(T3[3])                    #accessing data
print(T3[3:])                    #slicing
print(T3.index('string'))         #indexing
print(len(T3))                      #length
T3 +=T3                              #concatenate
print(T3)
print(T3 * 3)                        #repeat
print(T3)