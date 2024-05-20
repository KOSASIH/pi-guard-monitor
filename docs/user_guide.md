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

Run the Docker container:

