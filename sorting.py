import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    for min_index in range(len(values)):
        print(values)
        min_value = values[min_index]
        min_ind = min_index
        for i in range(min_index, len(values)):
            if values[i] < min_value:
                min_ind = i
                min_value = values[i]
        values[min_ind], values[min_index] = values[min_index], values[min_ind]
        print(values)


def bubble_sort(values):
    cisla = values.copy()
    plt.ion()
    plt.show()

    for i in range(len(cisla)):
        for j in range(len(cisla) -1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(cisla)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(cisla)), cisla, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if cisla[j] > cisla[j + 1]:
                cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
    plt.ioff()
    plt.show()
    return cisla

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, hodnota):
        result = []

        for i in range(len(self.scores)):
            if self.scores[i] == hodnota:
                result.append(i)
        return result

    def get_sorted(self):
        cisla = self.scores.copy()

        for i in range(len(cisla) -1):
            for j in range(len(cisla) - 1):
                if cisla[j] > cisla[j + 1]:
                    cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
            return cisla




if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(selection_sort(values))  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(bubble_sort(small))
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    print(results.count())

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print(results.find(100))
    print(results.get_sorted())

    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

