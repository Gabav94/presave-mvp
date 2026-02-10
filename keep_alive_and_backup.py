# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:47:13 2026

@author: Gabriel
"""

from supabase import create_client
import json
import datetime

URL = "SUPABASE_URL"
KEY = "SUPABASE_SERVICE_ROLE_KEY"

supabase = create_client(URL, KEY)

# 1. KEEP ALIVE (actividad real)
supabase.table("profiles").select("id").limit(1).execute()

# 2. BACKUP SIMPLE
tables = ["profiles", "campaigns", "tokens", "actions"]
backup = {}

for t in tables:
    backup[t] = supabase.table(t).select("*").execute().data

filename = f"backup_{datetime.date.today()}.json"
with open(filename, "w") as f:
    json.dump(backup, f, indent=2)

print("✅ DB viva + backup creado:", filename)
