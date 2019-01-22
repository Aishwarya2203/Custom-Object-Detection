import os
import sys
from textmagic.rest import TextmagicRestClient

client = TextmagicRestClient("aishwaryamurkute", "iiiwtmZyKkQHaozyCEtyYgDGZTre2T")

client.messages.create(phones="+1 4243818357", text="Aishwarya is Home")
