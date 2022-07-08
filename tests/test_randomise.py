import path_helper
import mock_random

import randomise
import func

def test_answer(mocker):
    print('func', func)
    print('randomise', randomise)

    mocker.patch.object(randomise, "random", mock_random.cycler_0_9)
    assert randomise.my_function() == 0
    assert randomise.my_function() == 1
    assert randomise.my_function() == 2
    assert randomise.my_function() == 3
    assert randomise.my_function() == 4
    assert randomise.my_function() == 5
    assert randomise.my_function() == 6
    assert randomise.my_function() == 7
    assert randomise.my_function() == 8
    assert randomise.my_function() == 9
    assert randomise.my_function() == 0

