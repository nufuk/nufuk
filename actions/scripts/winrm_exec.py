import winrm
from st2common.runners.base_action import Action

class Execute_WinRM_Command(Action):
    def run(self, url, username, password, command, transport="ntlm", ssl=False, console_type="cmd", endpoint="wsman", port="5985"):
        validate = 'validate'
        if not ssl:
            validate = 'ignore'


        s = winrm.Session(f'{url}:{port}/{endpoint}', auth=(username, password), transport=transport, server_cert_validation=validate)
        r = ""
        if console_type == 'cmd':
            r = s.run_cmd(command)
        elif console_type == "ps":
            r = s.run_ps(command)

        print(r.status_code)
        print(r.std_err)
        print(r.std_out)
        return