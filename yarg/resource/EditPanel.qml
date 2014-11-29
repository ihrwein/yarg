import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ColumnLayout {
    width: parent.width
    height: parent.height
    RowLayout {
        spacing: 0
        width: parent.width
        Button {
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Save & Close"
            onClicked: {
                mainController.edit_panel_save_clicked()
                stackView.pop();
            }
        }
        Button {
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Close"
            onClicked: {
                mainController.edit_panel_close_clicked()
                stackView.pop();
            }
        }
    }
    Text {
        Layout.fillWidth: true
        Layout.minimumHeight: 30
        font.pointSize: 16
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        text : mainController.selected_profile.name
    }
    property int rowHeight: 25
    TabView {
        id: tabView
        Layout.fillWidth: true
        Layout.fillHeight: true
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
                                mainController.selected_profile.source_paths.addItem("asd")
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
                                Button { text: '-' }
                            }
                        }
                    }
                }
            }
        }
        Tab {
            title: 'Rsync parameters'
            ListView {
                Layout.fillWidth: true
                Layout.fillHeight: true
                model: mainController.selected_profile.rsync_options
                spacing:0
                anchors.top: parent.top
                anchors.topMargin: 10
                delegate: Item {
                    width: parent.width
                    height: 30
                    RowLayout {
                        width: parent.width
                        height: parent.height
                        Text {
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            Layout.preferredWidth: tabView.width / 3
                            text: object.key
                        }
                        Loader {
                            Layout.fillWidth: true
                            Layout.fillHeight: true
                            property variant model: object
                            sourceComponent: object.option_type == 'bool' ? bool_option_model : object.option_type == 'string' ? string_option_model : int_option_model
                        }
                    }
                }
            }
        }
    }
    Component {
        id: bool_option_model
        Item {
            anchors {
                right: parent.right
                rightMargin: 10
            }
            CheckBox {
                id: bool_option_value
                anchors {
                    verticalCenter: parent.verticalCenter
                    horizontalCenter: parent.horizontalCenter
                }
                checked: model.value
                style: CheckBoxStyle {
                    label: Item {}
                }
                Component.onCompleted: checked = model.value
                onClicked: model.value = checked
                Connections {
                    target: model
                    onValueChanged: bool_option_value.checked = model.value
                }
            }
        }
    }
    Component {
        id: string_option_model
        Item {
            Layout.fillWidth: true
            TextField {
                anchors {
                    verticalCenter: parent.verticalCenter
                    right: parent.right
                    rightMargin: 10
                }
                horizontalAlignment: Text.AlignHCenter
                width: parent.width
                id: string_option_value
                text: model.value
            }
            Binding {
                target: model
                property: 'value'
                value: string_option_value.text
            }
        }
    }
    Component {
        id: int_option_model
        Item {
            Layout.fillWidth: true
            TextField {
                anchors {
                    verticalCenter: parent.verticalCenter
                    right: parent.right
                    rightMargin: 10
                }
                horizontalAlignment: Text.AlignHCenter
                width: parent.width
                id: int_option_value
                text: model.value
                validator: IntValidator {}
            }
            Binding {
                target: model
                property: 'value'
                value: int_option_value.text
            }
        }
    }
    Component {
        id: float_option_model
        Item {
            Layout.fillWidth: true
            TextField {
                anchors {
                    verticalCenter: parent.verticalCenter
                    right: parent.right
                    rightMargin: 10
                }
                horizontalAlignment: Text.AlignHCenter
                width: parent.width
                id: float_option_value
                text: model.value
                validator: DoubleValidator {locale: 'en-US'}
            }
            Binding {
                target: model
                property: 'value'
                value: float_option_value.text
            }
        }
    }
}

