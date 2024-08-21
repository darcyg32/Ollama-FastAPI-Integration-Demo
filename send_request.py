import requests
import json
import sys

# Function to send a request to the FastAPI server
def send_request(model, prompt, stream=False, formatted=False):
    # Determine the URL based on whether a formatted response is requested
    url = "http://localhost:8000/generate_formatted" if formatted else "http://localhost:8000/generate"
    headers = {"Content-Type": "application/json"}  # Specify the content type as JSON
    data = {
        "model": model,     # Model name to be used
        "prompt": prompt,   # Prompt to be sent to the model
        "stream": stream    # Streaming flag
    }

    # Send a POST request to the appropriate FastAPI endpoint
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

    # Handle the response based on the status code
    if response.status_code == 200:
        if formatted:
            json_response = response.json()     # Parse the JSON response
            print(json_response["response"])    # Print the formatted response
        else:
            # Stream and print each line of the response
            for line in response.iter_lines():
                if line:
                    print(line.decode('utf-8'))
    else:
        # Print an error message if the request failed
        print(f"Error: {response.status_code} - {response.text}")

# Entry point of the script when run from the command line
if __name__ == "__main__":
    # Check if the required args are provided
    if len(sys.argv) < 3:
        print("Usage: python send_request.py <model> <prompt> [stream] [formatted]")
        sys.exit(1)

    # Extract coommand line args
    model = sys.argv[1]
    prompt = sys.argv[2]
    stream = len(sys.argv) > 3 and sys.argv[3].lower() == "true"
    formatted = len(sys.argv) > 4 and sys.argv[4].lower() == "true"

    # Call the function to send the request
    send_request(model, prompt, stream, formatted)
