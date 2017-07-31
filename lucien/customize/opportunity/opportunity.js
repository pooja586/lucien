// For license information, please see license.txt

// frappe.provide("erpnext.crm");
frappe.ui.form.on("Opportunity", {
	validate: function (frm) {
		frm.reload_doc();
	},	
	refresh: function(frm) {
		frm.add_custom_button(__('x'), function() {
		 		frappe.set_route("List", "Opportunity")
				 
		})
	}
});
