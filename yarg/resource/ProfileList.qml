import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ColumnLayout {
    RowLayout {
        spacing: 0
        Layout.fillWidth: true
        Layout.minimumHeight: 40
        Button {
            Layout.fillWidth: true
            Layout.minimumHeight: 40
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
            height: content.height + 20
            border.width: ListView.isCurrentItem ? 2 : 1
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
            ColumnLayout {
                id: content
                anchors {
                    verticalCenter: parent.verticalCenter
                    left: parent.left
                    right: parent.right
                    margins: 10
                }
                ColumnLayout {
                    Text {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignHCenter
                        font.pointSize: 10
                        text: object.name
                    }
                    RowLayout {
                        Layout.minimumHeight: 30
                        Layout.fillWidth:true
                        Text {
                            Layout.fillWidth:true
                            text: 'Last sync: ' + (object.last_sync != '' ? object.last_sync : 'Never')
                        }
                        Text {
                            Layout.fillWidth:true
                            visible: object.sync_in_progress
                            text: 'Synchronizing...'
                        }
                    }
                }
                RowLayout {
                    visible: index == profileList.currentIndex
                    Layout.fillWidth: true
                    Button {
                        Layout.fillWidth: true
                        text: "Sync"
                        onClicked: {
                            updateSelection()
                            mainController.sync_clicked()
                        }
                    }
                    Button {
                        Layout.fillWidth: true
                        text: "Edit"
                        onClicked: {
                            updateSelection()
                            stackView.push(Qt.createComponent('EditPanel.qml'))
                        }
                    }
                    Button {
                        Layout.fillWidth: true
                        text: object.sync_in_progress ? 'Abort' : 'Delete'
                        onClicked: {
                            if(object.sync_in_progress) {
                                mainController.abort_sync_clicked(object.name)
                            } else {
                                updateSelection()
                                mainController.delete_profile_clicked()
                            }
                        }
                    }
                }
            }
        }
    }
}