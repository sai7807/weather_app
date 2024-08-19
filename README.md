# Weather App

This is a simple Weather App that fetches and displays weather data for various cities using the API Ninjas Weather API. The app provides real-time weather information such as temperature, humidity, cloud percentage, and wind speed.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Key](#api-key)
- [License](#license)

## Features

- Displays current weather data for a user-specified city.
- Shows additional weather information such as humidity, wind speed, and sunrise/sunset times.
- Responsive design using Bootstrap.
- Fetches weather data using Fetch API.

## Technologies Used

- HTML
- CSS (Bootstrap)
- JavaScript
- Weather API from API Ninjas

## Setup Instructions

### Prerequisites

- A web browser (Chrome, Firefox, etc.)
- Text editor (VS Code, Sublime, etc.)
- A valid API key from API Ninjas.

### Steps

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/weather-app.git
2. Navigate to the project directory:
cd weather-app

3. Replace the x-rapidapi-key in the script.js file with your own API key:
const options = {
  method: 'GET',
  Headers: {
    'x-rapidapi-key': 'your-api-key-here',
    'x-rapidapi-host': 'weather-by-api-ninjas.p.rapidapi.com'
  }
};

4. Open index.html in your browser to run the application:
  open index.html

License:
This project is licensed under the MIT License. See the LICENSE file for details.


### How to Use This `README.md` File

1. **Clone the Project**: Once added this file, users who clone this repository will have a clear understanding of how to set up and use this Weather App.
2. **Modify the URL**: Replace `https://github.com/your-username/weather-app.git` with the actual URL of your GitHub repository.
3. **Update API Key Section**: Ensure users know where and how to replace the API key with your own.

This `README.md` file will guide users through setting up and using your weather application, ensuring they have the necessary information to get started quickly.



