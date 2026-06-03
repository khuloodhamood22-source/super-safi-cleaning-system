# Super Safi

Super Safi is a cleaning services marketplace platform that connects customers with verified cleaning service providers.

The platform allows customers to browse available cleaning services, submit booking requests, and communicate with the company through a dedicated contact and support system.

Service providers can apply to join the platform by submitting their professional information and required documents. All applications are reviewed by the administration before approval.

The administration manages service providers, reviews provider applications, monitors bookings, handles customer inquiries, and maintains the overall quality of the platform.

The system is designed to provide a secure, reliable, and efficient environment for both customers and service providers while ensuring service quality through provider verification and administrative approval workflows.




# System Architecture

Super Safi follows a multi-layer architecture that combines a web interface, REST API services, administrative management tools, and provider management workflows within a single Django-based platform.

The system is designed around three primary user roles:

* Customers
* Service Providers
* Administrators

Customers interact with the platform through the website to browse services, submit booking requests, and contact support.

Service providers can apply to join the platform by submitting professional information and required verification documents. Applications are reviewed by administrators before providers become active on the platform.

Administrators manage service providers, provider services, provider availability schedules, bookings, reviews, and customer inquiries through the Django Administration Panel.

The backend is implemented using Django and Django REST Framework. RESTful APIs expose service, provider, and booking resources for integration and future extensibility.

Redis is integrated as an additional infrastructure component and the application is containerized using Docker Compose to simplify deployment and development workflows.

Architecture Overview

Client Browser
│
▼
Frontend Website
│
▼
Django Application
│
┌────┼────┐
│    │    │
▼    ▼    ▼
Admin API Business Logic
│
▼
Database
│
▼
Redis


# User Roles and Responsibilities

## Customer

Customers are the primary users of the platform. They can browse available cleaning services, submit booking requests, provide contact information, and communicate with the company through the Contact & Support page.

The booking process allows customers to select a cleaning service, specify the preferred booking date and time, provide an address, and submit a service request. The system automatically calculates booking details and creates a pending booking record for administrative review.

Customers may also submit feedback and reviews after completed services.

---

## Service Provider

Service providers are professionals or companies that offer cleaning services through the platform.

To join the platform, providers submit an application containing professional information and verification documents, including business registration and licensing information.

Provider applications are reviewed by administrators before approval.

Each approved provider can:

* Offer one or more cleaning services.
* Define service pricing.
* Specify service duration.
* Configure weekly availability schedules.
* Receive bookings through the platform.

The system supports provider verification, licensing records, and approval workflows to ensure service quality and reliability.

---

## Administrator

Administrators manage all operational aspects of the platform through the Django Administration Panel.

Administrative responsibilities include:

* Managing cleaning services.
* Reviewing and approving provider applications.
* Managing provider availability schedules.
* Monitoring customer bookings.
* Reviewing customer feedback and ratings.
* Handling customer inquiries submitted through the Contact & Support page.
* Monitoring platform activity and maintaining service quality.

The administrator acts as the central authority responsible for platform governance and provider verification.


# Core Features

## Service Management

The platform maintains a centralized catalog of cleaning services. Each service contains descriptive information, images, and activation status controls managed through the administration panel.

Examples of supported services include:

* Home Cleaning
* Apartment Cleaning
* Office Cleaning
* Post-Event Cleaning

Only active services are exposed through the public website and REST API.

---

## Provider Application and Verification

Service providers can apply to join the platform through the provider registration system.

Applicants submit professional information and supporting verification documents, including licensing and business registration details.

Each application is initially assigned a **Pending** status and is reviewed by the administration team before approval.

Provider status values include:

* Pending
* Approved
* Rejected

This verification workflow helps maintain service quality and platform trustworthiness.

---

## Provider Service Management

Approved providers may offer multiple services through the platform.

Each provider service record contains:

* Associated provider
* Service type
* Service price
* Estimated service duration
* Activation status

