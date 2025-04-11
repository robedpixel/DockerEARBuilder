# Use the nginx official image
FROM nginx

ARG ELASTIC_VERSION
ENV ELASTIC_VERSION=${ELASTIC_VERSION:-8.17.0}

# Install packages
RUN apt-get update && apt-get install -y jq

# Create Artifact storage directory
RUN mkdir -p /opt/elastic-packages/downloads
ENV DOWNLOAD_BASE_DIR=/opt/elastic-packages/downloads

# Artifact Registry creation
COPY ./downloads /opt/elastic-packages/downloads

# Copy EAR NGINX Configuration
RUN chown -R nginx:nginx /opt/elastic-packages 
COPY nginx-ear.conf /etc/nginx/nginx.conf
COPY index.html /opt/elastic-packages/index.html

# Expose the EAR port
EXPOSE 9080