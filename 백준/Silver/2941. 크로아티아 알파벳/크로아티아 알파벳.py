croatia = {0:'c=', 1:'c-', 2:'dz=', 3:'d-', 4:'lj', 5:'nj', 6:'s=', 7:'z='}
li_values = list(croatia.values())
s = input()
sen = ''

for value in li_values:
    if value in s:
        s = s.replace(value, '?')
print(len(s))
        
    

