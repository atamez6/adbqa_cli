from ..utils_tools import adb_main_runner as am

class Devices_commands:

    def __init__(self):
        pass



    def send_command(self,command):
        try:
            command_return = am.adb_runner_comm(command)
            return print(f"command return => {command_return}")
        
        except Exception as e:
            print(e)
            return None

    def check_device_id(self,device_id):
        if not device_id:
            raise ValueError("device_id error or missing")
        
        return device_id.strip()

    def adb_devices(self):
        
        devices_commands= "adb devices"
        return self.send_command(devices_commands)
   


    def adb_connect(self,device_id):
        device_id = self.check_device_id(device_id)

        connect_commands= f"adb connect {device_id}"

        return self.send_command(connect_commands)



    def adb_disconnect(self,device_id):
        device_id = self.check_device_id(device_id)
        disconnect_commands= f"adb disconnect {device_id}"
        return self.send_command(disconnect_commands)





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
   device_id="192 d68.0.108:5555"
   run = Devices_commands()
   #run.adb_devices(device_id)
   #run.adb_disconnect(device_id)
   run.adb_connect(device_id)
   #run.adb_devices()

   '''
   en devices ver el estado, wait, for device, etc
   '''