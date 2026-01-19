def assign_role(email):
    if email.endswith("@admin.hospital.org"): return "admin"
    if email.endswith("@hospital.org"): return "doctor"
    return "doctor"
