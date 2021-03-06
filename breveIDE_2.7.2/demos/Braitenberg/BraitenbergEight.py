
# Note: this file was automatically converted to Python from the
# original steve-language source code.  Please see the original
# file for more detailed comments and documentation.


import breve
import os

class myBraitenbergControl( breve.BraitenbergControl ):
	def __init__( self ):
		breve.BraitenbergControl.__init__( self )
		self.leftSensor = None
		self.leftWheel = None
		self.light = None
		self.n = 0
		self.rightSensor = None
		self.rightWheel = None
		self.vehicle = None
		self.scenario = 'Elipse'
		self.block = None
		self.sound = None
		self.obj = None
		
		self.blw = None
		self.brw = None
		
		myBraitenbergControl.init( self )

	def init( self ):
			
		'''Creates the vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergEightMaker, 1 )
		self.watch( self.vehicle )
		self.vehicle.move(breve.vector(0,1,9))
		
		self.block = breve.createInstances( breve.BraitenbergSound,1)
		self.block.move( breve.vector (0, 1, 16))
		self.block.setIntensity(1.5)

		self.block = breve.createInstances( breve.BraitenbergSound,1)
		self.block.move( breve.vector (0, 1, 0))
		self.block.setIntensity(1.5)	


breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
