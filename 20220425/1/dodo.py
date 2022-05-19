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
            (create_folder, ["AppBase/ru/LC_MESSAGES"]),
            "pybabel compile -D DateTime -l ru -i po/ru/LC_MESSAGES/DateTime.po -d AppBase",
        ],
        "file_dep": ["po/ru/LC_MESSAGES/DateTime.po"],
        "targets": ["AppBase/ru/LC_MESSAGES/DateTime.mo"],
    }


def task_test():
    "Test stuff"
    pass


def task_build():
    "Build stuff"
    pass


def task_dist():
    "build distribution"
    pass


def task_clear():
    "cleanup"
    pass
