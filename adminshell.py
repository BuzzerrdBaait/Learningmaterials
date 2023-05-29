import subprocess

def run_powershell_command(command):
    try:
        # Use subprocess to run PowerShell
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        
        # Check for errors
        if result.returncode != 0:
            print(f"PowerShell command failed with error code {result.returncode}")
            print(result.stderr)
            return None
        
        # Return the output
        return result.stdout.strip()
    except FileNotFoundError:
        print("PowerShell is not available.")
        return None

command = "Get-Process | Select-Object Name, CPU"
powerShell_command = "Start-Process PowerShell -Verb RunAs -ArgumentList '-Command', '{}' ".format(command)
#run_powershell_command(powerShell_command)

output = run_powershell_command(powerShell_command)

if output:
    print(output)