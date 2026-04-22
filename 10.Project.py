class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = str(firstname)
        self.LastName = str(lastname)
        self.TNumber = str(tnumber)
        self.Grades = scores

    def RunningAverage(self):
        valid_scores = [float(s) for s in self.Grades if s.strip()]
        return sum(valid_scores) / len(valid_scores) if valid_scores else 0.0

    def TotalAverage(self):
        processed_scores = [float(s) if s.strip() else 0.0 for s in self.Grades]
        return sum(processed_scores) / len(processed_scores) if processed_scores else 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

def main():
    print(f"{'First':<10} {'Last':<10} {'ID':<10} {'Running':<10} {'Semester':<10} {'Letter'}")
    print(f"{'Name':<10} {'Name':<10} {'Number':<10} {'Average':<10} {'Average':<10} {'Grade'}")
    print("-" * 65)

    with open('10.Project Student Scores.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            s = Student(parts[0], parts[1], parts[2], parts[3:])
            
            print(f"{s.FirstName:<10} {s.LastName:<10} {s.TNumber:<10} "
                  f"{s.RunningAverage():>7.2f} {s.TotalAverage():>10.2f} {s.LetterGrade():>7}")

if __name__ == "__main__":
    main()
