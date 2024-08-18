# SIPS - Smarter Inventory and Procurement System

SIPS is a comprehensive Inventory and Procurement System developed using Django, IoT, and Machine Learning. This web application is designed to efficiently manage user inventory, providing valuable insights through metrics such as optimal order quantity, reorder level, and emergency stock.

## Features

### Inventory Module
- **Real-time RFID Scanning**: Utilizes a Raspberry Pi connected to an RC522 to continuously scan RFID tags representing stock quantities.
- **Dynamic Stock Updates**: Scanning triggers real-time updates to the database, adjusting stock levels accordingly.
- **Metric Generation**: Generates metrics such as optimal order quantity, reorder level, and emergency stock for informed decision-making.

### Procurement Module
- **Automated RFQ Generation**: When stock falls below the reorder level, the system automatically generates a Request for Quotation (RFQ).
- **Seamless Integration**: RFQs are seamlessly sent to the Procurement Module for streamlined procurement processes.

## Technology Stack

- **Backend**: Developed using Django framework.
- **IoT Integration**: Raspberry Pi connected to an RC522 for RFID scanning.
- **Machine Learning Model**: SARIMAX utilized for predictive analysis.
- **Frontend**:
  - Inventory Module: Built with htmx for a dynamic user interface.
  - Procurement Module: Developed using Next.js for a robust and responsive frontend.

## Why SIPS?

SIPS goes beyond traditional inventory management systems by incorporating IoT for real-time updates and Machine Learning for predictive analytics. The integration of htmx and Next.js ensures a smooth and efficient user experience.

## How to Contribute

We welcome contributions from the community to enhance and improve SIPS. If you have ideas, bug reports, or feature requests, please open an issue or submit a pull request.

Let's build a smarter future with SIPS!
