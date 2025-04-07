app_name = "wasper_inventory"
app_title = "Wasper Inventory"
app_publisher = "Wasper"
app_description = "Inventory Management Solution"
app_email = "support@wasper.com"
app_license = "MIT"

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["module", "in", ["Wasper Inventory"]]
        ]
    },
    {
        "doctype": "Property Setter",
        "filters": [
            ["module", "in", ["Wasper Inventory"]]
        ]
    },
    {
        "doctype": "Workspace",
        "filters": [
            ["module", "in", ["Wasper Inventory"]]
        ]
    }
]

# Includes
includes = [
    "wasper_inventory.reports",
    "wasper_inventory.email_templates"
]

# Scheduled Tasks
scheduler_events = {
    "all": [
        "wasper_inventory.scheduler_events.all"
    ],
    "daily": [
        "wasper_inventory.scheduler_events.daily"
    ],
    "hourly": [
        "wasper_inventory.scheduler_events.hourly"
    ],
    "weekly": [
        "wasper_inventory.scheduler_events.weekly"
    ]
}

# Website Routes
website_routes = [
    {
        "from_route": "/pos",
        "to_route": "pos"
    }
]

# DocType Events
doc_events = {
    "Item": {
        "validate": "wasper_inventory.doc_events.item.validate"
    },
    "POS Invoice": {
        "on_submit": "wasper_inventory.doc_events.pos_invoice.on_submit",
        "on_cancel": "wasper_inventory.doc_events.pos_invoice.on_cancel"
    },
    "Stock Entry": {
        "on_submit": "wasper_inventory.doc_events.stock_entry.on_submit",
        "on_cancel": "wasper_inventory.doc_events.stock_entry.on_cancel"
    }
}

# Permissions
permissions = [
    {
        "role": "System Manager",
        "doctype": "POS Profile",
        "permlevel": 0,
        "rights": ["read", "write", "create", "delete", "report", "export", "import", "print", "email"]
    },
    {
        "role": "POS User",
        "doctype": "POS Profile",
        "permlevel": 0,
        "rights": ["read", "write", "create", "report", "print"]
    }
]

# Website Context
website_context = {
    "favicon": "/assets/wasper_inventory/images/favicon.ico",
    "splash_image": "/assets/wasper_inventory/images/splash.png"
}

# Application Version
app_version = "1.0.0"

# Application Update
update_available = False

# Application Icon
app_icon = "octicon octicon-package"

# Application Color
app_color = "#5e64ff"

# Application Logo
app_logo_url = "/assets/wasper_inventory/images/logo.png"