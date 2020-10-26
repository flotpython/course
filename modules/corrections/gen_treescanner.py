from nbautoeval import (ExerciseGenerator, GeneratorArgs, 
                        PPrintRenderer, PPrintCallRenderer)


# @BEG@ name=treescanner
def treescanner(tree):
    """
    enumerate all leaves in a tree
    """
    # a typical example where
    # the 'yield from' statement 
    # is the only way to go
    if isinstance(tree, list):
        for subtree in tree:
            yield from treescanner(subtree)
    else:
        yield tree
# @END@

def tree(offset, width, depth):
    """
    one root, width sons, width**2 grandsons
    """
    def build(width, depth):
        if depth == 0:
            return [0]
        else:
            return [build(width, depth-1) for _ in range(width)]
    def number_leaves(tree, value):
        for i, subtree in enumerate(tree):
            if not isinstance(subtree, list):
                tree[i] = value
                value += 1
            else:
                value = number_leaves(subtree, value)
        return value
    raw = build(width, depth)
    number_leaves(raw, offset)
    return raw

T1 = [tree(1, 2, 2), tree(10, 3, 2), tree(20, 2, 3), 50, tree(100, 2, 4)]

T2 = tree(1, 2, 5)


treescanner_args = [
    GeneratorArgs([], islice=(1000,)),
    GeneratorArgs(0, islice=(1000,)),
    GeneratorArgs([0], islice=(1000,)),
    GeneratorArgs([[0]], islice=(1000,)),
    GeneratorArgs([1, [2]], islice=(1000,)),
    GeneratorArgs([[1, 2], 3, [4, 5]], islice=(1000,)),
    GeneratorArgs(T1, islice=(1000,)),
    GeneratorArgs(T2, islice=(1000,)),
]

# max_iterations is mostly a provision to avoid endless loops
exo_treescanner = ExerciseGenerator(
    treescanner, treescanner_args, max_iterations=100,
    nb_examples=6,
    result_renderer=PPrintRenderer(width=40),
    call_renderer=PPrintCallRenderer(width=40),
)
