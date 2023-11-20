# Github actions

![Run Tests and deploy](https://github.com/Sander-317/cd_pipline/actions/workflows/run-test.yml/badge.svg)

## Report

This time I encounter no really big problems (that was a supprise ) but here are the problems I did encounter. but before that i added some fun stuff go to http://157.230.19.4/jokes/"number" the number you added is the number of jokes you get now lets get to the problems

1. The first problem I encountered was how to log in vps. I tried somethings but it didn’t work and google to the rescue a little later I found appleboy/ssh-action@master action and it worked.

2. The second problem I encountered was after I ran all my actions but they didn’t stop I tried to restart the gunicorn but I didn’t work after trying different things that didn’t work I finally asked it on slack and Jordy pointed out that I needed te restart the service but they didn’t work ether then he told maby you should reboot the server en after that everything worked as intended.

3. The third problem I tried to add the GitHub action badge to the flask server and it didn’t work that was because I used the markdown syntax then I turned it in an img tag and everything worked fine.

In the beginning I got some superpy flash backs from all the new stuff introduced but I started figuring thins out one by one and it was easier then I thought I really liked this assignment.
