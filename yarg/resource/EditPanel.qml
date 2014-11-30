import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.1
import QtQuick.Controls.Styles 1.1
import QtQuick.Layouts 1.0

ColumnLayout {
    width: parent.width
    height: parent.height
    RowLayout {
        spacing: 0
        width: parent.width
        Layout.fillWidth: true
        Layout.minimumHeight: 40
        Button {
            Layout.minimumHeight: 40
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            style: ButtonStyle {}
            text: "Save & Close"
            onClicked: {
                stackView.pop();
                mainController.edit_panel_save_clicked()
            }
        }
        Button {
            Layout.minimumHeight: 40
            Layout.maximumWidth: parent.width / 2
            Layout.fillWidth: true
            text: "Close"
            onClicked: {
                stackView.pop();
                mainController.edit_panel_close_clicked()
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
        BasicOptionsTab {}
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
                            sourceComponent: object.option_type == 'bool' ? bool_option_model : object.option_type == 'str' ? string_option_model : int_option_model
                        }
                    }
                }
            }
        }
    }
    Component {
        id: bool_option_model
        Item {
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
                text: model ? model.value : ''
                placeholderText: model ? model.hint : ''
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
                text: model ? model.value : ''
                placeholderText: model ? model.hint : ''
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
                placeholderText: model.hint
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

