def dict_remove_keys(d, keys):
    return {k: v for k, v in d.items() if k not in keys}

class FilterModule(object):
    def filters(self):
        return {
            'dict_remove_keys': dict_remove_keys
        }
