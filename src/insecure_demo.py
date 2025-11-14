import subprocess

def run_os_command_untrusted(user_input):
    """
    Intentionally insecure example for Bandit demo:
    shell=True on untrusted input can be dangerous.
    """
    subprocess.Popen(user_input, shell=True)  # Bandit should flag this
