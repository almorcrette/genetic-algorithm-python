import path_helper

from randomise_genotype import randomise_genotype


def test_randomise_genotype_returns_sequence_integer_as_integer():
    num_spaces = 5
    num_features = 3
    num_responses = 7
    genotype = randomise_genotype(num_spaces, num_features, num_responses)
    assert isinstance(genotype, int) == True


def test_randomise_genotype_returns_integer_with_num_features_to_power_num_spaces_digits():
    pass


def test_randomise_genotype_returns_integer_whose_digits_are_only_in_range_of_num_responses():
    pass

# test that return values are random