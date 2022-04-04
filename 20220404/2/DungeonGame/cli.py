"""CMD REPL interface for the game."""

from DungeonGame.game_logic import Monster, attack, move_and_bound_check, print_field
import readline  # noqa: F401
import shlex
import cmd


class DungeonGame(cmd.Cmd):
    """
    Simple REPL interface. No more, no less.
    """

    dungeon = [[[] for _ in range(10)] for _ in range(10)]
    player_coords = [0, 0]

    prompt = ">>"

    def do_add(self, args):
        """
        Add a monster to the field.

        Usage: add monster name <name> hp <hp> coords <x> <y>
        """
        _, _, name, _, hp, _, x, y = shlex.split(args)
        self.dungeon[int(x)][int(y)].append(Monster(name=name, hp=int(hp)))

    def do_show(self, arg):
        """
        Show all monster on the field.

        Usage: show
        """
        print_field(self.dungeon)

    def do_move(self, arg):
        """
        Move player on the field.

        Usage: move <direction>
        """
        move_and_bound_check(arg, self)

    def do_attack(self, arg):
        """
        Attack a monster in the cell.

        Usage: attack <monster_name>
        """
        attack(arg, self)

    def complete_move(self, prefix, line, start_index, end_index):
        """Autocomplete move instruction."""
        return [s for s in ("up", "down", "left", "right") if s.startswith(prefix)]

    def complete_attack(self, prefix, line, start_index, end_index):
        """Autocomplete attack instruction."""
        x, y = self.player_coords
        monster_names = map(lambda x: x.name, self.dungeon[x][y])
        return [s for s in monster_names if s.startswith(prefix)]
