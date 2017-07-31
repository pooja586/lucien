# -*- coding: utf-8 -*-
# Copyright (c) 2017, indictrans technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cstr, flt, getdate, comma_and, cint, nowdate
from frappe.model.document import Document

class Planning(Document):
	def validate(self):
		self.validate_date()

	def validate_date(self):
		if getdate(self.start_date) > getdate(self.end_date):
			frappe.throw(_("Start date ahead of end date"))
		
