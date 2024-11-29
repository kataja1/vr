import random

dilers = 0
speletajs = 0
turpinat = True

for i in range(0, 2):
    speletajs += random.randint(1,11)
    dilers += random.randint(1,11)

      
if dilers < 16:
    dilers +=  random.randint(1,11)
    
    if dilers == 21 :
        print('dilers uzvareja D:')    
    elif dilers > 21:
        print('dilers uzvareja :D') 
        
print(dilers)    

while turpinat:
    print(speletajs)
    user = input('panemt vel vienu karti? [Y/N]')
    if user == 'N' or user == 'n':
        break
    speletajs += random.randint(1,11)
   
    if speletajs == 21 :
        print('speletajs uzvareja :D')  
        break
    elif speletajs > 21:
        print('speletajs uzvareja D:')
        break
    