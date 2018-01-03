import numpy as np
import time

class FilmCurve:

    def __init__(self, zones, densities, x_precision = 12):

        # Store for later use
        self.zones = zones
        self.densities = densities
        self.x_precision = x_precision

        #
        # Determine the 5th grade polynomial coefficients
        # and create f(y) model function
        #
        coefficients, residuals, _, _, _ = np.polyfit(zones, densities, 5, full=True)
        self.coefficients = coefficients
        self.residuals    = residuals
        self.interpolator = np.poly1d( coefficients )


    #
    # OK, thats simple
    #
    def findDensity( self, zone ):
        return self.interpolator( zone )


    #
    # Kind of goal seek:
    # Find x where interpolator(x) first meets (and firstly equals)
    # the given density y.
    #
    def findZone( self, density ):

        # Find good start point for x,
        # incrementing with decreasing steps
        # until calculated y (density) value slightly below the target value

        density_in_curve=False
        for z in self.zones:
            if not density_in_curve:
                y = self.interpolator( z )
                if y >= density:
                    density_in_curve = True


        if density_in_curve:
            x = 0
        else:
            y_found = False
            for x in range(1, 100000, 1):
                y = self.interpolator( x )
                # print "x,y: ", x, y
                if y >= density:
                    y_found = True
                    return y
            if not y_found:
                return x
            x = x - 1

        timeout = time.time() + 30 # 30 seconds from now

        y = None
        for i in range(1, self.x_precision):
            x_increment = (10**i-1)**-1
            while time.time() <= timeout and y <= density:
                y = self.interpolator( x )
                if y < density:
                    x = x + x_increment

            # y now is greater than requested,
            # so step back and calculate new (smaller) y
            x = x - x_increment
            y = self.interpolator( x )


        # Now perform 'precise' goal seek,
        # starting from last found x
        x_increment = (10** self.x_precision)**-1
        y = None

        while time.time() <= timeout and y <= density:
            y = self.interpolator( x )
            x = x + x_increment

        # x is zone
        return x


    # Find the in-fact zone for the given density
    # and return the numeric difference to given zone
    # as *negative* number.
    #
    # N.B. The result is negative as used in darkroom analysis.
    def getOffset( self, zone, density):

        found_at = self.findZone( density )

        return zone - found_at

