from database.DB_connect import DBConnect
from model.arco import Arco
from model.pilota import Pilota


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(y1, y2):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select d.*
                    from races r, results r2, drivers d
                    where r.`year` >= %s and r.`year` <= %s
                    and r.raceId = r2.raceId
                    and r2.driverId = d.driverId
                    and r2.`position` > 0
                    group by d.driverId """

        cursor.execute(query, (y1, y2))

        for row in cursor:
            results.append(Pilota(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(y1, y2, idMap):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT r1.driverId AS d1, r2.driverId AS d2, COUNT(DISTINCT r1.raceId) AS peso
                    FROM results r1, results r2, races r
                    WHERE r1.raceId = r2.raceId                  
                      AND r1.constructorId = r2.constructorId    
                      AND r1.raceId = r.raceId                   
                      AND r.year >= %s AND r.year <= %s          
                      AND r1.position > 0                        
                      AND r2.position > 0                        
                      AND r1.driverId > r2.driverId              
                    GROUP BY r1.driverId, r2.driverId """

        cursor.execute(query, (y1, y2))

        for row in cursor:
            results.append(Arco(idMap[row["d1"]], idMap[row["d2"]], row["peso"]))

        cursor.close()
        conn.close()
        return results

