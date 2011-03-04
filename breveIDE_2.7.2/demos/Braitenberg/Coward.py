
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


import breve

class myBraitenbergControl( breve.BraitenbergControl ):
	def __init__( self ):
		breve.BraitenbergControl.__init__( self )
		self.leftSensor = None
		self.leftWheel = None
		self.n = 0
		self.rightSensor = None
		self.rightWheel = None
		self.vehicle = None
		myBraitenbergControl.init( self )

	def init( self ):
		self.n = 0
		while ( self.n < 10 ):
			breve.createInstances( breve.BraitenbergLight, 1 ).move( breve.vector( ( 20 * breve.breveInternalFunctionFinder.sin( self, ( ( self.n * 6.280000 ) / 10 ) ) ), 1, ( 20 * breve.breveInternalFunctionFinder.cos( self, ( ( self.n * 6.280000 ) / 10 ) ) ) ) )
			self.n = ( self.n + 1 )

		self.vehicle = breve.createInstances( breve.BraitenbergVehicle, 1 )
		self.watch( self.vehicle )
		self.vehicle.move( breve.vector( 0, 2, 14 ) )
		self.leftWheel = self.vehicle.addWheel( breve.vector( -0.500000, 0, 1.500000 ) )
		self.rightWheel = self.vehicle.addWheel( breve.vector( -0.500000, 0, -1.500000 ) )
		self.rightSensor = self.vehicle.addSensor( breve.vector( 2.000000, 0.400000, -1.500000 ) )
		self.leftSensor = self.vehicle.addSensor( breve.vector( 2.000000, 0.400000, 1.500000 ) )
		self.leftSensor.link( self.leftWheel )
		self.rightSensor.link( self.rightWheel )
		self.leftSensor.setBias( 15 )
		self.rightSensor.setBias( 15 )


breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()


