import os
from edapi import EdAPI
from edapi.models.user import User
# load from environment variables
from dotenv import load_dotenv
load_dotenv()

ed = EdAPI(os.getenv("ED_API_TOKEN"))

user_info = ed.get_user_info()
user: User = user_info.get_user_info_summary()

print(f"Hello {user.name}!")
