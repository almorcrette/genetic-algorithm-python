import path_helper

from create_genome import create_genome


def test_create_genome_returns_list_with_number_elements_equal_to_features_to_power_of_spaces():
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


def test_create_genome_returns_list_of_unique_elements():
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


def test_create_genome_returns_list_of_strings_of_length_spaces():
    spaces = 5
    features = 3
    genome = create_genome(spaces, features)
    for x in genome:
        assert len(x) == spaces

    spaces = 5
    features = 2
    genome = create_genome(spaces, features)
    for x in genome:
        assert len(x) == spaces

    spaces = 3
    features = 3
    genome = create_genome(spaces, features)
    for x in genome:
        assert len(x) == spaces

# Final test which checks that every char is one of the digits in the range of features

def test_create_genome_returns_list_of_strings_whose_characters_are_only_digits_in_range_of_features():
    spaces = 5
    features = 3
    feature_options = list(range(features))
    genome = create_genome(spaces, features)
    for x in genome:
        for char in x:
            assert int(char) in feature_options

    spaces = 5
    features = 2
    feature_options = list(range(features))
    genome = create_genome(spaces, features)
    for x in genome:
        for char in x:
            assert int(char) in feature_options

    spaces = 3
    features = 3
    feature_options = list(range(features))
    genome = create_genome(spaces, features)
    for x in genome:
        for char in x:
            assert int(char) in feature_options
