import os
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "{Device Connection String}"

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while True:
            # Get the data from the IoT device
            data = get_data_from_device()
            message = Message(data)

            # Send the message to IoT Hub
            client.send_message(message)
            print("Message sent: {}".format(data))
            time.sleep(1)

    except KeyboardInterrupt:
        print("IoT Hub device sample stopped")

if __name__ == '__main__':
    iothub_client_telemetry_sample_run()


# 
# This code sends periodic messages containing real-time data from the IoT device to the Azure IoT Hub. 
# The get_data_from_device function should be replaced with the actual code to retrieve the data from the IoT device.