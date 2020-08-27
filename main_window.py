import json

# Third party imports
from PyQt5.QtWidgets import (QMainWindow)

# Local imports
from main_window_init import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic pyqt init for gui window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configuration = json.load(open("configuration.json", "r"))

        # Class variables to hold state of check boxes
        self.inspire_courage_enabled = False
        self.haste_enabled = False
        self.two_weapon_fighting_enabled = False
        self.deadly_aim_enabled = False
        self.point_blank_enabled = False
        self.improved_point_blank_enabled = False
        self.up_close_and_deadly_enabled = False

        # Connections to toggle state on check box click
        self.ui.inspire_courage_check_box.clicked.connect(self.inspire_courage_toggled)
        self.ui.haste_check_box.clicked.connect(self.haste_toggled)
        self.ui.two_weapon_fighting_check_box.clicked.connect(self.two_weapon_fighting_toggled)
        self.ui.deadly_aim_check_box.clicked.connect(self.deadly_aim_toggled)
        self.ui.point_blank_check_box.clicked.connect(self.point_blank_toggled)
        self.ui.improved_point_blank_check_box.clicked.connect(self.improved_point_blank_shot_toggled)
        self.ui.close_and_deadly_check_box.clicked.connect(self.up_close_and_deadly_toggled)

        # Auto update when spin box toggled
        self.ui.num_hits_spin_box.valueChanged.connect(self.update_output)
        self.ui.crit_multiplier_spin_box.valueChanged.connect(self.update_output)

        # Initialize output with initial settings
        self.update_output()

    def inspire_courage_toggled(self, state):
        self.inspire_courage_enabled = state
        self.update_output()

    def haste_toggled(self, state):
        self.haste_enabled = state
        self.update_output()

    def two_weapon_fighting_toggled(self, state):
        self.two_weapon_fighting_enabled = state
        self.update_output()

    def deadly_aim_toggled(self, state):
        self.deadly_aim_enabled = state
        self.update_output()

    def improved_point_blank_shot_toggled(self, state):
        self.improved_point_blank_enabled = state
        self.point_blank_enabled = state
        self.ui.point_blank_check_box.setChecked(state)
        self.update_output()

    def point_blank_toggled(self, state):
        self.point_blank_enabled = state
        self.update_output()

    def up_close_and_deadly_toggled(self, state):
        self.up_close_and_deadly_enabled = state
        self.update_output()

    def update_output(self):
        # Calculate dex bonus
        dex_bonus = int((self.configuration['DEX'] - 10) / 2)

        # Calculate Attack Bonus
        attack_bonus = self.calculate_attack_bonus(dex_bonus)

        # Calculate number of attacks
        num_attacks = 1 + int((self.configuration['BAB'] - 1) / 5)

        # Main Attacks
        attack_text = f' Attack Bonus: + {attack_bonus}'
        if self.two_weapon_fighting_enabled:
            attack_text = attack_text + f'/{attack_bonus}'
        # Haste Attack
        if self.haste_enabled:
            attack_text = attack_text + f'/{attack_bonus}'
        # Iterative Attacks
        for i in range(num_attacks - 1):
            # Add more iteratives so long as the required feats are had
            if self.two_weapon_fighting_enabled and self.configuration['TWO_WEAPON_FIGHTING_LEVEL'] > i+1:
                attack_text = attack_text + f'/{attack_bonus - (5 * (i + 1))}'
            attack_text = attack_text + f'/{attack_bonus - (5 * (i + 1))}'
        self.ui.attack_bonus_label.setText(attack_text)

        # Set new spin box max
        spin_max = num_attacks
        if self.haste_enabled:
            spin_max += 1
        self.ui.num_hits_spin_box.setMaximum(spin_max)

        # Get num hits
        num_hits = int(self.ui.num_hits_spin_box.value())

        # Calculate Damage Bonus
        damage = self.calculate_damage(dex_bonus) * num_hits

        # Calculate Dice
        dice, crit_dice = self.calculate_dice(num_hits)

        self.ui.damage_label.setText(f'Damage: {dice} + {damage}')

        crit_mod = int(self.ui.crit_multiplier_spin_box.value())
        self.ui.crit_damage_label.setText(
            f'Critical Damage: {crit_dice} + {crit_mod * damage}')

    def calculate_attack_bonus(self, dex_bonus):
        attack_bonus = self.configuration['BAB'] + self.configuration['WEAPON_BONUS'] + dex_bonus + \
                       self.configuration['ATTACK_BONUS']

        if self.inspire_courage_enabled:
            attack_bonus += self.configuration['INSPIRE']

        if self.haste_enabled:
            attack_bonus += self.configuration['HASTE']

        if self.deadly_aim_enabled:
            attack_bonus += self.configuration['DEADLY_AIM_PENALTY']

        if self.point_blank_enabled:
            attack_bonus += self.configuration['POINT_BLANK']

        if self.improved_point_blank_enabled:
            attack_bonus += self.configuration['IMPROVED_POINT_BLANK']

        if self.two_weapon_fighting_enabled:
            attack_bonus += self.configuration['TWO_WEAPON_FIGHTING_PENALTY']

        return attack_bonus

    def calculate_damage(self, dex_bonus):
        damage = self.configuration['WEAPON_BONUS'] + dex_bonus + self.configuration['DAMAGE_BONUS']

        if self.inspire_courage_enabled:
            damage += self.configuration['INSPIRE']

        if self.point_blank_enabled:
            damage += self.configuration['POINT_BLANK']

        if self.improved_point_blank_enabled:
            damage += self.configuration['IMPROVED_POINT_BLANK']

        if self.deadly_aim_enabled:
            damage += self.configuration['DEADLY_AIM_BONUS']

        return damage

    def calculate_dice(self, hits):
        weapon_dice = self.configuration['DAMAGE_DIE']

        crit_multiplier = int(self.ui.crit_multiplier_spin_box.value())

        up_close_and_personal_dice = self.configuration['UP_CLOSE_AND_DEADLY_DICE']

        if not self.up_close_and_deadly_enabled:
            dice = f'{hits * (weapon_dice[0])}d{weapon_dice[1]}'
            crit_dice = f'{hits * (crit_multiplier * weapon_dice[0])}d{weapon_dice[1]}'
        elif self.up_close_and_deadly_enabled:
            dice = f'{hits * (weapon_dice[0] + up_close_and_personal_dice[0])}d{weapon_dice[1]}'
            crit_dice = f'{hits * (crit_multiplier * weapon_dice[0] + up_close_and_personal_dice[0])}d{weapon_dice[1]}'
        else:
            dice = 'error'
            crit_dice = 'error'

        return dice, crit_dice
