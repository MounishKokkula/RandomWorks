"""
The below program could be used as a utils library for array operations.

Methods:
1. Flatten an array/list (words array & list are being interchangeably in the code below)

Author: Mounish Kokkula
Edit: version #1
Date: Feb 15th 2021
"""


class ArrayOperations:
    def __init__(self):
        pass

    def flatten_array(self, input_array: list, flat_array=None):
        # Time complexity
        # O(N+d), i.e. O(N) where n is number of elements in input list
        # and d is the dimension of innermost list
        """
        :param input_array: Arbitrarily nested list of integers
        :param flat_array: Flattened array of integer's (optional)
        :return: flat_array -> flattened integer list
        """
        if flat_array is None:
            flat_array = []
        for item in input_array:  # Iterating over the input list, O(N)
            # Check if the input contains anything other than list and int
            # Check if input is a list - compute recursively
            if isinstance(item, list):
                self.flatten_array(item, flat_array)
            # Check if it is an integer of list- add to the output
            elif isinstance(item, int):
                flat_array.append(item)

            else:
                raise ValueError
        return flat_array

    def array_handler(self, input_array: list, flat_array=None):
        try:
            return self.flatten_array(input_array, flat_array)
        except:
            return "Not a integer. Check Input!"


if __name__ == "__main__":
    # The below test cases can be used for sanity checking
    # however a unittest is being used to individual test cases
    test = ArrayOperations()
    print("1. Returns flattened array. input: [1, 2, [3, [4, 5]], 6])")
    print(test.array_handler([1, 2, [3, [4, 5]], 6]))
    print("\n")

    print("2. Returns flattened array. input: ")
    print(test.array_handler(
        [1, 2, [3, [4, [5, [6, [7, [8]]]]]], 9, [10, 11, [12, 13, [14, 15, [16, [17, [18, [19, [20]]]]]]]]]))
    print("\n")

    print("3. Should not return flattened array as it contains a string. input: [1, 2, [3, "'"magic"'"]]")
    print(test.array_handler([1, 2, [3, "magic"]]))
    print("\n")

    print("4. Should not return flattened array as it contains a string. input: [1, 2, [3, [4, "'"5"'"]], "'"6"'"]")
    print(test.array_handler([1, 2, [3, [4, "5"]], "6"]))
    print("\n")


# Please find the python library sample execution below
# from iteration_utilities import deepflatten
# multi_depth_list = [[0,1],[[2,[3,[4,[5,[6]]]]]],[7,8]]
# flatten_list = list(deepflatten(multi_depth_list))
# print(flatten_list)
