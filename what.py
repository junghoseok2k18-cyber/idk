from datetime import datetime

from hms_classes import Store, ValidationError


DATE_FMT = "%Y-%m-%d"
DATETIME_FMT = "%Y-%m-%d %H:%M"


# -------------------------------------------------------------------- input
def ask(prompt, required=True):
    while True:
        value = input(f"{prompt}: ").strip()
        if value or not required:
            return value or None
        print("  This field is required.")


def ask_int(prompt):
    while True:
        try:
            return int(ask(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def ask_date(prompt):
    while True:
        value = ask(prompt + " (YYYY-MM-DD)")
        try:
            datetime.strptime(value, DATE_FMT)
            return value
        except ValueError:
            print("  Invalid date format.")


def ask_datetime(prompt):
    while True:
        value = ask(prompt + " (YYYY-MM-DD HH:MM)")
        try:
            return datetime.strptime(value, DATETIME_FMT)
        except ValueError:
            print("  Invalid date/time format.")


def ask_amount(prompt):
    while True:
        try:
            amount = round(float(ask(prompt)), 2)
            if amount >= 0:
                return amount
        except ValueError:
            pass
        print("  Enter a non-negative amount.")


def show(rows, columns):
    """columns is a list of (header, key) pairs."""
    if not rows:
        print("  (no records)")
        return
    table = [[str(r.get(key, "") or "") for _, key in columns] for r in rows]
    widths = [max(len(h), *(len(row[i]) for row in table)) for i, (h, _) in enumerate(columns)]
    print("  " + " | ".join(h.ljust(w) for (h, _), w in zip(columns, widths)))
    print("  " + "-+-".join("-" * w for w in widths))
    for row in table:
        print("  " + " | ".join(cell.ljust(w) for cell, w in zip(row, widths)))


# --------------------------------------------------------------- operations
def add_department(db):
    name = ask("Department name")
    if any(d["name"].lower() == name.lower() for d in db.all("departments")):
        raise ValidationError("A department with that name already exists.")
    print(f"  Department added (ID {db.insert('departments', {'name': name})}).")


def add_doctor(db):
    show(db.all("departments"), [("ID", "id"), ("Name", "name")])
    dept_id = ask_int("Department ID")
    if not db.get("departments", dept_id):
        raise ValidationError("Department does not exist.")
    name = ask("Full name")
    specialization = ask("Specialization")
    phone = ask("Phone", False)
    email = ask("Email", False)
    if email and any((d.get("email") or "").lower() == email.lower() for d in db.all("doctors")):
        raise ValidationError("A doctor with that email already exists.")
    doctor_id = db.insert("doctors", {
        "full_name": name, "specialization": specialization,
        "dept_id": dept_id, "phone": phone, "email": email,
    })
    print(f"  Doctor added (ID {doctor_id}).")


def add_patient(db):
    name = ask("Full name")
    dob = ask_date("Date of birth")
    if dob > datetime.now().strftime(DATE_FMT):
        raise ValidationError("Date of birth cannot be in the future.")
    gender = ask("Gender (Male/Female/Other)").capitalize()
    if gender not in ("Male", "Female", "Other"):
        raise ValidationError("Gender must be Male, Female or Other.")
    patient_id = db.insert("patients", {
        "full_name": name, "dob": dob, "gender": gender,
        "phone": ask("Phone", False), "address": ask("Address", False),
        "created_at": datetime.now().strftime(DATETIME_FMT),
    })
    print(f"  Patient registered (ID {patient_id}).")


def search_patients(db):
    term = ask("Name or phone contains").lower()
    rows = [p for p in db.all("patients")
            if term in p["full_name"].lower() or term in (p.get("phone") or "").lower()]
    show(sorted(rows, key=lambda p: p["full_name"]),
         [("ID", "id"), ("Name", "full_name"), ("DOB", "dob"), ("Gender", "gender"), ("Phone", "phone")])


def list_doctors(db):
    depts = {d["id"]: d["name"] for d in db.all("departments")}
    rows = [{**d, "department": depts.get(d["dept_id"], "?")} for d in db.all("doctors")]
    show(sorted(rows, key=lambda d: d["full_name"]),
         [("ID", "id"), ("Name", "full_name"), ("Specialization", "specialization"),
          ("Department", "department"), ("Phone", "phone")])


def book_appointment(db):
    patient_id = ask_int("Patient ID")
    doctor_id = ask_int("Doctor ID")
    if not db.get("patients", patient_id):
        raise ValidationError("Patient does not exist.")
    if not db.get("doctors", doctor_id):
        raise ValidationError("Doctor does not exist.")
    when = ask_datetime("Appointment time")
    if when < datetime.now():
        raise ValidationError("Cannot book in the past.")
    when_str = when.strftime(DATETIME_FMT)
    if any(a["doctor_id"] == doctor_id and a["appt_datetime"] == when_str
           and a["status"] != "Cancelled" for a in db.all("appointments")):
        raise ValidationError("That doctor is already booked at that time.")
    appt_id = db.insert("appointments", {
        "patient_id": patient_id, "doctor_id": doctor_id,
        "appt_datetime": when_str, "reason": ask("Reason", False), "status": "Scheduled",
    })
    print(f"  Appointment booked (ID {appt_id}).")


def list_appointments(db):
    patients = {p["id"]: p["full_name"] for p in db.all("patients")}
    doctors = {d["id"]: d["full_name"] for d in db.all("doctors")}
    rows = [{**a, "patient": patients.get(a["patient_id"], "?"),
             "doctor": doctors.get(a["doctor_id"], "?")} for a in db.all("appointments")]
    show(sorted(rows, key=lambda a: a["appt_datetime"]),
         [("ID", "id"), ("Patient", "patient"), ("Doctor", "doctor"),
          ("Time", "appt_datetime"), ("Status", "status")])


def cancel_appointment(db):
    appt = db.get("appointments", ask_int("Appointment ID"))
    if not appt or appt["status"] != "Scheduled":
        raise ValidationError("No scheduled appointment with that ID.")
    db.update("appointments", appt["id"], status="Cancelled")
    print("  Appointment cancelled.")


def complete_appointment(db):
    """Record diagnosis, mark the visit complete and issue a bill."""
    appt = db.get("appointments", ask_int("Appointment ID"))
    if not appt or appt["status"] != "Scheduled":
        raise ValidationError("No scheduled appointment with that ID.")
    diagnosis = ask("Diagnosis")
    prescription = ask("Prescription", False)
    notes = ask("Notes", False)
    amount = ask_amount("Bill amount")
    db.insert("medical_records", {
        "appointment_id": appt["id"], "diagnosis": diagnosis,
        "prescription": prescription, "notes": notes,
    })
    db.insert("bills", {
        "appointment_id": appt["id"], "amount": amount, "paid": False,
        "issued_at": datetime.now().strftime(DATETIME_FMT),
    })
    db.update("appointments", appt["id"], status="Completed")
    print("  Visit recorded and bill issued.")


def patient_history(db):
    patient_id = ask_int("Patient ID")
    doctors = {d["id"]: d["full_name"] for d in db.all("doctors")}
    records = {r["appointment_id"]: r for r in db.all("medical_records")}
    rows = []
    for a in db.all("appointments"):
        if a["patient_id"] == patient_id:
            rec = records.get(a["id"], {})
            rows.append({**a, "doctor": doctors.get(a["doctor_id"], "?"),
                         "diagnosis": rec.get("diagnosis"),
                         "prescription": rec.get("prescription")})
    show(sorted(rows, key=lambda r: r["appt_datetime"], reverse=True),
         [("Time", "appt_datetime"), ("Doctor", "doctor"), ("Status", "status"),
          ("Diagnosis", "diagnosis"), ("Prescription", "prescription")])


def unpaid_bills(db):
    appts = {a["id"]: a for a in db.all("appointments")}
    patients = {p["id"]: p["full_name"] for p in db.all("patients")}
    rows = []
    for b in db.all("bills"):
        if not b["paid"]:
            appt = appts.get(b["appointment_id"], {})
            rows.append({**b, "patient": patients.get(appt.get("patient_id"), "?")})
    show(rows, [("Bill ID", "id"), ("Patient", "patient"),
                ("Amount", "amount"), ("Issued", "issued_at")])


def pay_bill(db):
    bill = db.get("bills", ask_int("Bill ID"))
    if not bill or bill["paid"]:
        raise ValidationError("No unpaid bill with that ID.")
    db.update("bills", bill["id"], paid=True)
    print("  Bill marked as paid.")


# --------------------------------------------------------------------- menu
MENU = [
    ("Add department", add_department),
    ("Add doctor", add_doctor),
    ("Register patient", add_patient),
    ("Search patients", search_patients),
    ("List doctors", list_doctors),
    ("Book appointment", book_appointment),
    ("List appointments", list_appointments),
    ("Cancel appointment", cancel_appointment),
    ("Complete visit (record + bill)", complete_appointment),
    ("Patient history", patient_history),
    ("Unpaid bills", unpaid_bills),
    ("Pay bill", pay_bill),
]


def main():
    db = Store()
    while True:
        print("\n=== Hospital Management System ===")
        for i, (label, _) in enumerate(MENU, 1):
            print(f" {i:>2}. {label}")
        print("  0. Exit")
        choice = input("Select: ").strip()
        if choice == "0":
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(MENU):
            print("  Invalid choice.")
            continue
        try:
            MENU[int(choice) - 1][1](db)
        except ValidationError as e:
            print(f"  Error: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\n  Cancelled.")


if __name__ == "__main__":
    main()