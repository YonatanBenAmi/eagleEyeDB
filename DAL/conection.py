import mysql.connector

def open_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="eagleeyedb"
        )
    except Exception as ex:
        print(ex)

#----------------------------------------------------------------

class AgentDAL:
    def __init__(self):
        self.conn = open_connection()    #Get connection.
        self.cursor = self.conn.cursor() #Variable with query access.

    def create_aget(self,code_name, real_name, location, status, missions_completed):
        query = "INSERT INTO agents (CodeName, RealName, Location, Status, MissionsCompleted) VALUES (%s, %s, %s, %s, %s)"
        val = (code_name, real_name, location, status, missions_completed)
        self.cursor.execute(query, val)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()






# disconnect from server


