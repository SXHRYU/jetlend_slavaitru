def remove_duplicates(dicts: list[dict]) -> list[dict | None]:
    seen: set(tuple[str, ...]) = set()
    res: list[dict] = []

    for value in dicts:
        item: tuple[str, ...] = tuple(value.items())
        if item not in seen:
            seen.add(item)
            res.append(value)
    return res


raw_list: list[dict] = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"},
]
print(remove_duplicates(raw_list))

# Time complexity: O(N*K),
# где N - кол-во элементов в списке `dicts`,
# K - кол-во элементов в самом большом словаре из списка `dicts`.
