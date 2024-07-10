from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def upload_image():
    from werkzeug.utils import secure_filename # type: ignore
    import os

    if 'image' in frappe.request.files:
        image = frappe.request.files['image']
        filename = secure_filename(image.filename)
        file_path = os.path.join(frappe.get_site_path('public', 'files'), filename)
        
        # Save the file
        image.save(file_path)

        # Perform image scanning or processing
        scanned_data = scan_image(file_path)

        # Return scanned data (you can format it as needed)
        return frappe._dict({
            'scanned_data': scanned_data
        })
    else:
        frappe.throw(_("No image file found"))

def scan_image(file_path):
    # Dummy function to simulate scanning
    # Replace with your actual scanning logic
    # Example: Scan image and return some data
    return {
        'scanned_text': 'Some scanned text from image',
        'file_path': file_path
    }



# import requests
# import base64

# url = "https://app.nanonets.com/api/v2/OCR/FullText"

# payload={'urls': ['MY_IMAGE_URL']}
# files=[
#   ('file',('FILE_NAME',open('FILE_PATH','rb'),'application/pdf'))
# ]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files, auth=requests.auth.HTTPBasicAuth('REPLACE_API_KEY', ''))

# print(response.text)