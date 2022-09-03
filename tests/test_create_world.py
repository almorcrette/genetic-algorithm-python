import path_helper

from create_world import create_world
from generate_trial import generate_trial


def test_create_world_returns_list_length_num_trials():
    num_trials = 10
    trial_generator = generate_trial
    world = create_world(num_trials, trial_generator)
    assert len(world) == num_trials

    num_trials = 5
    trial_generator = generate_trial
    world = create_world(num_trials, trial_generator)
    assert len(world) == num_trials

    num_trials = 2
    trial_generator = generate_trial
    world = create_world(num_trials, trial_generator)
    assert len(world) == num_trials