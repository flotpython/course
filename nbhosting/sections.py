# pylint: disable=c0111
from nbhosting.courses import (
    Sections, Section, Notebook,
    notebooks_by_pattern, sections_by_directory)

def sections(coursedir, track):
    """
    coursedir is a CourseDir object that points 
    at the root directory of the filesystem tree
    that holds notebooks
    track is a name that is set by the nbhosting admin,
    by default it is "course" which would mean the full 
    course, but you can define alternate tracks among the
    course material

    result should be a Sections object
    """

    if track == "exos":
        return sections_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, "w?/w*-s*-x*.ipynb"))

    # test the generic sectioning algo
    if track == "default":
        return sections_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, "w?/w*-s*-[cx]*.ipynb"))

    # default for track is 'course'
    if track == "course":
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
        return Sections(coursedir, sections)
