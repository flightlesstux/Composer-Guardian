# Composer Guardian 🛡️

Ahoy there! Meet your friendly Composer Guardian, an awesome Python script that looks out for updates to your PHP packages in your `composer.json` file. Not only does this Python marvel fetch the latest version of each package, but it also sends a lovely notification to your Slack channel. Ain't that amazing?

## Features

-   💾 Reads your `composer.json` file and checks for package updates
-   📦 Fetches the latest stable versions of your PHP packages from Packagist
-   🤖 Automatically skips packages with specified prefixes or package names
-   📤 Sends notifications to your Slack channel via webhook
-   😎 Works with both command-line arguments and environment variables
-   🎉 Fun and warm console outputs to brighten up your day

## Requirements

-   Python 3.6 or higher
-   `requests` library (`pip install requests`)

## Installation

1.  Clone this repository or download the script.
    
2.  Install the required libraries:
    

1.  `pip install -r requirements.txt` 
    
2.  Run the script, and watch the magic unfold!
    

## Usage

You can use Composer Guardian by running the following command:


`python composer_guardian.py --composer-file-path <composer-file-path> --slack-webhook-url <slack-webhook-url>` 

Or, you can use environment variables:

`export COMPOSER_FILE_PATH=<composer-file-path>
export SLACK_WEBHOOK_URL=<slack-webhook-url>
python composer_guardian.py` 

### Arguments and Environment Variables

-   `--composer-file-path` or `COMPOSER_FILE_PATH`: The path to your `composer.json` file (default: `composer.json`)
-   `--slack-webhook-url` or `SLACK_WEBHOOK_URL`: Your Slack webhook URL for sending notifications. If you are not providing Slack Webhook Url, The Composer Guardian will skip to send notification.

## Example Output

 ```
 _____                                             _____                     _ _             
/  __ \                                           |  __ \                   | (_)            
| /  \/ ___  _ __ ___  _ __   ___  ___  ___ _ __  | |  \/_   _  __ _ _ __ __| |_  __ _ _ __  
| |    / _ \| '_ ` _ \| '_ \ / _ \/ __|/ _ | '__| | | __| | | |/ _` | '__/ _` | |/ _` | '_ \ 
| \__/| (_) | | | | | | |_) | (_) \__ |  __| |    | |_\ | |_| | (_| | | | (_| | | (_| | | | |
 \____/\___/|_| |_| |_| .__/ \___/|___/\___|_|     \____/\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                      | |                                                                    
                      |_|

Composer Guardian found package updates!

Package Name                             Current version Latest version
---------------------------------------- --------------- --------------
guzzlehttp/guzzle                        6.5.5            7.4.1         
symfony/console                          5.3.0            5.4.2
aws/aws-sdk-php                          3.225.4          3.263.10
composer/semver                          3.2.9            3.3.2
doctrine/migrations                      3.4.*            3.6.0
elasticsearch/elasticsearch              7.17.*           v8.7.0
endroid/qr-code                          4.5.*            4.8.2
league/oauth2-facebook                   ^2.0             2.2.0
geoip2/geoip2                            ~2.0             v2.13.0
google/apiclient                         ^2.0             v2.13.2
google/cloud-bigquery                    ^1.5             v1.24.0
google/cloud-translate                   ^1.2             v1.13.1
gregwar/captcha                          1.1.*            v1.2.0
griffinledingham/php-apple-signin        ^1.1             1.1
guzzlehttp/guzzle                        7.4.*            7.5.0
jenssegers/agent                         ^2.6             v2.6.4
mobiledetect/mobiledetectlib             2.8.*            3.74.0
mpdf/mpdf                                ^8.1             v8.1.5
mustache/mustache                        v2.14.*          v2.14.2
nesbot/carbon                            2.57.*           2.66.0
patrickbussmann/oauth2-apple             0.2.6            0.2.10
php-amqplib/php-amqplib                  v3.2.0           v3.5.3
phpoffice/phpspreadsheet                 ^1.5             1.28.0
symfony/console                          5.*@stable       v6.2.8
symfony/event-dispatcher                 5.*@stable       v6.2.8
symfony/http-foundation                  5.*              v6.2.8
symfony/lock                             5.*@stable       v6.2.8
symfony/yaml                             5.*@stable       v6.2.7
symfony/service-contracts                2.5.*            v3.2.1
facebook/php-business-sdk                16.0.*           16.0.2
mongodb/mongodb                          1.15.*           1.15.0
psr/event-dispatcher                     1.0.0            1.0.0
```


