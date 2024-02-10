class Student:
    def init(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("Attributes and their values:")
        for key, value in vars(self).items():
            print(f"{key}: {value}")

    def add_class_attribute(self, student_class):
        self.student_class = student_class
        print(f"Added student_class attribute with value: {self.student_class}")

    def remove_name_attribute(self):
        del self.student_name
        print("Removed student_name attribute")


student_instance = Student(student_id=2200030645, student_name="HARISH")
student_instance.display_attributes()
student_instance.add_class_attribute(student_class="B.TECH 2ND YEAR")
student_instance.remove_name_attribute()
student_instance.display_attributes()
