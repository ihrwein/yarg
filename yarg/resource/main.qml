import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ApplicationWindow {
    visible: true
    width: 400
    height: 480
    title: qsTr("YARG")

    property alias editPanel: editPanel
    StackView {
        anchors.fill: parent
        id: stackView
        initialItem: profileList
    }
    Item {
        visible: false
        id: mainComponent
        ProfileList {id: profileList}
        EditPanel {id: editPanel}
    }
}
