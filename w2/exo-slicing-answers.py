import string
chaine = string.lowercase

print 'question 1', chaine [-5:-2]

print 'question 2', chaine [ -4: ]

print 'question 3', chaine [ 3::2 ]

print 'question 4', chaine [ -3::-3 ]

connue = 'abcd'
composite = 'abcd0123456789abcd'

print 'question 5', composite [ len(connue) : -len(connue) ]
