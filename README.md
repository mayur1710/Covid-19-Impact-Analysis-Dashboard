# COVID-19 Impact Analysis Dashboard

![image](https://github.com/user-attachments/assets/d0bf4f01-d9f6-416b-966f-2034dd281739)

This web application provides a comprehensive and interactive dashboard for visualizing COVID-19 statistics across different states. The dashboard includes real-time data visualizations such as total cases, active cases, recovered cases, deaths, and commodity usage (Mask, Sanitizer, Oxygen) along with zone-wise distributions.

The project utilizes **Dash** for the web framework, **Plotly** for interactive visualizations, and **Pandas** for data manipulation. The dashboard is styled with **Bootstrap** for a responsive and modern look.

## Project Overview

The dashboard allows users to explore:
- COVID-19 statistics like total, active, recovered, and deceased cases across states.
- Usage data of key commodities like masks, sanitizers, and oxygen.
- Zone-wise COVID-19 impact (Red Zone, Blue Zone, Green Zone, Orange Zone).

## Features
- **COVID-19 Data**: Displays data for each state with the total, active, recovered, and deceased cases.
- **Commodity Usage Graphs**: Visualizes commodity usage (Mask, Sanitizer, Oxygen) over time.
- **State-wise Statistics**: Bar charts and line graphs displaying state-specific data.
- **COVID-19 Zones**: Pie charts that show the distribution of different zones (Red, Blue, Green, Orange).
- **Responsive Design**: The dashboard is fully responsive and uses Bootstrap for a smooth user experience on both desktop and mobile.

## Technologies Used
- **Python**: Main programming language used.
- **Dash**: Framework used to build the interactive web application.
- **Plotly**: Data visualization library used for generating the graphs and charts.
- **Pandas**: Library used to load and manipulate the dataset.
- **Bootstrap**: Frontend framework for creating a responsive and aesthetically pleasing design.

## Setup Instructions

### Prerequisites:
- Python 3.x
- pip (Python package installer)

### Installation Steps:
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/mayur1710/Covid-19-Impact-Analysis-Dashboard.git
   cd Covid-19-Impact-Analysis-Dashboard
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

4. Download the `state_wise_daily.csv` file (make sure the file is in your project directory).

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:8050/
   ```

## Usage

Once you launch the application, you can interact with the following elements:
- **Dropdowns**: Use the dropdown menus to filter data:
  - Select a commodity (Mask, Sanitizer, Oxygen) to visualize its usage over time.
  - Select a COVID-19 zone (Red, Blue, Green, Orange) to see the zone distribution.
  
- **Bar Chart**: View a bar chart of state-specific data (total, hospitalized, recovered, or deceased cases) based on the dropdown selection.

- **Line Graph**: View the trend for commodities (Mask, Sanitizer, Oxygen) based on the status dropdown.

- **Pie Chart**: View the distribution of the COVID-19 zones (Red, Blue, Green, Orange).

## Example

When you open the app, you will see an interactive dashboard with:
- A summary of COVID-19 statistics, including total cases, active cases, recovered cases, and deaths.
- A bar chart for the selected category (Hospitalized, Recovered, etc.).
- A line graph for the chosen commodity (Mask, Sanitizer, Oxygen).
- A pie chart that shows the distribution of COVID-19 zones.



## Acknowledgements
- Data Source: The data used in this project is publicly available and can be found in the `state_wise_daily.csv` file.
- Libraries: This project uses Dash, Plotly, Pandas, and Bootstrap.

