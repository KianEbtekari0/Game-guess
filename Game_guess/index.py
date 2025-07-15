print('    *')
print('   ---')
print('  ------ ')
print(' --------')

print('  --  -- ')
print('   ----  ')
print('What is my name?')
print('guess')

count = 0
limit = 3
name = "kian"
k = "k"
kia = "kia"

while count < limit:
    start = str(input('Guess: '))
    count += 1
    if start == name:
        print('you won!')
        break
    
    if start == k:
        print('one k')

    if start == kia:
        print('mmm.ok')
    
    else:
        print('No...')

else:
    print('sorry, you faild')

if count == 1:
    print('you are very good')

if count == 2:
    print('it was not bad. but you won')

if count == 3:
    print('It was bad, but you won')
