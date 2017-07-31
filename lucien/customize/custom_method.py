# -*- coding: utf-8 -*-
# Copyright (c) 2017, indictrans technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cstr, flt, getdate, comma_and, cint, nowdate
from frappe.model.document import Document


def send_mail(**kwargs):
	"""Notify sales user for approval details"""
 	
 	try:
		frappe.sendmail(recipients=kwargs.get('mailid'), subject="Subscription Details",
			message=render_mail_template(val=kwargs), delayed=False)
	except frappe.OutgoingEmailError:
		pass 