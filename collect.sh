#!/bin/bash

for var in $(docker ps -aq)
do
	cid=$(docker inspect -f '{{json .Id}}' $var)
	cid=${cid:1}
	cid=${cid%?}
	cname=$(docker inspect -f '{{json .Name}}' $var)
	echo $(du -sh /var/lib/docker/containers/$cid | cut -f1) $cname	
done
