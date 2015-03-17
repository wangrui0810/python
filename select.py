__author__ = 'Administrator'

def select(list):
    for i in range(0, 6):
        min = i
        for j in range(i+1, 7):
            if list[j] < list[min]:
                min = j
        if min != list[i]:
            t = list[i]
            list[i] = list[min]
            list[min] = t
    print list


def main():
    list = []
    for i in range(0, 7):
        list.append(input())
    select(list)



if __name__ == "__main__":
    main()


