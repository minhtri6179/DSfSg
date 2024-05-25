from typing import Any


class KeyValue:
    """Node key value pair"""

    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value


class HashMap:
    """Hash map implementation"""

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key: str):
        """Super simple Hash function"""
        hash_value = 0
        for k in key:
            hash_value += ord(k)
        return hash_value % self.capacity

    def get(self, key: str):
        """Get the value using Open Addressing"""
        hash_key = self.get(key)
        while self.map[hash_key] is not None:
            if self.map[hash_key].key == key:
                return self.map[hash_key].value
            hash_key = (hash_key + 1) % self.capacity
        return None

    def put(self, key: str, value: str):
        """Put the value using Open Addressing"""
        hash_key = self.hash(key)
        while True:
            if self.map[hash_key] is None:
                self.map[hash_key] = KeyValue(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    return False
                return True
            elif self.map[hash_key].key == key:
                self.map[hash_key].value = value
                return

            hash_key += 1
            hash_key = hash_key % self.capacity
