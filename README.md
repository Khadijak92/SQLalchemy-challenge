# Climate Data Analysis and Flask API

This project provides a detailed climate analysis and data exploration of a climate database using Python, SQLAlchemy, Pandas, and Matplotlib. Additionally, it implements a Flask API based on the developed queries to provide access to the analyzed data.

## Overview
In this project, we analyza and explore climate data stored in a SQLite database. THe analysis involves performing queries to ectract relevant information about precipitation and station data. Additionally, we visualize the data using Matplolib to gain insights into the climate patterns.
A Flask API is designes to provide access to the analyzed data. The API offers various routes to retrieve precipitation, station and temperature oberservation data in JSON format.

## Getting Started
To run the project locally, follow these steps:

- Clone the repository to your local machine.
- Ensure you have Python and the required dependencies installed (numpy, pandas, matplotlib, flask, sqlalchemy).
- Navigate to the project directory.
- Run the Flask application using python app.py.
- Access the API routes using a web browser or an API client.


## Flask API
The Flask API provides access to the analyzed climate data through various routes.

## Available Routes
- /: Homepage. Lists all available routes.
- /api/v1.0/precipitation: Returns the last 12 months of precipitation data in JSON format.
- /api/v1.0/stations: Returns a list of stations from the dataset in JSON format.
- /api/v1.0/tobs: Returns temperature observations for the previous year from the most-active station in JSON format.
- /api/v1.0/<start> and /api/v1.0/<start>/<end>: Returns minimum, average, and maximum temperatures for the specified date range in JSON format.

