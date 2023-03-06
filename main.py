import json


class Player:
    """
    The Player object contains info about one player
    :param first_name: Is the first name of a player
    :type: str
    :param first_name: Is the last name of a player
    :type: str
    :param current_energy: Is the current_energy of a player
    :type: int
    :param movements: Is the all movements that a player can do
    :type: dict
    :param attacks: Is the all attacks that a player have
    :type: dict
    """

    def __init__(self, first_name, last_name, current_energy, movements, attacks):
        self.first_name = first_name
        self.last_name = last_name
        self.current_energy = current_energy
        self.movements = movements
        self.attacks = attacks
        print(f'{self.first_name} esta listo para pelear')

    def get_movements_and_attack(self, movement, blow):
        """
        get_movements_and_attack get if its an attack in the conbination of movements more blows
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
        return movement[0:m], attack

    def tell_turn_battle(self, movement, blow):
        """
        tell_story print the history in a turn
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


def initialize_players():
    """
    initialize_players call the constructors of each player with the data of the files.
    :return: a tuple of objects with attacks and movements permitted by each player
    """
    f_player1 = open('player1.json')
    data_player1 = json.load(f_player1)
    f_player2 = open('player2.json')
    data_player2 = json.load(f_player2)

    player1 = Player(**data_player1)
    player2 = Player(**data_player2)

    return player1, player2


def check_battle_requirements(json_battle, max_len_movement):
    """
    initialize_players call the constructors of each player with the data of the files
    :param json_battle: json with move and hit buttons
    :param max_len_movement: each movement is a string of maximum length 5
    :void: only prints if the requirements are not met
    """
    movements_player1 = json_battle["player1"]["movimientos"]
    blows_player1 = json_battle["player1"]["golpes"]
    for index, movement in enumerate(movements_player1):
        if len(movement) > 5:
            print(
                f'No se puede iniciar la pelea por que el turno {index}({movement}) del jugador {player1.first_name}(player1) tiene mas de {max_len_movement} movimientos')

        if len(blows_player1[index]) > 1:
            print(
                f'No se puede iniciar la pelea por que el turno {index}({blows_player1[index]}) del jugador {player1.first_name}(player1) tiene mas de un golpe')

    movements_player2 = json_battle["player2"]["movimientos"]
    blows_player2 = json_battle["player2"]["golpes"]
    for index, movement in enumerate(movements_player2):
        if len(movement) > 5:
            print(
                f'No se puede iniciar la pelea por que el turno {index}({movement}) del jugador {player1.first_name}(player1) tiene mas de {max_len_movement} movimientos')

        if len(blows_player1[index]) > 1:
            print(
                f'No se puede iniciar la pelea por que el turno {index}({blows_player2[index]}) del jugador {player2.first_name}(player2) tiene mas de un golpe')


def tell_battle(json_battle, player1, player2):

    for index in range(max(len(json_battle["player1"]["movimientos"]), len(json_battle["player2"]["movimientos"]))):
        if index < len(json_battle["player1"]["movimientos"]):
            player1.tell_turn_battle(json_battle["player1"]["movimientos"][index],
                                     json_battle["player1"]["golpes"][index])
        if index < len(json_battle["player2"]["movimientos"]):
            player2.tell_turn_battle(json_battle["player2"]["movimientos"][index],
                                     json_battle["player2"]["golpes"][index])
        if player1.current_energy == 0:
            print(
                f'{player2.first_name} acaba de ganar y le queda {player2.current_energy} de energia')
            break
        if player2.current_energy == 0:
            print(
                f'{player1.first_name} acaba de ganar y le queda {player1.current_energy} de energia')
            break


if __name__ == '__main__':
    player1, player2 = initialize_players()
    json_battle = {"player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
                   "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]}}
    check_battle_requirements(json_battle, max_len_movement=5)
    tell_battle(json_battle, player1, player2)
