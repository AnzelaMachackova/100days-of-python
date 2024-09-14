
# Pixela Habit Tracker

## Purpose
This command-line interface script interacts with the Pixela API to manage habit-tracking graphs, providing functionalities such as creating, updating, viewing statistics, and deleting graphs.

## Features
- **Create Graph**: Initializes a new graph if it doesn't already exist.
- **Update Graph**: Modifies data points on an existing graph.
- **Graph Statistics**: Provides statistical analysis of graph data.
- **Delete Graph**: Removes a specified graph.

## Usage
Before using the script, ensure Python and the `requests` library are installed on your system. Navigate to the script's directory in your terminal to execute commands.

### Commands
- **Create a Graph**
  ```bash
  python habit_tracker.py --create --graphid [GRAPH_ID]
  ```
- **Update a Graph**
  ```bash
  python habit_tracker.py --update --graphid [GRAPH_ID]
  ```
- **Get Statistics of a Graph**
  ```bash
  python habit_tracker.py --stats --graphid [GRAPH_ID]
  ```
- **Delete a Graph**
  ```bash
  python habit_tracker.py --delete --graphid [GRAPH_ID]
  ```
Replace `[GRAPH_ID]` with the actual ID of the graph you intend to interact with.

## Prerequisites
- **Python**: Make sure Python is installed on your system.
- **Requests Library**: Install via pip if not already installed:
  ```bash
  pip install requests
  ```
- **Configuration**: Add `userinfo.py` with your Pixela `USERNAME` and `TOKEN`.

## File Structure
- **habit_tracker.py**: Main script handling command-line arguments and directing operations.
- **pixela_functions.py**: Contains all functions for Pixela API interactions.

## Support
For additional help or more information about Pixela APIs, refer to the [official Pixela documentation](https://docs.pixe.la/).
