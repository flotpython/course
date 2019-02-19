# pylint: disable=c0111
from nbhosting.courses import (
    Sections, Section, Notebook,
    notebooks_by_pattern, sections_by_directory)

def sections(coursedir, viewpoint):
    """
    coursedir allows for pattern-matching approches
    """

    if viewpoint == "exos":
        return sections_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, "w?/w*-s*-x*.ipynb"))

    # test the generic sectioning algo
    if viewpoint == "default":
        return sections_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, "w?/w*-s*-[cx]*.ipynb"))

    # default for viewpoint is 'course'
    if viewpoint == "course":
        # this for now is just some random selection
        # for testing manual sectioning
        weeks = [
            "Prise en mains",
            "Types de base / Syntaxe",
            "Renforcements / Références partagées",
            "Fonctions / Portée des variables",
            "Itération / Importation",
            "Classes",
            "Écosystème data science",
            "Programmation asynchrone",
            "Sujets avancés",
        ]
        sections = [
            Section(coursedir=coursedir,
                    name=week,
                    notebooks=notebooks_by_pattern(
                        coursedir,
                        f"w{w}/w*-s*-[cx]*.ipynb"))
            for (w, week) in enumerate(weeks, 1)]
        return Sections(sections)
