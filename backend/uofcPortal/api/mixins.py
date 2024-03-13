class GradeMixins:
    def grade_to_letter(self, grade):
        if grade >= 97:
            return 'A+'
        elif grade >= 93:
            return 'A'
        elif grade >= 90:
            return 'A-'
        elif grade >= 87:
            return 'B+'
        elif grade >= 83:
            return 'B'
        elif grade >= 80:
            return 'B-'
        elif grade >= 77:
            return 'C+'
        elif grade >= 73:
            return 'C'
        elif grade >= 70:
            return 'C-'
        elif grade >= 67:
            return 'D+'
        elif grade >= 63:
            return 'D'
        elif grade >= 60:
            return 'D-'
        else:
            return 'F'
        
    # Convert numeric grade to GPA points.
    def grade_to_gpa(self, grade):
        if grade >= 97:
            return 4.0  # A+
        elif grade >= 93:
            return 4.0  # A
        elif grade >= 90:
            return 3.7  # A-
        elif grade >= 87:
            return 3.3  # B+
        elif grade >= 83:
            return 3.0  # B
        elif grade >= 80:
            return 2.7  # B-
        elif grade >= 77:
            return 2.3  # C+
        elif grade >= 73:
            return 2.0  # C
        elif grade >= 70:
            return 1.7  # C-
        elif grade >= 67:
            return 1.3  # D+
        elif grade >= 63:
            return 1.0  # D
        elif grade >= 60:
            return 0.7  # D-
        else:
            return 0.0  # F

    def gpa_to_letter_grade(self, gpa):
        if gpa >= 4.0:
            return 'A+'
        elif gpa >= 3.7:
            return 'A'
        elif gpa >= 3.3:
            return 'A-'
        elif gpa >= 3.0:
            return 'B+'
        elif gpa >= 2.7:
            return 'B'
        elif gpa >= 2.3:
            return 'B-'
        elif gpa >= 2.0:
            return 'C+'
        elif gpa >= 1.7:
            return 'C'
        elif gpa >= 1.3:
            return 'C-'
        elif gpa >= 1.0:
            return 'D+'
        elif gpa >= 0.7:
            return 'D'
        elif gpa >= 0.0:
            return 'F'
        else:
            return 'F'

        
    def calculate_term_gpa_and_letter_grade(self, courses):
        if not courses:
            return 0, 'N/A'  # If no courses taken in a semester, return 0 GPA and N/A as letter grade
        

        total_gpa = sum(self.grade_to_gpa(course['grade']) for course in courses)
        term_gpa = total_gpa / len(courses)
        letter_grade = self.gpa_to_letter_grade(term_gpa)
        return term_gpa, letter_grade


    def calculate_overall_gpa(self, activity):
        total_units = 0
        total_weighted_gpa = 0
        
        for term, info in activity.items():
            # Calculate term GPA if not already done
            if 'TermGPA' not in info or 'Units Enrolled' not in info:
                term_gpa, term_letter_grade = self.calculate_term_gpa_and_letter_grade(info['courses'])
                info['TermGPA'] = term_gpa
                units_enrolled = sum(course.get('units', 3) for course in info['courses'])
                info['Units Enrolled'] = units_enrolled
            else:
                units_enrolled = info['Units Enrolled']
                term_gpa = info['TermGPA']
            
            total_units += units_enrolled
            total_weighted_gpa += term_gpa * units_enrolled

        if total_units == 0:
            return 0  # Avoid division by zero
        overall_gpa = round(total_weighted_gpa / total_units, 2)
        return overall_gpa