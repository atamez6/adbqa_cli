import subprocess


def check_device_id(**args):
    devce_id= args[device_id]
    if device_id:
        device_id = device_id.strip().lower()
    if not device_id:
        print("Error: device: id missed")

def adb_runner_comm(**args):
    try:
        subprocess.run(f"adb {args["command"]} {args["device_id"]}",capture_output=True, text=True)
    except Exception as error_connecting:
        print("error connecting")
        return 0