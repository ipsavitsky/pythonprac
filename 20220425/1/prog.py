import gettext
from pyfiglet import Figlet

translation = gettext.translation('prog', 'po', fallback=True)

_, ngettext = translation.gettext, translation.ngettext

def solve(a: float, b: float) -> float | None:
    if a == 0:
        return None
    return -b / a


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    f = Figlet(font="graceful")
    res = solve(a, b)
    if not res:
        print(f.renderText(_("NO ROOTS")))
    else:
        print(f.renderText(_("Root: {}").format(res)))
    # print(f.renderText(str(solve(a, b))))
