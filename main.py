class Student:
    

    def __init__(self):
        self.mathematics = 'Математика'
        self.physics = 'Физика'
        self.chemistry = 'Химия'
        self.english = 'Английский'
        self.informatics = 'Информатика'
        self.physicalTraining ='Физкультура'
        self.userName = input('Имя студента-')
        self.userSername = input('Фамилия студента-')
    
    
    
    
    def FillAssessments(self,item,):
        isOpen = True
        grade = []
        print('Заполните оценки по предмету',item)
        print('Если хотите добавить оценку,то напишите цифру')
        print('Для выхода exit')

        while isOpen:
            comend = input('ввод-')
            if comend == 'exit':
                isOpen = False
            else:
                comend = int(comend)
                grade.append(comend)
        return grade


    def LestStudent(self):
        predmet ={self.mathematics: self.FillAssessments(self.mathematics),
                  self.physics: self.FillAssessments(self.physics),
                  self.chemistry: self.FillAssessments(self.chemistry),
                  self.informatics: self.FillAssessments(self.informatics),
                  self.physicalTraining: self.FillAssessments(self.physicalTraining),
                  self.english: self.FillAssessments(self.english),}
        print('оценки по предмету', self.mathematics,'|',predmet[self.mathematics],'|',sum(predmet[self.mathematics])/len(predmet[self.mathematics]))
        print('оценки по предмету', self.physics,'|',predmet[self.physics],'|',sum(predmet[self.physics])/len(predmet[self.physics]))
        print('оценки по предмету', self.chemistry,'|',self.chemistry,'|',sum(predmet[self.chemistry])/len(predmet[self.chemistry]))
        print('оценки по предмету', self.informatics,'|',self.informatics,'|',sum(predmet[self.informatics])/len(predmet[self.informatics]))  
        print('оценки по предмету', self.physicalTraining,'|',self.physicalTraining,'|',sum(predmet[self.physicalTraining])/len(predmet[self.physicalTraining]))
        print('оценки по предмету', self.english,'|',self.english,'|',sum(predmet[self.english])/len(predmet[self.english]))                       

student = Student()
student.LestStudent()