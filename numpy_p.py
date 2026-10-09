# # # # import numpy as np

# # # # my_array = np.array([
# # # #                      [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
# # # #                      [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
# # # #                      [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', 'a']],
# # # #                      ])

# # # # arr = np.array([[1, 2, 3, 4], 
# # # #                 [5, 6, 7, 8], 
# # # #                 [9, 10, 11, 12], 
# # # #                 [13, 14, 15,16]])

# # # # # array[start: end: step] end is exclusive i.e, it won't include the ending numbered row
# # # # print(arr[1:3, 1:3])


# # # import numpy as np

# # # #scalar arithmatic

# # # my_array = np.array([1, 2, 3])

# # # print(my_array + 1)
# # # print(my_array - 2)
# # # print(my_array * 3)
# # # print(my_array / 4)
# # # # print(my_array // 4)
# # # print(my_array ** 5)

# # import numpy as np

# # #vectorised math function
# # my_array = np.array([1, 2, 3, 4, 5, 6])
# # score = np.array([91, 55, 100, 73, 82, 64])
# # print(score == 100)
# # print(my_array * score)
# # print((my_array / score))
# # print(score < 60)
# # score[score < 60] = 0
# # print(score)
# # fruits = np.array([])


# import pandas as pd

# # print(pd.__version__)

# data = [100, 103, 105, 786]

# series = pd.Series(data, index = ["a", "b", "cat", "dog"])

# print(series)
# print(series[series < 200])


# calories = {"Day 1": 2000, "Day 2": 2100, "Day 3": 2500}

# series2 = pd.Series(calories)

# print(series)

import pandas as pd

data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [88, 99, 101]
}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

print(df)