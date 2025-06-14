class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None, description=""):
        self.task_id = task_id
        self.priority = priority  # Higher number for higher priority (for max-heap)
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.description = description

    # For comparison in heap operations (important for max-heap)
    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Prio={self.priority}, Desc='{self.description}')"

#implementing a Max-Heap.
class PriorityQueue:
    def __init__(self):
        self.heap = []  # Array/list representation of the max-heap

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _sift_up(self, i):
        #Moves a task up the heap to maintain the max-heap property.Used after insertion.
        while i > 0 and self.heap[self._parent(i)].priority < self.heap[i].priority:
            parent_idx = self._parent(i)
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

    def _sift_down(self, i):
        #Moves a task down the heap to maintain the max-heap property.Used after extraction or decrease-key operations.
        max_idx = i
        n = len(self.heap)
        while True:
            left_c = self._left_child(i)
            right_c = self._right_child(i)

            if left_c < n and self.heap[left_c].priority > self.heap[max_idx].priority:
                max_idx = left_c
            if right_c < n and self.heap[right_c].priority > self.heap[max_idx].priority:
                max_idx = right_c

            if i != max_idx:
                self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                i = max_idx
            else:
                break

    def insert(self, task):
        #Inserts a new task into the priority queue.Time Complexity: O(log n)
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)
        # Analysis: Appending takes O(1). _sift_up traverses from leaf to root,
        # which is proportional to the height of the heap (log n). Thus, O(log n).

    def extract_max(self):
        #Removes and returns the task with the highest priority.Time Complexity: O(log n)
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._sift_down(0)  # Sift down the new root
        return max_task
        # Analysis: Swapping and popping takes O(1). _sift_down traverses from root to leaf,
        # which is proportional to the height of the heap (log n). Thus, O(log n).

    def increase_key(self, task_id, new_priority):
        """
        Increases the priority of an existing task and adjusts its position.
        Assumes task_id is unique and we can find the task by ID.
        In a real-world scenario, you might store indices or use a hash map for O(1) lookup.
        For simplicity here, we'll iterate to find the task.
        Time Complexity: O(n) for finding task + O(log n) for sifting = O(n) (worst case if not using a lookup table)
                         If task index is known (e.g., via a hash map), then O(log n).
        """
        found_idx = -1
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                found_idx = i
                break

        if found_idx == -1:
            print(f"Task with ID {task_id} not found.")
            return False

        if new_priority < self.heap[found_idx].priority:
            print(f"New priority {new_priority} is not an increase for Task ID {task_id}. Use decrease_key if needed.")
            return False

        self.heap[found_idx].priority = new_priority
        self._sift_up(found_idx) # Sift up because priority increased
        return True
        # Analysis: Finding the task by ID takes O(n) in the worst case (linear scan).
        # _sift_up takes O(log n). Therefore, the overall complexity is O(n).
        # Note: In production, a dictionary mapping task_id to heap index would make finding O(1),
        # reducing this operation to O(log n).

    def decrease_key(self, task_id, new_priority):
        """
        Decreases the priority of an existing task and adjusts its position.
        Time Complexity: O(n) for finding task + O(log n) for sifting = O(n) (worst case if not using a lookup table)
                         If task index is known, then O(log n).
        """
        found_idx = -1
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                found_idx = i
                break

        if found_idx == -1:
            print(f"Task with ID {task_id} not found.")
            return False

        if new_priority > self.heap[found_idx].priority:
            print(f"New priority {new_priority} is not a decrease for Task ID {task_id}. Use increase_key if needed.")
            return False

        self.heap[found_idx].priority = new_priority
        self._sift_down(found_idx) # Sift down because priority decreased
        return True
        # Analysis: Similar to increase_key, O(n) without an index lookup table, O(log n) with one.

    def is_empty(self):
        #Checks if the priority queue is empty.Time Complexity: O(1)
        return len(self.heap) == 0


