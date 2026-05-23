import subprocess



def adb_runner_comm(command):
    try:
        response_stdout =subprocess.run(f'{command}',capture_output=True, text=True,shell=True)
        command_return = response_stdout.stdout + response_stdout.stderr

        return command_return
    except Exception as error:
        print("error runnign command")
        print(error)
        return None