# API Reference

The pi-guard-monitor system provides a RESTful API for interacting with the system. This API reference documents the available endpoints, request and response formats, and any other relevant details.

# Endpoints

1. GET /status

Returns the current status of the pi-guard-monitor system.
Response:
200 OK: System is online and functioning correctly.
500 Internal Server Error: System is experiencing issues.
Example Response:

```json
1.
2. {
3.  "status": "online",
4.  "version": "1.0.0"
5. }

```

2. GET /sensors
Returns a list of available sensors and their current readings.
Response:
200 OK: List of sensors and their readings.
404 Not Found: No sensors available.
Example Response:

```
1. [
2.  {
3.    "id": 1,
4.    "name": "Temperature Sensor",
5.    "reading": 22.5,
6.    "unit": "°C"
7.  },
8.  {
9.   "id": 2,
10.    "name": "Humidity Sensor",
11.    "reading": 60.2,
12.    "unit": "%"
13. }
14. ]

```

3. . GET /sensors/:id

Returns the current reading for a specific sensor.
Parameters:
id: The ID of the sensor to retrieve.
Response:
200 OK: Sensor reading.
404 Not Found: Sensor not found.
Example Response:

```json
1. 
2. {
3.  "id": 1,
4.  "name": "Temperature Sensor",
5.  "reading": 22.5,
6.  "unit": "°C"
7. }

```

4. POST /alerts

Creates a new alert for the pi-guard-monitor system.
Request Body:
sensor_id: The ID of the sensor that triggered the alert.
threshold: The threshold value that triggered the alert.
message: A brief message describing the alert.
Response:
201 Created: Alert created successfully.
400 Bad Request: Invalid request data.
Example Request Body:

5. Example Request Body:

```json
1. 
2. {
3.  "sensor_id": 1,
4.  "threshold": 25.0,
5.  "message": "Temperature exceeded 25°C"
6. }
```

5. GET /alerts
Returns a list of all alerts triggered by the pi-guard-monitor system.
Response:
200 OK: List of alerts.
404 Not Found: No alerts available.
Example Response:

```json
1.
2. [
3.  {
4.   "id": 1,
5.   "sensor_id": 1,
6.    "threshold": 25.0,
7.    "message": "Temperature exceeded 25°C",
8.    "timestamp": "2023-02-20T14:30:00Z"
9.  },
10.  {
11.   "id": 2,
12.    "sensor_id": 2,
13.   "threshold": 70.0,
14.    "message": "Humidity exceeded 70%",
15.    "timestamp": "2023-02-20T15:00:00Z"
16.  }
17. ]
```

# Error Handling

The pi-guard-monitor system uses standard HTTP status codes to indicate errors. The following error codes are used:

400 Bad Request: Invalid request data or malformed request.
404 Not Found: Resource not found.
500 Internal Server Error: System error or unexpected condition.
Security
The pi-guard-monitor system uses HTTPS encryption to secure all API requests. API keys or authentication tokens may be required for certain endpoints; please refer to the system's documentation for more information.

This is just a sample API reference, and you should adjust it according to your system's specific requirements and endpoints.
