from nbhosting.courses import (
    Section, notebooks_by_pattern, group_by_directories)

def sections(root, viewpoint):
    """
    root is the expanded course root, for mattern-matching approches
    """

    if viewpoint == "exos":
        return group_by_directories(
            root,
            notebooks_by_pattern(root, "w?/w*-s*-x*.ipynb"))

    if viewpoint == "manual":
        # this for now is just some random selection
        # for testing manual sectioning
        return [
            Section(root=root,
                    name="Intro",
                    notebooks=[
                        "w1/w1-s1-c1-versions-python.ipynb",
                        "w1/w1-s4-c2-interpreteur-et-notebooks.ipynb",
                        "w1/w1-s6-x1-flottants.ipynb",
                    ] + notebooks_by_pattern(root, "w2/*ipnb")),
            Section(root=root,
                    name="numpy",
                    notebooks=notebooks_by_pattern(root, "w7/w7-s*-[cx]*"))
        ]

    # default is for viewpoint == 'course'
    return group_by_directories(     # default is "course":
        root,
        notebooks_by_pattern(root, "w?/w*-s*-[cx]*.ipynb"))
