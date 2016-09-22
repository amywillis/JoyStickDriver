import gobject
import signal
import os
import time
from joy import	Joystick


def axisHandler(signal,number,value,init):
    print("%s %s %s %s" % ('axis',number,value,init) ) 
    
try: 		
        j = Joystick(0) 
        j.connect('axis',axisHandler)
        loop = gobject.MainLoop()
        context = loop.get_context()
        while True: 			
			if context.pending():
				context.iteration( True )
			else:
				time.sleep(0.01)

		#loop.run() 
except Exception,e: 
        print(e) 
