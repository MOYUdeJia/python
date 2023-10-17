# 奥特曼打小怪兽
from abc import ABCMeta, abstractmethod
from random import randint, randrange
from time import sleep


class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):  # 大招（至少打50滴血），使用成功返回True，反则False
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):  # 魔法攻击，使用成功返回True，反则False
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):  # 回复魔法值
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return f'~~~{self._name}奥特曼~~~' + \
               f'生命值：{self._hp}' + \
               f'魔法值：{self._mp}'


class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return f'~~~{self._name}小怪兽~~~' + \
               f'生命值：{self._hp}'


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('缔笙', 1000, 120)
    m1 = Monster('卫岳', 250)
    m2 = Monster('武心婵', 500)
    m3 = Monster('霍光', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(f'\n========第{fight_round}回合========\n')
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print(f'{u.name}使用普通攻击打了{m.name}')
            u.attack(m)
            print(f'{u.name}的魔法值恢复了{u.resume()}')
        elif skill <= 9:
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击')
            else:
                print(f'{u.name}使用魔法失败')
        else:
            if u.huge_attack(m):
                print(f'{u.name}使用大招虐了{m.name}')
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            print(f'{m.name}回击了{u.name}')
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
        sleep(1)
    if u.alive > 0:
        print(f'{u.name}奥特曼胜利')
    else:
        print('小怪兽胜利')


if __name__ == '__main__':
    main()
