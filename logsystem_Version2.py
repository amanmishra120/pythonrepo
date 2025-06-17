import collections
import re
from typing import List, Dict

class LogSystem:
    def __init__(self, capacity: int = 5):
        
        self.capacity = capacity
        self.all_logs = []  
        self.user_logs = collections.defaultdict(list)  
        self.log_level_counts = collections.defaultdict(int) 
        self.recent_logs = collections.deque(maxlen=capacity)  

    def add_log(self, line: str) -> None:
       
        match = re.match(r"\[(.*?)\] (\w+) (.*?): (.*)", line)
        if not match:
            print(f"Warning: Could not parse log line: {line}")
            return

        timestamp_str, log_level, user_id, message = match.groups()

        parsed_log = {
            "timestamp": timestamp_str,
            "level": log_level,
            "user_id": user_id,
            "message": message
        }

        self.all_logs.append(parsed_log)
        self.user_logs[user_id].append(parsed_log)
        self.log_level_counts[log_level] += 1
        self.recent_logs.append(parsed_log)

    def get_user_logs(self, user_id: str) -> List[Dict]:
       
        return self.user_logs.get(user_id, [])

    def count_levels(self) -> Dict[str, int]:
        
        return dict(self.log_level_counts)

    def filter_logs(self, keyword: str) -> List[Dict]:
        
        keyword_lower = keyword.lower()
        return [log for log in self.all_logs if keyword_lower in log["message"].lower()]

    def get_recent_logs(self) -> List[Dict]:
     
        return list(self.recent_logs)


if __name__ == "__main__":
    logs_data = [
        "[2025-06-16T10:00:00] INFO user1: Started process",
        "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
        "[2025-06-16T10:00:02] INFO user2: Login successful",
        "[2025-06-16T10:00:03] WARN user3: Low memory",
        "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
        "[2025-06-16T10:00:05] INFO user1: Retrying connection",
        "[2025-06-16T10:00:06] DEBUG user4: Debugging network issue",
        "[2025-06-16T10:00:07] INFO user5: Data sync complete"
    ]

    log_system = LogSystem(capacity=3) 

    print("Adding logs to the system:")
    for log_line in logs_data:
        log_system.add_log(log_line)
        print(f"Added: {log_line}")

    print("\n--- Testing Functionalities ---")

    print("\nLogs for user1:")
    user1_logs = log_system.get_user_logs("user1")
    for log in user1_logs:
        print(log)

    print("\nLogs for user2:")
    user2_logs = log_system.get_user_logs("user2")
    for log in user2_logs:
        print(log)

    print("\nLog Level Frequencies:")
    level_counts = log_system.count_levels()
    print(level_counts)

    print("\nLogs containing 'connect' (case-insensitive):")
    filtered_by_keyword = log_system.filter_logs("connect")
    for log in filtered_by_keyword:
        print(log)

    print("\nLogs containing 'process':")
    filtered_by_keyword_2 = log_system.filter_logs("process")
    for log in filtered_by_keyword_2:
        print(log)

    print("\nMost Recent Logs (capacity=3):")
    recent_logs = log_system.get_recent_logs()
    for log in recent_logs:
        print(log)

    print("\nAdding one more log to demonstrate recent logs capacity:")
    log_system.add_log("[2025-06-16T10:00:08] INFO user1: Process finished")
    print("\nMost Recent Logs after new addition:")
    recent_logs_after_add = log_system.get_recent_logs()
    for log in recent_logs_after_add:
        print(log)