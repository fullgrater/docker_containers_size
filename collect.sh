#!/bin/bash

for var in $(docker ps -aq)
do
	cid=$(docker inspect -f '{{json .Id}}' $var)
	cid=${cid:1}
	cid=${cid%?}
	echo $(du -sh /var/lib/docker/containers/$cid)	
done
