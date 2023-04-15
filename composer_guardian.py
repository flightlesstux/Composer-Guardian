import json
import requests
import re
import argparse
import os

def read_composer_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_latest_package_version(package_name, timeout=5):
    url = f'https://packagist.org/packages/{package_name}.json'
    response = None
    try:
        response = requests.get(url, timeout=timeout)

        if response.status_code == 200:
            data = response.json()

            version_pattern = re.compile(r'^v?\d+(\.\d+)*$')
            stable_versions = [
                version for version, details in data['package']['versions'].items()
                if version_pattern.match(version)
            ]

            if not stable_versions:
                return None

            latest_version = max(stable_versions, key=lambda v: tuple(map(int, (v.lstrip('v').split(".")))))
        else:
            return None
    except (json.JSONDecodeError, requests.exceptions.Timeout):
        print(f"Error: Unable to fetch data for package '{package_name}'. Skipping...")
        if isinstance(response, requests.Response) and response.status_code == 404:
            print(f"Error: Package '{package_name}' not found. Skipping...")
        elif isinstance(response, requests.Response) and response.elapsed.total_seconds() > timeout:
            print(f"Error: Timeout occurred while fetching data for package '{package_name}'. Skipping...")
        return None

    return latest_version

def get_updates(packages):
    package_updates = []
    skipped_prefixes = ['ext-']
    excluded_packages = ['php']

    for package, current_version in packages.items():
        if any(package.startswith(prefix) for prefix in skipped_prefixes):
            print(f"Skipping package '{package}'...")
            continue
        elif package in excluded_packages:
            print(f"Excluding package '{package}'...")
            continue

        latest_version = get_latest_package_version(package)
        if latest_version:
            package_updates.append((package, current_version, latest_version))
        else:
            print(f"Error: Unable to fetch data for package '{package}'. Skipping...")

    return package_updates

def main():
    print(r"""
 _____                                             _____                     _ _             
/  __ \                                           |  __ \                   | (_)            
| /  \/ ___  _ __ ___  _ __   ___  ___  ___ _ __  | |  \/_   _  __ _ _ __ __| |_  __ _ _ __  
| |    / _ \| '_ ` _ \| '_ \ / _ \/ __|/ _ | '__| | | __| | | |/ _` | '__/ _` | |/ _` | '_ \ 
| \__/| (_) | | | | | | |_) | (_) \__ |  __| |    | |_\ | |_| | (_| | | | (_| | | (_| | | | |
 \____/\___/|_| |_| |_| .__/ \___/|___/\___|_|     \____/\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                      | |                                                                    
                      |_|                                                                                
    """)

    parser = argparse.ArgumentParser(description='Check for updates to packages in a composer.json file.')
    parser.add_argument('--composer-file-path', type=str, default='composer.json', help='Path to the composer.json file')
    parser.add_argument('--slack-webhook-url', type=str, help='Slack webhook URL to send notifications to')
    args = parser.parse_args()

    composer_file = args.composer_file_path or os.environ.get('COMPOSER_FILE_PATH')

    if not os.path.exists(composer_file):
        print(f"Error: The composer.json file '{composer_file}' was not found. \nYou can use --composer-file-path /path/to/your/composer.json \nOr use export COMPOSER_FILE_PATH=/path/to/your/composer.json")
        exit(1)

    composer_data = read_composer_json(composer_file)
    packages = composer_data['require']

    updates = get_updates(packages)

    if len(updates) <= 0:
        print("\nNo package updates found.")
    else:
        print("\nComposer Guardian found package updates!\n")
        table_header = "{:<40} {:<16} {:<14}".format('Package Name', 'Current version', 'Latest version')
        table_divider = "{:<40} {:<16} {:<14}".format('-'*40, '-'*16, '-'*14)
        table_body = "\n".join("{:<40} {:<16} {:<14}".format(package, current_version, latest_version) for package, current_version, latest_version in updates)
        print(table_header)
        print(table_divider)
        print(table_body)

        slack_webhook_url = args.slack_webhook_url or os.environ.get('SLACK_WEBHOOK_URL')

        if slack_webhook_url:
            message = {
                'text': f"Composer Guardian found package updates:\n```{table_header}\n{table_divider}\n{table_body}```"
            }
            response = requests.post(slack_webhook_url, json=message)
            if response.status_code == 200:
                print("\n")
            else:
                print(f"\nError: Unable to send Slack webhook notification. Status code: {response.status_code}")
        else:
            print("\nSkipping Slack notification. Neither --slack-webhook-url argument nor SLACK_WEBHOOK_URL environment variable was provided.")

if __name__ == '__main__':
    main()
