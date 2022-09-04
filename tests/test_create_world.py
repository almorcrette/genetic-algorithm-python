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


def mock_generate_trial_returning_count():
    val = [0]

    def inc():
        val[0] += 1
        return val[0]
    return inc


def test_create_world_returns_list_of_returns_of_trial_generator_calls():
    num_trials = 3
    trial_generator = mock_generate_trial_returning_count()
    world = create_world(
        num_trials,
        trial_generator
        )
    print(world)
    assert world == [1, 2, 3]

    num_trials = 5
    trial_generator = mock_generate_trial_returning_count()
    world = create_world(
        num_trials,
        trial_generator
        )
    print(world)
    assert world == [1, 2, 3, 4, 5]
