"""Tests for sample module."""

from datetime import date

import pytest

from datagen.sample import Sample


def test_sample_creation(default_params, fx_grids, fx_persons):
    """Test sample creation with default parameters."""
    sample = Sample.make(default_params, fx_grids, fx_persons)
    assert sample.id.startswith("S")
    assert len(sample.id) == 5  # S + 4 digits
    assert sample.grid in [g.id for g in fx_grids]
    assert sample.person in [p.id for p in fx_persons]
    assert 0 <= sample.x < fx_grids[0].size
    assert 0 <= sample.y < fx_grids[0].size
    assert (
        default_params.sample_date_min <= sample.when <= default_params.sample_date_max
    )
    assert (
        default_params.sample_mass_min <= sample.mass <= default_params.sample_mass_max
    )


@pytest.mark.parametrize(
    "changed",
    [{"id": ""}, {"grid": ""}, {"x": -1}, {"y": -1}, {"mass": 0}, {"mass": -1}],
)
def test_sample_parameter_validation(changed):
    """Test invalid sample parameters are rejected."""
    values = {
        "id": "",
        "grid": "G0001",
        "x": 5,
        "y": 3,
        "person": "P0001",
        "when": date(2025, 6, 15),
        "mass": 1.23,
        **changed,
    }
    with pytest.raises(ValueError):
        Sample(**values)


def test_sample_csv_output():
    """Test CSV string output."""
    sample = Sample(
        id="S0001",
        grid="G0001",
        x=5,
        y=3,
        person="P0001",
        when=date(2025, 6, 15),
        mass=1.23,
    )
    csv_output = str(sample)
    assert csv_output == "S0001,G0001,5,3,P0001,2025-06-15,1.23"


def test_sample_unique_ids(default_params, fx_grids, fx_persons):
    """Test that samples get unique IDs."""
    sample1 = Sample.make(default_params, fx_grids, fx_persons)
    sample2 = Sample.make(default_params, fx_grids, fx_persons)
    assert sample1.id != sample2.id


def test_sample_id_format(default_params, fx_grids, fx_persons):
    """Test sample ID format is consistent."""
    sample = Sample.make(default_params, fx_grids, fx_persons)
    assert sample.id[0] == "S"
    assert sample.id[1:].isdigit()
    assert len(sample.id[1:]) == 4
