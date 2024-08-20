import requests
import json
import sys

def send_request(model, prompt, stream=False, formatted=False):
    url = "http://localhost:8000/generate_formatted" if formatted else "http://localhost:8000/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

    # Print the response
    if response.status_code == 200:
        if formatted:
            json_response = response.json()
            print(json_response["response"])
        else:
            for line in response.iter_lines():
                if line:
                    print(line.decode('utf-8'))
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python send_request.py <model> <prompt> [stream] [formatted]")
        sys.exit(1)

    model = sys.argv[1]
    prompt = sys.argv[2]
    stream = len(sys.argv) > 3 and sys.argv[3].lower() == "true"
    formatted = len(sys.argv) > 4 and sys.argv[4].lower() == "true"
    send_request(model, prompt, stream, formatted)
