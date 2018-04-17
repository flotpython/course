l1 = [ 'a', 'b', 'c' ]
l2 = [ 1, 2, 3]

tuples_tree = [ [ (x,y) for x in l1] for y in l2]
print 'tuples_tree',tuples_tree

tuples_list = [ (x,y) for x in l1 for y in l2]
print 'tuples_list',tuples_list

tuples = zip(l1,l2) 
print 'tuples obtenus par zip',tuples

simple_hash = { k:v for (k,v) in tuples }
print 'simple_hash',simple_hash

