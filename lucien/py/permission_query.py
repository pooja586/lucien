from __future__ import unicode_literals
import frappe



@frappe.whitelist()
def get_permission_query_conditions(user):
	# pass
	if not user: user = frappe.session.user

	roles = frappe.get_roles(user)
	if user == "Administrator":
		return ""
	else:
		if "Sales Executive" in roles:
			names = frappe.db.sql("""select distinct reference_name from tabToDo where reference_type ='Customer' and owner ='{0}'""".format(user), as_list=1)
			# print "\n\n______________names",names 
			flat_list = [item for sublist in names for item in sublist]
			names = tuple([x.encode('UTF8') for x in list(flat_list) if x])
			print "\n\n______________names",names 
			cond = "in {0}".format(names)
			# return "`tabCustomer`.name {0}".format(cond);
			return "`tabCustomer`.owner in ('chaitrali.w@indictranstech.com')"





# @frappe.whitelist()
# def get_permission_query_conditions(user):
# roles = frappe.get_roles(user)
# names=[]
# if "Technician" in roles:
# 	reference_names=frappe.get_all("ToDo",fields='reference_name', filters={'owner':user})
# 	for i in range(0,len(reference_names)):
# 		names.insert(i,reference_names[i]["reference_name"]) 
# 	list2 = tuple([x.encode('UTF8') for x in list(names) if x])
# 	cond="";
# 	if len(list2)>1:
# 	cond = 11111111111111111
# if len(list2)==1:
# cond = "= '{0}'".format(list(list2)[0])
# if "Technician" in roles:
# #frappe.db.sql("""select name from `tabIssue` where name {0}""".format(cond),as_list=1,debug=1)
# return "`tabIssue`.name {0}".format(cond);
# if "Telecom Manager" in roles:
# cond="= '{0}'".format(user)
# return "`tabIssue`.owner {0}".format(cond);