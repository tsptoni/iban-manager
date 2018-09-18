
# Update and apt-get basic packages
apt-get update && apt-get install -y postgresql-server-dev-${POSTGRES_VERSION}
apt-get install -y vim