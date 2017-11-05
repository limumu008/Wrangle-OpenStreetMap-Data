'''Explore the data by using SQL'''

import sqlite3

def number_of_docs():
    result = c.execute("SELECT COUNT(*) FROM ways_nodes")
    return result.fetchone()[0]

def number_of_nodes():
    result = c.execute("SELECT COUNT(*) FROM nodes")
    return result.fetchone()[0]

def number_of_ways():
    result = c.execute("SELECT COUNT(*) FROM ways")
    return result.fetchone()[0]

def number_of_unique_users():
    result = c.execute("SELECT COUNT(DISTINCT(e.uid)) \
                       FROM ( SELECT uid FROM nodes \
                       UNION ALL SELECT uid FROM ways) e")
    return result.fetchone()[0]

def top_10_contributors():
    result = c.execute("SELECT e.user, COUNT(*) as num \
                       FROM (SELECT user FROM nodes UNION ALL\
                       SELECT user FROM ways) e GROUP BY e.user\
                       ORDER BY num DESC LIMIT 10")
    return result.fetchall()
def number_of_once_users():
    # The number of appearing only once user
    result = c.execute("SELECT  COUNT(*) FROM\
                       (SELECT e.user, COUNT(*) as num\
                       FROM (SELECT user FROM nodes \
                       UNION ALL SELECT user FROM ways) e\
                       GROUP BY e.user HAVING num=1)  u")
    return result.fetchone()[0]

def top_10_zipcode():
    result = c.execute("SELECT tags.value, COUNT(*) as count\
                       FROM (SELECT * FROM nodes_tags\
                       UNION ALL SELECT * FROM ways_tags) tags\
                       WHERE tags.key='postcode'\
                       GROUP BY tags.value\
                       ORDER BY count DESC LIMIT 10")
    return result.fetchall()

def top_10_cuisine():
    result = c.execute("SELECT nodes_tags.value, COUNT(*) as num\
                       FROM nodes_tags\
                       JOIN (SELECT DISTINCT(id) FROM nodes_tags\
                       WHERE value='restaurant') i\
                       ON nodes_tags.id=i.id\
                       WHERE nodes_tags.key='cuisine'\
                       GROUP BY nodes_tags.value\
                       ORDER BY num DESC LIMIT 10")
    return result.fetchall()

def common_ammenities():
    result = c.execute("SELECT tags.value, COUNT(*) as count\
                       FROM (SELECT * FROM nodes_tags\
                       UNION ALL SELECT * FROM ways_tags) tags\
                       WHERE tags.key = 'amenity'\
                       GROUP BY tags.value\
                       ORDER BY count DESC LIMIT 10")
    return result.fetchall()                 
if __name__ == '__main__':
    
    db = sqlite3.connect("houston.db")
    c = db.cursor()
    
    print "Number of documents: ", number_of_docs()
    print "Number of nodes: ", number_of_nodes()
    print "Number of ways: ", number_of_ways()
    print "Number of unique users: ", number_of_unique_users()
    print "Top 10 contributors: ", top_10_contributors()
    print "Number of users with one contribute: ", number_of_once_users()
    print "Top 10 zipcodes: ", top_10_zipcode()
    print "Popular cuisines: ", top_10_cuisine()
    print "Common ammenities: ", common_ammenities()