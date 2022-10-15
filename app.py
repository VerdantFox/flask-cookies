from datetime import timedelta

from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route("/")
def read_cookies():
    """Read all the cookies."""
    return render_template("template.html", cookies=request.cookies)


@app.route("/set-cookie")
def set_cookie():
    """Set a new session cookie. The default cookie expires when the session ends."""
    response = make_response(render_template("template.html", cookies=request.cookies))
    response.set_cookie("cookie_name", "cookie_value")
    return response


@app.route("/set-path-cookie")
def set_path_cookie():
    """Set a new session cookie with the path value set.

    Will only be sent if the path matches the request path.
    Will match /set-path-cookie, /set-path-cookie/ and /set-path-cookie/anything
    """
    response = make_response(render_template("template.html", cookies=request.cookies))
    response.set_cookie(
        "path_cookie_name", "path_cookie_value", path="/set-path-cookie"
    )
    return response


@app.route("/set-expiring-cookie")
def set_expiring_cookie():
    """Set a new cookie that expires in 15 seconds."""
    response = make_response(render_template("template.html", cookies=request.cookies))
    response.set_cookie("expiring_cookie_name", "expiring_cookie_value", max_age=15)
    return response


@app.route("/set-long-lasting-cookie")
def set_long_lasting_cookie():
    """Set a new cookie that expires in 400 days (the maximum mx_cookie age)."""
    response = make_response(render_template("template.html", cookies=request.cookies))
    response.set_cookie(
        "long_cookie_name", "long_cookie_value", max_age=timedelta(days=400)
    )
    return response


@app.route("/delete-cookies")
def delete_cookies():
    """Delete all cookies we created."""
    response = make_response(render_template("template.html", cookies=request.cookies))
    response.delete_cookie("cookie_name")
    response.delete_cookie("path_cookie_name")
    response.delete_cookie("expiring_cookie_name")
    response.delete_cookie("long_cookie_name")
    return response
