from send_request import send_request

def demo_streaming_response():
    print("\n--- Streaming Response ---")
    send_request(model="llama3.1", prompt="Write a haiku.", stream=True)
    print("\n--- End of Streaming Response ---")

def demo_formatted_response():
    print("\n--- Formatted Response ---")
    send_request(model="llama3.1", prompt="Write a haiku.", stream=True, formatted=True)
    print("\n--- End of Formatted Response ---")

def demo_complete_json_response():
    print("\n--- Complete JSON Response ---")
    send_request(model="llama3.1", prompt="Write a haiku.")
    print("\n--- End of Complete JSON Response ---")

if __name__ == "__main__":
    print("Demo Script Execution\n")
    
    print("Demo Streaming Response:")
    demo_streaming_response()
    
    print("\nDemo Formatted Response:")
    demo_formatted_response()
    
    print("\nDemo Complete JSON Response:")
    demo_complete_json_response()
