# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lucien"
app_title = "Lucien Tech"
app_publisher = "indictrans technologies"
app_description = "Publishing Business amd Operations"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "khushal.t@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lucien/css/lucien.css"
# app_include_js = "/assets/lucien/js/lucien.js"

# include js, css files in header of web template
# web_include_css = "/assets/lucien/css/lucien.css"
# web_include_js = "/assets/lucien/js/lucien.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lucien.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lucien.install.before_install"
# after_install = "lucien.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lucien.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Customer": "lucien.py.permission_query.get_permission_query_conditions",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doctype_js={
	"Lead":["customize/lead/lead.js"],
	"Opportunity":["customize/opportunity/opportunity.js"]
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lucien.tasks.all"
# 	],
# 	"daily": [
# 		"lucien.tasks.daily"
# 	],
# 	"hourly": [
# 		"lucien.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lucien.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lucien.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lucien.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lucien.event.get_events"
# }

