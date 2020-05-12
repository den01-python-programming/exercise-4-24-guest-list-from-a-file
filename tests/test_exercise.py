import pytest
import src.exercise
import os

def test_exercise():
    os.chdir('src')
    input_values = ["names.txt","james","ada","leo",""]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["Name of the file:","Enter names, an empty line quits.","The name is not on the list.",\
                      "Enter names, an empty line quits.","The name is on the list.",\
                      "Enter names, an empty line quits.","The name is not on the list.","Enter names, an empty line quits.","Thank you!"]
