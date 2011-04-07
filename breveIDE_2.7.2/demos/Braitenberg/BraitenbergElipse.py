
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
		self.block = None
		self.sound = None
		self.obj = None
		
		self.blw = None
		self.brw = None
		
		myBraitenbergControl.init( self )

	def init( self ):
			
		'''Creates the vehicle.'''
		self.vehicle = breve.createInstances( breve.BraitenbergElipser, 1 )
		self.watch( self.vehicle )

		intensity = 1
	
		'''Makes the initial setup of the vehicle and places it in the right position.'''
		self.vehicle.move(breve.vector(2,1,10))
		self.vehicle.rotate(breve.vector(0,1,0),3.14)
		
		'''Sets the scenario.'''
		self.sound = breve.createInstances( breve.BraitenbergSound,1)
		self.sound.move( breve.vector(2,1,15))
		self.sound.setIntensity(intensity)

		self.sound = breve.createInstances( breve.BraitenbergSound,1)
		self.sound.move( breve.vector(-20,1,15))
		self.sound.setIntensity(intensity)

breve.myBraitenbergControl = myBraitenbergControl


# Create an instance of our controller object to initialize the simulation

myBraitenbergControl()
