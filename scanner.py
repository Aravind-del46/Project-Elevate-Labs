import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Payloads to test
payloads = {
    "xss": "<script>alert(1)</script>",
    "sqli": "' OR '1'='1"
}

# Get all forms from HTML content
def get_forms(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("form")

# Extract form action, method, inputs
def extract_form_info(form):
    action = form.get("action")
    method = form.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.get("type", "text")
        input_name = input_tag.get("name")
        inputs.append({"type": input_type, "name": input_name})

    return {"action": action, "method": method, "inputs": inputs}

# Test each form with payloads
def test_form(form_details, base_url):
    action = form_details["action"]
    method = form_details["method"]
    inputs = form_details["inputs"]
    form_url = urljoin(base_url, action)

    for vuln_type, payload in payloads.items():
        data = {}
        for input in inputs:
            if input["type"] == "text" and input["name"]:
                data[input["name"]] = payload
            elif input["name"]:
                data[input["name"]] = "test"

        try:
            if method == "post":
                response = requests.post(form_url, data=data)
            else:
                response = requests.get(form_url, params=data)

            if payload in response.text:
                print(f"[!!] Possible {vuln_type.upper()} vulnerability detected at: {form_url}")
                print(f"     Payload: {payload}")
            else:
                print(f"[OK] No {vuln_type.upper()} at: {form_url}")
        except Exception as e:
            print(f"[ERROR] Could not test form at {form_url}: {e}")

# Main scanner function
def scan_url(url):
    print(f"[+] Scanning: {url}")
    try:
        html = requests.get(url).text
    except Exception as e:
        print(f"[ERROR] Could not fetch URL: {e}")
        return

    forms = get_forms(html)
    print(f"[+] Found {len(forms)} forms")

    for i, form in enumerate(forms):
        print(f"\n--- Form #{i+1} ---")
        print(form)  # Show raw HTML (debugging)
        form_info = extract_form_info(form)
        print(f"Action: {form_info['action']}")
        print(f"Method: {form_info['method'].upper()}")
        print("Inputs:")
        for input in form_info["inputs"]:
            print(f" - {input['name']} ({input['type']})")
        test_form(form_info, url)

# ✅ USE THIS URL — has a GET form!
target_url = "https://xss-game.appspot.com/level1/frame"
scan_url(target_url)
