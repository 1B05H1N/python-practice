import subprocess
import json
import pkg_resources

def list_installed_packages():
    # List currently installed packages using pkg_resources
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return installed_packages

def check_package_updates():
    # Get a list of outdated packages using pip list --outdated
    result = subprocess.run(['pip', 'list', '--outdated', '--format=json'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to fetch outdated packages.")
        return None

    # Parse the JSON output
    try:
        outdated_packages = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Failed to decode JSON output from pip.")
        return None

    return outdated_packages

def upgrade_packages(packages):
    for pkg in packages:
        response = input(f"Do you want to upgrade {pkg['name']} from {pkg['version']} to {pkg['latest_version']}? (y/n): ")
        if response.lower() == 'y':
            subprocess.run(['pip', 'install', '--upgrade', pkg['name']], check=True)
            print(f"{pkg['name']} has been upgraded.")
        else:
            print(f"Skipped upgrading {pkg['name']}.")

def main():
    # Get all installed packages
    installed_packages = list_installed_packages()
    print("Installed Packages:")
    for package, version in installed_packages.items():
        print(f"{package}=={version}")

    # Check for updates
    outdated_packages = check_package_updates()
    if outdated_packages:
        print("\nPackages that can be upgraded:")
        for pkg in outdated_packages:
            print(f"{pkg['name']} (Current: {pkg['version']} Latest: {pkg['latest_version']})")

        upgrade_packages(outdated_packages)
    else:
        print("\nAll packages are up to date or failed to check updates.")

if __name__ == "__main__":
    main()