This design allows different providers to offer the same service with independent pricing and scheduling configurations.

---

## Provider Availability Scheduling

The platform supports weekly availability management.

Providers can define:

* Available days
* Start time
* End time
* Availability status

Availability records allow the platform to manage scheduling and future booking allocation logic.

---

## Customer Booking System

Customers can submit booking requests directly through the platform without requiring account registration.

The booking process collects:

* Customer name
* Customer phone number
* Selected service
* Booking date
* Booking time
* Service address

The system automatically assigns an active provider service and calculates booking duration based on the selected service configuration.

---

## Automated Commission Management

The platform automatically calculates marketplace commission for every booking.

Current commission rate:

* Platform Commission: 10%
* Provider Earnings: 90%

Commission values are automatically generated during booking creation to ensure consistent financial calculations.

---

## Customer Reviews and Ratings

After service completion, customers can submit reviews and ratings for service providers.

Review records contain:

* Customer reference
* Provider reference
* Rating score
* Written feedback
* Review creation date

The review system supports quality monitoring and provider performance evaluation.

---

## Contact and Support System

Customers can communicate directly with the platform using the Contact & Support page.

Submitted inquiries are stored within the system and can be reviewed through the administration panel.

The contact system supports:

* General inquiries
* Customer support requests
* Feedback submissions
* Partnership inquiries

This feature provides a dedicated communication channel between customers and platform administrators.



# Database Design

The database design follows a relational structure that models the interactions between customers, service providers, services, bookings, reviews, and administrative processes.

The system is designed to ensure scalability, maintainability, and data integrity through clearly defined relationships between entities.

## Service

The Service entity represents the cleaning services offered through the platform.

Key attributes include:

* Service Name
* Description
* Service Image
* Active Status

A single service can be offered by multiple service providers.

---

## ServiceProvider

The ServiceProvider entity represents cleaning professionals or companies registered on the platform.

Key attributes include:

* Full Name
* Phone Number
* City
* Profile Image
* Description
* Experience Years
* Verification Information
* Business Registration Information
* Licensing Information
* Approval Status

Each provider is linked to a unique system user account.

---

## ProviderService

The ProviderService entity acts as a bridge between providers and services.

This entity allows multiple providers to offer the same service while maintaining independent pricing and duration configurations.

Key attributes include:

* Provider Reference
* Service Reference
* Service Price
* Estimated Duration
* Active Status

Relationship:

* One Provider → Many Provider Services
* One Service → Many Provider Services

---

## ProviderAvailability

The ProviderAvailability entity manages provider scheduling information.

Key attributes include:

* Day of Week
* Start Time
* End Time
* Availability Status

Relationship:

* One Provider → Many Availability Records

This design enables flexible scheduling and future booking optimization.

---

## Booking

The Booking entity represents customer service requests.

Key attributes include:

* Customer Information
* Selected Provider Service
* Booking Date
* Start Time
* End Time
* Address
* Notes
* Booking Status
* Total Price
* Commission Amount
* Provider Earnings

Relationship:

* One Provider Service → Many Bookings

The booking model also contains automated commission calculations to support marketplace revenue management.

---

## Review

The Review entity stores customer feedback.

Key attributes include:

* Booking Reference
* Customer Reference
* Provider Reference
* Rating
* Comment
* Creation Date

Relationship:

* One Booking → One Review

This relationship ensures that reviews are linked to completed service experiences.

---

## ContactMessage

The ContactMessage entity stores customer inquiries and support requests.

Key attributes include:

* Name
* Email
* Phone Number
* Subject
* Message Content
* Submission Date

Contact records are managed through the administration panel and provide a communication channel between customers and platform administrators.


# Entity Relationships

The primary entity relationships within the platform are summarized below:

User
│
└── ServiceProvider

Service
│
└── ProviderService

ServiceProvider
│
├── ProviderService
├── ProviderAvailability
└── Review

