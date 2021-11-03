#!/bin/bash
shutdown_(){

delay_=$(( $1 * 60 ))
echo $delay_
echo "The computer will shut down in: $1  minutes"
echo "CRTL+C to cancel"

sleep $delay_

sudo shutdown -h now

}


echo "Enter time in minutes"
read n



shutdown_ $n
