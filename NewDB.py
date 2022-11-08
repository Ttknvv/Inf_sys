import sqlite3
import os

def InpSetStud():
    dirName = "DB"
    fileName = "Students.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        student_id BIGINT,
        student_name TEXT, 
        birthday DATE,
        class_id BIGINT,
        cabinet_class_id BIGINT,
        status_id BIGINT,
        control BIGINT,
        address_id BIGINT,
        site_id BIGINT,
        phone_number_id BIGINT
    )""")
    db.commit()

def InpSetSite():
    dirName = "DB"
    fileName = "Site.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        site_id BIGINT,
        row BIGINT,
        desk BIGINT
    )""")
    db.commit()

def InpSetClass():
    dirName = "DB"
    fileName = "Class.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        class_id BIGINT,
        class TEXT
    )""")
    db.commit()

def InpSetCab():
    dirName = "DB"
    fileName = "Cabinet.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        cabinet_class_id BIGINT,
        cabinet_class BIGINT
    )""")
    db.commit()

def InpSetStat():
    dirName = "DB"
    fileName = "Status.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        status_id BIGINT,
        status BIGINT
    )""")
    db.commit()

def InpSetNum():
    dirName = "DB"
    fileName = "Phone_number.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        phone_number_id BIGINT,
        phone_number BIGINT
    )""")
    db.commit()

def InpSetAddr():
    dirName = "DB"
    fileName = "Address.db"
    path = os.path.join(dirName, fileName)
    db = sqlite3.connect(path)
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS Phonebook (
        address_id BIGINT,
        address TEXT
    )""")
    db.commit()

InpSetStud()
InpSetSite()
InpSetClass()
InpSetCab()
InpSetStat()
InpSetNum()
InpSetAddr()