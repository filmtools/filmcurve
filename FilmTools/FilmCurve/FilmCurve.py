import numpy as np
import time

class FilmCurve:

    def __init__(self, zones, densities, x_precision = 12):
        self.setDensities( densities )
        self.setZones( zones )
        self.x_precision = x_precision


    def setZones(self, zones):
        self.zones = zones
        self.createInterpolator()


    def getZones( self ):
        return self.zones


    def setDensities( self, densities):
        self.densities = densities


    def getDensities( self):
        return self.densities


    def createInterpolator( self ):
        #
        # Determine the 5th grade polynomial coefficients
        # and create f(y) model function
        #
        zones_arr = np.array( self.getZones() )
        densities_arr = np.array( self.getDensities() )

        self.coefficients, self.residuals, _, _, _ = np.polyfit(zones_arr, densities_arr, 5, full=True)
        self.interpolator = np.poly1d( self.coefficients )


    def setOffset( self, offset ):
        offset_zones = [ x + offset for x in self.zones]
        self.setZones( offset_zones )


    # Find the in-fact zone for the given density
    # and return the numeric difference to given zone
    # as *negative* number.
    #
    # N.B. The result is negative as used in darkroom analysis.
    def getOffset( self, zone, density):

        found_at = self.findZone( density )

        return zone - found_at


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

        #
        # A. Experiment - is this better than the B. section below?
        #

        # zone_interpolated = np.interp( density, self.interpolator(self.zones), self.zones)
        # return zone_interpolated


        # B. Find good start point for x,
        # incrementing with decreasing steps
        # until calculated y (density) value slightly below the target value

        x = 0
        y = None

        timeout = time.time() + 30 # 30 seconds from now

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


