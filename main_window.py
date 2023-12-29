import json

# Third party imports
from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.QtGui import QKeySequence

# Local imports
from main_window_init import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic pyqt init for gui window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configuration = json.load(open('configuration.json', 'r'))

        # Initialize tracked resources
        health_points = self.configuration['HP']
        self.ui.health_points_spin_box.setMaximum(health_points)
        self.ui.health_points_spin_box.setValue(health_points)
        grit_pool = self.configuration['GRIT_POOL']
        self.ui.grit_pool_spin_box.setMaximum(grit_pool)
        self.ui.grit_pool_spin_box.setValue(grit_pool)

        # Class variables to hold state of check boxes
        self.inspire_courage_enabled = False
        self.haste_enabled = False
        self.two_weapon_fighting_enabled = False
        self.deadly_aim_enabled = False
        self.point_blank_enabled = False
        self.improved_point_blank_enabled = False
        self.up_close_and_deadly_enabled = False
        self.rapid_shot_enabled = False

        # Close program on Ctrl+Q
        shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        shortcut_close.activated.connect(self.close)

        # Connections to toggle state on check box click
        self.ui.inspire_courage_check_box.toggled.connect(self.inspire_courage_toggled)
        self.ui.haste_check_box.toggled.connect(self.haste_toggled)
        self.ui.two_weapon_fighting_check_box.toggled.connect(self.two_weapon_fighting_toggled)
        self.ui.deadly_aim_check_box.toggled.connect(self.deadly_aim_toggled)
        self.ui.point_blank_check_box.toggled.connect(self.point_blank_toggled)
        self.ui.improved_point_blank_check_box.toggled.connect(self.improved_point_blank_shot_toggled)
        self.ui.close_and_deadly_check_box.toggled.connect(self.up_close_and_deadly_toggled)
        self.ui.rapid_shot_check_box.toggled.connect(self.rapid_shot_toggled)

        # Auto update when spin box toggled
        self.ui.num_hits_spin_box.valueChanged.connect(self.update_output)
        self.ui.crit_multiplier_spin_box.valueChanged.connect(self.update_output)
        self.ui.up_close_and_deadly_spin_box.valueChanged.connect(self.update_output)

        # Initialize output with initial settings
        self.update_output()

    def inspire_courage_toggled(self, checked):
        self.inspire_courage_enabled = checked
        self.update_output()

    def haste_toggled(self, checked):
        self.haste_enabled = checked
        self.update_output()

    def two_weapon_fighting_toggled(self, checked):
        self.two_weapon_fighting_enabled = checked
        self.update_output()

    def deadly_aim_toggled(self, checked):
        self.deadly_aim_enabled = checked
        self.update_output()

    def improved_point_blank_shot_toggled(self, checked):
        self.improved_point_blank_enabled = checked

        if checked:
            self.ui.point_blank_check_box.setChecked(checked)

        self.update_output()

    def point_blank_toggled(self, checked):
        self.point_blank_enabled = checked

        if not checked:
            self.ui.improved_point_blank_check_box.setChecked(checked)

        self.update_output()

    def up_close_and_deadly_toggled(self, checked):
        self.up_close_and_deadly_enabled = checked
        self.ui.up_close_and_deadly_spin_box.setEnabled(checked)
        self.update_output()

    def rapid_shot_toggled(self, checked):
        self.rapid_shot_enabled = checked
        self.update_output()

    def update_output(self):
        # Calculate dex bonus
        dex_bonus = (self.configuration['DEX'] - 10) // 2

        # Calculate attack bonus
        attack_bonus = self.calculate_attack_bonus(dex_bonus)

        # Calculate number of attacks
        num_attacks = 1 + ((self.configuration['BAB'] - 1) // 5)

        # Main Attacks
        attack_text = f' Attack Bonus: + {attack_bonus}'
        if self.two_weapon_fighting_enabled:
            attack_text += f'/{attack_bonus}'

        # Haste attack
        if self.haste_enabled:
            attack_text += f'/{attack_bonus}'

        # Rapid shot attack
        if self.rapid_shot_enabled:
            attack_text += f'/{attack_bonus}'

        # Iterative attacks
        for i in range(1, num_attacks):
            # Add more iteratives so long as the required feats are had
            if self.two_weapon_fighting_enabled and self.configuration['TWO_WEAPON_FIGHTING_LEVEL'] > i:
                attack_text += f'/{attack_bonus - (5 * i)}'

            attack_text += f'/{attack_bonus - (5 * i)}'

        self.ui.attack_bonus_label.setText(attack_text)

        # Set new spin box max
        spin_max = num_attacks
        if self.haste_enabled:
            spin_max += 1

        if self.two_weapon_fighting_enabled:
            spin_max += self.configuration['TWO_WEAPON_FIGHTING_LEVEL']

        if self.rapid_shot_enabled:
            spin_max += 1

        self.ui.num_hits_spin_box.setMaximum(spin_max)

        # Get num hits
        num_hits = int(self.ui.num_hits_spin_box.value())

        # Set up close and deadly maximum to number of hits
        self.ui.up_close_and_deadly_spin_box.setMaximum(num_hits)

        # Calculate damage bonus
        damage = self.calculate_damage(dex_bonus) * num_hits

        # Calculate dice
        dice, crit_dice = self.calculate_dice(num_hits)

        self.ui.damage_label.setText(f'Damage: {dice} + {damage}')

        crit_mod = int(self.ui.crit_multiplier_spin_box.value())
        self.ui.crit_damage_label.setText(f'Critical Damage: {crit_dice} + {crit_mod * damage}')

    def calculate_attack_bonus(self, dex_bonus):
        conf = self.configuration

        attack_bonus = conf['BAB'] + conf['WEAPON_BONUS'] + dex_bonus + conf['ATTACK_BONUS']

        if self.inspire_courage_enabled:
            attack_bonus += conf['INSPIRE']

        if self.haste_enabled:
            attack_bonus += conf['HASTE']

        if self.deadly_aim_enabled:
            attack_bonus += conf['DEADLY_AIM_PENALTY']

        if self.point_blank_enabled:
            attack_bonus += conf['POINT_BLANK']

        if self.improved_point_blank_enabled:
            attack_bonus += conf['IMPROVED_POINT_BLANK']

        if self.two_weapon_fighting_enabled:
            attack_bonus += conf['TWO_WEAPON_FIGHTING_PENALTY']

        if self.rapid_shot_enabled:
            attack_bonus += conf['RAPID_SHOT_PENALTY']

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
        crit_multiplier = int(self.ui.crit_multiplier_spin_box.value())
        num_dice, num_faces = self.configuration['DAMAGE_DIE']
        dice = f'{hits * num_dice}d{num_faces}'
        crit_dice = f'{hits * (crit_multiplier * num_dice)}d{num_faces}'

        if self.up_close_and_deadly_enabled:
            num_invocations = int(self.ui.up_close_and_deadly_spin_box.value())
            num_dice, num_faces = self.configuration['UP_CLOSE_AND_DEADLY_DICE']
            up_close_and_deadly_dice = f'{num_invocations * num_dice}d{num_faces}'

            dice += f' + {up_close_and_deadly_dice}'
            crit_dice += f' + {up_close_and_deadly_dice}'

        return dice, crit_dice

