with open('pi_million_digits.txt') as opened_file:
    pi_str = opened_file.read()

if '15927' in pi_str:
    print('yes')
else:
    print('no')