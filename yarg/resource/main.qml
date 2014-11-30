import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ApplicationWindow {
    id: applicationWindow
    visible: true
    width: 400
    height: 480
    title: 'YARG'

    StackView {
        anchors.fill: parent
        id: stackView
        initialItem: ProfileList {id: profileList}
    }
}
