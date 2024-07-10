# your_custom_app/item_api.py

from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_item_details(item_code=None):
    if item_code:
        # If item code is provided, fetch details for the specific item
        item = frappe.get_doc("Item", item_code)
        if item:
            return {
                "item_code": item.item_code,
                "category":item.custom_category,
                "Sub category":item.custom_sub_category,
                "item_name": item.item_name,
                "item_company": item.custom_item_company,
                "item_packing": item.custom_item_packing,
                "item_type": item.custom_item_type,
                # Add other fields as needed
            }
        else:
            return {"error": _("Item not found")}
    else:
        # If no item code provided, fetch details for all items
        items = frappe.get_all("Item", fields=["item_code", "custom_category", "custom_sub_category", "item_name", "custom_item_company", "custom_item_packing", "custom_item_type"])
    
    return items
