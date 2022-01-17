from nbautoeval import ExerciseGenerator, GeneratorArgs, PPrintRenderer


# @BEG@ name=primes
import math
import itertools

def primes():
    """
    enumerate prime numbers
    """
    # the primes we have found so far
    previous = [2, 3]
    yield 2
    yield 3
    # consider only odd numbers
    for n in itertools.count(5, 2):
        # deemed prime until we find a divisor
        is_prime = True
        # no need to go beyond this
        root = math.sqrt(n)
        # try only primes
        for i in previous:
            # above root, no need to go on
            if i > root:
                break
            # a divisor is found
            # no need to go on either
            if n % i == 0:
                is_prime = False
                break
        # yield, and record in previous
        if is_prime:
            previous.append(n)
            yield n
# @END@

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
    result_renderer=PPrintRenderer(width=30),
)

primes_ko = itertools.count



# prime-squares

# @BEG@ name=prime_squares
def prime_squares():
    """
    iterates over the squares of prime numbers
    """
    # a generator expression is the most obvious way that springs to mind
    return (prime**2 for prime in primes())
# @END@


# @BEG@ name=prime_squares more=bis
def prime_squares_bis():
    """
    same using a generator function
    """
    # a generator expression is the most obvious way that springs to mind
    for prime in primes():
        yield prime**2
# @END@


prime_squares_args = [
    GeneratorArgs(islice=(10,)),
]

exo_prime_squares = ExerciseGenerator(
    prime_squares, prime_squares_args,
    max_iterations=100,
    result_renderer=PPrintRenderer(width=30),
)



### LEGOs

# @BEG@ name=prime_legos
import itertools

def prime_legos():
    """
    iterates over shifted primes (with a 5-items padding with 1s)
    and over primes squares
    """
    part1 = itertools.chain(itertools.repeat(1, 5), primes())
    part2 = (prime**2 for prime in primes())
    return zip(part1, part2)
# @END@


# @BEG@ name=prime_legos more=bis
import itertools

def prime_legos_bis():
    """
    same behaviour
    we optimize CPU performance by creating a single instance
    of the primes() generator, and duplicate it using `itertools.tee()`
    """
    # this is where the pseudo-copy takes place
    primes1, primes2 = itertools.tee(primes(), 2)
    # the rest is of course the same as in the naive version
    part1 = itertools.chain(itertools.repeat(1, 5), primes1)
    part2 = (prime**2 for prime in primes2)
    return zip(part1, part2)
# @END@


args_prime_legos = [
    GeneratorArgs(islice=(10,)),
    GeneratorArgs(islice=(50, 100, 10)),
]

exo_prime_legos = ExerciseGenerator(
    prime_legos, args_prime_legos,
    max_iterations=101,
    nb_examples=0,
    result_renderer=PPrintRenderer(width=30),
)

def prime_legos_ko():
    return zip(primes(), primes())



# prime-th-primes

# @BEG@ name=prime_th_primes
def prime_th_primes():
    """
    iterate the n-th prime number, with n it self being prime

    given that primes() emits 2, 3, 5
    then prime_th_primes() starts with 5 which has index 2 in that enumeration
    """
    # optimizing a bit, don't compute primes twice
    primes1, primes2 = itertools.tee(primes())

    # current will scan all prime numbers
    current = next(primes1)
    # index will scan all integers
    for index, prime in enumerate(primes2):
        # when it matches 'current' it means we have a winner
        if index == current:
            yield prime
            current = next(primes1)
# @END@


# @BEG@ name=prime_th_primes more=bis
def prime_th_primes_bis():
    """
    same purpose

    this approach is a little more manual
    as we do our own calls to next()

    """
    # optimizing a bit, don't compute primes twice
    primes1, primes2 = itertools.tee(primes())

    # this start with -1 because it's a number of times we need to do next()
    # and, as opposed with usual indexing that starts at 0
    # to get item at index 0 we need to do ONE next()
    current_index = -1

    while True:
        # what's the next prime index
        next_index = next(primes1)
        # the amount of times we must iterate on primes2
        offset = next_index - current_index
        # move primes2 forward that many times
        for _ in range(offset):
            output = next(primes2)
        # we have a winner
        yield output
        # this is where we are, so we can compute the next hop
        current_index = next_index
# @END@


args_prime_th_primes = [
    GeneratorArgs(islice=(10,)),
    GeneratorArgs(islice=(1, 20, 2)),
]

exo_prime_th_primes = ExerciseGenerator(
    prime_th_primes, args_prime_th_primes,
    max_iterations=50,
    result_renderer=PPrintRenderer(width=30),
)

def prime_th_primes_ko():
    return itertools.islice(prime_th_primes(), 1, None)




###
# not yet operational
# requires nbautoeval features that are not yet ready
# 0.6.1 was badly broken
def differential(iterator):
    previous = next(iterator)
    while True:
        current = next(iterator)
        yield current - previous
        previous = current


def squares():
    return (i**2 for i in itertools.count())

differential_args = [
    GeneratorArgs(itertools.count(), islice=(10,)),
    GeneratorArgs(squares(), islice=(10,)),
]

exo_differential = ExerciseGenerator(
    differential, differential_args,
    max_iterations=200,
    result_renderer=PPrintRenderer(width=30),
)

differential_ko = lambda : (2*n+1 for n in itertools.count())
