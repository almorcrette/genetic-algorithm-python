import path_helper
import mock_random

import randomise
import func

def test_answer(mocker):
    print('func', func)
    print('randomise', randomise)

    mocker.patch.object(randomise, "random", mock_random.mock_random)
    assert randomise.my_function() == 1
    assert randomise.my_function() == 2
    assert randomise.my_function() == 3
