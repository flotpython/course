"""
This module is for nbhosting

is describes the tracks available in the course,
and for each of them provides a more legible
sectioning than the one we could guess from the file system names

NOTE that notebook metadata like a human-friendly name can be provided
in the 'notebookname' and 'version' metadata keys

so as far as individual notebooks are concerned,
it's enough to provide notebook paths;
however it is desirable to provide also a human-friendly name for each section,
which cannot be found elsewhere on the disk.
"""
from nbhosting.courses import (
    Sections, Section, Notebook,
    notebooks_by_pattern, sections_by_directory,
    DEFAULT_TRACK)


WEEK_NAMES = {
    'w1': "1. Prise en mains",
    'w2': "2. Types de base / Syntaxe",
    'w3': "3. Renforcements / Références partagées",
    'w4': "4. Fonctions / Portée des variables",
    'w5': "5. Itération / Importation",
    'w6': "6. Classes",
    'w7': "7. Écosystème data science",
    'w8': "8. Programmation asynchrone",
    'w9': "9. Sujets avancés",
}

def _exo_track(coursedir):
    return sections_by_directory(
        coursedir,
        notebooks_by_pattern(coursedir, "w?/w*-s*-x*.ipynb"),
            dir_labels = WEEK_NAMES)


# mostly for testing the generic sectioning code
def _generic_track(coursedir):
    return sections_by_directory(
        coursedir,
        notebooks_by_pattern(coursedir, "w?/w*-s*-[cx]*.ipynb"))


def _course_track(coursedir):
    # a more elaborate sectioning, still based
    # on the filesystem structure but with better names
    return sections_by_directory(
        coursedir,
        notebooks_by_pattern(coursedir, f"w?/w*-s*-[cx]*.ipynb"),
        dir_labels = WEEK_NAMES)


def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks

    this returns a dictionary that maps track names to sectioning data

    it can be either a single Sections object,
    or if you want to define several tracks, a dictionary
    'track_name' -> Sections obj

    in the latter case, it is expected that the dictionary
    contains a key named 'course'
    """

    return {
        'exos': _exo_track(coursedir),
#        'generic': _generic_track(coursedir),
        DEFAULT_TRACK: _course_track(coursedir),
    }
