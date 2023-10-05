import time
import board
import digitalio
import pwmio


from adafruit_motor import motor

left_motor_forward = board.GP15
left_motor_backward = board.GP14
right_motor_forward = board.GP12
right_motor_backward = board.GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000)
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000)


Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0

Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0

while True:


#Both  forward
    Right_Motor_speed = .5 #Makes right motor go forward
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = .5 #Makes left motor go forward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
#Both backward
    Left_Motor_speed = -.5 #Makes let motor go backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -.5 #Makes right motor go backward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)    
#Both left
    Left_Motor_speed = 0 #Makes left motor go forward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(0)
    Right_Motor_speed = .5 #Makes right motor go forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(1)
#Both right
    Right_Motor_speed =0 #Makes right motor go forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(0)
    Left_Motor_speed = 0.5 #Makes left motor go forward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
