import os

service_name = os.environ.get("SERVICE_NAME")
service_version = os.environ.get("SERVICE_VERSION")

status = f"Deployment for service '{service_name}' is triggered with version {service_version}"
mr_link="https://github.com/terracd-automation/trigger-action"

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)

set_output("status", status)
set_output("merge_request_link", mr_link)