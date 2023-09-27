import sys
from database.db_utils import connect_to_database, add_message


def main():
    # Connect to the database
    if connect_to_database():
        print("Connected to database")
        add_message("hello/","hello world")
        
        #client = mqtt.Client()
        #client.on_connect = on_connect
        #client.on_message = on_message
    
        # Connect to the MQTT broker
        # You will need to change the hostname to the IP address or hostname of your MQTT broker
        #client.connect("mqtt.eclipse.org", 1883, 60)  
    
        # Blocking call that processes network traffic, dispatches callbacks, and handles reconnecting.
        #client.loop_forever()
    else:
        sys.exit(1)
    

if __name__ == "__main__":
    main()