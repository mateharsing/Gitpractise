import requests
import random
from requests.auth import HTTPBasicAuth
from getpass import getpass

# <editor-fold desc="hidden code">
# Configuration
USERNAME = 'automation'
PASSWORD = '123Engine123'
BASE_URL = 'https://mharsing-med.jamacloud.com/rest/v1'
# </editor-fold>

# Configuration
BASE_URL = 'https://mharsing-med.jamacloud.com/rest/v1'
PROJECT_ID = 98  # your project ID in Jama where the results are headed
ITEM_TYPE_ID = 213  # Automated Test Result
PARENT_ITEM_ID = 18008  # Valid parent item (e.g., a Set or Folder)
VERIFICATION_CASE_ID = 18013  # ID of the verification case in
RELATIONSHIP_TYPE_ID = 4  # ID of the relationship between AUT Test Runs and Verifications
PICKLIST_FIELD_KEY = 'test_result$213'  # key for the picklist where my PASS/FAIL results go

# ECG test cases using Greek letters
ecg_cases = {
    "α": "Normal sinus rhythm",
    "β": "Sinus bradycardia",
    "γ": "Sinus tachycardia",
    "δ": "Atrial fibrillation",
    "ε": "Ventricular tachycardia",
    "ζ": "ST elevation",
    "η": "ST depression",
    "θ": "PVCs",
    "ι": "LBBB",
    "κ": "RBBB",
    "λ": "T-wave inversion",
    "μ": "QT prolongation"
}

auth = HTTPBasicAuth(USERNAME, PASSWORD)

for greek, condition in ecg_cases.items():
    print(f"\n📡 Creating test result for {greek} – {condition}")
    result_value = random.choice([942, 943])  # 942 = Passed, 943 = Failed ; you could also set this in the beginning

    payload = {
        "project": PROJECT_ID,
        "itemType": ITEM_TYPE_ID,
        "location": {
            "parent": {
                "item": PARENT_ITEM_ID
            }
        },
        "fields": {
            "name": f"ECG Test – {greek} ({condition})",
            "description": f"Automated test result for {condition}",
            PICKLIST_FIELD_KEY: result_value
        }
    }

    item_response = requests.post(f'{BASE_URL}/items', auth=auth, json=payload)
    if item_response.status_code != 201:
        print("❌ Failed to create item.")
        print("Status Code:", item_response.status_code)
        print("Response Body:", item_response.text)
        continue

    new_item_id = item_response.json()['meta']['id']
    print(f"✅ Created item ID: {new_item_id}")

    # Create relationship (Verification Case → Test Result)
    relationship_payload = {
        "fromItem": VERIFICATION_CASE_ID,
        "toItem": new_item_id,
        "relationshipType": RELATIONSHIP_TYPE_ID
    }

    rel_response = requests.post(f'{BASE_URL}/relationships', auth=auth, json=relationship_payload)
    if rel_response.status_code != 201:
        print("❌ Failed to create relationship.")
        print("Status Code:", rel_response.status_code)
        print("Response Body:", rel_response.text)
        continue

    print(f"🔗 Linked to verification case {VERIFICATION_CASE_ID}")
