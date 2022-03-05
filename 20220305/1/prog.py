from dataclasses import dataclass
import readline
import shlex
import cmd

@dataclass
class Monster():
    name: str
    # coords: tuple[int, int]
    hp: int



class DungeonGame(cmd.Cmd):
    dungeon = [[[] for _ in range(10)] for _ in range(10)]
    player_coords = (0, 0)


    prompt = '>>'
    def do_add(self, args):
        _, _, name, _, hp, _, x, y = shlex.split(args)
        self.dungeon[int(x)][int(y)].append(Monster(name=name, hp=int(hp)))


    def do_show(self, arg):
        for x, row in enumerate(self.dungeon):
            for y, cell in enumerate(row):
                for monster in cell:
                    print(f'{monster.name} at {x, y} hp {monster.hp}')

    def do_move(self, arg):
        move_successful = True
        match arg:
            case 'up':
                pass
            case 'down':
                pass
            case 'left':
                pass
            case 'right':
                pass
            case _:
                pass
        
        if move_successful:
            print(f'player at {self.player_coords}')
            x, y = self.player_coords
            if self.dungeon[x][y]:
                print(f'ecountered: {" ".join(self.dungeon[x][y])}')
        else:
            print('cannot move')

    def do_attack(self, arg):
        pass


if __name__ == '__main__':
    DungeonGame().cmdloop()
