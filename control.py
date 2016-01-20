a = 0
b = 0
i=1

def getchar():
 import tty, termios, sys
 fd = sys.stdin.fileno()
 old_settings = termios.tcgetattr(fd)
 try:
  tty.setraw(sys.stdin.fileno())
  ch = sys.stdin.read(1)
 finally:
  termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
 return ch
import RPIO
from RPIO import PWM
servo = PWM.Servo()
#motor speed
#maxs=9990
maxs=19000
#set up left and right motor controls
servo.set_servo(22,maxs)
servo.set_servo(23,maxs)
#RPIO.setup(7,RPIO.OUT)#
RPIO.setup(17,RPIO.OUT)# enable
#RPIO.setup(13,RPIO.OUT)# enable
RPIO.setup(24,RPIO.OUT)
print 'q to quit, wasd to drive'
while 1:
 ch = getchar()
 if ch == 'q':
  RPIO.cleanup()
  break
 elif ch == 'w':
  RPIO.output(17,False)
  RPIO.output(24,False)
 elif ch =='s':
  RPIO.output(17,True)
  RPIO.output(24,True)
 elif ch =='a':
  RPIO.output(17,True)
  RPIO.output(24,False)

 elif ch =='d':
  RPIO.output(17,False)
  RPIO.output(24,True)
 
