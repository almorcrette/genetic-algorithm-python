import path_helper

from randomise_genotype import randomise_genotype


def test_randomise_genotype_returns_string_of_integers():
    num_spaces = 5
    num_features = 3
    num_responses = 7
    genotype = randomise_genotype(num_spaces, num_features, num_responses)
    assert isinstance(genotype, str) == True
    assert isinstance(int(genotype), int) == True


def test_randomise_genotype_returns_string_length_num_features_to_power_num_spaces():
    num_spaces = 5
    num_features = 3
    num_responses = 7
    genotype = randomise_genotype(num_spaces, num_features, num_responses)
    assert len(genotype) == num_features ** num_spaces


def test_randomise_genotype_returns_integer_whose_digits_are_only_in_range_of_num_responses():
    num_spaces = 5
    num_features = 3
    num_responses = 7
    response_options = list(range(num_responses))

    genotype = randomise_genotype(num_spaces, num_features, num_responses)

    for char in genotype:
        assert int(char) in response_options


# test that return values are random