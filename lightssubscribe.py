import paho.mqtt.publish as publish

publish.single("lights/control", "[0,0,0,0,0,0,0,255,255,255,255,255,0,0,0,0,0,0,255,255]", hostname="mqtt.panerahackathon.com")