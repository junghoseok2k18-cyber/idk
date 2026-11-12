# CS 26 – Software Development Fundamentals
## Exam 2: Python Program Technical Documentation (Weeks 4–5)

**Assessment type:** Documentation  
**Final output:** One Markdown file (`.md`)  
**Suggested filename:** `CS26_Exam2_Surname_Firstname.md`  
**Coverage:** Lists, tuples, dictionaries, functions, modular programming, file handling, error handling, testing, and debugging.

## 1. Task overview
Prepare technical documentation for a **Python program you have developed or been assigned**. Explain the problem, objectives, program structure, data structures, functions, modules, file operations, error handling, testing, and debugging. The assessment evaluates your understanding and ability to document a program, not merely the quantity of code copied into the report.

The program described must genuinely demonstrate the required Week 4–5 concepts. A simple inventory, expense tracker, student record, or sales recorder is acceptable, provided its implementation supports the explanations. Do not claim a feature or successful test that you have not implemented or performed.

## 2. Required output and submission
1. Write the report in **Markdown**, using a text editor such as Visual Studio Code, Notepad, or another editor that saves plain-text `.md` files.
2. Save the file using the suggested filename. **Submit the `.md` file**, not only a screenshot or PDF.
3. Use Markdown headings, tables, bullet lists, and fenced Python code blocks for clarity.
4. Include short, relevant code excerpts from the actual program. Explain what each excerpt does. Avoid pasting the entire program without discussion.
5. Present **at least five test cases**, including a normal case, a boundary case, and an invalid-input or failure case. Record actual results observed when testing.
6. Describe **at least one debugging issue** you encountered, or clearly state that no defect was observed and explain your verification process. Do not invent evidence.
7. Include the names and purposes of any files or modules. Do not include private credentials, passwords, or personal information in sample data.
8. Submit the Markdown document through the instructor-designated channel by the announced deadline. If source files are also requested separately, follow that additional instruction.

## 3. Required sections

### A. Program title and overview
State the program name, intended users, and its main purpose in 1–2 paragraphs.

### B. Problem description (15% criterion, together with objectives)
Describe the existing problem and why the program is needed. Identify the inputs, processing, and outputs.

### C. Program objectives
Give 3–5 specific, verifiable objectives. Example: “Calculate the total value of products using their quantity and unit price.”

### D. Program requirements and features
Explain the program's major functions and any assumptions or limitations. Distinguish features already implemented from planned enhancements.

### E. Program structure and modules
Show a small file tree and explain what each `.py` file does. Describe how one module imports and uses another.

### F. Data structures
Explain **a list, tuple, and dictionary** used in your program. For each, give a representative Python snippet and justify why that structure fits the data.

### G. Functions
Document the important functions using a table with function name, parameters, return value, and purpose. Explain at least two short code excerpts.

### H. File handling
Identify file name and format, modes (`r`, `w`, `a`, etc.), and the role of `with open(...)`. Explain how the program handles absent or malformed files. State whether records persist between runs.

### I. Error handling
Describe expected errors and the `try`/`except` logic used to handle them. Distinguish input-validation errors from unexpected programming errors.

### J. Testing, debugging, and results
Provide a test table with **test ID, scenario, input, expected result, actual result, and status**. Include at least five cases. Explain a real debugging observation and the correction, if any. State how you verified the correction.

### K. Conclusion
Summarize what the program achieves, its limitations, and 1–2 possible improvements.

### L. References (if applicable)
Cite any documentation, tutorials, or external examples used. Acknowledge assistance and follow your institution's academic-integrity policy.

## 4. Markdown formatting guide

| Purpose | Markdown syntax |
|---|---|
| Main heading | `# Program Title` |
| Section heading | `## Problem Description` |
| Subheading | `### Inputs` |
| Bullet | `- An item` |
| Bold | `**Important**` |
| Inline code | `` `inventory.py` `` |
| Python code block | Three backticks followed by `python`, then code, then three backticks |
| Table | Use `|` to separate columns and `---` under headings |

**Example:**

````markdown
## Function Description

The `calculate_total()` function multiplies quantity by price.

```python
def calculate_total(quantity, price):
    return quantity * price
```

| Input | Expected output |
|---|---|
| `2, 50` | `100` |
````

## 5. How to create the Markdown file

1. Open **Visual Studio Code** or Notepad.
2. Create a new plain-text file.
3. Type `# CS 26 Exam 2 – Technical Documentation` as the first heading.
4. Add the required sections above using `##` headings.
5. Insert concise explanations, relevant Python code blocks, and test tables.
6. Save as `CS26_Exam2_Surname_Firstname.md`. In Notepad, choose **Save as type: All Files** so the file does not become `.md.txt`.
7. In VS Code, press **Ctrl+Shift+V** to preview Markdown (or use the editor's Markdown preview command).
8. Check that headings, code fences, and tables render correctly; proofread technical terms and verify test evidence.
9. Submit the actual `.md` file.

## 6. Rubric (100 points)

| Assessment criterion | Weight | Evidence to look for |
|---|---:|---|
| Problem Description and Objectives | 15% | Clear problem, users, inputs/outputs, measurable objectives |
| Program Structure, Functions and Data Structures | 25% | Accurate modules, functions, list/tuple/dictionary examples and explanations |
| Modular Programming, File Handling and Error Handling | 20% | Meaningful module separation, correct file operations, specific exception handling |
| Testing, Debugging and Results | 20% | Five credible tests, actual results, meaningful debugging/verification |
| Organization and Technical Writing | 20% | Logical headings, readable Markdown, correct terminology, clear original writing |
| **Total** | **100%** | |

## 7. Submission checklist
- [ ] My report is saved as a `.md` file.
- [ ] All required sections are present.
- [ ] I explained actual uses of lists, tuples, dictionaries, and functions.
- [ ] I described modules, file handling, and error handling accurately.
- [ ] My test table contains at least five cases and genuine actual results.
- [ ] I explained debugging or verification without inventing evidence.
- [ ] Python snippets and Markdown tables display correctly.
- [ ] I checked spelling, sources, and academic integrity.

**Note:** The suggested five-test minimum, file-naming convention, and section headings are classroom instructions developed to operationalize the syllabus assessment; the rubric percentages are taken directly from the provided syllabus.
