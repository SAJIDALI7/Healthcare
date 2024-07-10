from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_sub_category_details(sub_category_id=None):
    if sub_category_id:
        # If category_id is provided, fetch details for the specific category
        sub_category = frappe.get_doc("Sub Category", sub_category_id)
        if sub_category:
            return {
                "sub_category_id": sub_category.sub_category_id,
                "category": sub_category.category,
                "sub_category_name": sub_category.sub_category_name,
                # Add other fields as needed
            }
        else:
            return {"error": _("Sub Category not found")}
    else:
        # If no category_id provided, fetch details for all categories
        sub_category = frappe.get_all("Sub Category", fields=["sub_category_id", "category", "sub_category_name"])
        return sub_category
