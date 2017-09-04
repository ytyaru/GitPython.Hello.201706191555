#from git import Repo
import git
import os.path
import datetime
import pytz
#path_local_repo = "/share/testgit/searchTwitter"
path_local_repo = os.path.abspath(os.path.dirname(__file__))
if os.path.isdir(os.path.join(path_local_repo, '.git')): repo = git.Repo(path_local_repo)
else:
    repo = git.Repo.init()
    repo.index.add([__file__])
    repo.index.commit('初回コミット。')
for item in repo.iter_commits('master'):
    print(item)
    print('hexsha:', item.hexsha)
    print(item.__class__) # git.objects.commit.Commit
    print('author:', item.author)
    print('authored_date:', item.authored_date)
    print('author_tz_offset:', item.author_tz_offset)
    print('committer:', item.committer)
    print('committed_date:', item.committed_date)
    print('committer_tz_offset:', item.committer_tz_offset)
    print('message:', item.message)
    print('summary:', item.summary)
    print('stats:', item.stats)
    print('parents:', item.parents)
    print('tree:', item.tree)

    t = datetime.datetime.fromtimestamp(item.authored_date)
    print(t)
    """
    authored_date = datetime.datetime.utcfromtimestamp(item.authored_date)
    authored_date += datetime.timedelta(seconds=(item.author_tz_offset * -1)) # なぜかoffsetが-9時間(-32400秒)になっていた。+09:00のはず。
    unix = authored_date.timestamp()  # calendar.timegm と異なり float の値が返される
    print(int(unix))
#    authored_date = datetime.datetime.fromtimestamp(unix, tz=pytz.utc)
#    authored_date = datetime.datetime.fromtimestamp(unix)
    print(authored_date)
    """
"""
import calendar
import datetime
import pytz


# UTC の aware オブジェクト
# Python 3.2 以降では tz = datetime.timezone.utc も可
tz = pytz.utc
now = datetime.datetime.now(tz)
print(now)

# UTC の aware オブジェクト -> Unix time
unix = calendar.timegm(now.utctimetuple())
print(unix)

# Python 3.3 以降では calendar を使わずに書けます
# UTC の aware オブジェクト -> Unix time
unix = now.timestamp()  # calendar.timegm と異なり float の値が返される
print(int(unix))

# Unix time -> UTC の aware オブジェクト
now = datetime.datetime.fromtimestamp(unix, tz=tz)
print(now)


# PST の aware オブジェクト
tz = pytz.timezone("US/Pacific")
now = datetime.datetime.now(tz)
print(now)

# PST の aware オブジェクト -> Unix time
unix = calendar.timegm(now.utctimetuple())
print(unix)

# Python 3.3 以降では calendar を使わずに書けます
# PST の aware オブジェクト -> Unix time
unix = calendar.timegm(now.utctimetuple())
unix = now.timestamp() # calendar.timegm と異なり float の値が返される
print(int(unix))

# Unix time -> PST の aware オブジェクト
now = datetime.datetime.fromtimestamp(unix, tz=tz)
print(now)
"""