ProviderService
│
└── Booking

Booking
│
└── Review

ContactMessage
(Independent Support Module)

This relational structure separates operational, scheduling, financial, and customer-support concerns while maintaining clear ownership and responsibility across system components.


# Authentication and Authorization

The platform implements token-based authentication using JSON Web Tokens (JWT) through Django REST Framework Simple JWT.

Authentication endpoints:

* `/api/token/`
* `/api/token/refresh/`

JWT authentication enables secure access to protected API resources and provides a scalable foundation for future mobile or third-party integrations.

The platform currently supports:

* User authentication
* Access token generation
* Refresh token generation
* Secure API communication

Administrative functionality is protected through the Django Administration Panel.

---

## Authorization Strategy

The platform separates responsibilities across three primary user roles:

### Customer

Customers interact with public-facing functionality including:

* Browsing services
* Submitting booking requests
* Sending support inquiries
* Submitting reviews

### Service Provider

Approved providers can:

* Offer services
* Manage availability schedules
* Receive customer bookings
* Maintain professional profiles

### Administrator

Administrators possess full platform privileges and are responsible for:

* Provider approval
* Service management
* Booking oversight
* Customer support management
* Review moderation
* Platform maintenance

This role-based separation improves security and operational control.


# REST API Documentation

The platform exposes RESTful API endpoints using Django REST Framework.

## Services API

Endpoint:

```text
GET /api/services/
```

Purpose:

Returns all active cleaning services available on the platform.

---

## Service Providers API

Endpoint:

```text
GET /api/providers/
```

Purpose:

Returns approved service providers available for customer bookings.

---

## Provider Services API

Endpoint:

```text
GET /api/provider-services/
```

Purpose:

Returns provider-specific service offerings including pricing and duration information.

---

## Bookings API

Endpoint:

```text
GET /api/bookings/
```

Purpose:

Returns booking records stored in the system.

---

## Guest Booking API

Endpoint:

```text
POST /api/guest-booking/
```

Purpose:

Allows customers to create booking requests without account registration.

Required information includes:

* Service identifier
* Customer name
* Customer phone
* Booking date
* Booking time
* Address

The system automatically:

* Locates an active provider
* Calculates service duration
* Calculates booking end time
* Creates a booking record
* Assigns pending status

Response includes:

* Booking identifier
* Booking status
* Success message

---

## JWT Authentication API

### Obtain Access Token

```text
POST /api/token/
```

### Refresh Token

```text
POST /api/token/refresh/
```

These endpoints support secure API authentication and session management.


# Booking Workflow

The booking workflow is designed to simplify service requests while minimizing customer friction.

## Step 1 – Service Selection

The customer browses available cleaning services through the website.

Available services may include:

* Home Cleaning
* Apartment Cleaning
* Office Cleaning
* Post-Event Cleaning

---

## Step 2 – Booking Submission

The customer submits:

* Name
* Phone Number
* Preferred Date
* Preferred Time
* Service Address

The platform allows guest bookings without requiring account registration.

---

## Step 3 – Provider Assignment

The system identifies an active provider capable of delivering the selected service.

Provider assignment is performed automatically using provider-service relationships.

---

## Step 4 – Time Calculation

The platform automatically calculates:

* Start Time
* End Time

using the configured service duration.

---

## Step 5 – Booking Creation

A booking record is generated with:

* Customer information
* Service information
* Provider information
* Pricing information

Initial booking status:

```text
Pending
```

---

## Step 6 – Administrative Processing

Administrators can review, monitor, and manage booking requests through the Django Administration Panel.

Booking statuses include:

* Pending
* Accepted
* Rejected
* Completed
* Cancelled

This workflow provides a structured lifecycle for service delivery management.



# Provider Application Workflow

The platform supports an online provider onboarding process designed to verify service quality and ensure marketplace reliability.

## Step 1 – Application Submission

A prospective service provider submits an application through the platform.

