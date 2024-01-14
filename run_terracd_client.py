import os

service_name = os.environ.get("SERVICE_NAME")
service_version = os.environ.get("SERVICE_VERSION")

status = f"Deployment for service '{service_name}' is triggered with version {service_version}"
mr_link="https://github.com/terracd-automation/trigger-action"
print(f"::set-output status={status}")
print(f"::set-output merge_request_link={mr_link}")