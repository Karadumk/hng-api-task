# Simple REST API

A lightweight REST API that returns user information including email address, current UTC datetime, and GitHub repository URL.

## Description

This API is built with Flask and provides a single endpoint that returns:
- Your registered email address
- Current datetime in ISO 8601 format
- GitHub URL of the project's codebase

Check out [HNG Python Developers](https://hng.tech/hire/python-developers)

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo
cd your-repo
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install flask flask-cors
```

4. Run the application
```bash
python main.py
```

The server will start on `http://localhost:5000`

## API Documentation

### Endpoint Information

- **URL**: `/`
- **Method**: `GET`
- **Authentication**: None required

### Response example

```json
{
    "email": "Kgkpt2018@gmail.com",
    "current_datetime": "2024-02-03T12:34:56.789123Z",
    "github_url": "https://github.com/Karadumk/hng-api-task"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| email | string | The registered email address |
| current_datetime | string | Current UTC datetime in ISO 8601 format |
| github_url | string | GitHub repository URL |

### Example Usage

#### Using cURL
```bash
curl http://localhost:5000
```

## Error Handling

The API returns standard HTTP status codes:
- 200: Successful request
- 500: Server error

## Deployment

The application is configured to run on host "0.0.0.0" making it suitable for deployment on cloud platforms. The default port is 5000.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
