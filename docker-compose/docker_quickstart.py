"""This script is automatically executed every 6h on my server via cron"""

# additional imports random amount of likes and unfollows
import random

from instapy import InstaPy
from instapy.util import smart_run



# login credentials
insta_username = 'passaro.manidestro'
insta_password = 'coelho123'

dont_likes = ['sex','nude','naked','beef','pork','seafood',
            'egg','chicken','cheese','sausage','lobster',
            'fisch','schwein','lamm','rind','kuh','meeresfrüchte',
            'schaf','ziege','hummer','yoghurt','joghurt','dairy',
            'meal','food','eat','pancake','cake','dessert',
            'protein','essen','mahl','breakfast','lunch',
            'dinner','turkey','truthahn','plate','bacon',
            'sushi','burger','salmon','shrimp','steak',
            'schnitzel','goat','oxtail','mayo','fur','leather',
            'cream','hunt','gun','shoot','slaughter','pussy',
            'breakfast','dinner','lunch']

friends = ['']

like_tag_list = ['30anos','29anos', '28anos', '31anos', '27anos', '26anos', 'casa', 'work', 'trabalho', 'workhard', 'home', 'investimento', 'capitalismo', 'casa', 'imobiliario','moradia','porche','comprarcasa','futebol']


# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['girl']

accounts = ['accounts with similar content']

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  bypass_security_challenge_using='sms',
                  disable_image_load=True)

with smart_run(session):
    session.login()

    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)

    # settings
    session.set_relationship_bounds(enabled=True,
				   max_followers=15000)



    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    session.follow_by_locations(['c1900940/setubal-portugal/'], amount=100)

    session.follow_by_locations(['c1895008/lisbon-portugal/'], amount=100)

    # actions
    session.like_by_tags(random.sample(like_tag_list, 3), amount=random.randint(50, 100), interact=True)
    
    session.unfollow_users(amount=random.randint(50,150), InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=48*60*60, sleep_delay=501)