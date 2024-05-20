# pi-guard-monitor.py

import logging
import sys

from core.threat_detection import ThreatDetection
from core.threat_prevention import ThreatPrevention
from core.threat_response import ThreatResponse

def main():
    # Initialize logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.handlers.RotatingFileHandler(
                'pi-guard-monitor.log',
                maxBytes=10485760,
                backupCount=5
            )
        ]
    )

    # Initialize threat detection
    threat_detection = ThreatDetection()

    # Initialize threat prevention
    threat_prevention = ThreatPrevention()

    # Initialize threat response
    threat_response = ThreatResponse()

    # Main loop
    while True:
        # Detect threats
        threats = threat_detection.detect_threats()

        # Prevent threats
        threat_prevention.prevent_threats(threats)

        # Respond to threats
        threat_response.respond_to_threats(threats)

if __name__ == '__main__':
    main()
