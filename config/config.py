# Configuration File
# This file contains all configuration settings
# Keep this file separate from the main script for easier obfuscation

# Account Configuration
YOUR_BIRTHDAY = "2 4 1950"  # Format: "month day year"
YOUR_GENDER = "1"  # 1=Male, 2=Female, 3=Other
YOUR_PASSWORD = ""  # Leave empty to read from password.txt

# 5sim API Configuration
FIVESIM_API_KEY = ""  # Enter your 5sim API key here (or leave empty to read from 5sim_config.txt)
FIVESIM_COUNTRY = "usa"  # Options: usa, russia, ukraine, kazakhstan, etc.
FIVESIM_OPERATOR = "any"  # Options: any, virtual, etc.

# Names Configuration
USE_ARABIC_NAMES = True  # True to use Arabic names, False to use English names
NAMES_FILE = "data/names.txt"  # File containing names (one per line or JSON format)

# User Agents Configuration
USER_AGENTS_FILE = "config/user_agents.txt"  # File containing user agents (one per line)
