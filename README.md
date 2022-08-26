# bamboo-cli
Bamboo CLI client for controlling a remote Atlassian bamboo server.

## Configuration

Configuration is done using environment variables (or cli arguments). Please set following env variables:
 - BAMBOO_SERVER (URL where your Bamboo instance is running)
 - BAMBOO_USER (username)
 - BAMBOO_PASSWORD (password)

e.g. on Linux run

```
export BAMBOO_SERVER=https://your-bamboo-instance.com && export BAMBOO_USER=your_username && export BAMBOO_PASSWORD=*******
```
## Run locally

```
pip install -r requirements.txt

python3 src/main.py --help
```

## Build package with setuptools

```
./build.sh

# install package locally
pip install -e .

#run the app
bcli --help
```

