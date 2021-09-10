from Scweet.scweet import scrap
from Scweet.user import get_user_information, get_users_following, get_users_followers
data = scrap(words=['Space Tourism'], start_date="2021-01-01", max_date="2021-08-07", from_account = None,interval=1, 
      headless=True, display_type="Top", save_images=False, 
             resume=False, filter_replies=True, proximity=True)
data.head()