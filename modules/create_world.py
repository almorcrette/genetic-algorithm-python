def create_world(num_trials, trial_generator, *generator_args):
    world = []
    for _ in range(num_trials):
        world.append(trial_generator(*generator_args))
    return world
