"""
This module is for nbhosting

is describes the tracks available in the course,
and for each of them provides a more legible sectioning
than the one we could guess from the file system names

NOTE that notebook metadata like a human-friendly name can be provided
in the 'notebookname' and 'version' metadata keys

so as far as individual notebooks are concerned,
it's enough to provide notebook paths;
however it is desirable to provide also a human-friendly
name for each section,
which cannot be found elsewhere on the disk.
"""
from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory)

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

# plain track contains everything under w?
def _course_track(coursedir):
    # a more elaborate sectioning, still based
    # on the filesystem structure but with better names
    return track_by_directory(
        coursedir,
        name="mooc",
        description='Compléments du MOOC Python 3',
        notebooks=notebooks_by_pattern(coursedir, f"w?/w*-s*-[cx]*.md"),
        directory_labels=WEEK_NAMES)


# we use this pattern in -x* to create a track
# that contains only exercises
def _exo_track(coursedir):
    return track_by_directory(
        coursedir,
        name="exos",
        description='Exercices extraits du MOOC Python 3',
        notebooks=notebooks_by_pattern(coursedir, "w?/w*-s*-x*.md"),
        directory_labels=WEEK_NAMES)


def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks

    """

    return [
        track_by_directory(
	    coursedir,
            name="mooc",
            description='Compléments du MOOC Python 3',
            notebooks=(notebooks_by_pattern(coursedir, f"w?/w*-s*-[cx]*.md")),
            directory_labels=WEEK_NAMES),
        track_by_directory(
            coursedir,
            name="exos",
            description='Exercices extraits du MOOC Python 3',
            notebooks=(notebooks_by_pattern(coursedir, f"w?/w*-s*-x*.md")),
            directory_labels=WEEK_NAMES)
    ]