The application includes:

* Full Name
* Phone Number
* City
* Professional Description
* Years of Experience
* Professional License Number
* Commercial Register Number
* Tax Number
* Supporting Documents

Submitted documents may include:

* Professional License File
* Commercial Registration File

---

## Step 2 – Application Registration

Upon submission, a Provider Application record is created and stored in the system.

The application includes:

* Full Name
* Phone Number
* City
* Professional Description
* Years of Experience
* Professional License Number
* Commercial Register Number
* Tax Number
* Supporting Documents

Uploaded documents may include:

* Professional License File
* Commercial Registration File
* Profile Image

At this stage, the application is stored in the Provider Applications module and is available for administrative review.

The applicant is informed that the application will be reviewed and that a response will be provided within 72 hours.

---

## Step 3 – Administrative Review Queue

Submitted applications enter an administrative review queue.

Administrators can access all submitted applications through the Django Administration Panel, where they can review:

* Applicant information
* Professional qualifications
* Experience details
* Uploaded verification documents

The review process helps ensure:

* Provider legitimacy
* Service quality
* Regulatory compliance
* Platform trustworthiness

---

## Step 4 – Administrative Communication

After reviewing the submitted application and supporting documents, administrators contact the applicant directly using the provided phone number.

Communication may be performed through:

* Phone Call
* SMS
* WhatsApp

Applicants are notified regarding the outcome of their application after the review process is completed.

---

## Step 5 – Provider Onboarding

Applicants who satisfy platform requirements may proceed to the provider onboarding process.

Administrators can then create and manage provider records, configure services, define pricing, and set provider availability schedules before making provider services available within the platform.

This workflow ensures that all providers are reviewed before participating in marketplace operations.

# Provider Application Review Workflow

The provider application process is designed to maintain service quality and platform reliability.

## Application Evaluation

Administrators evaluate:

* Personal information
* Professional qualifications
* Service experience
* Licensing documentation
* Commercial registration records
* Supporting verification files

---

## Administrative Decision

Based on the submitted information and documents, administrators determine whether the applicant satisfies platform requirements.

Applicants are then contacted directly using the phone number provided during application submission.

---

## Quality Assurance

The review process helps ensure:

* Provider authenticity
* Service reliability
* Professional standards compliance
* Customer trust and platform quality

This workflow provides a controlled onboarding process while allowing administrators to verify applicants before introducing them to platform operations.






# Contact and Support Workflow

The Contact & Support module provides a communication channel between customers and platform administrators.

## Step 1 – Inquiry Submission

Customers submit:

* Name
* Email Address
* Subject
* Message Content

through the Contact & Support page.

---

## Step 2 – Message Storage

Submitted inquiries are stored as ContactMessage records within the database.

Each message contains:

* Customer information
* Subject
* Message content
* Submission timestamp

---

## Step 3 – Administrative Review

Administrators can review customer inquiries through the Django Administration Panel.

---

## Supported Inquiry Types

The Contact & Support system supports:

* General inquiries
* Customer assistance requests
* Feedback submissions
* Partnership opportunities
* Business communication

This workflow ensures a centralized support channel for all customer communication.

# Commission Calculation Logic

The platform follows a marketplace revenue model based on automated commission calculations.

## Commission Policy

Current commission rate:

```text
10%
```

---

## Calculation Formula

Platform Commission:

```text
Commission = Total Price × 10%
```

Provider Earnings:

```text
Provider Earnings = Total Price − Commission
```

---

## Automated Processing

Commission values are automatically calculated whenever a booking is created.

This calculation is performed within the booking model to ensure consistency and eliminate manual processing errors.

---

## Example

Booking Total:

```text
100.00
```

Platform Commission:

```text
10.00
```

Provider Earnings:

```text
90.00
```

This approach provides transparent revenue sharing between the platform and service providers.

# Testing Strategy

The project includes automated tests implemented using Django's testing framework.

