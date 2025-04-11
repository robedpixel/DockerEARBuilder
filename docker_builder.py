from pathlib import Path
import subprocess
from urllib.request import urlretrieve
download_server = "https://artifacts.elastic.co/downloads/"
download_list = ( "apm-server/apm-server-<version>-linux-x86_64.tar.gz",
 "apm-server/apm-server-<version>-linux-x86_64.tar.gz.sha512",
 "apm-server/apm-server-<version>-linux-x86_64.tar.gz.asc",
 "beats/auditbeat/auditbeat-<version>-linux-x86_64.tar.gz",
 "beats/auditbeat/auditbeat-<version>-linux-x86_64.tar.gz.sha512",
 "beats/auditbeat/auditbeat-<version>-linux-x86_64.tar.gz.asc",
 "beats/elastic-agent/elastic-agent-<version>-linux-x86_64.tar.gz",
 "beats/elastic-agent/elastic-agent-<version>-linux-x86_64.tar.gz.sha512",
 "beats/elastic-agent/elastic-agent-<version>-linux-x86_64.tar.gz.asc",
 "beats/filebeat/filebeat-<version>-linux-x86_64.tar.gz",
 "beats/filebeat/filebeat-<version>-linux-x86_64.tar.gz.sha512",
 "beats/filebeat/filebeat-<version>-linux-x86_64.tar.gz.asc",
 "beats/heartbeat/heartbeat-<version>-linux-x86_64.tar.gz",
 "beats/heartbeat/heartbeat-<version>-linux-x86_64.tar.gz.sha512",
 "beats/heartbeat/heartbeat-<version>-linux-x86_64.tar.gz.asc",
 "beats/metricbeat/metricbeat-<version>-linux-x86_64.tar.gz",
 "beats/metricbeat/metricbeat-<version>-linux-x86_64.tar.gz.sha512",
 "beats/metricbeat/metricbeat-<version>-linux-x86_64.tar.gz.asc",
 "beats/osquerybeat/osquerybeat-<version>-linux-x86_64.tar.gz",
 "beats/osquerybeat/osquerybeat-<version>-linux-x86_64.tar.gz.sha512",
 "beats/osquerybeat/osquerybeat-<version>-linux-x86_64.tar.gz.asc",
 "beats/packetbeat/packetbeat-<version>-linux-x86_64.tar.gz",
 "beats/packetbeat/packetbeat-<version>-linux-x86_64.tar.gz.sha512",
 "beats/packetbeat/packetbeat-<version>-linux-x86_64.tar.gz.asc",
 "cloudbeat/cloudbeat-<version>-linux-x86_64.tar.gz",
 "cloudbeat/cloudbeat-<version>-linux-x86_64.tar.gz.sha512",
 "cloudbeat/cloudbeat-<version>-linux-x86_64.tar.gz.asc",
 "endpoint-dev/endpoint-security-<version>-linux-x86_64.tar.gz",
 "endpoint-dev/endpoint-security-<version>-linux-x86_64.tar.gz.sha512",
 "endpoint-dev/endpoint-security-<version>-linux-x86_64.tar.gz.asc",
 "fleet-server/fleet-server-<version>-linux-x86_64.tar.gz",
 "fleet-server/fleet-server-<version>-linux-x86_64.tar.gz.sha512",
 "fleet-server/fleet-server-<version>-linux-x86_64.tar.gz.asc",
 "prodfiler/pf-host-agent-<version>-linux-x86_64.tar.gz",
 "prodfiler/pf-host-agent-<version>-linux-x86_64.tar.gz.sha512",
 "prodfiler/pf-host-agent-<version>-linux-x86_64.tar.gz.asc",
 "prodfiler/pf-elastic-collector-<version>-linux-x86_64.tar.gz",
 "prodfiler/pf-elastic-collector-<version>-linux-x86_64.tar.gz.sha512",
 "prodfiler/pf-elastic-collector-<version>-linux-x86_64.tar.gz.asc",
 "prodfiler/pf-elastic-symbolizer-<version>-linux-x86_64.tar.gz",
 "prodfiler/pf-elastic-symbolizer-<version>-linux-x86_64.tar.gz.sha512",
 "prodfiler/pf-elastic-symbolizer-<version>-linux-x86_64.tar.gz.asc")
def main():
    print("Starting Elastic Artifact Registry docker image builder")
    Path("docker/downloads").mkdir(parents=True, exist_ok=True)
    elk_version = input("Enter ELK version to download:")
    for artifact in download_list:
        resolved_endpoint = artifact.replace("<version>",elk_version)
        split_list= resolved_endpoint.split("/")
        file_name = split_list[len(split_list)-1]
        download_url = download_server+resolved_endpoint
        destination_url =  "docker/downloads/"+resolved_endpoint
        download_folder = "docker/downloads/" + resolved_endpoint.removesuffix("/" + file_name)
        Path(download_folder).mkdir(parents=True, exist_ok=True)
        destination_file = Path(destination_url)
        if not destination_file.is_file():
            print("Downloading: "+download_url)
            urlretrieve(download_url, destination_url)
        else:
            print(file_name+" exists! skipping!")
    print("Finished downloading artifacts")
    print("Please go into the docker folder and use podman-compose or docker-compose to build the ear image")


if __name__ == "__main__":
    main()