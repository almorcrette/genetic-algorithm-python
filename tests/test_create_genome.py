import path_helper

from create_genome import create_genome


def test_create_genome_return_list_w_num_els_equal_to_features_to_power_of_spaces():
    spaces = 5
    features = 3
    genome = create_genome(spaces, features)
    assert len(genome) == features ** spaces

    spaces = 5
    features = 5
    genome = create_genome(spaces, features)
    assert len(genome) == features ** spaces

    spaces = 10
    features = 3
    genome = create_genome(spaces, features)
    assert len(genome) == features ** spaces

    spaces = 0
    features = 0
    genome = create_genome(spaces, features)
    assert len(genome) == features ** spaces


def test_create_genome_return_list_of_unique_elements():
    spaces = 5
    features = 3
    genome = create_genome(spaces, features)
    for x in genome:
        genome.remove(x)
        for y in genome:
            assert x != y
        genome.append(x)

    spaces = 5
    features = 2
    genome = create_genome(spaces, features)
    for x in genome:
        genome.remove(x)
        for y in genome:
            assert x != y
        genome.append(x)

    spaces = 3
    features = 3
    genome = create_genome(spaces, features)
    for x in genome:
        genome.remove(x)
        for y in genome:
            assert x != y
        genome.append(x)


def test_create_genome_return_list_of_elements_each_a_string_of_spaces_number_of_chars():
    spaces = 5
    features = 3
    genome = create_genome(spaces, features)
    for x in genome:
        assert len(x) == spaces