## Model Testing

The following business rules are tested:

### Service Creation

Verifies that service records are created successfully and active status values are assigned correctly.

### Booking Commission Calculation

Verifies automatic commission generation and provider earnings calculations.

---

## API Testing

### Services API Availability

Tests confirm that the Services API endpoint returns successful responses and exposes service data correctly.

---

## Testing Benefits

The testing layer helps ensure:

* Data integrity
* Business rule validation
* API reliability
* Reduced regression risk
* Improved maintainability

Automated testing contributes to long-term platform stability and development confidence.


# Docker Deployment

The platform is containerized using Docker and Docker Compose to simplify development, deployment, and environment consistency.

## Containers

### Web Container

Responsible for:

* Running the Django application
* Serving frontend pages
* Serving REST API endpoints
* Managing business logic

### Redis Container

Responsible for:

* Supporting Redis-based functionality
* Providing high-performance in-memory data storage
* Supporting future caching and background processing enhancements

---

## Docker Compose Configuration

The platform uses a multi-container architecture:

```text
Web Application
        │
        ▼
      Redis
```

Docker Compose manages service orchestration and container startup procedures.

---

## Benefits of Containerization

* Consistent development environments
* Simplified deployment
* Dependency isolation
* Improved maintainability
* Scalability readiness

The use of Docker ensures that the application behaves consistently across different operating systems and deployment environments.


# Redis Integration

Redis is integrated as an infrastructure component within the platform architecture.

Redis provides an in-memory data store that can support:

* Application caching
* Session storage
* Performance optimization
* Background task processing
* Future scalability improvements

The Redis service is deployed as a dedicated container and operates independently from the Django application container.

This separation improves system modularity and allows future expansion without major architectural changes.


# Project Structure

The project follows a modular Django architecture.

```text
super-safi-main
│
├── backend
│   │
│   ├── config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── marketplace
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       ├── admin.py
│       ├── tests.py
│       └── migrations
│
├── templates
├── static
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Architectural Separation

The project separates responsibilities into:

* Configuration Layer
* Business Logic Layer
* API Layer
* Data Layer
* Presentation Layer

This structure improves maintainability and long-term extensibility.


# Installation and Setup

## Prerequisites

Before running the project, ensure the following software is installed:

* Python 3.12+
* Docker
* Docker Compose
* Git

---

## Clone Repository

```bash
git clone <repository-url>
cd super-safi-main
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file and configure the required environment variables:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## Database Migration

```bash
python backend/manage.py makemigrations
python backend/manage.py migrate
```

---

## Create Administrator Account

```bash
python backend/manage.py createsuperuser
```


# Running the Project

## Using Docker

Build and start containers:

```bash
docker compose build
docker compose up -d
```

Application URL:

```text
http://localhost:8000
```

Administration Panel:

```text
http://localhost:8000/admin
```

---

## Running Tests

Execute automated tests:

```bash
python backend/manage.py test
```

---

## API Access

Example endpoints:

```text
/api/services/
/api/providers/
/api/provider-services/
/api/bookings/
/api/guest-booking/
/api/token/
/api/token/refresh/
```

The API can be consumed by future web, mobile, or third-party applications.



# Future Enhancements

Several enhancements can be implemented in future versions of the platform:

## Customer Features

* Customer account management
* Booking history dashboard
* Booking cancellation requests
* Real-time booking tracking

---

## Provider Features

* Provider self-service dashboard
* Availability management interface
* Earnings analytics
* Booking acceptance and rejection controls

---

## Platform Features

* Online payment integration
* Automated provider matching
* Intelligent scheduling algorithms
* Real-time notifications
* Email and SMS integrations
* Multi-language support

---

## Technical Enhancements

* CI/CD pipelines
* Production deployment environment
* Automated backups
* Advanced caching strategies
* Monitoring and logging solutions

These enhancements would further improve scalability, user experience, and operational efficiency.


