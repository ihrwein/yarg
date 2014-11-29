import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ColumnLayout {
    RowLayout {
        spacing: 0
        Layout.fillWidth: true
        Button {
            Layout.fillWidth: true
            text: "Add new profile"
            onClicked: {
                mainController.add_new_profile_clicked()
            }
        }
    }
    ListView {
        spacing: 2
        clip: true
        Layout.fillHeight: true
        Layout.fillWidth: true
        model: mainController.profile_model
        id: profileList

        highlight: Rectangle {
            color: 'lightGray'
            width: 20
            height: 20
        }
        delegate: Rectangle {
            id: wrapperRect
            border.color: object.out_of_sync ? 'red' : 'black'
            color: ListView.isCurrentItem ? 'lightGray' : 'white'
            ListView.onAdd: SequentialAnimation {
                NumberAnimation { target: wrapperRect; property: "scale"; from: 0; to: 1; duration: 250; easing.type: Easing.InOutQuad }
            }
            function updateSelection() {
                profileList.currentIndex = index
                mainController.profile_selection_changed(index)
            }
            MouseArea{
                anchors.fill: parent
                onClicked: updateSelection()
            }
            anchors {
                left: parent.left
                right: parent.right
                margins: 5
            }
            height: content.height + 15
            border.width: 1
            RowLayout {
                id: content
                anchors {
                    verticalCenter: parent.verticalCenter
                    left: parent.left
                    right: parent.right
                    margins: 5
                }
                ColumnLayout {
                    Text {
                        text: object.name
                    }
                    Text {
                        text: object.last_sync
                    }
                    Text {
                        visible: object.sync_in_progress
                        text: 'synchronizing'
                    }
                }
                RowLayout {
                    anchors.right: parent.right
                    Button {
                        style: ButtonStyle {}
                        text: "Sync"
                        onClicked: {
                            updateSelection()
                            mainController.sync_clicked()
                        }
                    }
                    Button {
                        style: ButtonStyle {}
                        text: "Edit"
                        onClicked: {
                            updateSelection()
                            //flipBar.flipUp()
                            stackView.push(editPanel)
                        }
                    }
                    Button {
                        style: ButtonStyle {}
                        text: "Delete"
                        visible: !object.sync_in_progress
                        onClicked: {
                            updateSelection()
                            mainController.delete_profile_clicked()
                        }
                    }
                }
            }
        }
    }
}