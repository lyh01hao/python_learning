def is_palindrome(n):
    return str(n) == str(n)[::-1]

l = [12, 2332, 3443, 5678]
r = filter(is_palindrome, l)
for i in r:
    print(i)
