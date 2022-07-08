import pytest
from functools import reduce
import path_helper

from generate_trial import generate_trial


def test_generate_trial_return_has_width_and_height_equal_to_size():
    size = 10
    food_proportion = 0
    trial = generate_trial(size, food_proportion)
    assert len(trial) == size

    size = 20
    food_proportion = 0
    trial = generate_trial(size, food_proportion)
    assert len(trial) == size


def test_generate_trial_returns_cells_only_0s_and_1s():
    size = 10
    food_proportion = 0.1
    trial = generate_trial(size, food_proportion)
    for i in range(size):
        for j in range(size):
            assert (trial[i][j] == 1 or trial[i][j] == 0)

    size = 10
    food_proportion = 0.5
    trial = generate_trial(size, food_proportion)
    for i in range(size):
        for j in range(size):
            assert (trial[i][j] == 1 or trial[i][j] == 0)

    size = 20
    food_proportion = 0.5
    trial = generate_trial(size, food_proportion)
    for i in range(size):
        for j in range(size):
            assert (trial[i][j] == 1 or trial[i][j] == 0)


def test_generate_trial_returns_food_proportion_cells_of_1s():
    size = 10
    food_proportion = 0.1
    num_cells = food_proportion * size * size
    trial = generate_trial(size, food_proportion)
    total_food = 0
    for x in trial:
        total_food += reduce(lambda a, b: a + b, x)
    assert total_food == num_cells

    size = 10
    food_proportion = 0.2
    num_cells = food_proportion * size * size
    trial = generate_trial(size, food_proportion)
    total_food = 0
    for x in trial:
        total_food += reduce(lambda a, b: a + b, x)
    assert total_food == num_cells

    size = 10
    food_proportion = 0.7
    num_cells = food_proportion * size * size
    trial = generate_trial(size, food_proportion)
    total_food = 0
    for x in trial:
        total_food += reduce(lambda a, b: a + b, x)
    assert total_food == num_cells


def test_generate_trial_raises_error_if_food_proportion_greater_than_1():
    size = 10
    food_proportion = 1.1
    exception_msg = 'food_proportion must be between 0 and 1'
    with pytest.raises(Exception, match=exception_msg):
        generate_trial(size, food_proportion)


def test_generate_trial_raises_error_if_food_proportion_less_than_0():
    size = 10
    food_proportion = 1.1
    exception_msg = 'food_proportion must be between 0 and 1'
    with pytest.raises(Exception, match=exception_msg):
        generate_trial(size, food_proportion)
