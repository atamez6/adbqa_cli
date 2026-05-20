from ..utils_tools import adb_main_runner as am

class Devices_commands:

    def __init__(self,device_id):
        pass

    def check_device_id(self,device_id):
            if not device_id:
                print("Error: device: id missed")
                return None
            
            device_id = device_id.strip()
            return device_id



    def adb_connect(self,device_id):
        try:
            device_id = self.check_device_id(device_id)
            if not device_id:
                return None
            return am.adb_runner_comm(command="connect",device_id=device_id)
        
        except Exception as e:
            print("error connecting")
            return None


    def adb_disconnect(self,device_id):
        try:
            device_id = self.check_device_id(device_id)
            if not device_id:
                return None
            return am.adb_runner_comm(command="disconnect",device_id=device_id)
        
        except Exception as e:
            print("error disconnecting")
            return None
