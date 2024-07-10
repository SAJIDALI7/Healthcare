from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_category_details(category_id=None):
    if category_id:
        # If category_id is provided, fetch details for the specific category
        category = frappe.get_doc("Category", category_id)
        if category:
            return {
                "category_id": category.category_id,
                "category_name": category.category_name,
                # Add other fields as needed
            }
        else:
            return {"error": _("Category not found")}
    else:
        # If no category_id provided, fetch details for all categories
        categories = frappe.get_all("Category", fields=["category_id", "category_name"])
        return categories
