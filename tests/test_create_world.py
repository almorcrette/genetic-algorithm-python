import path_helper

from create_world import create_world
from generate_trial import generate_trial


def test_create_world_returns_list_length_num_trials():
    num_trials = 10
    trial_generator = generate_trial
    generator_arg_size = 10
    generator_arg_food_proportion = 0.5
    world = create_world(
        num_trials,
        trial_generator,
        generator_arg_size,
        generator_arg_food_proportion
        )
    assert len(world) == num_trials

    num_trials = 5
    trial_generator = generate_trial
    generator_arg_size = 10
    generator_arg_food_proportion = 0.5
    world = create_world(
        num_trials,
        trial_generator,
        generator_arg_size,
        generator_arg_food_proportion
        )
    assert len(world) == num_trials

    num_trials = 2
    trial_generator = generate_trial
    generator_arg_size = 10
    generator_arg_food_proportion = 0.5
    world = create_world(
        num_trials,
        trial_generator,
        generator_arg_size,
        generator_arg_food_proportion
        )
    assert len(world) == num_trials

# Missing tests for trial_generator and generator_args