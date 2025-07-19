# First 
Once the yolo_mjpg.py python script is running on the KV260, in another terminal you will run this (also on the KV260).

./mjpg_streamer -i "./input_file.so -f /tmp -n stream.jpg -d 0.1" \
-o "./output_http.so -p 8080 -w ./www -l 0.0.0.0"

# Next
Now YOLO should be working, and the MJPG streamer should be working as well.
# View
To view the output, you will need to visit the IP address created. This IP could be your Tailscale VPN or local IP address.

http://100.76.21.119:8080/?action=stream
