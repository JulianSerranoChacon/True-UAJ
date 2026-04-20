# Analytics example

A python script to analyze the events extracted from this browser game: <https://gjimenezucm.github.io/giftjam2023/>

Download Telemetry button only works on Chrome browsers.

# Install and run

Requires Python >=3.8. 

0. Run a terminal (Windows or Linux) and move to this directory
1. Create a virtual environment with `python -m venv .venv`
2. Load the environment:
    - Linux: `source ./.venv/bin/activate`
    - Windows: `.\.venv\Scripts\activate.bat`
3. Install dependencies with `pip install -r requirements.txt`
4. Run the script with `python analyze.py`

Terminal will display some metric stats and the script will create a heatmap.png file with a heatmap of deaths.