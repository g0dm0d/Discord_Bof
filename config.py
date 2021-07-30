import pymysql


try:
    connection = pymysql.connect(
        host = 'fdb32.awardspace.net',
        port = 3306,
        user = '3905017_bof',
        password = 'wanja331331',
        database = '3905017_bof'
    )
    print('succ')
except Exception as ex:
    print(ex)