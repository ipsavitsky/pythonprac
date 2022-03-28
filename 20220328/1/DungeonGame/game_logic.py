"""All functions for game logic."""

from dataclasses import dataclass


@dataclass
class Monster:
    name: str
    hp: int

    def __str__(self):
        return f"{self.name} {self.hp} hp"


def print_field(dung_map):
    for x, row in enumerate(dung_map):
        for y, cell in enumerate(row):
            for monster in cell:
                print(f"{monster.name} at ({x} {y}) hp {monster.hp}")


def move_and_bound_check(arg, dungeon):
    move_successful = True
    match arg:
        case "up":
            if dungeon.player_coords[0] + 1 > 9:
                move_successful = False
            else:
                dungeon.player_coords[0] += 1
        case "down":
            if dungeon.player_coords[0] - 1 < 0:
                move_successful = False
            else:
                dungeon.player_coords[0] -= 1
        case "left":
            if dungeon.player_coords[1] - 1 < 0:
                move_successful = False
            else:
                dungeon.player_coords[1] -= 1
        case "right":
            if dungeon.player_coords[1] + 1 > 9:
                move_successful = False
            else:
                dungeon.player_coords[1] += 1
        case _:
            move_successful = False

    if move_successful:
        x, y = dungeon.player_coords
        print(f"player at {x} {y}")
        if dungeon.dungeon[x][y]:
            print(f'ecountered: {", ".join(map(str, dungeon.dungeon[x][y]))}')
        else:
            print("cannot move")


def attack(arg, dungeon):
    monster_damaged = False
    x, y = dungeon.player_coords
    for monster in dungeon.dungeon[x][y]:
        if monster.name == arg:
            monster_damaged = True
            monster.hp -= 10
            if monster.hp > 0:
                print(f"{monster.name} lost 10 hp, now has {monster.hp} hp")
            else:
                print(f"{monster.name} dies")
                dungeon.dungeon[x][y].remove(monster)
            break
    if not monster_damaged:
        print(f"no {arg} here")
