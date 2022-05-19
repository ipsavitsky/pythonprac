from doit.tools import create_folder

def task_pot():
    "generate pot"
    return {
        "targets": ["prog.pot"],
        "actions": ["pybabel extract -o prog.pot prog.py"],
    }


def task_po():
    "Translate stuff"
    return {
        "task_dep": ["pot"],
        "actions": ["pybabel init -d po -i prog.pot -l ru"],
        "targets": ["po/ru/LC_MESSAGES/prog.po"],
    }


def task_mo():
    """Compile translations."""
    return {
        "actions": [
            (create_folder, ["po/ru/LC_MESSAGES"]),
            "pybabel compile -l ru -i po/ru/LC_MESSAGES/messages.po -d po",
        ],
        "file_dep": ["po/ru/LC_MESSAGES/messages.po"],
        "targets": ["po/ru/LC_MESSAGES/messages.mo"],
    }


def task_test():
    "Test stuff"
    yield {'actions': ['coverage run -m unittest -v tests/test_prog.py'], 'name': "run"}
    yield {'actions': ['coverage report'], 'verbosity': 2, 'name': "report"}


def task_gitclean():
    """Clean all generated files not tracked by GIT."""
    return {
            'actions': ['git clean -xdf'],
           }

def task_sdist():
    """Create source distribution."""
    return {
            'actions': ['python -m build -s'],
            'task_dep': ['gitclean'],
           }


def task_wheel():
    """Create binary wheel distribution."""
    return {
            'actions': ['python -m build -w'],
            'task_dep': ['mo'],
           }


def task_clear():
    "cleanup"
    pass
