def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        position = _partition(items, start, end, comp)
        _quick_sort(items, start, position - 1, comp)
        _quick_sort(items, position + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = pivot, items[i + 1]
    return i + 1


if __name__ == '__main__':
    items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(quick_sort(items))
