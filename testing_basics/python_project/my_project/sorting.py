def merge(list_1: list, list_2: list) -> list:
    result = []
    
    index_1 = 0
    index_2 = 0
    
    for _ in range(len(list_1)+len(list_2)):
        val_1 = list_1[index_1]
        val_2 = list_2[index_2]
        if val_1 <= val_2:
            result.append(val_1)
            index_1 += 1
        else:
            result.append(val_2)
            index_2 += 1

        if index_1 == len(list_1):
            result.extend(list_2)
            break
        if index_2 == len(list_2):
            result.extend(list_1)
            break
        
    return result

def sort_list(input_list: list) -> list:
    
    length = len(input_list)
    
    if length <= 1:
        return input_list

    return merge(
        sort_list(input_list[:length//2]), 
        sort_list(input_list[length//2:]), 
    )