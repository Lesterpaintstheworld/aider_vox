import unittest
from unittest.mock import MagicMock

import aider_vox
from aider_vox.coders import Coder
from aider_vox.commands import Commands
from aider_vox.help import Help
from aider_vox.io import InputOutput
from aider_vox.models import Model


class TestHelp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        io = InputOutput(pretty=False, yes=True)

        GPT35 = Model("gpt-3.5-turbo")

        coder = Coder.create(GPT35, None, io)
        commands = Commands(io, coder)

        help_coder_run = MagicMock(return_value="")
        aider_vox.coders.HelpCoder.run = help_coder_run

        try:
            commands.cmd_help("hi")
        except aider_vox.commands.SwitchCoder:
            pass
        else:
            # If no exception was raised, fail the test
            assert False, "SwitchCoder exception was not raised"

        help_coder_run.assert_called_once()

    def test_init(self):
        help_inst = Help()
        self.assertIsNotNone(help_inst.retriever)

    def test_ask_without_mock(self):
        help_instance = Help()
        question = "What is aider_vox?"
        result = help_instance.ask(question)

        self.assertIn(f"# Question: {question}", result)
        self.assertIn("<doc", result)
        self.assertIn("</doc>", result)
        self.assertGreater(len(result), 100)  # Ensure we got a substantial response

        # Check for some expected content (adjust based on your actual help content)
        self.assertIn("aider_vox", result.lower())
        self.assertIn("ai", result.lower())
        self.assertIn("chat", result.lower())

        # Assert that there are more than 5 <doc> entries
        self.assertGreater(result.count("<doc"), 5)


if __name__ == "__main__":
    unittest.main()
