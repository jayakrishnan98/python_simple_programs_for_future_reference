def bubble_sort(std, size1):
    for n in range(size1):
        for o in range(size1 - (n + 1)):
            if std[o].get_total() < std[o + 1].get_total():
                temp = std[o]
                std[o] = std[o + 1]
                std[o + 1] = temp


def calculate_rank(std, size1):
    bubble_sort(std, size1)
    for m in range(size1):
        std[m].set_rank(m + 1)


class Student:
    def __init__(self, name1, mark1):
        self.rank = 0
        self.name = name1
        self.mark = mark1
        self.total = 0
        self.percentage = 0

    def cal_total(self):
        for p in range(5):
            self.total = self.total + self.mark[p]

    def get_total(self):
        return self.total

    def cal_percentage(self):
        self.percentage = (self.total / 500) * 100

    def set_rank(self, rank):
        self.rank = rank

    def display_values(self):
        print(f"Name of the student;{self.name}")
        print(f"Rank;{self.rank}")
        print("Marks are;")
        for q in range(5):
            print(f"Mark for subject{q}= {self.mark[q]}")
        print(f"Total Mark;{self.total}")
        print(f"Percentage;{self.percentage}")


st = list()
size = int(input("Enter the number of Students;"))
for i in range(size):
    mark = list()
    name = input(f"Enter the name of the student{i + 1};")
    print("Mark Entry,")
    for j in range(5):
        mark.append(int(input(f"Mark for Subject{j + 1};")))
    st.append(Student(name, mark))
    st[i].cal_total()
    st[i].cal_percentage()
calculate_rank(st, size)
print("\n\n\n")
for i in range(size):
    st[i].display_values()

