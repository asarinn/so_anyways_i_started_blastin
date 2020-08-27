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
        self.raging_enabled = False
        self.charging_enabled = False
        self.flanking_enabled = False
        self.water_subtype_enabled = False
        self.sneak_attack_enabled = False

        # Connections to toggle state on check box click
        self.ui.inspire_courage_check_box.clicked.connect(self.inspire_courage_toggled)
        self.ui.haste_check_box.clicked.connect(self.haste_toggled)
        self.ui.raging_check_box.clicked.connect(self.raging_toggled)
        self.ui.charging_check_box.clicked.connect(self.charging_toggled)
        self.ui.flanking_bonus_check_box.clicked.connect(self.flanking_toggled)
        self.ui.water_subtype_check_box.clicked.connect(self.water_subtype_toggled)
        self.ui.flanking_bonus_check_box.clicked.connect(self.flanking_toggled)
        self.ui.sneak_attack_check_box.clicked.connect(self.sneak_attack_toggled)

        # Auto update when spin box toggled
        self.ui.num_hits_spin_box.valueChanged.connect(self.update_output)

        # Initialize output with initial settings
        self.update_output()

    def inspire_courage_toggled(self, state):
        self.inspire_courage_enabled = state
        self.update_output()

    def haste_toggled(self, state):
        self.haste_enabled = state
        self.update_output()

    def raging_toggled(self, state):
        self.raging_enabled = state
        self.update_output()

    def charging_toggled(self, state):
        self.charging_enabled = state
        self.update_output()

    def water_subtype_toggled(self, state):
        self.water_subtype_enabled = state
        self.update_output()

    def flanking_toggled(self, state):
        self.flanking_enabled = state
        self.update_output()

    def sneak_attack_toggled(self, state):
        self.sneak_attack_enabled = state
        self.update_output()

    def update_output(self):
        raw_dex = self.configuration['DEX']
        if self.raging_enabled:
            raw_dex += self.configuration['RAGE_DEX_BONUS']

        bonus_dex = int((raw_dex - 10) / 2)

        # Calculate Attack Bonus
        attack_bonus = self.calculate_attack_bonus(bonus_dex)

        # Calculate number of attacks
        num_attacks = 1 + int((self.configuration['BAB'] - 1) / 5)

        attack_text = f' Attack Bonus: +{attack_bonus}'
        if self.haste_enabled:
            attack_text = attack_text + f'/{attack_bonus}'
        for i in range(num_attacks - 1):
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
        damage = self.calculate_damage(bonus_dex) * num_hits

        # Calculate Dice
        dice, crit_dice = self.calculate_dice(num_hits)

        self.ui.damage_label.setText(f'Damage: {dice} + {damage}')

        crit_mod = self.configuration["WEAPON_CRITICAL_MOD"]
        self.ui.crit_damage_label.setText(
            f'Critical Damage: {crit_dice} + {crit_mod * damage}')

    def calculate_attack_bonus(self, dex):
        attack_bonus = self.configuration['BAB'] + self.configuration['WEAPON_BONUS'] + dex

        if self.inspire_courage_enabled:
            attack_bonus += self.configuration['INSPIRE']

        if self.haste_enabled:
            attack_bonus += self.configuration['HASTE']

        if self.charging_enabled:
            attack_bonus += self.configuration['CHARGE']

        if self.flanking_enabled:
            attack_bonus += self.configuration['FLANKING']

        if self.sneak_attack_enabled:
            attack_bonus += self.configuration['SNEAK_ATTACK_BONUS']

        return attack_bonus

    def calculate_damage(self, dex):
        damage = self.configuration['WEAPON_BONUS'] + dex

        if self.inspire_courage_enabled:
            damage += self.configuration['INSPIRE']

        return damage

    def calculate_dice(self, hits):
        weapon_dice = self.configuration['DAMAGE_DIE']

        crit_multiplier = self.configuration['WEAPON_CRITICAL_MOD']

        sneak_dice = self.configuration['SNEAK_DAMAGE_DIE']

        if self.water_subtype_enabled and not self.sneak_attack_enabled:
            dice = f'{hits * (weapon_dice[0])}d{weapon_dice[1]}'
            crit_dice = f'{hits * (crit_multiplier * weapon_dice[0] + 3)}d{weapon_dice[1]}'
        elif self.sneak_attack_enabled and not self.water_subtype_enabled:
            dice = f'{hits * (weapon_dice[0]+sneak_dice[0])}d{weapon_dice[1]}'
            crit_dice = f'{hits * (crit_multiplier * weapon_dice[0]+sneak_dice[0])}d{weapon_dice[1]}'
        elif not self.sneak_attack_enabled and not self.water_subtype_enabled:
            dice = f'{hits * (weapon_dice[0])}d{weapon_dice[1]}'
            crit_dice = f'{hits * (crit_multiplier * weapon_dice[0])}d{weapon_dice[1]}'
        elif self.sneak_attack_enabled and self.water_subtype_enabled:
            dice = f'{hits * (weapon_dice[0] + sneak_dice[0])}d{weapon_dice[1]}'
            crit_dice = f'{hits * (crit_multiplier * weapon_dice[0] + 3 + sneak_dice[0])}d{weapon_dice[1]}'
        else:
            dice = 'error'
            crit_dice = 'error'

        return dice, crit_dice
