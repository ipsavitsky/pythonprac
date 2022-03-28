from dataclasses import dataclass
import readline
import shlex
import cmd


@dataclass
class Monster():
    name: str
    hp: int
    def __str__(self):
        return f'{self.name} {self.hp} hp'



class DungeonGame(cmd.Cmd):
    dungeon = [[[] for _ in range(10)] for _ in range(10)]
    player_coords = [0, 0]


    prompt = '>>'
    def do_add(self, args):
        _, _, name, _, hp, _, x, y = shlex.split(args)
        self.dungeon[int(x)][int(y)].append(Monster(name=name, hp=int(hp)))


    def do_show(self, arg):
        for x, row in enumerate(self.dungeon):
            for y, cell in enumerate(row):
                for monster in cell:
                    print(f'{monster.name} at ({x} {y}) hp {monster.hp}')

    def do_move(self, arg):
        move_successful = True
        match arg:
            case 'up':
                if self.player_coords[0] + 1 > 9:
                    move_successful = False
                else:
                    self.player_coords[0] += 1
            case 'down':
                if self.player_coords[0] - 1 < 0:
                    move_successful = False
                else:
                    self.player_coords[0] -= 1
            case 'left':
                if self.player_coords[1] - 1 < 0:
                    move_successful = False
                else:
                    self.player_coords[1] -= 1
            case 'right':
                if self.player_coords[1] + 1 > 9:
                    move_successful = False
                else:
                    self.player_coords[1] += 1
            case _:
                move_successful = False
        
        if move_successful:
            x, y = self.player_coords
            print(f'player at {x} {y}')
            if self.dungeon[x][y]:
                print(f'ecountered: {", ".join(map(str, self.dungeon[x][y]))}')
        else:
            print('cannot move')

    def do_attack(self, arg):
        monster_damaged = False
        x, y = self.player_coords
        for monster in self.dungeon[x][y]:
            if monster.name == arg:
                monster_damaged = True
                monster.hp -= 10
                if monster.hp > 0:
                    print(f'{monster.name} lost 10 hp, now has {monster.hp} hp')
                else:
                    print(f'{monster.name} dies')
                    self.dungeon[x][y].remove(monster)
                break

        if not monster_damaged:
            print(f'no {arg} here')
    

    def complete_move(self, prefix, line, start_index, end_index):
        return [s for s in ('up', 'down', 'left', 'right') if s.startswith(prefix)]

    def complete_attack(self, prefix, line, start_index, end_index):
        x, y = self.player_coords
        monster_names = map(lambda x: x.name, self.dungeon[x][y])
        return [s for s in monster_names if s.startswith(prefix)]


if __name__ == '__main__':
    DungeonGame().cmdloop()
