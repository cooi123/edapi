import os
from edapi import EdAPI
from edapi.models.user import User
# load from environment variables
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

ed = EdAPI(os.getenv("ED_API_TOKEN"))

user: User = ed.get_user_info()
active_courses = user.get_active_courses()
print(f"Hello {user.name}!")
# convert active courses into pandas df
active_courses_df = pd.DataFrame(
    [course.to_dict() for course in active_courses])
threads = ed.list_all_threads(course_id=14448)
student_thread = [
    thread for thread in threads if thread.user and thread.user.course_role == "student"]
print(f"Total number of threads: {len(threads)}")
