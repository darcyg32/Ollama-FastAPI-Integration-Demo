# FastAPI and Ollama Integration Demo

This project demonstrates how to integrate FastAPI with Ollama, a tool for running and managing AI models. It showcases three main functionalities:
1. **Streaming Responses**: Receive and display raw streaming responses from the Ollama API.
2. **Formatted Responses**: Aggregate and format streaming responses into a cohesive output.
3. **Complete JSON Responses**: Handle and display complete JSON responses from the Ollama API.

## Dependencies
### Required Software
- **Python**: Ensure you have Python 3.7 or later installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Requests**: A simple HTTP library for Python.
- **Ollama**: A tool for running AI models locally.

### Installation
1. **FastAPI and Requests**:
    You can install FastAPI and Requests using pip:
    `pip install fastapi requests`
    
2. **Ollama**:
    Follow the instructions on the [Ollama GitHub repository](https://github.com/ollama/ollama) to install Ollama. Make sure to download and install the version that includes the `llama3.1` model.
    
    For a quick installation via the command line, use:
    `pip install ollama`
    Ensure that you have the `llama3.1` model available. You can usually download and install it through Ollama’s CLI or the web interface.
    
## Files
- **app.py**: Defines a FastAPI application with endpoints for generating raw and formatted responses from the Ollama API.
- **send_request.py**: A command-line script to send requests to the FastAPI server and print responses. It supports both raw and formatted responses.
- **demo_script.py**: Demonstrates how to use the FastAPI endpoints to retrieve streaming, formatted, and complete JSON responses.

## Usage
### Clone the Repository:
```sh
git clone https://github.com/your-username/fastapi-ollama-demo.git
cd fastapi-ollama-demo
```
### Set Up a Virtual Environment:
```sh
python -m venv venv
source venv/bin/activate
```
### Install Dependencies:
```sh
pip install -r requirements.txt
```
### Running the FastAPI Server
1. Start the FastAPI server:
    `uvicorn app:app --reload`
    The server will be available at `http://localhost:8000`.
### Sending Requests
1. **Using the Command-Line Script**:
    You can use `send_request.py` to interact with the FastAPI server. Here’s how to use it:
    `python send_request.py <model> <prompt> [stream] [formatted]`
    - `<model>`: The name of the model to use (e.g., `llama3.1`).
    - `<prompt>`: The prompt to send to the model.
    - `[stream]`: Optional flag to enable streaming (default is `False`).
    - `[formatted]`: Optional flag to get a formatted response (default is `False`).
    
    Example:
    `python send_request.py llama3.1 "Write a haiku." True True`
    
2. **Using the Demo Script**:
    Run `demo_script.py` to see the demo in action:
    `python demo_script.py`
    This script will show examples of streaming, formatted, and complete JSON responses.

3. **Using cURL:**
   - Get Raw Streaming Response Example:
        ```sh
        curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{
          "model": "llama3.1",
          "prompt": "Write a haiku.",
          "stream": true
        }'
        ```
   - Get Formatted Response Example:
        ```sh
        curl -X POST "http://localhost:8000/generate_formatted" -H "Content-Type: application/json" -d '{
          "model": "llama3.1",
          "prompt": "Write a haiku.",
          "stream": false
        }'
        ```
   - Get Complete JSON Response Example:
        ```sh
        curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{
          "model": "llama3.1",
          "prompt": "Write a haiku.",
          "stream": false
        }'
        ```
   
    
## Additional Notes

- Ensure that Ollama is properly configured and running locally on `http://localhost:11434`. Update the URL in `app.py` if your Ollama instance is hosted elsewhere.
- The FastAPI server and Ollama must be running simultaneously to process requests successfully.
- For more details on FastAPI and Requests, refer to their respective documentation:
    - [FastAPI Documentation](https://fastapi.tiangolo.com/)
    - [Requests Documentation](https://requests.readthedocs.io/en/latest/)

## System Specifications
For reference, this project was developed and tested on the following hardware:
- Processor: AMD Ryzen 5 5600X 6-Core
- GPU: NVIDIA GeForce RTX 3060 Ti
- RAM: 32 GB
- Operating System: Ubuntu/WSL on Windows 11
- Storage: 2 TB SSD
- These specifications were sufficient for running the FastAPI server and Ollama integration demo. If you encounter any performance issues or have different specifications, you may need to adjust your setup accordingly.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
