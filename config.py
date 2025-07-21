
import json
import os

CONFIG_PATH = "vendowise_config.json"
DEFAULT_CONFIG = {
    "min_stock_buffer_days": 7,
    "delay_days": 5,
    "max_po_delay": 5,
    "max_location_risk": 6,
    "max_reject": 0.03,
    "max_payment_terms": 45
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
    try:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
    except:
        config = DEFAULT_CONFIG
    return {**DEFAULT_CONFIG, **config}

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)
