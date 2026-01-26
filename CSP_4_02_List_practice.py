def bookends(li: list):
    return[li.pop(0), li.pop()]
def inOrder(li : list):
    for index in range(len(li) - 1):
        if li[index] > li[index + 1]:
            return False
    return True
def find(li: list, target : int):
    count = 0
    for item in li:
        if item == target:
            return count
        else:
            count += 1
    return(-1)
def removeLowest(li):
    mini = 0
    for i in range(len(li)):
        if li[mini] > li[i]:
            mini = i
    lowest = li.pop(mini)
    return(lowest)
def keepOrder(li: list, value):
    for i in range(len(li)):
        if value < li[i]:
            li.insert(i, value)
            return li
    return li.append(value)
def merge(l1:list, l2:list):
    merged_list = l1.copy()
    for i in range(len(l2)):
        keepOrder(merged_list, l2[i])
    return merged_list

"""
    Given a list of numbers remove the first and last elements from the list and
    return a new list of those two elements.
    You can assume any list given is at least 2 elements long.
    Example list of [1,5,7,3,2] the original list would become [5,7,3] and the new
    list would be [1,2]
    :param list:
    :return:
--
    Given a list of numbers return true if the list is in ascending order.
    :param list:
    :return:
--
    Given a list of numbers and a target value return the index location of the
    target value within the list.
    If the target value is not in the list return -1
    If multiple of the target value exist within the list you may return either
    index.
    You are not alowed to use the built-in index method from python.
    Example list [1,3,5,7,9] target = 3 returned value would be 1 because 3 can be
    found at the first index.
    Example list [3, 7, 8, 1, 0, 1, 12] target = 1 a return of either 3 or 5 would
    be valid.
    Example list [1,3,5,6,9] target 7 returns -1 because 7 is not within the list.
    :param list:
    :param target:
    :return:
--
    Given a list of numbers remove the lowest element from the list. You may assume the list is at least 1 element long.
    If there are multiple of the lowest number you just need to remove 1.
    Example list [3,6,7,2,12] would become [3,6,7,12]
    :param list:
    :return:
--
    Given a list of numbers that is in order and a value. Place the value into the
    list such that the list is still in order.
    Example list=[1,3,5,6] value =4 the resulting list would be [1,3,4,5,6]
    :param list:
    :param value:
    :return:
--
    Given two lists that are in order. produce a new list that is the two lists merged together and in order.
    Make sure to not modify either of the original lists.
    Example l1 = [1,3,5] l2 = [2,4,6,8] -> [1,2,3,4,5,6,8]
    :param l1:
    :param l2:
    :return:
    """