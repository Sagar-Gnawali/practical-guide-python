# Create a function to to check list is empty or not if not print the items in the list
def check_list(items):
    if items:
        for it in items:
            if it is None:
                continue
            else: 
                print(it)
    else: 
        print('OOPS! lists is empty')

check_list(['red', 'green', None, 'blue'])
check_list([])
check_list([None, None])
check_list([1,2,4])