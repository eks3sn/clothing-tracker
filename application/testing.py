
# clothing super class, then other smaller ones (instead of just string type)
from heapq import merge
import string


'''
uses mergesort
https://www.programiz.com/dsa/merge-sort
'''
def mergeSort(list):
    if len(list) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(list)//2
        L = list[:r]
        M = list[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            item1 = L[i]
            item2 = M[j]
            if Clothing.get_wears(item1) < Clothing.get_wears(item2):
                print(Clothing.get_wears(item1))
                list[k] = L[i]
                i += 1
            else:
                list[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            list[k] = M[j]
            j += 1
            k += 1

# eventually implement time had a piece of clothing?

'''
Parent class clothing defines ID, brand, color, # of wears
    Has a master list of all clothing items
    sort items by wear

Child classes: tops, bottoms, gym clothes, outerwear
    In these the type is defined, as well as separete lists for each
    Automatically added to master clothing list
    sort items by wear
'''
#--------------------------Parent--------------------------#

class Clothing:
    all_clothes = []
    def __init__(self, id, brand, color, wears) -> None:
        self.id = id
        self.brand = brand
        self.color = color
        self.wears = wears
    
    def append(item) -> None:
        Clothing.all_clothes.append(item)

    def get_all() -> list:
        return Clothing.all_clothes

    def get_wears(item) -> int:
        return item.wears

    def sort() -> list:
        list = Clothing.get_all()
        mergeSort(list)
        return list

#--------------------------Children--------------------------#

class Top(Clothing):
    tops_list = []
    def __init__(self, id, brand, color, wears, type) -> None:
        super().__init__(id, brand, color, wears)
        self.type = type
        Clothing.append(self) # automatically add to all clothes

    def append(item) -> None: # manually as of now
        #item = Top.get(item)
        Top.tops_list.append(item)

    def __repr__(self):
        return f'{self.color} {self.type} from {self.brand}'

    def get_all() -> list:
        return Top.tops_list

    def sort() -> list:
        list = Top.get_all()
        mergeSort(list)
        return list


class Bottom(Clothing):
    bottoms_list = []
    def __init__(self, id, brand, color, wears, type) -> None:
        super().__init__(id, brand, color, wears)
        self.type = type
        Clothing.append(self) # automatically add to all clothes

    def append(item) -> None: # manually as of now
        #item = Top.get(item)
        Bottom.bottoms_list.append(item)

    def __repr__(self):
        return f'{self.color} {self.type} from {self.brand}'

    def get_all() -> list:
        return Bottom.bottoms_list

    def sort() -> list:
        list = Bottom.get_all()
        mergeSort(list)
        return list

class Gym(Clothing):
    gym_list = []
    def __init__(self, id, brand, color, wears, type) -> None:
        super().__init__(id, brand, color, wears)
        self.type = type
        Clothing.append(self) # automatically add to all clothes

    def append(item) -> None: # manually as of now
        #item = Top.get(item)
        Gym.gym_list.append(item)

    def __repr__(self):
        return f'{self.color} {self.type} from {self.brand}'

    def get_all() -> list:
        return Gym.gym_list

    def sort() -> list:
        list = Gym.get_all()
        mergeSort(list)
        return list

class Outerwear(Clothing):
    outer_list = []
    def __init__(self, id, brand, color, wears, type) -> None:
        super().__init__(id, brand, color, wears)
        self.type = type
        Clothing.append(self) # automatically add to all clothes

    def append(item) -> None: # manually as of now
        #item = Top.get(item)
        Outerwear.outer_list.append(item)

    def __repr__(self):
        return f'{self.color} {self.type} from {self.brand}'

    def get_all() -> list:
        return Outerwear.outer_list

    def sort() -> list:
        list = Outerwear.get_all()
        mergeSort(list)
        return list



def main():
    top1 = Top(1, "aritzia", "green", 3, "tank top")
    top2 = Top(1, "brandy", "blue", 1, "tank top")
    top3 = Top(1, "urban", "blue", 0, "tank top")
    Top.append(top1)
    Top.append(top2)
    list = Clothing.get_all()
    print(list)
    newList = Clothing.sort()
    print(list)

main()