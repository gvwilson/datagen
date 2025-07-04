"""Test fixtures and configuration."""

import pytest
from datagen.parameters import Parameters
from datagen.person import Person
from datagen.grid import Grid
from datagen.sample import Sample


@pytest.fixture
def default_params():
    """Default parameters for testing."""
    return Parameters()


@pytest.fixture
def fx_persons(default_params):
    """Sample persons for testing."""
    return [Person.make(default_params) for _ in range(3)]


@pytest.fixture
def fx_grids(default_params):
    """Sample grids for testing."""
    return [Grid.make(default_params) for _ in range(2)]


@pytest.fixture
def fx_samples(default_params, fx_grids, fx_persons):
    """Sample samples for testing."""
    return [Sample.make(default_params, fx_grids, fx_persons) for _ in range(5)]
