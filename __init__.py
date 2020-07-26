from mycroft import MycroftSkill, intent_file_handler


class HdmiCecControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.cec.hdmi.intent')
    def handle_control_cec_hdmi(self, message):
        self.speak_dialog('control.cec.hdmi')


def create_skill():
    return HdmiCecControl()

