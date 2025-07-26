from langflow.custom import Component
from langflow.io import MessageTextInput, Output, MessageInput
from langflow.schema.message import Message


class MultiChoiceRouterComponent(Component):
    display_name = "Multi-Choice Router"
    description = "Routes an input message to one of five outputs based on text comparison."
    icon = "split"
    name = "MultiChoiceRouter"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    inputs = [
        MessageTextInput(
            name="input_text",
            display_name="Text Input",
            info="The primary text input for the operation.",
        ),
        MessageTextInput(
            name="match_text1",
            display_name="Match Text for Choice 1",
            info="If input text matches this text, route to Choice 1.",
        ),
        MessageTextInput(
            name="match_text2",
            display_name="Match Text for Choice 2",
            info="If input text matches this text, route to Choice 2.",
        ),
        MessageTextInput(
            name="match_text3",
            display_name="Match Text for Choice 3",
            info="If input text matches this text, route to Choice 3.",
        ),
        MessageTextInput(
            name="match_text4",
            display_name="Match Text for Choice 4",
            info="If input text matches this text, route to Choice 4.",
        ),
        MessageTextInput(
            name="match_text5",
            display_name="Match Text for Choice 5",
            info="If input text matches this text, route to Choice 5.",
        ),
        MessageTextInput(
            name="match_text6",
            display_name="Match Text for Choice 6",
            info="If input text matches this text, route to Choice 6.",
        ),
        MessageTextInput(
            name="match_text7",
            display_name="Match Text for Choice 7",
            info="If input text matches this text, route to Choice 7.",
        ),
        MessageInput(
            name="message",
            display_name="Message",
            info="The message to pass through either route.",
            advanced=True,
        ),
    ]

    outputs = [
        Output(display_name="Choice 1", name="choice1", method="choice1_response"),
        Output(display_name="Choice 2", name="choice2", method="choice2_response"),
        Output(display_name="Choice 3", name="choice3", method="choice3_response"),
        Output(display_name="Choice 4", name="choice4", method="choice4_response"),
        Output(display_name="Choice 5", name="choice5", method="choice5_response"),
        Output(display_name="Choice 6", name="choice6", method="choice6_response"),
        Output(display_name="Choice 7", name="choice7", method="choice7_response"),
    ]

    def evaluate_match(self, input_text: str, match_text: str) -> bool:
        """Evaluates if input text exactly matches the match text"""
        input_text = input_text.lower()
        match_text = match_text.lower()
        
        return input_text == match_text

    def stop_other_routes(self, active_route: str):
        """Stops all routes except the active one"""
        routes_to_stop = ["choice1", "choice2", "choice3", "choice4", "choice5", "choice6", "choice7"]
        routes_to_stop.remove(active_route)
        for route in routes_to_stop:
            self.stop(route)

    def choice1_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text1)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice1")
            return self.message
        return self.message

    def choice2_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text2)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice2")
            return self.message
        return self.message

    def choice3_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text3)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice3")
            return self.message
        return self.message

    def choice4_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text4)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice4")
            return self.message
        return self.message
        
    def choice5_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text5)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice5")
            return self.message
        return self.message

    def choice6_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text6)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice6")
            return self.message
        return self.message

    def choice7_response(self) -> Message:
        is_match = self.evaluate_match(self.input_text, self.match_text7)
        if is_match:
            self.status = self.message
            self.stop_other_routes("choice7")
            return self.message
        return self.message
