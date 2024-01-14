import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

blog = notion.databases.query(
    **{
        "database_id": "42cdc1ff34f3484180dc0607c896b31a"
    }
)

print(blog)