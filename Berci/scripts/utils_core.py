def get_last_nth_occurence_of_list_element(plist, pelem, nth):
    index_after = [idx for idx, s in enumerate(plist) if pelem in s]
    if not index_after:
        return None
    return index_after[-nth] + 1