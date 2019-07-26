import sqlite3

def get_chrome_cookies():
    conn = sqlite3.connect('/home/agalan/.config/chromium/Default/Cookies')
    query = 'select * from cookies where host_key="www.wgsn.com";'
    # return [{"name": r[0], "value": r[1], "path": r[2]} for r in conn.execute(query)]
    return [{"name": r[2], "value": r[0], "path": r[4]} for r in conn.execute(query)]
    # return [{r[0],  r[2],r[4]} for r in conn.execute(query)]

print (get_chrome_cookies())