# Copyright (c) 2025, Osama and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
    
  def before_submit(self):
     exists = frappe.db.exists(
		 "Library Membership", {
			 "library_member": self.library_member,
             "docstatus": DocStatus.SUBMITTED,
             "to_date":(">", self.from_date),
		 },
	 ) 
     if exists:
         frappe.throw("This membership already exists")  
