# 🎓 Student Grade Management System

A simple yet powerful Python program to manage student grades, calculate their average, and classify their performance. Perfect for educators or anyone managing student data!

---

## 🚀 Features

- **Add Student Data**: Input student names and up to 3 subject grades.
- **Automatic Calculations**: Calculate the average grade for each student.
- **Performance Classification**: Classify students based on their average grade (A, B, C, D, F).
- **Student Report**: Display a well-formatted report of all students and their performance.

---

## 🛠️ How to Use

### Running the Program

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shadyelsawy536/Student-grade-management.git
   cd student-grade-management
2. **Run the program**:
   python main.py
3. **Follow the On-Screen Instructions:**
   
   -Choose 1 to input student grades.
   
   -Choose 2 to display the student report.
   
   -Choose 0 to exit the program.
   
📝 Example Output

Student Grade Management System  
1. Input student grades  
2. Display student report  
0. Exit
Choose an operation (1, 2, or 0 to exit): 1  

Enter student's name: John Doe  
Enter grade for subject 1: 85  
Enter grade for subject 2: 90  
Enter grade for subject 3: 80  

Students Grade Report:  
------------------------------------------------  
Name        Grades      Average    Classification  
John Doe    [85, 90, 80]   85.00      B  
------------------------------------------------  

📂 Code Overview
Key Functions
1. calc_average(grades):

   - Calculates the average of a list of grades.
   
   - Returns 0 if the list is empty.

2. class_of_grade(average):

- Classifies the student's performance based on their average grade:
   
   - A: 90–100
   
   - B: 80–89
   
   - C: 70–79
   
   - D: 60–69
   
   - F: Below 60

3. input_student_data():

   - Prompts the user to input a student's name and grades for 3 subjects.
   
   - Validates input to ensure grades are between 0 and 100.

4. report(students):

   - Displays a formatted report of all students, including their grades, average, and classification.

5. Main Loop:

   - Allows the user to input student data, view reports, or exit the program.


👨‍💻 Author
Shady Elsawy
[Email](shadyelsawy536@gmail.com) | [GitHub](https://github.com/Shadyelsawy536)


