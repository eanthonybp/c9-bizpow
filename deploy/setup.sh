#!/usr/bin/env bash

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/eanthonybp/c9-bizpow.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
apt-get update
apt-get install -y python3-dev sqlite python-pip supervisor nginx git

# Upgrade pip to the latest version.
pip install --upgrade pip
pip install virtualenv

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/bizpow-alpha

mkdir -p $VIRTUALENV_BASE_PATH
virtualenv --python=python3 $VIRTUALENV_BASE_PATH/bizpow-alpha

source $VIRTUALENV_BASE_PATH/bizpow-alpha/bin/activate
pip install -r $PROJECT_BASE_PATH/bizpow-alpha/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/bizpow-alpha/bizpow-alpha

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/bizpow-alpha/deploy/supervisor.conf /etc/supervisor/conf.d/supervisor.conf
supervisorctl reread
supervisorctl update
supervisorctl restart bizpow-alpha

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/bizpow-alpha/deploy/nginx_config.conf /etc/nginx/sites-available/profiles_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/bizpow-alpha.conf /etc/nginx/sites-enabled/bizpow-alpha.conf
systemctl restart nginx.service

echo "DONE! :)"