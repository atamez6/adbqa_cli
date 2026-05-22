from ..utils_tools import adb_main_runner as am

class Devices_commands:

    def __init__(self):
        pass



    def send_command(self,command):
        try:
            command_stdout = am.adb_runner_comm(command)
            print(f"command stdout => {command_stdout}")
            return True
        
        except Exception as e:
            print(e)
            return None

    def check_device_id(self,device_id):
        if not device_id:
            print("Error: device: id missed")
            return None
        
        device_id = device_id.strip()
        return device_id

    def adb_devices(self):
        
        devices_commands= "adb devices"
        self.send_command(devices_commands)
        return True


    def adb_connect(self,device_id):
        device_id = self.check_device_id(device_id)
        connect_commands= f"adb connect {device_id}"
        self.send_command(connect_commands)
        return True


    def adb_disconnect(self,device_id):
        device_id = self.check_device_id(device_id)
        disconnect_commands= f"adb disconnect {device_id}"
        self.send_command(disconnect_commands)
        return True




    def adb_logcat(self,device_id):
        #adb -s <device_id> logcat -d
        #print head20 en pantalla, full logs as txt
        #logs as file, function read file, search for events, top wef,crash
        #i can search a word in the log file as "claro" 
        #todo con singularidad y separado,,,,
        pass

    def adb_memory(self,device_id):
        pass

    def adb_install(self,device_id):
        pass


    def adb_uninstall(self,device_id):
        pass

    def adb_screen(self,device_id):
        pass

    def adb_reboot(self,device_id):
        pass

    def adb_root(self,device_id):
        pass

    def adb_dumpsys(self,device_id):
        pass

    def adb_star_stop_app(self,device_id):
        pass

    
    def adb_file_mgr(self,device_id):
        pass


if __name__ == "__main__":
   device_id="192.168.0.108:5555"
   run = Devices_commands()
   #run.adb_devices(device_id)
   run.adb_disconnect(device_id)
   run.adb_connect(device_id)
   run.adb_devices()

   '''
   en devices ver el estado, wait, for device, etc
   '''