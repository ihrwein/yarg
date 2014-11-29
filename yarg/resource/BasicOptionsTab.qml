import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

Tab {
    height: parent.height
    width: parent.width
    title: 'Basic options'
    ColumnLayout {
        height: parent.height
        width: parent.width
        anchors.top: parent.top
        anchors.topMargin: 10
        RowLayout {
            Layout.preferredHeight: rowHeight
            Layout.fillWidth: true
            Text {
                anchors {
                    verticalCenter: parent.verticalCenter
                }
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: tabView.width / 3
                text: 'Name'
            }
            TextField {
                id:name_value
                anchors {
                    verticalCenter: parent.verticalCenter
                    right: parent.right
                    rightMargin: 10
                }
                horizontalAlignment: Text.AlignHCenter
                Layout.fillWidth: true
                text: mainController.selected_profile.name
            }
            Binding {
                target: mainController.selected_profile
                property: 'name'
                value: name_value.text
            }
        }
        RowLayout {
            Layout.preferredHeight: rowHeight
            width: parent.width
            Text {
                anchors {
                    verticalCenter: parent.verticalCenter
                }
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: tabView.width / 3
                text: 'Last synchronization'
            }
            Text {
                anchors {
                    verticalCenter: parent.verticalCenter
                    right: parent.right
                    rightMargin: 10
                }
                horizontalAlignment: Text.AlignHCenter
                Layout.fillWidth: true
                text: mainController.selected_profile.last_sync
            }
        }
        RowLayout {
            Layout.preferredHeight: rowHeight
            width: parent.width
            Text {
                anchors {
                    verticalCenter: parent.verticalCenter
                }
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: tabView.width / 3
                text: 'Remote component'
            }
            RowLayout {
                Layout.preferredHeight: rowHeight
                Layout.fillWidth: true
                ExclusiveGroup { id: remoteComponentSelectionGroup }
                RadioButton {
                    Layout.fillWidth: true
                    id: remoteSourceButton
                    text: 'Source'
                    exclusiveGroup: remoteComponentSelectionGroup
                }
                RadioButton {
                    Layout.fillWidth: true
                    id: remoteDestinationButton
                    checked: true
                    text: 'Destination'
                    exclusiveGroup: remoteComponentSelectionGroup
                }
                RadioButton {
                    Layout.fillWidth: true
                    id: noRemoteComponentButton
                    text: 'Neither'
                    exclusiveGroup: remoteComponentSelectionGroup
                }
            }
        }
        ColumnLayout {
            id: remoteComponentConfiguration
            visible: !noRemoteComponentButton.checked
            Layout.fillWidth: true
            RowLayout {
                Layout.preferredHeight: rowHeight
                width: parent.width
                Text {
                    anchors {
                        verticalCenter: parent.verticalCenter
                    }
                    horizontalAlignment: Text.AlignHCenter
                    Layout.preferredWidth: tabView.width / 3
                    text: 'Remote host'
                }
                TextField {
                    anchors {
                        verticalCenter: parent.verticalCenter
                        right: parent.right
                        rightMargin: 10
                    }
                    horizontalAlignment: Text.AlignHCenter
                    Layout.fillWidth: true
                    text: 'host'
                }
            }
            RowLayout {
                Layout.preferredHeight: rowHeight
                width: parent.width
                Text {
                    anchors {
                        verticalCenter: parent.verticalCenter
                    }
                    horizontalAlignment: Text.AlignHCenter
                    Layout.preferredWidth: tabView.width / 3
                    text: 'Remote port'
                }
                TextField {
                    anchors {
                        verticalCenter: parent.verticalCenter
                        right: parent.right
                        rightMargin: 10
                    }
                    horizontalAlignment: Text.AlignHCenter
                    Layout.fillWidth: true
                    text: 'port'
                }
            }
            RowLayout {
                Layout.preferredHeight: rowHeight
                width: parent.width
                Text {
                    anchors {
                        verticalCenter: parent.verticalCenter
                    }
                    horizontalAlignment: Text.AlignHCenter
                    Layout.preferredWidth: tabView.width / 3
                    text: 'Remote user'
                }
                TextField {
                    anchors {
                        verticalCenter: parent.verticalCenter
                        right: parent.right
                        rightMargin: 10
                    }
                    horizontalAlignment: Text.AlignHCenter
                    Layout.fillWidth: true
                    text: 'user'
                }
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Layout.preferredHeight: rowHeight
            Text {
                anchors {
                    verticalCenter: parent.verticalCenter
                }
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: tabView.width / 3
                text: 'Destination path'
            }
            TextField {
                Layout.fillWidth: true
                text: 'path'
                horizontalAlignment: Text.AlignHCenter
                anchors {
                    verticalCenter: parent.verticalCenter
                    right: parent.right
                    rightMargin: 10
                }
            }
        }
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Text {
                Layout.fillHeight: true
                horizontalAlignment: Text.AlignHCenter
                Layout.preferredWidth: tabView.width / 3
                text: 'Source paths'
            }
            ColumnLayout {
                Layout.fillHeight: true
                Layout.fillWidth: true
                anchors {
                    right: parent.right
                    rightMargin: 10
                }
                Button {
                    Layout.fillWidth: true
                    text: '+'
                    onClicked: {
                        mainController.add_source_path_clicked()
                    }
                }
                ListView {
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    model: mainController.selected_profile.source_paths
                    delegate: RowLayout {
                        height: rowHeight + 5
                        width: parent.width
                        TextField {
                            Layout.fillWidth: true
                            text: object
                        }
                        Button {
                            text: '-'
                            onClicked: {
                                mainController.remove_source_path_clicked(index)
                            }
                        }
                    }
                }
            }
        }
    }
}