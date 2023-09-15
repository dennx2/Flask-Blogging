# Flask Blogging

This blogging application is constructed using the Flask framework, providing users with the ability to create new posts, view existing content, like posts, and delete them.

## Prerequisites

Before you can run the Flask program, make sure you have the following prerequisites installed on your system:

1. **Python**: Make sure you have Python 3.x installed. You can download Python from the official website: [python.org/downloads](https://www.python.org/downloads/).

2. **Virtual Environment (optional but recommended)**: It is a good practice to create a virtual environment to isolate your project's dependencies. You can create one using `venv`:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:
    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```


3. **Denpendencies**: Install dependencies from requirements.txt::
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Follow these steps to run the Flask program:

1. **Clone the Repository**: If you haven't already, clone the repository to your local machine.
    ```bash
    git clone https://github.com/dennx2/flask-blogging.git
    ```

2. **Configure Your Flask Application**: Create a `config.py` file to configure them based on the `config_template.py` provided in the project.

3. **Run the Flask Application**: In your terminal, navigate to the project directory containing `app.py`, and run the following command:
    ```bash
    python app.py
    ``` 

    This command will start the Flask development server, and you should see output indicating that the server is running. By default, the server should be accessible at `http://localhost:5000/` in your web browser.

4. **Access the Application**: Open a web browser and go to `http://localhost:5000/` to access the Flask application.

5. **Stopping the Server**: To stop the Flask development server, press `Ctrl+C` in the terminal where it's running.

That's it! You should now have the application up and running on your local machine.