import MySQLdb
import _mysql_exceptions

db = MySQLdb.connect("localhost", "root", "root")

valid_malware_infos = {"MALWARE", "NOT_MALWARE"}

def get_url_info(url):
    cursor = db.cursor()
    query = "SELECT malware_info from dev.url_infos where url = %s"
    cursor.execute(query, (url,))

    result = cursor.fetchone()

    if (not result):
        return None

    malware_info = result[0]
    print("Got malware_info : "+malware_info +" , for url : "+url)
    try:
        cursor.close()
    except:
        pass
    return malware_info

def save_url_info(url, malware_info):
    if malware_info not in valid_malware_infos:
        raise Exception("Invalid value of malware_info found : "+malware_info+". Allowed Values  :"+valid_malware_infos)
    cursor = db.cursor()
    insert_query = "INSERT INTO dev.url_infos (url, malware_info) VALUES (%s, %s)"
    try:
        cursor.execute(insert_query, (url, malware_info,))
    except _mysql_exceptions.IntegrityError as e:
        raise e

    db.commit()
    try:
        cursor.close()
    except:
        pass
    return "SUCCESS"


if __name__=="__main__":
    # Testing the code
    info = get_url_info("http://google.com")
    print (info)

    resp = save_url_info("somefakesite.com", "MALWARE")
    print(resp)









