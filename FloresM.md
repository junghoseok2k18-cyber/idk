# Hospital Management System
## CS 26 - Exam 2 Documentation

**Document type:** Illustrative sample  
**Course coverage:** Weeks 4–5 Python concepts  
**Program type:** Console-based application

## A. Program Overview

The Hospital Management System is a console application for organizing basic hospital information. Staff can manage departments, doctors, patients, appointments, medical records, and bills. The program stores its data in local JSON files.

The application is divided into two Python files: `what.py` handles prompts, menus, and workflows; `hms_classes.py` provides the storage class and validation exception used by the interaction file.

## B. Problem Description

Keeping patient and appointment information in disconnected files or on paper can make records difficult to find and update. This program provides a simple, centralized way to register patients, find patient records, schedule appointments, record completed visits, and track bills.

**Inputs:** Department and doctor details; patient name, date of birth, gender, phone, and address; appointment details; visit diagnosis, prescription, notes, and bill amount; and bill or record IDs for lookups and updates.

**Processing:** The program validates entered values, assigns IDs, checks references to existing patients, doctors, and departments, prevents past or conflicting appointments, and updates appointment and bill statuses.

**Outputs:** Confirmation and validation messages, formatted lists of doctors, patients, appointments, medical history, and unpaid bills, and JSON data files saved locally.

## C. Objectives

1. Add departments and associate doctors with existing departments.
2. Register patients with basic personal and contact information.
3. Search for patients by name or phone number.
4. Schedule, list, and cancel appointments.
5. Record a completed visit with diagnosis, prescription, and notes.
6. Create bills for completed visits and mark unpaid bills as paid.
7. Preserve application records between runs using JSON files.

## D. Program Requirements and Features
- Add departments and doctors.
- Register and search for patients.
- List doctors with their department names.
- Book, list, and cancel appointments.
- Complete an appointment by recording visit details and issuing a bill.
- View a patient's appointment and medical history.
- List unpaid bills and mark a bill as paid.

## E. Program Structure
```text
inventory_project/
├── what.py
├── classss.py    
└── record.json       # Created when records are saved
```

1. **`what.py` — User interaction and application workflows**
   - Prompts for and validates user input.
   - Displays tabular results.
   - Implements the department, doctor, patient, appointment, medical-record, and billing workflows.
   - Displays the main menu and handles menu selection.
   - Imports `Store` and `ValidationError` from `hms_classes.py`.

2. **`hms_classes.py` — Reusable classes**
   - `Store` reads and writes JSON records, assigns IDs, and provides methods to list, insert, retrieve, and update records.
   - `ValidationError` represents invalid operations that the interaction layer can report to the user.

Run the application from the folder containing both files with:

```text
python what.py
```

## F. Data Structures Used

- **Lists:** `Store.all()` returns a list of records. Lists are also used for menu options, search results, and rows prepared for display.
- **Dictionaries:** Each record is represented as a dictionary of fields, such as a patient's name and date of birth. Dictionaries also map record IDs to names when displaying related doctors, departments, or patients.
- **Tuples:** Menu entries pair a label with its handler function. Table column definitions pair a display heading with the dictionary key to show.
- **JSON:** The lists and dictionaries are serialized to local `.json` files so records can be loaded on later runs.

## G. Function and Responsibilities

### `what.py`

- `ask`, `ask_int`, `ask_date`, `ask_datetime`, and `ask_amount` collect and validate user input.
- `show` prints lists of dictionary records in aligned columns.
- `add_department` and `add_doctor` create department and doctor records.
- `add_patient` and `search_patients` register and find patients.
- `list_doctors` and `list_appointments` display records with related names.
- `book_appointment` checks patient and doctor IDs, appointment time, and doctor availability.
- `cancel_appointment` changes a scheduled appointment to cancelled.
- `complete_appointment` records visit details, creates a bill, and marks the appointment completed.
- `patient_history` displays a patient's appointments and available diagnosis and prescription information.
- `unpaid_bills` and `pay_bill` display outstanding bills and mark a bill as paid.
- `main` creates the store, displays the menu, dispatches the selected action, and reports handled errors.

### `hms_classes.py`

- `Store._path`, `_read`, and `_write` manage paths and JSON file operations.
- `Store.all` and `Store.save_all` read and save a table's records.
- `Store.insert` assigns an ID and adds a record.
- `Store.get` retrieves a record by ID.
- `Store.update` changes fields on a record.
- `ValidationError` is raised by application workflows when an operation cannot be completed.

## H. File Handling Procedures

The `Store` class creates the configured data directory if it does not exist. Each record category is stored in its own JSON file: `departments.json`, `doctors.json`, `patients.json`, `appointments.json`, `medical_records.json`, and `bills.json`. The `meta.json` file stores the next ID counters.

When a table is read for the first time and its file does not exist, the store treats it as an empty list. When saving, the store writes to a temporary file in the data directory and then replaces the target file. This reduces the risk of leaving a partially written JSON file if a write is interrupted.

By default, the data directory is `hms_data` in the current working directory. Setting `HMS_DATA_DIR` changes its location. The application does not currently include backup, export, or data migration features.

## I. Error Handling

- Required fields cannot be left blank. Optional phone, email, address, reason, prescription, and notes may be left blank.
- Integer, date, date/time, and non-negative amount inputs are checked and prompted again when invalid.
- Future dates of birth, appointments in the past, duplicate department names, and duplicate doctor email addresses are rejected.
- The program checks that referenced departments, patients, doctors, appointments, and bills exist before using them.
- An occupied doctor time slot cannot be booked unless the existing appointment was cancelled.
- Workflow validation failures raise `ValidationError` and are displayed as an error message in the menu.
- A missing JSON data file is treated as an empty table. A malformed JSON file stops the program with a message identifying the corrupted file.
- `KeyboardInterrupt` and `EOFError` during an operation are handled by displaying a cancellation message.

## J. Testing, Debugging, and Results

Basic checks performed:

| Test | Result |
|---|---|
| Compile `what.py` and `hms_classes.py` | Passed |
| Start the application and choose Exit | Passed; the menu displayed and the program exited |
| Import `Store` and insert, retrieve, and update a record in a temporary directory | Passed |

Additional functional checks should include registering and searching for a patient, booking and cancelling an appointment, completing a visit, and paying its bill. Invalid dates, unknown IDs, duplicate department names, and conflicting appointment times should also be checked to confirm that the expected validation messages appear.

## K. Conclusion

The program demonstrates a basic, two-module management application using functions, classes, lists, dictionaries, tuples, input validation, and JSON file handling. It supports core record, appointment, visit, and billing workflows. It does not currently implement user login, role-based access, inventory management, reminders, or reports; those features are outside the current program's scope.

## L. References

- `what.py` — user interaction and application workflows.
- `hms_classes.py` — storage and validation classes.
- [Python `json` module documentation](https://docs.python.org/3/library/json.html)
- [Python `datetime` module documentation](https://docs.python.org/3/library/datetime.html)
- [Python `os` module documentation](https://docs.python.org/3/library/os.html)
- [Python `tempfile` module documentation](https://docs.python.org/3/library/tempfile.html)
