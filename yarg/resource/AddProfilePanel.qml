import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

Item {
    RowLayout {
        spacing: 0
        width: parent.width
        Button {
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Save & Close"
            onClicked: {
                stackView.pop();
                mainController.save_new_profile_clicked()
                newProfileName.text = ''
            }
        }
        Button {
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Close"
            onClicked: {
                mainController.discard_new_profile_clicked()
                stackView.pop();
                newProfileName.text = ''
            }
        }
    }
    ColumnLayout {
        height: parent.height
        width: parent.width
        Item {
            Layout.fillHeight: true
            Layout.fillWidth:true
        }
        Text {
            text: "New profile's name"
            font.pointSize: 16
            Layout.minimumHeight: 30
            Layout.fillWidth: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
        /*
        TextField {
            id: newProfileName
            focus: true
            Layout.minimumHeight: 30
            anchors {
                right: parent.right
                left: parent.left
                leftMargin: 5
                rightMargin: 5
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            Binding {
                target: mainController.new_profile
                property: 'name'
                value: newProfileName.text
            }
        }
        */
        Item {
            Layout.fillHeight: true
            Layout.fillWidth:true
        }
    }
}