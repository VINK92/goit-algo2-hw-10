class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = []

    def assign_subject(self, subject):
        self.assigned_subjects.append(subject)

def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_teacher_subjects_covered = set()
        
        for teacher in teachers:

            subjects_covered = remaining_subjects.intersection(teacher.can_teach_subjects)
            
            if len(subjects_covered) > len(best_teacher_subjects_covered):
                best_teacher = teacher
                best_teacher_subjects_covered = subjects_covered
            elif len(subjects_covered) == len(best_teacher_subjects_covered):

                if best_teacher.age > teacher.age:
                    best_teacher = teacher
                    best_teacher_subjects_covered = subjects_covered


        if best_teacher:
            schedule.append(best_teacher)
            for subject in best_teacher_subjects_covered:
                best_teacher.assign_subject(subject)
                remaining_subjects.remove(subject)
        else:
            return None

    return schedule

if __name__ == '__main__':

    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
