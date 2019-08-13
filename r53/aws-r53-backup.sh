#!/bin/bash
#
# Backup your AWS R53 zones with cli53 & AWS SDK, in batch
# https://github.com/barnybug/cli53
# https://docs.aws.amazon.com/cli/latest/userguide/installing.html
#
# Fill in your credentials & aws s3 bucket info in vars below and add the script to cron
#
# set credentials
#
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
#
# set vars
#
aws_s3_bucket=""
now=$(date +"%m-%d-%Y-%H-%M-%S-%Z")
#
#
#
#
mkdir -p ~/dns/awsr53_backups/$now
cli53 list | grep -Po '(?<=\s)\S+(?>\.\s)' |  
while read line; 
do
        echo "Doing backup of ${line} with cli53 export...";
        cli53 export ${line}  >> ~/dns/awsr53_backups/$now/${line}bk; 
done
echo "Creating tar archive..."
tar -zvcf ~/dns/awsr53_backups/${now}/${now}.tgz -C ~/dns/awsr53_backups/$now . 
echo "Uploading to aws s3 bucket..."
aws s3 cp ~/dns/awsr53_backups/${now}/${now}.tgz s3://${aws_s3_bucket}/
