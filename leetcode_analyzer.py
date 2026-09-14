from datetime import datetime, timedelta
streak =0
logs = [
    {"date": "2026-08-24", "problem": "Two Sum", "minutes": 15, "difficulty": "Easy"},
    {"date": "2026-08-25", "problem": "Contains Duplicate", "minutes": 15, "difficulty": "Easy"},
    {"date": "2026-08-26", "problem": "Valid Anagram", "minutes": 15, "difficulty": "Easy"},
    {"date": "2026-08-27", "problem": "Best Time to Buy and Sell Stock", "minutes": 20, "difficulty": "Easy"},
    {"date": "2026-08-28", "problem": "Maximum Subarray", "minutes": 25, "difficulty": "Medium"},
    {"date": "2026-08-31", "problem": "Move Zeroes", "minutes": 40, "difficulty": "Easy"},
    {"date": "2026-09-01", "problem": "Missing Number", "minutes": 35, "difficulty": "Easy"},
    {"date": "2026-09-02", "problem": "Single Number", "minutes": 15, "difficulty": "Easy"},
    {"date": "2026-09-03", "problem": "Majority Element", "minutes": 25, "difficulty": "Easy"},
    {"date": "2026-09-04", "problem": "Intersection of Two Arrays", "minutes": 30, "difficulty": "Easy"},
    {"date": "2026-09-04", "problem": "Valid Palindrome", "minutes": 35, "difficulty": "Easy"},
    {"date": "2026-09-07", "problem": "Reverse String", "minutes": 15, "difficulty": "Easy"},
    {"date": "2026-09-07", "problem": "Reverse Vowels of a String", "minutes": 30, "difficulty": "Easy"},
    {"date": "2026-09-07", "problem": "Is Subsequence", "minutes": 30, "difficulty": "Easy"},
    {"date": "2026-09-07", "problem": "Merge Sorted Array", "minutes": 25, "difficulty": "Easy"},
]

def average_time(logs):
    total_time = sum(log['minutes'] for log in logs)
    return total_time / len(logs) if logs else 0

def problems_by_difficulty(logs):
    total_easy = sum(1 for log in logs if log['difficulty'] == 'Easy')
    total_medium = sum(1 for log in logs if log['difficulty'] == 'Medium')
    total_hard = sum(1 for log in logs if log['difficulty'] == 'Hard')
    print(f'Easy: {total_easy}, Medium: {total_medium}, Hard: {total_hard}')

def current_streak(logs):
    all_dates = [log['date'] for log in logs]
    streak = 0
    check_day = datetime.strptime(max(all_dates), "%Y-%m-%d")
    
    while check_day.strftime("%Y-%m-%d") in all_dates:
        streak += 1
        check_day = check_day - timedelta(days=1)
    
    return streak

print('Tong So Bai Da Lam:', len(logs))
print('Thoi Gian Trung Binh:', int (average_time(logs)), 'phut/bai')
problems_by_difficulty(logs)
print('Streak hien tai:',current_streak(logs))