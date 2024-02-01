from functions import *

sample_list = SingleLinkedList()

def main():
    # INSERT
    insertList(sample_list)
    sample_list.showList()

    # must input value to insert
    i_value = input('\n\nValue to insert: ')
    a_value = input('Insert after: ')
    sample_list.insertAfter(i_value, a_value)  # insert i_value after a_value

    i_value = input('\nValue to insert: ')
    sample_list.insertLast(i_value)

    sample_list.showList()

    # DELETE
    sample_list.deleteFirst()
    print('\nDeleted the first node')
    sample_list.showList()

    # sample_list.deleteLast()
    # print('\nDeleted the last node')
    # sample_list.showList()

    # SEARCH AN ELEMENT
    s_value = input('\n\nSearch value: ')
    s = sample_list.search(s_value)
    if s is None:
        print('Does not exist')
    else:
        print('Exist')

    # SORT
    sample_list.sortAsc()
    print('Ascending sort: ')
    sample_list.showList()

    sample_list.sortDesc()
    print('Descending sort: ')
    sample_list.showList()

    # LENGTH
    l = sample_list.checkLength()
    print(f'\nThe list has {l} element(s)')

if __name__ == "__main__":
    main()  
    
