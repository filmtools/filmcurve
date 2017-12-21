# content of test_sample.py

import pytest
from FilmTools.FilmCurve import FilmCurve


class TestFilmCurve(object):

    @pytest.mark.parametrize("target,density,expected_offset", [
        (8, 1.29, -1.63)
    ])
    def test_findOffset(self, target, density, expected_offset):
        zones = [ 0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00 ]
        densities = [ 0.02, 0.08, 0.17, 0.29, 0.44, 0.63, 0.86, 1.03, 1.16, 1.22, 1.34 ]
        calculator = FilmCurve(zones, densities)

        offset = calculator.getOffset( target, density )

        max_deviation = 0.005
        assert abs(offset - expected_offset) <= max_deviation



    @pytest.mark.parametrize("density,expected_zone", [
        (1.29, 9.63)
    ])
    def test_FindZone(self, density, expected_zone):
        zones = [ 0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00 ]
        densities = [ 0.02, 0.08, 0.17, 0.29, 0.44, 0.63, 0.86, 1.03, 1.16, 1.22, 1.34 ]
        calculator = FilmCurve(zones, densities)

        zone = calculator.findZone( density )

        max_deviation = 0.005
        assert abs(zone - expected_zone) <= max_deviation




    @pytest.mark.parametrize("zone,expected_density", [
        (4.00, 0.44)
    ])
    def test_findDensity(self, zone,expected_density):
        zones = [ 0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00 ]
        densities = [ 0.02, 0.08, 0.17, 0.29, 0.44, 0.63, 0.86, 1.03, 1.16, 1.22, 1.34 ]
        calculator = FilmCurve(zones, densities)

        density = calculator.findDensity( zone )

        max_deviation = 0.005
        assert abs(density - expected_density) <= max_deviation
