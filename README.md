# Python Selenium Framework Bookcart

A Custom Python Selenium Framework built with pytest

## Installation

Use pip to install packages from requirements.txt file.

```bash
pip install -r requirements.txt
```

## Usage

Run the tests through tox as follows
```bash
BROWSER=chrome HEADLESS=true tox
```

## Features

### Pytest configuration
Manage pytest configuration in the `pytest.ini` file.

### Tox configuration
Tox configuration for different environments can be managed from `tox.ini` file. Parallel test execution is also configured in this file. 

### Environment configuration
The `.env` file holds the configuration of the Application under test.

### GUI and No-GUI auth
In the file `/tests/conftest.py` there is a fixture `no_gui_login` that facilitates login through API call and adds the application cookies to the browser. 
Use the fixture `driver` for GUI login.

### Init driver
The file `/utils/driver_factory.py` is responsible for initializing the driver object. 

### Logging
Logging is managed through python logging. Logs are generated in the `logs` folder. 

### Reporting
Html reports are generated through `pytest-html` plugin. The reports are generated in the `reports` folder. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.# Python Selenium Framework Bookcart

A Custom Python Selenium Framework built with pytest

## Installation

Use pip to install packages from requirements.txt file.

```bash
pip install -r requirements.txt
```

## Usage

Run the tests through tox as follows
```bash
BROWSER=chrome HEADLESS=true tox
```

## Features

### Pytest configuration
Manage pytest configuration in the `pytest.ini` file.

### Tox configuration
Tox configuration for different environments can be managed from `tox.ini` file. Parallel test execution is also configured in this file. 

### Environment configuration
The `.env` file holds the configuration of the Application under test.

### GUI and No-GUI auth
In the file `/tests/conftest.py` there is a fixture `no_gui_login` that facilitates login through API call and adds the application cookies to the browser. 
Use the fixture `driver` for GUI login.

### Init driver
The file `/utils/driver_factory.py` is responsible for initializing the driver object. 

### Logging
Logging is managed through python logging. Logs are generated in the `logs` folder. 

### Reporting
Html reports are generated through `pytest-html` plugin. The reports are generated in the `reports` folder. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.