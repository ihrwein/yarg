import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import qmlRegisterType, QQmlApplicationEngine

from yarg.gui.main_controller import MainController
from yarg.gui.profile_view_model import ProfileViewModel


def main():
    app = QGuiApplication(sys.argv)
    qmlRegisterType(MainController, 'MainController', 1, 0, 'MainController')
    qmlRegisterType(ProfileViewModel, 'ProfileViewModel', 1, 0, 'ProfileViewModel')
    engine = QQmlApplicationEngine()
    main_controller = MainController()
    main_controller.profile_selection_changed(0)
    engine.rootContext().setContextProperty('mainController', main_controller)
    engine.load(QUrl.fromLocalFile('../yarg/resource/Main.qml'))
    window = engine.rootObjects()[0]
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()