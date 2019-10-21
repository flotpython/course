from itertools import count

from nbautoeval import ExerciseGenerator, GeneratorArgs

def primes():
    """
    enumerate prime numbers
    """
    # the set of primes we have found so far
    # so we avoid divisions by non-primes
    cache_primes = set()
    
    for n in count(2):
        for i in range(2, n):
            # no need to try to divide by non-primes
            if i not in cache_primes:
                continue
            # not a prime, go to n+1
            if n % i == 0:
                break
        # remember that a 'for' statement 
        # can be attached an 'else' which
        # gets executed when no 'break' statement has triggered
        # in our case, we run this 'else' part when n is prime
        else:
            # n is prime, remember it for the rest of the enumeration
            cache_primes.add(n)
            yield n
            
primes_args = [
    GeneratorArgs(islice=(20,)),
    GeneratorArgs(islice=(1, 6, 2)),
    GeneratorArgs(islice=(10, 20, 2)),
    GeneratorArgs(islice=(98, 101)),
]

# max_iterations is mostly a provision to avoid endless loops
exo_primes = ExerciseGenerator(
    primes, primes_args, max_iterations=501,
    nb_examples=0,
)