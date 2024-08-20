import requests
import json

def demo_streaming_response():
    url = "http://localhost:8000/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "prompt": "Write a haiku.",
        "stream": True
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
    
    print("\n--- Streaming Response ---")
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))
    print("\n--- End of Streaming Response ---")

def demo_formatted_response():
    url = "http://localhost:8000/generate_formatted"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "prompt": "Write a haiku.",
        "stream": True
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
    
    print("\n--- Formatted Response ---")
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["response"])
    else:
        print(f"Error: {response.status_code} - {response.text}")
    print("\n--- End of Formatted Response ---")

def demo_complete_json_response():
    url = "http://localhost:8000/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "prompt": "Write a haiku.",
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    print("\n--- Complete JSON Response ---")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error: {response.status_code} - {response.text}")
    print("\n--- End of Complete JSON Response ---")

if __name__ == "__main__":
    print("Demo Script Execution\n")
    
    print("Demo Streaming Response:")
    demo_streaming_response()
    
    print("\nDemo Formatted Response:")
    demo_formatted_response()
    
    print("\nDemo Complete JSON Response:")
    demo_complete_json_response()
