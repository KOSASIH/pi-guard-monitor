# User Guide

The pi-guard-monitor system is a versatile and powerful tool for monitoring various sensors and triggering alerts based on customizable thresholds. This user guide provides step-by-step instructions for installing, configuring, and using the pi-guard-monitor system.

Table of Contents

- Installation
- Configuration
- Usage
- Troubleshooting
<a name="installation"></a>

1. Installation

To install the pi-guard-monitor system, follow these steps:

- Install Docker on your system.
- Clone the pi-guard-monitor repository:

```bash

1. git clone https://github.com//pi-guard-monitor.git
2. cd pi-guard-monitor
```

Build the Docker image:

```bash

1. docker build -t pi-guard-monitor .
```

Run the Docker container:

```bash

1. docker run -d -p 8000:8000 pi-guard-monitor
```
<a name="configuration"></a>

2. Configuration

The pi-guard-monitor system can be configured using environment variables. The following environment variables are available:

- PORT: The port that the pi-guard-monitor system listens on. Default: 8000.
- SENSOR_1_NAME: The name of Sensor 1.
- SENSOR_1_THRESHOLD: The threshold value for Sensor 1.
- SENSOR_1_INTERVAL: The interval (in seconds) for reading Sensor 1.
- SENSOR_2_NAME: The name of Sensor 2.
- SENSOR_2_THRESHOLD: The threshold value for Sensor 2.
- SENSOR_2_INTERVAL: The interval (in seconds) for reading Sensor 2.
- ALERT_EMAIL: The email address to send alert notifications to.
- ALERT_EMAIL_PASSWORD: The password for the email account.

To set environment variables when running the Docker container, use the -e flag:

```bash

1. docker run -d -p 8000:8000 -e PORT=8000 -e SENSOR_1_NAME="Temperature" -e SENSOR_1_THRESHOLD=25.0 -e 2. 2. 2
2. SENSOR_1_INTERVAL=60 -e SENSOR_2_NAME="Humidity" -e SENSOR_2_THRESHOLD=70.0 -e SENSOR_2_INTERVAL=60 -e 3. 3. 3. 3. 3. 3. ALERT_EMAIL="you@example.com" -e ALERT_EMAIL_PASSWORD="your-password" pi-guard-monitor
```
<a name="usage"></a>

3. Usage

Once the pi-guard-monitor system is installed and configured, you can access it using a web browser or an API client.

3.1. Web Interface
Visit http://localhost:8000 in your web browser to access the pi-guard-monitor system's web interface.

3.2. API
The pi-guard-monitor system provides a RESTful API for interacting with the system. Refer to the API Reference for more information.

<a name="troubleshooting"></a>

4. Troubleshooting

If you encounter any issues with the pi-guard-monitor system, refer to the following troubleshooting steps:

Check the Docker logs:

```bash

docker logs <container-id>
```

- Ensure that the required environment variables are set correctly.
- Verify that the sensors are connected and functioning properly.
- Check the network connection and firewall settings.
- If you still cannot resolve the issue, please consult the pi-guard-monitorsystem's documentation or contact the support 
  team for assistance.

This is just a sample user guide, and you should adjust it according to your system's specific requirements and features.[INSTALLATION INSTRUCTIONS FOR pi-guard-monitor
