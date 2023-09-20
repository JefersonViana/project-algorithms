def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) == int and target_time >= 0:
        for student in permanence_period:
            is_valid = (type(student[0]) == int and
                        type(student[1]) == int)
            if is_valid:
                if target_time in list(range(student[0], student[1] + 1)):
                    count += 1
            else:
                return
        return count
    return


if __name__ == "__main__":
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5),
                          (4, 5), (4, 5), (6, 7)], 1))
