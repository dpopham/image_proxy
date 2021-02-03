#
# Stupidly simple server-side proxy service to receive unsplash image
# requests and in turn actually retrieve the images from unsplash.
#
# Written by Darren Popham
#
import requests
from flask import Flask, Response, request, stream_with_context, abort
import logging
import json

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/<path:image_url>', methods=['GET','OPTIONS'])
def image(image_url):
    url = f"https://{image_url}"
    all_args = request.args.to_dict()
    app.logger.info(f"Requesting unsplash URL: {url}")
    app.logger.info(f"ARGS: {all_args}")
    app.logger.info(f"METHOD: {request.method}")

    if image_url[:19] == "source.unsplash.com" or image_url[:19] == "images.unsplash.com":
        try:
            req = requests.get(f'{url}', params=all_args, stream = True)
            return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])
        except Exception as e:
            abort(404)

    abort(404)


# and so it begins......
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)

