import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ApplicationWindow {
    visible: true
    width: 400
    height: 480
    title: qsTr("YARG")
    FlipBar {
        anchors.fill: parent
        id: flipBar
        front : ProfileList {}
        back : EditPanel {}
    }
}
