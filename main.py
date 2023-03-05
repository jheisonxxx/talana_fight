# This is a sample Python script.
import json


class Player:
    '''
        The Player object contains info about one player
        :param first_name: Is the first name of a player
        :type arg: str
        :param first_name: Is the last name of a player
        :type arg: str
        :param current_energy: Is the current_energy of a player
        :type arg: int
        :param movements: Is the all movements that a player can do
        :type arg: dict
         :param attacks: Is the all attacks that a player have
        :type arg: dict
        '''

    def __init__(self, first_name, last_name, current_energy, movements, attacks):
        self.first_name = first_name
        self.last_name = last_name
        self.current_energy = current_energy
        self.movements = movements
        self.attacks = attacks
        print(f'{self.first_name} esta listo para pelear')

    def get_movements_and_attack(self, movement, blow):
        """
           get_movements_and_attack get if its an attack in the conbination of movements more blows.
           :param movement: secuence of movements in a turn
           :param blow: unique button of blow in a turn
           :return: a tuple with movements and attack
           """
        len_movement = len(movement)
        attack = blow
        m = 0
        while m < len_movement:
            if movement[m:len_movement] + blow in self.attacks:
                attack = movement[m:len_movement] + blow
                break
            m = m + 1
        return (movement[0:m], attack)

    def talk_story(self, movement, blow):
        """
                   talk_story print the history in a turn.
                   :param movement: secuence of movements in a turn
                   :param blow: unique button of blow in a turn
                   :void: Only print a turn of the history
                   """
        movements, attack = self.get_movements_and_attack(movement, blow)
        if len(movements) > 1 and len(attack) > 0:
            print(f'{self.first_name} se movio y {self.attacks[attack]["message"]}')
            self.current_energy -= self.attacks[attack]["energy"]
        elif len(movements) == 1 and len(attack) > 0:
            print(f'{self.first_name} {self.movements[movements]} y {self.attacks[attack]["message"]}')
            self.current_energy -= self.attacks[attack]["energy"]
        elif len(movements) == 0 and len(attack) > 0:
            print(f'{self.first_name} {self.attacks[attack]["message"]}')
            self.current_energy -= self.attacks[attack]["energy"]
        elif len(attack) == 0:
            print(f'{self.first_name} se movio')


def battle(name):
    print(f'Hi, {name}')
    movements1 = ["D", "DSD", "S", "DSD", "SD"]
    blows1 = ["K", "P", "", "K", "P"]
    movements2 = ["SA", "SA", "SA", "ASA", "SA"]
    blows2 = ["K", "", "K", "P", "P"]

    f_player1 = open('player1.json')
    data_player1 = json.load(f_player1)
    f_player2 = open('player2.json')
    data_player2 = json.load(f_player2)

    player1 = Player(**data_player1)
    player2 = Player(**data_player2)

    for index in range(max(len(movements1), len(movements2))):
        if index < len(movements1):
            player1.talk_story(movements1[index], blows1[index])
        if index < len(movements2):
            player2.talk_story(movements2[index], blows2[index])
        if player1.current_energy == 0:
            print(
                f'{player2.first_name} {player2.last_name} acaba de ganar y le queda {player2.current_energy} de energia')
            break
        if player2.current_energy == 0:
            print(
                f'{player1.first_name} {player1.last_name} acaba de ganar y le queda {player1.current_energy} de energia')
            break

    # print(player1.first_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    battle('Iniicalizando historia')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
