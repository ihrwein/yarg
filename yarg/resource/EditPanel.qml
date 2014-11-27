import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ColumnLayout {
    anchors.fill: parent
    RowLayout {
        spacing: 0
        width: parent.width
        Button {
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Save & Close"
            onClicked: {
                mainController.edit_panel_save_clicked()
                flipBar.flipDown();
            }
        }
        Button {
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Close"
            onClicked: {
                mainController.edit_panel_close_clicked()
                flipBar.flipDown();
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
    TabView {
        Layout.fillWidth: true
        Layout.fillHeight: true
        Tab {
            title:'Basic options'
            /*
            Column {
                spacing: 0
                Rectangle {
                    width: 50
                    height: 50
                }
                Rectangle {
                    width: 50
                    height: 50
                }
            }
            */
            Column {
                anchors.fill: parent
                RowLayout {
                    width: parent.width
                    height: 40
                    Text {
                        anchors {
                            verticalCenter: parent.verticalCenter
                        }
                        horizontalAlignment: Text.AlignHCenter
                        Layout.preferredWidth: parent.width / 3
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
                    width: parent.width
                    height: 40
                    Text {
                        anchors {
                            verticalCenter: parent.verticalCenter
                        }
                        horizontalAlignment: Text.AlignHCenter
                        Layout.preferredWidth: parent.width / 3
                        text: 'Source'
                    }
                    TextField {
                        anchors {
                            verticalCenter: parent.verticalCenter
                            right: parent.right
                            rightMargin: 10
                        }
                        horizontalAlignment: Text.AlignHCenter
                        Layout.fillWidth: true
                        text: mainController.selected_profile.source
                    }
                }
                RowLayout {
                    width: parent.width
                    height: 40
                    Text {
                        anchors {
                            verticalCenter: parent.verticalCenter
                        }
                        horizontalAlignment: Text.AlignHCenter
                        Layout.preferredWidth: parent.width / 3
                        text: 'Destination'
                    }
                    TextField {
                        anchors {
                            verticalCenter: parent.verticalCenter
                            right: parent.right
                            rightMargin: 10
                        }
                        horizontalAlignment: Text.AlignHCenter
                        Layout.fillWidth: true
                        text: mainController.selected_profile.destination
                    }
                }
                RowLayout {
                    width: parent.width
                    height: 40
                    Text {
                        anchors {
                            verticalCenter: parent.verticalCenter
                        }
                        horizontalAlignment: Text.AlignHCenter
                        Layout.preferredWidth: parent.width / 3
                        text: 'Last synced'
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
            }
        }
        Tab {
            title:'Rsync parameters'
            ListView {
                width: parent.width
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
                            Layout.fillWidth: true
                            Layout.maximumWidth: parent.width / 3
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

