# Encapsulation
# Instagram Account System

class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Incorrect password"

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password. Password not updated.")

insta = InstagramAccount("Aishwarya_Insta", "1234")
insta.add_private_reel("Gym Reel")
insta.add_private_reel("Travel Reel")
insta.add_archived_reel("Old Dance Reel")
insta.add_archived_reel("College Memories Reel")
print("\nFollower View:")
insta.display_private_reels(True)
print("\nNon-Follower View:")
insta.display_private_reels(False)
print("\nArchived reels (Correct Password):")
insta.display_archived_reels("1234")
print("\nArchived reels (Wrong Password):")
insta.display_archived_reels("0000")
print("\nGetter Method Output:")
print(insta.get_archived_reels("1234"))
print("\nUpdating Password:")
insta.set_password("1234", "5678")
print("\nArchived reels with new password:")
insta.display_archived_reels("5678")