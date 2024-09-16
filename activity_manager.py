import csv
from datetime import datetime

class CommunityActivityManager:
    def __init__(self, filename='activities.csv'):
        self.filename = filename
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        try:
            with open(self.filename, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Activity', 'Description', 'Status'])
        except FileExistsError:
            pass

    def add_activity(self, activity, description, status='Pending'):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), activity, description, status])

    def update_activity_status(self, activity, new_status):
        rows = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[1] == activity:
                    row[3] = new_status
                writer.writerow(row)

    def list_activities(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Activity: {row[1]}, Description: {row[2]}, Status: {row[3]}")

    def save_evidence(self, evidence_filename, description):
        with open('evidences.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), evidence_filename, description])

def main():
    manager = CommunityActivityManager()

    while True:
        print("\nCommunity Activity Manager")
        print("1. Add Activity")
        print("2. Update Activity Status")
        print("3. List Activities")
        print("4. Save Evidence")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            activity = input("Enter activity name: ")
            description = input("Enter activity description: ")
            manager.add_activity(activity, description)
        
        elif choice == '2':
            activity = input("Enter activity name to update: ")
            new_status = input("Enter new status: ")
            manager.update_activity_status(activity, new_status)
        
        elif choice == '3':
            manager.list_activities()
        
        elif choice == '4':
            evidence_filename = input("Enter evidence filename: ")
            description = input("Enter evidence description: ")
            manager.save_evidence(evidence_filename, description)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