## Docker Image Usage (Prebuilt Image)

For your convenience, I've published a prebuilt Docker image on Docker Hub. You can use the `flightlesstux/composer-guardian` image to run Composer Guardian without building the image yourself. Follow these simple steps to get started:

1.  Pull the prebuilt Docker image from Docker Hub:
   
-   `docker pull flightlesstux/composer-guardian` 
    
-   Run the Docker container with the required arguments or environment variables:
```
     docker run --rm \
        -v /path/to/your/composer.json:/app/composer.json \
        -e COMPOSER_FILE_PATH=/app/composer.json \
        -e SLACK_WEBHOOK_URL=<slack-webhook-url> \
        flightlesstux/composer-guardian
```
2. Replace `/path/to/your/composer.json` with the local path to your `composer.json` file and `<slack-webhook-url>` with your Slack webhook URL.
    

### Docker Compose (Prebuilt Image)

You can also use Docker Compose to run Composer Guardian with the prebuilt Docker image. Here's an example `docker-compose-prebuilt.yml` file:

```
    version: '3.8'
    services:
      composer-guardian:
        image: flightlesstux/composer-guardian
        volumes:
          - /path/to/your/composer.json:/app/composer.json
        environment:
          - COMPOSER_FILE_PATH=/app/composer.json
          - SLACK_WEBHOOK_URL=<slack-webhook-url>
```

Replace `/path/to/your/composer.json` with the local path to your `composer.json` file and `<slack-webhook-url>` with your Slack webhook URL.

To run Composer Guardian using Docker Compose with the prebuilt image, execute the following command in the same directory as your `docker-compose-prebuilt.yml` file: `docker-compose -f docker-compose-prebuilt.yml up` 

Now, you can effortlessly keep your PHP packages up-to-date with the Composer Guardian at your side, all from the comfort of a prebuilt Docker container! 🚀🎵🛡️


## Docker Image Usage

For those of you who prefer to run Composer Guardian in a Docker container, I've got you covered! Follow these simple steps to get started:

1.  Clone this repository or download the script.
    
2.  In the project directory, build the Docker image:
   
-   `docker build -t composer-guardian .` 
    
-   Run the Docker container with the required arguments or environment variables:
  

1.
```
docker run --rm \
        -v /path/to/your/composer.json:/app/composer.json \
        -e COMPOSER_FILE_PATH=/app/composer.json \
        -e SLACK_WEBHOOK_URL=<slack-webhook-url> \
        composer-guardian
``` 
    
Replace `/path/to/your/composer.json` with the local path to your `composer.json` file and `<slack-webhook-url>` with your Slack webhook URL.
    

### Docker Compose

You can also use Docker Compose to run Composer Guardian. Here's an example `docker-compose.yml` file:

```
version: '3.8'
services:
  composer-guardian:
    build: .
    volumes:
      - /path/to/your/composer.json:/app/composer.json
    environment:
      - COMPOSER_FILE_PATH=/app/composer.json
      - SLACK_WEBHOOK_URL=<slack-webhook-url>
```

Replace `/path/to/your/composer.json` with the local path to your `composer.json` file and `<slack-webhook-url>` with your Slack webhook URL.

To run Composer Guardian using Docker Compose, simply execute the following command in the same directory as your `docker-compose.yml` file:

`docker-compose up` 

And there you have it! Composer Guardian is now ready to serve you from within a Docker container. Enjoy your smooth sailing with your trusty Guardian aboard! 🐳🎵🛡️

## Contributing

Feel free to open issues or submit pull requests. I'd love to hear your ideas, jokes, or any feedback you may have!

## License

Composer Guardian is released under the MIT License. Check the [LICENSE] file for more details.

## May the Guardian be with you! 🛡️
