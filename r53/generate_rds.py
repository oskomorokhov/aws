# 
# https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-reusable-delegation-set
# 
# Challenge: 
# If you want to migrate existing hosted zones to use a reusable delegation set, 
# the existing hosted zones can't use any of the name servers that are assigned to the reusable delegation set.
# 
# It's relatively easy to create reusable delegation sets until you get one that has four name servers that don't overlap with any of the name servers in your hosted zones.
#
# Requirements: cli53 
# https://github.com/barnybug/cli53
#
# Cli53 Backup of all existing AWS R53 zones
# e.g. cli53 export example.com 
#
#

import subprocess
import re
from pathlib import Path

# set your cli53 profile here for all future cli53 API calls
cli53profile='xxx'

# set path to your zone backup

# check if any existing DS exist
data=subprocess.getoutput('cli53 dslist --profile '+cli53profile)
# extract DS ID from existing DS 
s1=re.search('(?<=\/)[A-Z0-9]+', data)

if not s1:
 # create new DS if none found
 data=subprocess.getoutput('cli53 dscreate --profile '+cli53profile)
 s1=re.search('(?<=\/)[A-Z0-9]+', data)

DSID=s1.group(0)

# extract NS servers from existing DS
s2=re.findall('(?<=\s)ns[^\,|\n]+(?=\,\s|\n|$)', data)

pattern='|'.join(s2)
p=Path('/awsr53_backup/')

files=[x for x in p.iterdir() if x.is_file()]

for f in files:

 with f.open() as file: d=file.read()
 s3=re.findall(pattern,d)
 if s3:
  #match found, DS not unique, repeat
  dsd=subprocess.getoutput('cli53 dsdelete '+DSID+' --profile '+cli53profile)  
  break
else:

 #no match found, DS is unique, full stop
 print(DSID)
