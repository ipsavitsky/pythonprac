import gettext

translation = gettext.translation('module', 'po', fallback=True)
_, ngettext = translation.gettext, translation.ngettext

def dialog():
    while s := input(_("Enter a string: ")):
        n = len(s.split())
        print(ngettext("{} word entered", "{} words entered", n).format(n))