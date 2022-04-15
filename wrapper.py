from swimlane import Swimlane
import os

# user module 'cronjob', function 'cronjob'
from userspace import cronjob

# these are test values defined in the Dockerfile
# may be overwritten in the deployment
SWIMLANE_URL = os.environ['SWIMLANE_URL']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
APPLICATION = os.environ['APPLICATION']

user_data = cronjob.job()

attachments = []
if user_data.get('attachments'):
    attachments = user_data['attachments']
    del user_data['attachments']

sw = Swimlane(SWIMLANE_URL, access_token=ACCESS_TOKEN,
              verify_ssl=False, write_to_read_only=True)
app = sw.apps.get(name=APPLICATION)
record = app.records.create(**user_data)

if attachments and len(attachments):
    for ff in attachments:
        record['attachments'].add(ff['filename'], ff['binary_contents'])
    record.save()
