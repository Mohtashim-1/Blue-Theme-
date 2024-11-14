app_name = "modern_desk1"
app_title = "Modern Desk1"
app_publisher = "mohtashim"
app_description = "Custom Theme"
app_email = "shoaibmohtashim973@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/modern_desk1/css/modern_desk1.css"
# app_include_js = "/assets/modern_desk1/js/modern_desk1.js"

app_include_css =  ["/assets/modern_desk1/css/theme.css",]
app_include_js = ["/assets/modern_desk1/js/theme.js",]

# include js, css files in header of web template
# web_include_css = "/assets/modern_desk1/css/modern_desk1.css"
# web_include_js = "/assets/modern_desk1/js/modern_desk1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "modern_desk1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "modern_desk1/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "modern_desk1.utils.jinja_methods",
# 	"filters": "modern_desk1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "modern_desk1.install.before_install"
# after_install = "modern_desk1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "modern_desk1.uninstall.before_uninstall"
# after_uninstall = "modern_desk1.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "modern_desk1.utils.before_app_install"
# after_app_install = "modern_desk1.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "modern_desk1.utils.before_app_uninstall"
# after_app_uninstall = "modern_desk1.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "modern_desk1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"modern_desk1.tasks.all"
# 	],
# 	"daily": [
# 		"modern_desk1.tasks.daily"
# 	],
# 	"hourly": [
# 		"modern_desk1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"modern_desk1.tasks.weekly"
# 	],
# 	"monthly": [
# 		"modern_desk1.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "modern_desk1.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "frappe.core.doctype.user.user.switch_theme": "modern_desk1.overrides.switch_theme.switch_theme"
}
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "modern_desk1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "modern_desk1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["modern_desk1.utils.before_request"]
# after_request = ["modern_desk1.utils.after_request"]

# Job Events
# ----------
# before_job = ["modern_desk1.utils.before_job"]
# after_job = ["modern_desk1.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"modern_desk1.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
