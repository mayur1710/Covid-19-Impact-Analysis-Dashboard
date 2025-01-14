
# COVID-19 Dashboard

A real-time dashboard to visualize COVID-19 statistics, commodities usage (Mask, Sanitizer, Oxygen), and regional zone data. This project uses Plotly, Dash, and Bootstrap to create an interactive web application displaying pandemic data across states.

## Project Overview

This web application provides insights into the COVID-19 situation, displaying total cases, active cases, recovered cases, and deaths for each state. Additionally, users can view graphs for different commodities such as masks, sanitizers, and oxygen. The dashboard also includes a pie chart to visualize the distribution of different COVID-19 zones (Red, Blue, Green, Orange).

## Features
- Total, Active, Recovered, and Deceased COVID-19 case counts.
- Line and Bar charts for COVID-19 commodity data (Mask, Sanitizer, Oxygen).
- Pie chart to display regional distribution (Red Zone, Blue Zone, Green Zone, Orange Zone).
- Bootstrap-based responsive layout.

## Technologies Used
- **Python**: Programming language used for the backend.
- **Dash**: Web framework for building interactive web applications.
- **Plotly**: Data visualization library for generating graphs and charts.
- **Pandas**: Data manipulation and analysis library used for handling CSV data.
- **Bootstrap**: CSS framework for responsive layout and styling.

## Setup Instructions

### Prerequisites:
- Python 3.x
- pip (Python package installer)

### Installation Steps:
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/covid-dashboard.git
   cd covid-dashboard
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # For Windows
   .\.venv\Scripts\activate
   # For macOS/Linux
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure that `requirements.txt` includes the following:
   ```
   dash
   plotly
   pandas
   ```

4. Download the `state_wise_daily.csv` file from the relevant source and save it in the project directory.

5. Run the app:
   ```bash
   python app.py
   ```

6. Open your web browser and visit:
   ```
   http://127.0.0.1:8050/
   ```

## Usage

### Interactive Dashboard
- **Dropdowns**: Select options from dropdown menus to filter data:
  - Choose the commodity (Mask, Sanitizer, Oxygen) to display its graph.
  - Choose the COVID-19 zone (Red, Blue, Green, Orange) to display its pie chart.

- **Bar Chart**: Displays state-level COVID-19 data, including total cases, hospitalized, recovered, or deceased based on the dropdown selection.

- **Line Graph**: Visualizes the distribution of commodities like Mask, Sanitizer, and Oxygen across different statuses.

- **Pie Chart**: Shows the distribution of COVID-19 zones (Red, Blue, Green, Orange) across states.



## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` includes an overview, setup instructions, usage examples, and how others can contribute to the project. Make sure to replace the placeholder links like `https://github.com/yourusername/covid-dashboard.git` with actual links relevant to your project.
