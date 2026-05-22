import subprocess



def adb_runner_comm(command):
    try:
        response_stdout =subprocess.run(f'{command}',capture_output=True, text=True,shell=True)
        command_stdout= response_stdout.stdout
        print(command_stdout)
        return command_stdout
    except Exception as error:
        print("error runnign command")
        return None