# Periodic Table

A lightweight Python application that provides interactive access to elemental data through both a Command Line Interface (CLI) and a Graphical User Interface (GUI) built with Tkinter.

## Features

* **Comprehensive Data**: Provides detailed information for chemical elements, including:
  * Atomic number and atomic mass
  * Symbol and element name
  * Electron configuration and shell breakdown
  * Electronegativity, density, melting/boiling points
  * Discovery history and discoverer details
* **Dual Interface**: Choose between a fast terminal workflow or a visual, click-based GUI layout.
* **Flexible Search**: Query elements by symbol, full name, or atomic number.

## Interfaces

### Command Line Interface (CLI)

* Interactive loop allowing multiple queries in one session.
* Case-insensitive quitting mechanism (`q` or `quit`).
* Cleanly formatted text output per element.

### Graphical User Interface (GUI)

* Interactive visual layout built with **Tkinter**.
* Color-coded category key for chemical groups (Non-metals, Noble Gases, Alkali Metals, Alkaline Earth Metals, Semimetals, Halogens).
* Instant detail display in a dedicated results panel.

## Requirements

* **Python**: Version 3.x or higher
* **Tkinter**: Included by default with standard Python installations on Windows and macOS. Linux users may need to install it via their package manager (e.g., `sudo apt-get install python3-tk`).

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Periodic-Table.git
   cd Periodic-Table
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

## Usage

### Running the CLI Application

Launch the terminal-based interactive prompt:

```bash
python cli.py
```

* **Example Inputs**: Enter `1`, `H`, or `Hydrogen` to retrieve information on Hydrogen. Enter `q` or `quit` to exit.

### Running the GUI Application

Launch the visual interface:

```bash
python gui.py
```