class HashTable:
    
    def __init__(self, capacity: int, load_factor=0.5):
        self.capacity = capacity
        self.size =  0
        self.load_factor = load_factor
        self.data = [[]] * capacity


    def insert(self, key: int, value: int) -> None:
        key_entries = self.data[key % self.capacity]
        key_index = -1
        for index, keyvals in enumerate(key_entries):
            if key == keyvals[0]:
                key_index = index
        if key_index == -1:
            key_entries.append((key, value))
            self.size += 1
        else:
            key_entries[key_index] = (key, value)
        current_load_factor = self.size / self.capacity
        if current_load_factor >= self.load_factor:
            self.resize()


    def get(self, key: int) -> int:
        key_entries = self.data[key % self.capacity]
        for cur_key, cur_value in key_entries:
            if cur_key == key:
                return cur_value
        return -1


    def remove(self, key: int) -> bool:
        key_entries = self.data[key % self.capacity]
        key_index = -1
        for index, key_vals in enumerate(key_entries):
            if key == key_vals[0]:
                key_index = index
        if key_index == -1:
            return False
        else:
            last_index = len(key_entries) - 1
            key_entries[key_index], key_entries[last_index] = key_entries[last_index], key_entries[key_index]
            key_entries.pop()
            self.size -= 1
            return True

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity *= 2
        old_data = self.data
        self.data = [[]] * self.capacity
        for key_entries in old_data:
            for key, val in key_entries:
                self.data[key % self.capacity].append((key, val))

