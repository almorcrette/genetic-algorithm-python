import path_helper

from create_genome import create_genome


def test_create_genome_return_list_w_num_els_equal_to_features_to_power_of_spaces():
    spaces = 5
    features = 3
    genome = create_genome(spaces, features)
    assert len(genome) == features ** spaces
