import os
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Azure API credentials
AZURE_ENDPOINT = "/"
AZURE_API_KEY = ""
DEPLOYMENT_NAME = "Phi-4"

@csrf_exempt
def chat_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        # ✅ Step 1: Read request data
        data = json.loads(request.body)
        user_message = data.get("message", "")

        if not user_message:
            return JsonResponse({"error": "Message is required"}, status=400)

        # ✅ Step 2: Prepare Azure API request
        headers = {
            "Content-Type": "application/json",
             "api-key": AZURE_API_KEY,
        }

        payload = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
            "model": DEPLOYMENT_NAME,
            "max_tokens": 1000,
        }

    
        response = requests.post(AZURE_ENDPOINT, headers=headers, json=payload)
    
   
        if response.status_code != 200:
            return JsonResponse({"error": f"Azure AI Error: {response.status_code}", "details": response.text}, status=500)

        response_data = response.json()

        if "choices" not in response_data or not response_data["choices"]:
            return JsonResponse({"error": "Invalid response from Azure AI", "debug": response_data}, status=500)

        return JsonResponse({"reply": response_data["choices"][0]["message"]["content"]})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format in request"}, status=400)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Request to Azure failed: {str(e)}"}, status=500)

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        return JsonResponse({"error": "Internal server error", "debug": str(e), "traceback": error_details}, status=500)
