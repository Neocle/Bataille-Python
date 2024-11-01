import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from ui.bataille_gui import Ui_MainWindow
from ui.start_game import Start_Dialog
from ui.end_game import End_Dialog
from ui.credits import CreditsDialog
from modules.bataille import Bataille

class StartGameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Start_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_game)

    def start_game(self):
        player1_name = self.ui.lineEdit.text().strip()
        player2_name = self.ui.lineEdit_2.text().strip()
        if not player1_name or not player2_name:
            QMessageBox.warning(self, "Erreur", "Donnez des noms valides pour les deux joueurs!")
            return
        try:
            num_cards = int(self.ui.comboBox.currentText())
            if num_cards <= 0:
                raise ValueError("Invalid card number")
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Entrer une nombre de cartes valide!")
            return

        self.player1_name = player1_name
        self.player2_name = player2_name
        self.num_cards = num_cards
        self.accept()

class EndGameDialog(QDialog):
    game_restart = QtCore.pyqtSignal()
    game_close = QtCore.pyqtSignal()

    def __init__(self, winner_name, parent=None):
        super(EndGameDialog, self).__init__(parent)
        self.ui = End_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(f"{winner_name} a gagné la partie!")
        self.ui.pushButton.clicked.connect(self.restart_game)
        self.ui.pushButton_2.clicked.connect(self.close_game)

    def restart_game(self):
        self.game_restart.emit()
        self.accept()

    def close_game(self):
        self.game_close.emit()
        self.reject()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.partie = None
        self.auto_play_active = False
        self.start_game_dialog()

        self.pushButton_3.clicked.connect(self.open_credits_dialog)
        self.pushButton_2.clicked.connect(self.jouer_auto)

    def open_credits_dialog(self):
        credits_dialog = CreditsDialog(self)
        credits_dialog.exec_()

    def jouer_auto(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.auto_play_active = True
        self.auto_play_turns()

    def start_game_dialog(self):
        dialog = StartGameDialog()
        dialog_result = dialog.exec_()

        if dialog_result == QDialog.Accepted:
            self.partie = Bataille(dialog.num_cards, dialog.player1_name, dialog.player2_name)
            self.partie.game_over.connect(self.game_over)
            self.partie.update_cards.connect(self.update_card_images)
            self.partie.game_message.connect(self.update_message_label)
            
            self.show()
            self.mettre_a_jour_labels()
        else:
            sys.exit()

    def game_over(self, winner_name):
        self.auto_play_active = False 
        end_game_dialog = EndGameDialog(winner_name, self)

        end_game_dialog.game_restart.connect(self.restart_game)
        end_game_dialog.game_close.connect(self.close)

        end_game_dialog.exec_()

    def restart_game(self):
        self.close()
        self.start_game_dialog()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
