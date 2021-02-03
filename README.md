## Local unsplash image proxy
(not a caching server, but it could be with minimal effort)

- written by: Darren Popham
- license: "Do whatever you want with it and if you like it, feel free to send me some kudos or anything else you might have lying around that seems appropriate.  Or don't, it's entirely up to you."

### What is this?

On my nextcloud cloud server I ran into an issue from people accessing the service from within "restrictive" nextworks, err networks that don't like the unsplash.com URLs and block them.

This then made me think, if I want to provide the pretty pictures, why not a proxy?   

But the challenge then became getitng the clients to use a proxy without actually getting them to configure a proxy.

The solution then was to putz with the unsplash.com URL, rewrite it to point back to my cloud server, who's URL was still allowed by the network deities, and in turn proxy the cal out to unsplash myself.

Not very efficient but it does prove that it is possible to introduce inline to an http response a redirection to a service that returns the expected result but does so behind the scenes.

In my case it works since I am telling the browser to request a URL that belongs to the same domain as the parent cloud service.  Score one for CORS and restrictive networks I guess, but in a less strict environent there is actually nothing to stop me from redirecting the expected response, in this case unsplash.com, to perhaps https://istealyourdata.com and still return the expected unsplash images......

To do so obviously requires some degree of access to the web server config or to a proxy server config without altering the source itself.  A classic man-in-the-middle attack.

In this case I use it for good!

Please don't pursue this for the forces of evil.

### Requirements:
- python3
- virtualenv

### Setup:
> cd PROXY_FOLDER
> virtualenv -p python3 vpython
> source vpython/bin/activate
> pip install -r requirements.txt

You can the run from the command line or setup an autostart mechanism (I included a sample systemctl script, but you would need to edit the folders as appropriate).

Also note that this method requires web server intervention, so I provided snippets for adding to an nginx config as well.

With the nginx config and the service running somewhere you can access then the responses from your nextcloud server get modified when sent to the client, and the client in turn returns the requests for the unsplash images to your web server.

Enjoy!
