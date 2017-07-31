// Copyright (c) 2017, indictrans technologies and contributors
// For license information, please see license.txt

frappe.provide("erpnext.crm");
frappe.ui.form.on("Opportunity", {	
	refresh: function(frm) {
		frm.add_custom_button(__('Close'), function() {
			frappe.set_route("List", "Opportunity")
			 
		})
	}
});
