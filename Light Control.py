#intiate GPIO Pins
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#intiate PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-48410fe0-13a2-11e8-a78c-ded3dc92678b"
pnconfig.publish_key = "pub-c-72bf2a98-14d8-488b-b6f9-2c4b76cbd3a7"
pnconfig.ssl = False

pubnub = PubNub(pnconfig)

pubnub.subscribe().channels('J-Lamp').execute()
